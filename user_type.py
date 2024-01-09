import tkinter as tk
from tkinter import messagebox
import requests

class BuildingGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Building & Rooms Management")

        # Create GUI elements
        self.view_buildings_button = tk.Button(root, text="View Buildings", command=self.view_buildings)
        self.add_building_button = tk.Button(root, text="Add Building", command=self.add_building)
        
        # Initially, hide the room-related buttons
        self.view_rooms_button = tk.Button(root, text="View Rooms", command=self.view_rooms, state=tk.DISABLED)
        self.add_room_button = tk.Button(root, text="Add Room", command=self.add_room, state=tk.DISABLED)

        # Place GUI elements on the window
        self.view_buildings_button.pack(pady=10)
        self.add_building_button.pack(pady=10)
        self.view_rooms_button.pack(pady=10)
        self.add_room_button.pack(pady=10)

    def view_buildings(self):
        response = requests.get("http://localhost:5000/buildings")
        if response.status_code == 200:
            buildings = response.json()["buildings"]
            messagebox.showinfo("Buildings", "\n".join(buildings))
            
            # Enable the room-related buttons after viewing buildings
            self.view_rooms_button.config(state=tk.NORMAL)
            self.add_room_button.config(state=tk.NORMAL)
        else:
            messagebox.showerror("Error", "Failed to fetch buildings.")

    # ... (existing code)


    def add_building(self):
        building_data = {"name": "building_1"}  # You can customize the building name as needed
        response = requests.post("http://localhost:5000/building", json=building_data)
        if response.status_code == 200:
            messagebox.showinfo("Add Building", "Building added successfully.")
        else:
            messagebox.showerror("Error", "Failed to add building.")


    def view_rooms(self):
        response = requests.get("http://localhost:5000/rooms")
        if response.status_code == 200:
            rooms = response.json()["rooms"]
            messagebox.showinfo("Rooms", "\n".join(rooms))
        else:
            messagebox.showerror("Error", "Failed to fetch rooms.")

    def add_room(self):
        messagebox.showinfo("Add Room", "Add Room functionality will be implemented here.")


if __name__ == "__main__":
    root = tk.Tk()
    app = BuildingGUI(root)
    root.mainloop()
