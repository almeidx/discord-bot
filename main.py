import discord, os
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

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

client.run('')
