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


# VERSION OF THE PROFESSOR

from random import randint # para simular la duracion de una cancion
from time import sleep

class Track:
    def __init__(self, title=None):
        self.title = title
        self.length = randint(5,6)


class MediaPlayerQueue(Queue_node):
    def __init__(self):
        super().__init__()

    def add_track(self, track):
        self.enqueue(track)

    def play(self):
        print(f"Count: {self.count}")

        while self.count > 0 and self.head is not None:
            current_track_node = self.dequeue()
            print(f"Now playing {current_track_node.title}")

            sleep(current_track_node.length)