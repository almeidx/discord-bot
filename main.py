import discord, os, json
from discord.ext import commands

with open('config.json', 'r') as c:
    config = json.load(c)
TOKEN = config['DISCORD_TOKEN']
DEFAULT_PREFIX = config['PREFIX']

def get_prefix(client, message):
    with open('prefixes.json', 'r') as file:
        prefixes = json.load(file)

    if str(message.guild.id) in prefixes:
        return prefixes[str(message.guild.id)]
    else:
        prefixes[str(message.guild.id)] = DEFAULT_PREFIX
        with open('prefixes.json', 'w') as file:
            json.dump(prefixes, file, indent=2)
        return DEFAULT_PREFIX

client = commands.Bot(command_prefix = get_prefix)

@client.command()
async def load(ctx, extention):
    client.load_extension(f'cogs.{extention}')
    await ctx.send(f'Loaded {extention}')

@client.command()
async def unload(ctx, extention):
    client.unload_extension(f'cogs.{extention}')
    await ctx.send(f'Unloaded {extention}')

@client.command()
async def reload(ctx, extention):
    client.unload_extension(f'cogs.{extention}')
    client.load_extension(f'cogs.{extention}')
    await ctx.send(f'Reloaded {extention}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)
