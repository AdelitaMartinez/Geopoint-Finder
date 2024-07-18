# GeoPoint Finder

## Overview

GeoPoint Finder is a Python application that utilizes a graphical user interface (GUI) to find the closest geographical point from a user-specified location. It reads a list of geographical points from a file, allows the user to input their coordinates (latitude and longitude), and calculates the closest point based on the Haversine formula.

## Features

- **GUI Interface**: Provides an intuitive interface using tkinter for Python.
- **Input Fields**: Allows users to enter their latitude, longitude, and the filename containing geographical points.
- **File Reading**: Reads points from a specified text file (`points.txt` by default).
- **Closest Point Calculation**: Calculates the closest geographical point to the user's entered location using the Haversine formula.
- **Output Display**: Displays the closest point's description and coordinates in the GUI.

## Installation

1. **Requirements**: Ensure Python 3.12.3 is installed on your system.
2. **Dependencies**: No additional dependencies are required beyond the standard Python libraries (`tkinter`).

## Usage

1. **Running the Application**: Execute `main.py` to launch the GUI.
2. **Input**: Enter your latitude and longitude in the respective fields. Optionally, change the filename if you have a different points file.
3. **Output**: Click the "Find Closest Location" button to display the closest geographical point based on your input.

## Files Included

- `main.py`: Contains the main application code with the tkinter GUI.
- `GeoPoint.py`: Library file defining the `GeoPoint` class for handling geographical points.
- `points.txt`: Default file containing geographical points with latitude, longitude, and descriptions.

## Credits

- **Programmer**: [Adelita Martinez](www.linkedin.com/in/adelitamartinez)
- **Email**: 94martinez.adelita@gmail.com

## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

---
