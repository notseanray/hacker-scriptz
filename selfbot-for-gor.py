# simple self bot made for a friend to message back when someone dms you
from discord.ext import commands

bot = commands.Bot("", self_bot=True)
@bot.event
async def on_ready():
    print("gor self bot is ready for action if you know what i mean")

@bot.event
async def on_message(message):
    if (message.guild == None) & (message.author.id != personalUserId):
        await message.channel.send("sheesh")

bot.run("Token", bot=False)