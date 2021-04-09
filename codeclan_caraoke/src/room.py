class Room:
    
    # Each room will be constructed as below with a descriptive room name, variable capacity, variable cost per person and a unique playlist.

    def __init__(self, roomname, capacity, costpp, playlist, guestlist):
        self.roomname = roomname
        self.capacity = capacity
        self.costpp = costpp
        self.playlist = playlist
        self.guestlist = guestlist

    def add_guest_to_room(self, guest):
        pass