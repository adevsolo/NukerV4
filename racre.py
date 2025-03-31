import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

# A rangok listája, amiket létre szeretnél hozni
roles_to_create = ["nuked by @duckys.lol"}
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

    for guild in bot.guilds:
        # Rangok létrehozása
        for role_name in roles_to_create:
            await guild.create_role(name=role_name)

    print('Minden rang létrehozva!')

bot.run('TOKEN')
