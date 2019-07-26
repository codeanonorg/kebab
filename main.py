import discords
from discord.ext import commands

# =========== utils functions ===========
cote = 0

def set_cote(txt):
	"""Determines the new kebab cote"""
	
	# test on txt here
	# ...
	
	global cote
	return cote + 1

# =========== bot functions =============

bot = commands.Bot(command_prefix='?')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def kebab(ctx):
	global cote

	msg = "```"
	msg += "La cote kebab de Tristan est de "
	msg += str(cote)
	msg += "```"
	print('debug')
	ctx.send(msg)

@bot.event
async def on_message(msg):
	global cote

	if msg.author == "0x5AD":
		cote = set_cote(msg.content)


print("log")
bot.run('')