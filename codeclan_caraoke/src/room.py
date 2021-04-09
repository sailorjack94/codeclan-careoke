class Room:
    
    # Each room will be constructed as below with a descriptive room name, variable capacity, variable cost per person and a unique playlist.

    def __init__(self, roomname, capacity, costpp, playlist, guestlist, roomtakings):
        self.roomname = roomname
        self.capacity = capacity
        self.costpp = costpp
        self.playlist = playlist
        self.guestlist = guestlist
        self.roomtakings = roomtakings

    def add_guest_to_room(self, guest):
        if (len(self.guestlist) < self.capacity) and guest.cash >= self.costpp:
            self.guestlist.append(guest)
            guest.cash -= self.costpp
            self.roomtakings += self.costpp

    def remove_guest_from_room(self, guest):
        if guest in self.guestlist:
            self.guestlist.remove(guest)
        else:
            return "They aren't in this room."

    def add_song_to_room(self, song):
        self.playlist.append(song)