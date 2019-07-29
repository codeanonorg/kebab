import discord
import json
import os

from discord.ext import commands

# =========== utils functions ===========

cote = 0

def set_cote(txt):
	"""
		Determines the new kebab cote.
	"""
	
	# test on txt here
	# ...
	
	global cote
	return cote + 1


# =========== bot functions =============

bot = commands.Bot(command_prefix='?')


@bot.event
async def on_ready():
	game = discord.Game("Surveiller Tristan")
	# affiche le statut
	await bot.change_presence(status=discord.Status.online, activity=game)
	print('*Bot is ready*')


@bot.event
async def on_message(msg):
	"""
		Process messages and update the Kebab cote>
	"""

	global cote
	
	# debug
	print(msg.author)
	
	# update the cote here
	# ...

	# since on_message overwrite commands
	# we need to manually process them 
	await bot.process_commands(msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def kebab(ctx):
	"""
		A command to display the kebab cote.
	"""
	global cote

	msg = "```"
	msg += "La cote kebab de Tristan est de "
	msg += str(cote)
	msg += "```"
	print('debug')
	await ctx.send(msg)


bot.run(os.environ["token"])

