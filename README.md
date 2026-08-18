Task 1.1P- Switching On lights: Modular Programming Approach

#Description
This project is a smart lighting system designed for an assisted-living environment.
The system uses an Arduino Nano 33 IoT, two LEDs and a push button. The first LED represents the porch light and the second LED represents the hallway light.
When the push button is pressed, both lights turn on. The porch light remains on for 30 seconds, while the hallway light remains on for 60 seconds.

# Hardware

i. Arduino Nano 33 IoT
ii. Two LEDs
iii.Two resistors
iv. Push button
v. Breadboard
vi.Jumper wires

# Pin Connections
i. D2 - Porch LED
ii. D3 - Hallway LED
iii. D4 - Push button
iv. GND - Ground

# Code overview
The program first defines the pins used by the two LEDs and the push button.
The setup function configures the LEDs as outputs and the push button as an input using the internal pull-up resistor. Both LEDs are initially switched off.
When the button is pressed, both LEDs are switched on and starting time is recorded. The program then checks the elapsed time. After 30 seconds, the porch LED is switched off.
After 60 seconds, the hallway LED is switched off.
Modular programming was useful in this project because the different parts of the lighting system have different responsibilities.
