# import discord
# from discord.ext import commands

# class Moderation(commands.Cog):
#     def __init__(self, bot):
#         self.bot = bot


# async def setup(bot):
#     await bot.add_cog(Moderation(bot)) 


# @bot.tree.command(name = "hello", description = "Says Hello!", guild = GUILD_ID)
# async def sayHello(interaction: discord.Interaction):
#     await interaction.response.send_message("Hi there!")

# @bot.event
# async def on_member_join(member):
#     channel = bot.get_channel(1373075944541257759)
#     if channel is not None:  # Check if the channel exists
#         await channel.send(f'Welcome {member.mention} to {member.guild.name}!')

# @bot.tree.command(name = "printer", description = "I will print whatever you give me!", guild = GUILD_ID)
# async def printer(interaction: discord.Interaction, printer: str):
#     await interaction.response.send_message(printer)