import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv

if load_dotenv('configs.env'):
    TOKEN = os.getenv('DISCORD_TOKEN')
else:
    TOKEN = os.environ['DISCORD_TOKEN']
    
GUILD_ID = discord.Object(id = 1047555977093853214)

intents = discord.Intents.default()
intents.message_content = True  # Needed for message content
intents.reactions = True       # Needed for reaction events
intents.members = True         # Needed for member join events

class Bot(commands.Bot):
    # Constructor
    def __init__(self):
        super().__init__(command_prefix = "?", intents = intents, help_command=None)

    # Loads Cogs 
    async def setup_hook(self):
        for fileName in os.listdir("./cogs"):
            if fileName.endswith(".py") and not fileName.startswith("_"):
                await self.load_extension(f"cogs.{fileName[:-3]}")

    # On ready and also adds the / commands for specific server
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        try:
            guild = discord.Object(id = 1047555977093853214)
            # synced = await self.tree.sync(guild = guild) #this is just for this server
            synced = await self.tree.sync()
            print(f'Synced {len(synced)} commands to guild {guild.id}')
            await self.tree.sync(guild = guild)

        except Exception as e: 
             print(f'Error sycing commands: {e}')
        

    async def on_member_join(self, member):
        channel = self.get_channel(1373075944541257759)
        if channel is not None:  # Check if the channel exists
            await channel.send(f'Welcome {member.mention} to {member.guild.name}!')

# Sets bot with Bot() class calling the default constructor
bot = Bot()

# If it is outside the Bot class
# @bot.event
# async def on_member_join(member):
#         channel = bot.get_channel(1373075944541257759)
#         if channel is not None:  # Check if the channel exists
#             await channel.send(f'Welcome {member.mention} to {member.guild.name}!')
    

bot.run(TOKEN)
