import discord, random
from discord.ext import commands

async def is_owner(ctx):
    return ctx.author.id == 385132696135008259

class Commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')

    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason = 'No reason specified.'):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')
    
    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason = 'No reason specified.'):
        await member.kick(reason=reason)
        await ctx.send(f'Kicked {member.mention}')

    @commands.command(aliases=['purge', 'prune'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount : int):
        await ctx.channel.purge(limit=amount)
    @clear.error
    async def clear_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please specify an amount of messages to delete.')

    @commands.command(aliases=['eightball', '8ball'])
    async def _8ball(self, ctx, *, question):
        responses = [
            'It is certain.',
            'It is decidedly so.',
            'Without a doubt.',
            'Yes - definitely.',
            'As I see it, yes.',
            'My reply is no.',
            'Don\'t count on it.',
            'Better not tell you now.',
            'Outlook not so good'
        ]
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {member.mention}')
                return

    @commands.command()
    @commands.check(is_owner)
    async def test(self, ctx):
        await ctx.send(f'Hi, {ctx.author}')

def setup(client):
    client.add_cog(Commands(client))

