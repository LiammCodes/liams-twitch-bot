# commands.py
# by Liam Moore
# March 30, 2020

# imports
import os
import spotipy
import requests
import spotipy.util as util
from colorama import Fore

# queue song function
def queue_song(song_name, author):

    # environment tables variables
    username = os.environ['SPOTIFY_USERNAME']
    client_id = os.environ['SPOTIPY_CLIENT_ID']
    client_secret = os.environ['SPOTIPY_CLIENT_SECRET']
    redirect_uri = os.environ['SPOTIPY_REDIRECT_URI']
    scope = 'user-modify-playback-state'

    # set token cache
    token = util.prompt_for_user_token(
        username,
        scope,
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri
    )

    # create spotify object
    sp = spotipy.Spotify(auth=token)

    # headers for requests
    headers={"Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token 
    }

    # search for a song
    search_result = sp.search(q='track:' + song_name)
    tracks = search_result["tracks"]["items"]

    # find first song uri in search results
    if tracks:
        # get name and artist
        name = tracks[0]["name"]
        artist = tracks[0]["album"]["artists"][0]["name"]

        # printing output to terminal
        print(Fore.GREEN + name + " by " + artist + " has been queued by " + author + "." + Fore.RESET)
        song_uri = tracks[0]["uri"]

        #create uri compatible for use in url
        song_code = song_uri.replace(":", "%3A")

    else:
        print(Fore.RED + song_name + " not found. Attempted by " + author + ". \n" + Fore.RESET)
        return "Song not found! Try again."

    # queue up song
    response = requests.post('https://api.spotify.com/v1/me/player/queue?uri=' + song_code,
        headers=headers
    )

    print(response.text)
    return name + " by " + artist + " has been queued!"

def github():
    return os.environ['GITHUB_LINK']

def discord():
    return os.environ['DISCORD_LINK']

def pw():
    return os.environ['CARX_PW']