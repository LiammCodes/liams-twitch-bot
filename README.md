# liams-bot
A twitch (and soon to be discord) bot that supports song requests through Spotify.

# SETUP
Fill out the file 'sample env.txt' and once you are done, rename the file to '.env'.

Set the BOT_NICK to the username of the Twitch account you'd like to use as your bot (shouldnt be the same as the account you want to stream with) and set the CHANNEL to the channel username you will be streaming with.

Make sure the SPOTIPY_REDIRECT_URI is set to whatever you set it on your spotify dev account (you can just use http://google.com)

Once your .env file is finished, make sure you have pipenv installed (pip install pipenv) and run 'bot.py' with 'pipenv run python bot.py'

On first launch, your web browser will open the SPOTIPY_REDIRECT_URI page (in my case I used google.com). Copy the URL in the browser, and paste it into the program in your terminal.

Once completed your twitch bot should be ready to take commands.
