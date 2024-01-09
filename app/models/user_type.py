from app import mongo



class Building:
    def add_building(self, building_data):
        # MongoDB insert operation
        mongo.db.buildings.insert(building_data)

    def get_buildings(self):
        # MongoDB find operation for buildings
        return mongo.db.buildings.find({"type": "building"})

    def add_room(self, room_data):
        # MongoDB insert operation
        mongo.db.buildings.insert(room_data)

    def get_rooms(self):
        # MongoDB find operation for rooms
        return mongo.db.buildings.find({"type": "room"})
