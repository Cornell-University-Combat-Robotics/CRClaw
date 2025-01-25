# CRClaw

CRClaw is a Raspberry Pi-powered claw machine project! This project leverages Python to control various functionalities such as joystick input, motor control, LCD display, and music playback.

## Features
- Motor Control: Manages the movement of the claw using stepper motors.
- Joystick Input: Provides control over claw positioning.
- LCD Display: Displays game status and instructions.
- Sensor Integration: Detects claw position and dropped items.
- Music Playback: Enhances user experience with background music.

## Prerequisites

Ensure you have the following installed on your Raspberry Pi:
1. Python 3.x
2. Pygame for music playback (`pip install pygame`)
3. RPi.GPIO for controlling hardware (`pip install RPi.GPIO`)

## Running the Project

1. Clone the repository to your Raspberry Pi:
    - `git clone https://github.com/yourusername/CRClaw.git`
    - `cd CRClaw`
2. Run the main program:
    - `python3 main.py`