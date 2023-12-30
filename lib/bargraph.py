from machine import Pin
from utime import sleep

class Bargraph:
    """
    Represents a bargraph component that controls a set of LEDs.

    Args:
        pins (list): A list of pin numbers corresponding to the LED pins.

    Attributes:
        leds (list): A list of Pin objects representing the LED pins.

    Methods:
        blink(amount=2, delay=0.06): Blinks the LEDs for a specified number of times with a given delay.
        fade_out(value, delay=0.02): Fades out the LEDs starting from the specified index with a given delay.
        fade_in(value, delay=0.02, reverse=False): Fades in the LEDs up to the specified index with a given delay.
        switch_on_greater_than(value, delay=0): Switches on the LEDs up to the specified index with a given delay.
        switch_off_between_range(start, delay=0, reverse=False): Switches off the LEDs within the specified range with a given delay.
        switch_off(): Switches off all the LEDs.
    """

    def __init__(self, pins):
            """
            Initializes a Bargraph object.

            Args:
                pins (list): A list of pin numbers to be used for the LEDs.

            Returns:
                None
            """
            
            self.leds = []
            for pin in pins:
                self.leds.append(Pin(pin, Pin.OUT))
                # print("Bargraph LED pin {} initialized successfully ".format(pin))

            for led in self.leds:
                led.on()

    def blink(self, amount=2, delay=0.06):
        """
        Blinks the bargraph LEDs.

        Args:
            amount (int, optional): The number of times to blink the LEDs. Defaults to 2.
            delay (float, optional): The delay in seconds between each blink. Defaults to 0.06.
        """
        for i in range(amount):
            for led in self.leds:
                led.value(0)
            sleep(delay)
            for led in self.leds:
                led.value(1)
            sleep(delay)

    def fade_out(self, value, delay=0.02):
        """
        Fades out the LEDs in the bargraph.

        Args:
            value (int): The starting value for fading out.
            delay (float, optional): The delay between each step of fading. Defaults to 0.02.
        """
        print("fade_out value: {}".format(value))
        for i in range(value, -1, -1):
            print("fade_out i: {}".format(i))
            self.leds[i].value(1)
            if delay > 0:
                sleep(delay)
            
    def fade_in(self, value, delay=0.02, reverse=False):
        """
        Fades in the LEDs of the bargraph.

        Args:
            value (int): The number of LEDs to fade in.
            delay (float, optional): The delay between each fade step. Defaults to 0.02.
            reverse (bool, optional): If True, fades in the LEDs in reverse order. Defaults to False.
        """
        print("fade_in value: {}".format(value))
        if reverse:
            for i in range(value, -1, -1):
                print("reverse fade_in i: {}".format(i))
                self.leds[i].value(0)
                if delay > 0:
                    sleep(delay)
        else:
            for i in range(value):
                print("fade_in i: {}".format(i))
                self.leds[i].value(0)
                if delay > 0:
                    sleep(delay)
        # for i in range(0, value):
        #     self.leds[i].value(0)
        #     if delay>0:sleep(delay)

    def switch_on_greater_than(self, value, delay=0):
        """
        Switches on the LEDs in the bargraph up to the specified value.
        
        Args:
            value (int): The value up to which the LEDs should be switched on.
            delay (float, optional): The delay between switching on each LED. Defaults to 0.
        """
        for i in range(value):
            self.leds[i].value(0)
            if delay > 0:
                sleep(delay)

    def switch_off_between_range(self, start, delay=0, reverse=False):
            """
            Switches off the LEDs in the range specified by the start index.
            
            Args:
                start (int): The start index of the range.
                delay (float, optional): The delay between turning off each LED. Defaults to 0.
                reverse (bool, optional): If True, the LEDs will be switched off in reverse order. Defaults to False.
            """
            
            if start<len(self.leds):
                if reverse:
                    for i in range(start, -1, -1):
                        self.leds[i].value(1)
                        if delay>0: sleep(delay)
                else:
                    for i in range(start, len(self.leds)):
                        self.leds[i].value(1)
                        if delay>0: sleep(delay)

    def switch_off(self):
        """
        Turns off all the LEDs in the bargraph.
        """
        for led in self.leds:
            led.value(1)