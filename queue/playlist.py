"""Module of a playlist class"""
from node_base_queue import Queue_node
import time 


class Playlist():
    """Class to create a queue based on nodes to make a 
        playlist musical.
        """
    def __init__(self):
        self.playlist = Queue_node()

    def add_song(self):
        """Function that ask for a name of a song, artist and duration"""        
        
        name = input("Song name: ")
        artist = input("Artist: ")
        duration = int(input("Duration in seconds: "))

        song_info = {'name':name, 'artist':artist, 'duration':duration}

        self.playlist.enqueue(song_info)
        print("Song added!")


    def play(self):
        """This function will play and dequeue the songs in order FIFO"""
        print("Playing Playlist")
        while self.playlist.head:
            print("----------Playing-------------")
            song_playing = self.playlist.dequeue()
            print(f"Song name: {song_playing['name']}")
            print(f"Artist: {song_playing['artist']}")
            print(f"Duration: {song_playing['duration']}")
            time.sleep(5)
        print("Playlist empty")

