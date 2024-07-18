# Main.py
# Programmer: Adelita Martinez
# Email: amartinez1013@cnm.edu
# Purpose: Demonstrate how to use a GUI
# Python Version: 3.12.3

import tkinter as tk
from tkinter import messagebox
from GeoPoint import GeoPoint

class GeoPointApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GeoPoint Finder")

          # Labels
        tk.Label(self.root, text="Enter Coordinates (Lat, Lon):").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(self.root, text="Enter File Name:").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(self.root, text="Closest Location:").grid(row=2, column=0, padx=10, pady=5)

        # Entry boxes
        self.coordinates_entry = tk.Entry(self.root)
        self.coordinates_entry.grid(row=0, column=1, padx=10, pady=5)
        self.filename_entry = tk.Entry(self.root)
        self.filename_entry.grid(row=1, column=1, padx=10, pady=5)

        # Text box for displaying closest location
        self.closest_location_text = tk.Text(self.root, height=5, width=50)
        self.closest_location_text.grid(row=2, column=1, padx=10, pady=5)

        # Button
        self.find_button = tk.Button(self.root, text="Find Closest Location", command=self.find_closest_location)
        self.find_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
