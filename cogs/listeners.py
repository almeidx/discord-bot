import discord, json
from discord.ext import commands

with open('config.json', 'r') as c:
    config = json.load(c)
DEFAULT_PREFIX = config['PREFIX']

class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot has started.')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('Command not found.')
        else:
            pass

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with open('prefixes.json', 'r') as file:
            prefixes = json.load(file)
        prefixes[str(guild.id)] = DEFAULT_PREFIX
        with open('prefixes.json', 'w') as file:
            json.dump(prefixes, file, indent=2)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        with open('prefixes.json', 'r') as file:
            prefixes = json.load(file)
        prefixes.pop(str(guild.id))
        with open('prefixes.json', 'w') as file:
            json.dump(prefixes, file, indent=2)

def setup(client):
    client.add_cog(Events(client))
