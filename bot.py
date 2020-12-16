# Liam's Bot
# by Liam Moore
# March 30, 2020

# imports
import re
import os
import sys
import json
import codecs
import random
import spotipy
import requests
import webbrowser
import commands as comm
import spotipy.util as util
from twitchio.ext import commands
from json.decoder import JSONDecodeError
from spotipy.oauth2 import SpotifyClientCredentials

# Set environment tables as variables
irc_token=os.environ['TMI_TOKEN']
client_id=os.environ['CLIENT_ID']
nick=os.environ['BOT_NICK']
prefix=os.environ['BOT_PREFIX']
initial_channels=[os.environ['CHANNEL']]

# check env tables
if [x for x in (irc_token, client_id, nick, prefix, initial_channels) if x is None]:
    print("Fill in the .env file.")
    exit(2)

# create bot object
bot = commands.Bot(
    # set up the bot
    irc_token=irc_token,
    client_id=client_id,
    nick=nick,
    prefix=prefix,
    initial_channels=initial_channels
)

# bot.py, below bot object
@bot.event
async def event_ready():
    'Called once when the bot goes online.'
    print(f"{os.environ['BOT_NICK']} joined the party!\n")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(os.environ['CHANNEL'], f"/me pulled up on the scene.")

# bot.py, below event_ready
@bot.event
async def event_message(ctx):
    'Runs every time a message is sent in chat.'
    # make sure the bot ignores itself and the streamer
    if ctx.author.name.lower() == os.environ['BOT_NICK'].lower():
        return
    
    #bot.py, in event_message, below the bot ignore stuffs
    await bot.handle_commands(ctx)

# cammands command
@bot.command(name='commands')
async def commandshelp(ctx):
    await ctx.send('!songrequest <name of song> - !translate <message> - !8ball <ask anything> - !discord - !github')

# github command
@bot.command(name='github')
async def print_github(ctx):
    await ctx.send(f"Check out some of my Python projects! {comm.github()}")

# discord command
@bot.command(name='discord')
async def print_discord(ctx):
    await ctx.send(f"Join our discord community! {comm.discord()}")

# songrequest command
@bot.command(name='songrequest')
async def songrequest(ctx):
    message = str(ctx.content)
    song_name = message[13:]

    if len(message) < 14:
        await ctx.send('Song request usage: !songrequest <song name>')
    
    elif "https://" in message:
        await ctx.send("Song request does not accept URL's, usage: !songrquest <song name>")

    else:
        await ctx.send(comm.queue_song(song_name, ctx.author.name))

# sr command (songrequest shortened)
@bot.command(name='sr')
async def sr(ctx):
    message = str(ctx.content)
    song_name = message[4:]

    if len(message) < 5:
        await ctx.send('Song request usage: !sr <song name>')

    elif "https://" in message:
        await ctx.send("Song request does not accept URL's, usage: !sr <song name>")

    else:
        await ctx.send(comm.queue_song(song_name, ctx.author.name))

# translation command (for ghost241)
@bot.command(name='translate')
async def translate(ctx):
    message = str(ctx.content)
    text = message[10:]
    
    if len(message) < 13:
        await ctx.send('Translation usage: !translate <message>')
    else:
        await ctx.send(f"{ctx.author.name} says: {comm.translate(text)}")

# tr command (translation shortened)
@bot.command(name='tr')
async def tr(ctx):
    message = str(ctx.content)
    text = message[4:]
    
    if len(message) < 5:
        await ctx.send('Translation usage: !tr <message>')
    else:
        await ctx.send(f"{ctx.author.name} says: {comm.translate(text)}")

# 8ball game
@bot.command(name='8ball')
async def tr(ctx):
    message = str(ctx.content)
    choices = ["Yes 100%!", "It will never happen...", "You will never know...", "Your question is stupid, you will die.", "Obviously.", "Idk brother..."]
    
    if len(message) < 9:
        await ctx.send('8ball usage: !8ball <ask me anything>')
    else:
        await ctx.send(f"{random.choice(choices)}")

# bot.py
if __name__ == "__main__":
    bot.run()