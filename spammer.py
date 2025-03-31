import discord
import asyncio
import random

# Bot token, amit a Discord Developer Portal-ból kell beszerezni
TOKEN = 'MTM1NjM2NjQxNzc4NzYyMTUyNw.G4Nrl2.2HoyttLnTRt91BiG_shOqQg6z4R07AHUwP6ybs'  # Cseréld le a saját bot tokenedre

# Bot kliens létrehozása
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot bejelentkezett: {client.user}')
    
    # Minden elérhető szerverre iterálunk
    for guild in client.guilds:
        print(f'Bot csatlakozott a(z) {guild.name} szerverhez.')
        
        # Csatornák listája, ahová üzeneteket küldhetünk
        channels = [channel for channel in guild.text_channels if channel.permissions_for(guild.me).send_messages]
        
        while True:
            if channels:  # Ellenőrizzük, hogy vannak-e elérhető csatornák
                channel = random.choice(channels)  # Véletlenszerű csatorna kiválasztása
                try:
                    await channel.send("@everyone WAKE UP! THIS SERVER HAS BEEN BEAMED BY @duckys.lol ")  # Az üzenet, amit küldeni szeretnél
                    await asyncio.sleep(0.000001)  # Várakozás 0.0001 másodpercig (10,000 üzenet/másodperc)
                except discord.Forbidden:
                    print(f'Nincs engedély az üzenet küldésére a(z) {channel.name} csatornába.')
                except discord.HTTPException as e:
                    print(f'Hiba történt az üzenet küldésekor: {e}')
                except Exception as e:
                    print(f'Ismeretlen hiba történt: {e}')
            else:
                print('Nincs elérhető csatorna az üzenetek küldésére.')

# Bot futtatása
client.run(TOKEN)
