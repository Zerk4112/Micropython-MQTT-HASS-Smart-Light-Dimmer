from machine import Pin
from utime import sleep
from rotary_irq_esp import RotaryIRQ
from util import *
from bargraph import Bargraph

# Load the settings from the settings.json file
settings = load_settings()

# Initialize the rotary encoder
rotary_encoder = RotaryIRQ(pin_num_clk=33, 
    pin_num_dt=32, 
    min_val=0, 
    max_val=9, 
    reverse=True, 
    range_mode=RotaryIRQ.RANGE_BOUNDED)

# Initialize the bargraph
led_bargraph = Bargraph([19, 21, 22, 23, 18, 5, 17, 16, 4, 2])

# Blink the bargraph to show that we're alive
led_bargraph.blink(1,0.2)

# Connect to WiFi and MQTT
connect_to_wifi(settings, led_bargraph)
client = connect_to_mqtt(settings, led_bargraph)

# Initialize the button for the rotary encoder
button = Pin(15, Pin.IN, Pin.PULL_DOWN)

# Initialize the rotary encoder values for change tracking
val_old=rotary_encoder.value()
val_new = 0

# Initialize the power state and button state
power_on=True
button_held=False

# Main loop
try:
    while True:

        # Check if the button is pressed
        if button.value()==0 and not button_held:

            # Button is pressed, mark it as held
            button_held=True

            # If the button is pressed, toggle the power, and send the new state to MQTT
            power_on = not power_on
            if power_on:
                client.publish("{}/power".format(settings['mqtt_base_topic']), "on")
                led_bargraph.fade_in(val_new)

            else:
                led_bargraph.fade_out(val_new)
                client.publish("{}/power".format(settings['mqtt_base_topic']), "off")

        # If the button is released, mark it as not held
        elif button.value()==1 and button_held:
            button_held=False
        
        # If the power is on, check if the rotary encoder has changed
        if power_on:
            val_new=rotary_encoder.value()

            # If the rotary encoder has changed, send the new value to MQTT
            if val_old!=val_new:
                client.publish("{}/brightness".format(settings['mqtt_base_topic']), str(map_value(val_new+1,0.9,10,0,255)))
                val_old=val_new
                print('changed: {}'.format(val_new))

            # Update the bargraph
            led_bargraph.switch_on_greater_than(val_new+1)
            led_bargraph.switch_off_between_range(val_new+1)
        else:

            # If the power is off, turn off the bargraph
            # TODO - cycle through animations periodically
            led_bargraph.switch_off()

        # Sleep for a bit
        sleep(0.06)
except KeyboardInterrupt:
    print("Program ended by user")
