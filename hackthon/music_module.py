# music_module.py
import os
import random
import pygame

MUSIC_FOLDER = "music"
pygame.mixer.init()

current_song = None

def play_music():
    """Play a random music file from the music folder."""
    global current_song
    try:
        songs = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith((".mp3", ".wav"))]

        if not songs:
            print("❌ No music files found in the 'music' folder.")
            return

        song = random.choice(songs)
        song_path = os.path.join(MUSIC_FOLDER, song)

        print(f"🎵 Playing: {song}")
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
        current_song = song_path

    except Exception as e:
        print(f"⚠ Error playing music: {e}")


def stop_music():
    """Stop the currently playing music."""
    pygame.mixer.music.stop()
    print("⏹ Music stopped.")