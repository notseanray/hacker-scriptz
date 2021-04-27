import discord
import os
from nbt import nbt
from discord.ext import commands
# basically taken from: https://github.com/Robitobi01/robi_bot
client = discord.Client()

smpworldfolder = "./folder/"

@client.event
async def on_ready():
    print("ready")

@client.event
async def on_message(ctx):
    if ctx.content == "tps":
        last_played = []
        for file in ['level.dat', 'level.dat_old']:
            last_played.append(nbt.NBTFile(os.path.join(smpworldfolder, file))['Data']['LastPlayed'].value)

        tps = 45.0 / ((last_played[0] - last_played[1]) / 1000.0) * 20.0

        if tps > 20.0:
            tps = 20.0
        if tps < 0.0:
            tps = 0.0
        # updates every 45 seconds
        await ctx.channel.send('The current TPS is: **' + str(round(tps, 2)))

try:
    client.run('TOKEN')
except:
    print('invalid token')




