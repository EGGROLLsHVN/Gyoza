import discord
from discord.ext import commands
from discord import app_commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
    
        if message.content.startswith('hello'):
            await message.channel.send(f'Hi there {message.author}')

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
            await reaction.message.channel.send('You reacted')


    @commands.command(name = "help")
    async def prefixHelp(self, ctx):
        #Displays all available commands
        helpEmbed = discord.Embed(title = "📜 Command Help", description=f"Use `(prefix)help (command)` for further command help \n\n Use `(prefix)(command)`to run a command.", color = discord.Color.blue())
        # Add commands by category
        helpEmbed.add_field(
            name="Moderation",
            value="`(prefix)ban`, `(prefix)kick`, `(prefix)mute`, `(prefix)clear`",
            inline=False
        )
        await ctx.send(embed=helpEmbed)
    
    @app_commands.command(name = "help", description = "All the commands that are supported by the bot")
    async def slashHelp(self, interaction: discord.Interaction):
        #Displays all available commands
        helpEmbed = discord.Embed(title = "📜 Command Help", description=f"Use `(prefix)help (command)` for further command help \n\n Use `(prefix)(command)`to run a command.", color = discord.Color.blue())
        helpEmbed.add_field(
            name="Moderation",
            value="`(prefix)ban`, `(prefix)kick`, `(prefix)mute`, `(prefix)clear`",
            inline=False
        )
        await interaction.response.send_message(embed=helpEmbed)

async def setup(bot):
    await bot.add_cog(Help(bot)) 