
# Light Control Project

## Overview

This project demonstrates the integration of a Django backend with TouchDesigner to control lighting settings. The backend manages light parameters such as color, intensity, and pattern, which are then fetched and applied in real-time by TouchDesigner. This showcases my proficiency in Python, application building, software architecture, and UI frameworks,

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Django Application](#django-application)
- [TouchDesigner Integration](#touchdesigner-integration)
- [Code Explanation](#code-explanation)
  - [Django Code](#django-code)
  - [TouchDesigner Code](#touchdesigner-code)
- [Video](#Video) 
- [Conclusion](#conclusion)

## Project Description

The Light Control Project is designed to manage and control lighting settings through a web interface. The Django backend provides an API to set and update light parameters, which are then fetched and applied by TouchDesigner to control a Light COMP.

### Disclaimer

This project was created by me in a short period of time as a small simulation to learn more about TouchDesigner and to have an idea of what could be implemented for the role at WHITEvoid. It may contain errors and areas that need improvement due to my first interaction with TouchDesigner.

## Features

- Control light color, intensity, and patterns.
- Web interface to set and update light settings.
- Real-time updates and application of settings in TouchDesigner.

## Technologies Used

- **Django (Python)**: Backend framework for managing light settings.
- **TouchDesigner**: Tool for fetching and applying light settings.
- **JSON**: Data exchange format between Django and TouchDesigner.

## Setup Instructions

### Django Application

1. **Clone the repository**:
    ```sh
    git clone https://github.com/Egaokira/light_control.git
    cd light_control
    ```

2. **Set up a virtual environment and install dependencies**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. **Run the Django server**:
    ```sh
    python manage.py migrate
    python manage.py runserver
    ```

4. **Access the Django application** at `http://127.0.0.1:8000/`.

### TouchDesigner Integration

1. **Open TouchDesigner** and create a new project.
2. **Add a Web Client DAT (`webclient1`), a Light COMP (`light1`), and a Script DAT**.
3. **Configure the Web Client DAT** to fetch data from the Django server:
    - URL: `http://127.0.0.1:8000/api/light_settings`
    - Method: `GET`
4. **Copy the provided TouchDesigner code** into the Script DAT.

## Django Application

The Django application handles the backend logic for managing light settings. It provides an API endpoint that returns the current settings in JSON format.

### API Endpoint

The Django application provides an endpoint `/api/light_settings` that returns the current light settings in JSON format.

## TouchDesigner Integration

TouchDesigner fetches the light settings from the Django application and applies them to a Light COMP.

### TouchDesigner Code

```python
import numpy
import json

# Setup custom parameters for the Script OP
def onSetupParameters(scriptOp):
    op('webclient1').par.request.pulse()
    page = scriptOp.appendCustomPage('Custom')
    page.appendFloat('Valuea', label='Value A')
    page.appendFloat('Valueb', label='Value B')

# Called whenever a custom pulse parameter is pressed
def onPulse(par):
    pass

# Main function to process the Web Client DAT data
def onCook(dat):
    try:
        # Reference the Web Client DAT
        web_client = op('webclient1')

        # Ensure the Web Client DAT is found
        if not web_client:
            return

        # Check if the Web Client has at least 13 rows
        if web_client.numRows >= 13:
            # Fetch the response data from the Web Client at row 13
            response_data = web_client[12, 0].val

            # Try to parse the response data as JSON
            try:
                parsed_json_data = json.loads(response_data)
            except json.JSONDecodeError:
                return
            
            # Ensure the parsed JSON data is a non-empty list
            if isinstance(parsed_json_data, list) and len(parsed_json_data) > 0:
                # Get the latest settings from the parsed JSON data
                latest_settings = parsed_json_data[-1]

                # Extract settings from the latest settings
                color = latest_settings.get('color')
                intensity = latest_settings.get('intensity')
                pattern = latest_settings.get('pattern')
                
                # Validate the color format
                if not color or len(color) != 7 or color[0] != '#':
                    return
                
                # Validate the intensity value
                if intensity is None or not (0 <= intensity <= 100):
                    return
                
                # Reference the Light COMP
                light = op('light1')
                if light:
                    # Set the color parameters
                    light.par.cr = int(color[1:3], 16) / 255
                    light.par.cg = int(color[3:5], 16) / 255
                    light.par.cb = int(color[5:7], 16) / 255
                    light.par.dimmer = intensity / 100
                    
                    # Handle the pattern settings
                    if pattern == 'pulse':
                        light.par.lighttype = 'cone'
                        light.par.coneangle = 45
                        light.par.conedelta = 5
                    elif pattern == 'static':
                        light.par.lighttype = 'point'
                    elif pattern == 'strobe':
                        light.par.lighttype = 'cone'
                        light.par.coneangle = 30
                        light.par.conedelta = 10
    except Exception as e:
        # Handle any exceptions that occur
        print(f"Error processing API data: {str(e)}")

# Initial pulse to fetch data from the Web Client
op('webclient1').par.request.pulse()

# Loop to continuously fetch and process data
def loop():
    onCook(op(me.name))
    op('webclient1').par.request.pulse()
    run("loop()", delayFrames=3000)

# Start the loop
loop()
```

## Video
https://github.com/user-attachments/assets/c456adb0-7621-46a1-87ca-0fd00a52e309


## Conclusion

The Light Control Project, created by me "Abderrahim Chadli", showcases my ability to develop and maintain software solutions, manage data structures, and integrate backend systems with frontend components. It highlights my proficiency in Python programming, Django framework, and TouchDesigner integration. This project was created to demonstrate my readiness to contribute effectively to the development and maintenance of the KINETIC LIGHTS event automation system at WHITEvoid. Note that this project was my first interaction with TouchDesigner and may contain errors and areas for improvement.
