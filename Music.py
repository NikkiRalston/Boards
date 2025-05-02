#importing queue
from queue import Queue

#starting a class called song
class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
    
    def __str__(self):
        return f"{self.title} by {self.artist}"

#this is where i made the music player 
class MusicPlayer:
    def __init__(self):
        self.playlist = Queue()
        
    def add_song(self, song):
        self.playlist.put(song)
        print(f"You have Added: {song}")
            
    def play_next(self):
        if not self.playlist.empty():
            next_song = self.playlist.get()
            print(f"Now Playing: {next_song}")
        else:
            print("No Playlist Found. Play Something.")
            
    def show_playlist(self):
        if self.playlist.empty():
            print("Playlist is Empty!")
        else:
            print("Songs up next:")
            temp_list = list(self.playlist.queue)
            for i, song in enumerate(temp_list, 1):
                print(f"{i}. {song}")


if __name__ == "__main__":
    #adding songs for the player to show/play
    player = MusicPlayer()
    player.add_song(Song("Let it go", "Indina Menzel"))
    player.add_song(Song("Anxiety", "Doechii"))
    player.add_song(Song("Love Again", "Alex Isley"))
    
    player.show_playlist()
    player.play_next()
    player.show_playlist()