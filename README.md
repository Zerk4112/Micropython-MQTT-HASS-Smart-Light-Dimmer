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

## Wiring Instructions

![Wiring Diagram](https://github.com/Zerk4112/Micropython-MQTT-HASS-Smart-Light-Dimmer/blob/main/img/v1%20Wiring%20Diagram.png?raw=true)

1. **Rotary Encoder:**
   - Connect CLK (Clock) pin of the rotary encoder to GPIO 33 on the ESP32.
   - Connect DT (Data) pin of the rotary encoder to GPIO 32 on the ESP32.
   - Connect SW (Switch/Button) pin of the rotary encoder to GPIO 15 on the ESP32.

2. **LED Bar Graph:**
   - Connect the first LED pin of the bar graph to GPIO 19 on the ESP32.
   - Connect the second LED pin of the bar graph to GPIO 21 on the ESP32.
   - Continue this pattern for the remaining LED pins and ESP32 pins (22, 23, 18, 5, 17, 16, 4, 2).

3. **Resistors:**
   - Connect a 220-ohm resistor from each LED pin on the bar graph to the 3V3 (3.3V) pin on the ESP32.
   - Connect the other end of each resistor to the corresponding LED pin.

4. **Power Supply:**
   - Connect the GND (Ground) pin of the rotary encoder to the GND (Ground) pin on the ESP32.
   - Connect the 3V3 (3.3V) pin of the rotary encoder to the 3V3 (3.3V) pin on the ESP32.

**Note:**

- The rotary encoder includes a built-in push button, and it's connected to GPIO 15.
- The resistors are wired to the 3V3 line, with the LEDs sinking the current. Connect the resistors to the anode (longer leg) of each LED, and the cathodes (shorter legs) to the corresponding pins on the ESP32.

By following these instructions and the provided diagram, you should be able to wire your smart light dimmer successfully. Ensure a common ground among all components and check the power requirements of your LED bar graph to avoid overloading the ESP32.

Certainly! Here's the updated Node-Red setup section with a note about customizing the brightness values in `boot.py`:

## Node-Red Setup

To seamlessly integrate the Smart Bulb Dimmer with Node-Red and Home Assistant, follow these steps:

1. Install Node-Red on your preferred platform or server.

2. Import the provided Node-Red Flows into your Node-Red instance. You can find these flows in the [node-red-flows](/node-red-flows) folder.

3. Customize the flows as needed. While all error handling is managed on the device, feel free to check the topics for each MQTT In node in the flows. Ensure the topics match your configuration.

### Flow Descriptions

#### 1. Brightness Control Flow

This flow manages brightness control. It listens to the `{{base_topic}}/brightness` MQTT topic. Note that the actual mapping of brightness values occurs in the Micropython script (`boot.py`). Ensure that the values sent via MQTT align with your smart lights' requirements.

![Brightness Control Flow](https://github.com/Zerk4112/Micropython-MQTT-HASS-Smart-Light-Dimmer/blob/dev/img/Node-Red%20Flow%20-%20Brightness.png?raw=true)

#### 2. Power Control Flow

The Power Control Flow manages the power state of the smart lights. It listens to the `{{base_topic}}/power` MQTT topic, interpreting received values ('on' or 'off') and triggering the corresponding Home Assistant service. Check the MQTT In node for the correct topic and adjust it if needed.

![Power Control Flow](https://github.com/Zerk4112/Micropython-MQTT-HASS-Smart-Light-Dimmer/blob/dev/img/Node-Red%20Flow%20-%20Power.png?raw=true)

### Customization Tips

- **MQTT Topics:**
  - Verify and adjust MQTT In node topics in each flow to match your configuration.

  - **Brightness Values:**
    - The actual mapping of brightness values occurs in the Micropython script (`boot.py`). Ensure that the values sent via MQTT align with your smart lights' requirements. Modify the Micropython script if necessary.

  - **Further Customization:**
    - Tailor the flows based on your preferences and the specific characteristics of your smart lights.

### Ideas and Todos

1. **Ping Response Flow**

   Create a flow to respond to pings from the device. If no response is received after a set number of attempts, trigger a notification to users.

2. **Status Check Flow**

   Implement logic in both the Micropython script and a Node-Red flow to check the status of the light entity. If the light entity is "unavailable" or "off," or otherwise unavailable for change requests, put the device in an error state. This flow should be triggered on device boot as well.

## Contributing

Any contributions you make are greatly appreciated.

## License

Distributed under the GNU v3 License. See `LICENSE` for more information.

## Useful Links

[Wiki.fluidnc.com - ESP32 Dev Kit Pin Reference](http://wiki.fluidnc.com/en/hardware/esp32_pin_reference)

## Contact

Zach Covington - <zerkdev09@gmail.com>
