# Micropython-MQTT-HASS-Smart-Light-Dimmer

DIY smart dimmer with Micropython on ESP32. Communicate with Home Assistant via MQTT, LED bargraph feedback, rotary encoder, and WiFi. Easily adaptable to other Micropython-compatible MCUs.

## Parts List

Here is a list of the components required for this project:

- Micropython-compatible MCU (e.g., ESP32)
- Rotary encoder
- LED bargraph (10 LEDs)
- 220 ohm resistors (10 pieces, one for each LED in the bargraph)
- Female soldering headers (optional)
- Male soldering headers (optional)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Micropython-compatible MCU (e.g., ESP32)
- Rotary encoder
- LED bargraph
- Home Assistant setup
- MQTT broker

### Installation

1. Clone the repo ```git clone https://github.com/Zerk4112/Micropython-MQTT-HASS-Smart-Light-Dimmer.git```
2. Upload the `boot.py` and `lib` folder to your MCU.
3. Make sure that you check the pinout of your MCU and change the pin numbers in `boot.py` accordingly.

## Usage

The `boot.py` script initializes the hardware and network connections for the device. It loads settings from a JSON file, initializes a rotary encoder and a LED bargraph, establishes WiFi and MQTT connections, and sets up a button for the rotary encoder.

The `lib` folder contains the following modules:

- `rotary_irq_esp.py & rotary.py`: Driver for the rotary encoder, from public repository: [miketeachman/micropython-rotary](https://github.com/miketeachman/micropython-rotary).
- `bargraph.py`: Contains the Bargraph class which is used to control a LED bargraph.
- `mqtt.py`: Contains the MQTT class which is used to establish an MQTT connection and publish/subscribe to topics, from public repository: [micropython/umqtt.simple](https://github.com/micropython/micropython-lib/tree/master/micropython/umqtt.simple).
- `util.py`: Contains utility functions for loading settings from a JSON file and establishing MQTT connections.

## Contributing

Any contributions you make are greatly appreciated.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Zach Covington - <zerkdev09@gmail.com>
