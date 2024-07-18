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

    def find_closest_location(self):
        try:
            # Get user input
            user_input = self.coordinates_entry.get().strip()
            filename = self.filename_entry.get().strip()

            # Parse coordinates input
            lat, lon = map(float, user_input.split(','))

            # Read points from file
            points = self.read_points_from_file(filename)

            # Create user GeoPoint
            user_point = GeoPoint(lat, lon, "User Location")

            # Find closest point
            closest_point = self.find_closest_point(user_point, points)

            # Display closest location in text box
            if closest_point:
                self.closest_location_text.delete('1.0', tk.END)
                self.closest_location_text.insert(tk.END, f"You are closest to {closest_point.Description} which is located at {closest_point.Point}")
            else:
                messagebox.showinfo("No Points Found", "No points found in the file.")

        except ValueError:
            messagebox.showerror("Error", "Invalid coordinates input. Please enter valid coordinates.")
        except FileNotFoundError:
            messagebox.showerror("File Not Found", f"File '{filename}' not found.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def read_points_from_file(self, filename):
        # Read points from specified file and return a list of GeoPoint Objects
        point_list = []
        with open(filename, 'r') as file:
            for line in file:
                lat, lon, description = line.strip().split(',')
                point = GeoPoint(float(lat), float(lon), description)
                point_list.append(point)
        return point_list

    def find_closest_point(self, user_point, point_list):
        # Find the closest GeoPoint to the user's input location.
        closest_point = None
        min_distance = float('inf')
        for point in point_list:
            distance = user_point.Distance(point.GetPoint())  # Use Distance method instead of distance_to
            if distance < min_distance:
                min_distance = distance
                closest_point = point
        return closest_point

if __name__ == "__main__":
    root = tk.Tk()
    app = GeoPointApp(root)
    root.mainloop()
