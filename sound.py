from pygame import mixer,time

def play_music(file_path):
    # Initialize Pygame mixer
    mixer.init()

    try:
        # Load the music file
        mixer.music.load(file_path)

        # Play the music
        mixer.music.play()

        # Wait for the music to finish playing
        while mixer.music.get_busy():
            time.Clock().tick(10)
        
        # Music finished playing, clean up
        mixer.quit()

    except pygame.error as e:
        print("Pygame error:", e)

# Path to the music file

music_file = "/home/ecobarter/Downloads/welcome.mp3"
#music_file_1 = "/home/ecobarter/Downloads/next.mp3"
# Call the function to play the music

if __name__ == "__main__":
    play_music(music_file)
