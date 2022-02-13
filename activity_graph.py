import discord
import os
import datetime
import time
import asyncio
import matplotlib.pyplot as plt

from discord.ext import commands
from discord.ext.commands import Bot

intents=intents=discord.Intents.all()

bot = commands.Bot(command_prefix='$', intents=intents, self_bot=True)
bot.remove_command('help')

# used for graph with matplotlib

x_axis = list(i for i in range(0, 25))  # hours
y_axis = list(0 for i in range(0, 25))  # messages

start_time = time.time()

@bot.event
async def on_ready():
	print(
        '\nReady!\n',
        f'\nClient User: {bot.user.name}#{bot.user.discriminator}',
        f'\nUser ID: {bot.user.id}',
        f'\nDiscord Library Version: {discord.__version__} ' +
        f'{discord.version_info.releaselevel}\n'
    )

@bot.event
async def on_message(message):
    # REPLACE WITH GUILD YOU WANT TO WATCH OR REMOVE CONDITIONAL COMPLETELY
    if message.guild.id != 1:
        return
    hour = int(message.created_at.strftime('%H')) - 5
    y_axis[hour] += 1
    await bot.process_commands(message)

@bot.command()
async def graph(ctx):
    msg = await ctx.send('generating graph...')

    plt.plot(x_axis, y_axis)
    plt.xlabel('Time of Day')
    plt.ylabel('Amount of Messages')
    plt.title('Discord Activity')
    plt.xticks(range(0, 25))
    plt.savefig('graph.png', bbox_inches='tight')
    plt.clf()

    await msg.edit(content='sending graph...')
    await ctx.send(file=discord.File('graph.png'))

    os.remove('graph.png')

@bot.command()
async def uptime(ctx):
	current_time=time.time()
	difference = int(round(current_time - start_time))
	text = str(datetime.timedelta(seconds=difference))
	embed = discord.Embed(color=0xadd8e6)
	embed.add_field(name="Uptime", value=text)
	embed.set_footer(text=f'{bot.user.name}#{bot.user.discriminator}')
	try:
		await ctx.send(embed=embed)
	except discord.HTTPException:
		await ctx.send("Current uptime: " + text)

bot.run("TOKEN", bot=False)
