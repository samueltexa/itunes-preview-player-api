import json
import requests
import time
import sys
import vlc

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])

data = response.json()
for result in data["results"]:
    print(result["trackName"])

    # Play the preview URL
    preview_url = result["previewUrl"]
    player = vlc.MediaPlayer(preview_url)
    
    # Set the volume (0 to 100)
    player.audio_set_volume(100)  # Adjust the volume level as needed
    
    player.play()
    
    # Wait for the preview to finish (30 seconds)
    time.sleep(300)
    player.stop()
