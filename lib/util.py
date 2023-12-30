import ujson
from utime import sleep
import network
from machine import reset
from umqtt.simple import MQTTClient

def map_value(value, in_min, in_max, out_min, out_max):
    """
    Maps a value from one range to another range.
    
    Args:
        value (float): The value to be mapped.
        in_min (float): The minimum value of the input range.
        in_max (float): The maximum value of the input range.
        out_min (float): The minimum value of the output range.
        out_max (float): The maximum value of the output range.
    
    Returns:
        float: The mapped value.
    """
    return (value - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

def connect_to_wifi(settings, led_bargraph):
    """
    Connects to Wi-Fi using the provided settings.

    Args:
        settings (dict): A dictionary containing the Wi-Fi settings, including 'wifi_ssid' and 'wifi_password'.
        led_bargraph: An object representing the LED bargraph.

    Returns:
        None
    """
    
    # Blink the bargraph to show that connection sequence has started
    led_bargraph.blink(1,0.03)

    # Get the Wi-Fi settings from the settings.json file
    ssid = settings['wifi_ssid']
    password = settings['wifi_password']

    # Connect to Wi-Fi
    wlan = network.WLAN(network.STA_IF)  # Create a station interface
    wlan.active(True)  # Activate the interface

    # Check if already connected
    if wlan.isconnected():
        print("Already connected to Wi-Fi")

        # Fade in the bargraph to show that we're connected
        led_bargraph.fade_in(len(led_bargraph.leds))
        return

    # Connect to Wi-Fi
    try:
        wlan.connect(ssid, password)
    except:
        print("Failed to connect to Wi-Fi")
        # If we failed to connect, blink the bargraph to show that we failed
        led_bargraph.blink(6)
        reset()

    # Define the maximum number of attempts to connect to Wi-Fi
    max_attempts = 20
    attempt_count = 0

    # Attempt to connect to Wi-Fi
    while not wlan.isconnected() and attempt_count < max_attempts:
        print("Waiting for wifi connection.. (attempt {} of {})".format(attempt_count, max_attempts))

        # Fade in and out the bargraph to show that we're waiting for Wi-Fi
        led_bargraph.fade_in(len(led_bargraph.leds)-1, reverse=True)
        print("waiting for wifi connection... leds1")
        sleep(0.2)
        led_bargraph.fade_out(len(led_bargraph.leds)-1),
        print("waiting for wifi connection... leds2")
        sleep(0.2)
        attempt_count += 1

    if wlan.isconnected():

        # Fade in the bargraph to show that we're connected
        print("Connected to Wi-Fi")
        print("IP Address:", wlan.ifconfig()[0])

        # Blink and fade in the bargraph to show that the connection sequence is complete
        led_bargraph.blink(2)
        led_bargraph.fade_in(len(led_bargraph.leds))
    else:
        # If we failed to connect, blink the bargraph to show that we failed
        print("Failed to connect to Wi-Fi")
        led_bargraph.blink(6, 0.02)
        
def connect_to_mqtt(settings, led_bargraph):
    """
    Connects to the MQTT broker using the provided settings and returns the MQTT client object.

    Args:
        settings (dict): A dictionary containing the MQTT broker settings.
        led_bargraph (object): An object representing the LED bargraph.

    Returns:
        MQTTClient: The MQTT client object.

    Raises:
        Exception: If failed to connect to the MQTT broker.
    """
    try:

        # Define the MQTT client and connect to the broker
        client = MQTTClient("bathroom_fixture_brightness", settings['mqtt_broker'], settings["mqtt_port"], settings["mqtt_user"], settings["mqtt_password"])
        client.connect()
        print('Connected to MQTT Broker: {}'.format(settings['mqtt_broker']))

        # Blink the bargraph to show that we're connected
        led_bargraph.blink(2)
        return client

    except:

        # If we failed to connect, blink the bargraph to show that we failed
        led_bargraph.blink(6,0.02)
        print("Failed to connect to MQTT Broker: {}".format(settings['mqtt_broker']))
        print("resetting...")
        print("length of leds: {}".format(len(led_bargraph.leds)))

        # Fade in and out the bargraph to show that we're resetting
        led_bargraph.fade_in(len(led_bargraph.leds)-1, reverse=True)
        led_bargraph.fade_out(len(led_bargraph.leds)-1)
        sleep(0.02)
        reset()

def load_settings():
    """
    Load the settings from the 'settings.json' file.

    Returns:
        dict: The loaded settings data.
    """

    # Load the settings from the 'settings.json' file
    with open('settings.json', 'r', encoding='utf-8') as f:

        # Parse the JSON data
        data = ujson.load(f)
        print("Settings loaded successfully: {}".format(data))

    # Return the settings data
    return data
