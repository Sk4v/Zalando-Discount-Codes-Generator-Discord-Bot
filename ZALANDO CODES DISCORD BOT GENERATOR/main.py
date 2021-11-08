'''
This script was written by SK4V for the entire sneakers game community !!!

You have to be careful not to overdo it, Zalando could ban the ip.
You can implement proxies using selenium in the codegenerator.py

!showcommands to see the Discord bot commands

'''

from codegenerator import code
import discord
from discord.ext import commands
from findcodes import fcode


token='YOUR DISCORD BOT TOKEN'
PATH = 'CHROME DRIVER INSTALLATION PATH' #ex. C:\Program Files (x86)\chromedriver.exe'
client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
@commands.is_owner()
async def ping(ctx):
    await ctx.send('Bot is online')


@client.command()
async def showcommands(ctx):
    mesage = ':flag_it: **!itnow [@username]** send in DM a link for your code \n' \
             ':flag_fr: **!frnow [@username]** send in DM a link for your code \n' \
             ':flag_nl: **!nlnow [@username]** send in DM a link for your code \n' \
             ':flag_es: **!esnow [@username]** send in DM a link for your code \n' \
             ':flag_be: **!benow [@username]** send in DM a link for your code \n'
    await ctx.send(mesage)


@client.command()
async def itnow(ctx, user: discord.Member, *, message=None):
    link_newsletter = 'https://www.zalando.it/zalando-newsletter/'
    print('eseguo codenow')
    await user.send(embed=discord.Embed(title='**YOUR CODE IS COMING**'))
    link_code = code(PATH,link_newsletter,1)
    embed=discord.Embed(title='**YOU WILL FIND YOUR CODE HERE** :flag_it:' + link_code)
    await user.send(embed=embed)
    try:
        mes = discord.Embed(title='**YOUR CODE** :flag_it:\n' + fcode(PATH,link_code))
        await user.send(embed=mes)
    except:
        mes2 = discord.Embed(title='*Ops I was unable to print the code ... you will find it by clicking the link above*')
        await user.send(embed=mes2)
        pass

@client.command()
async def frnow(ctx, user: discord.Member, *, message=None):
    link_newsletter = 'https://www.zalando.fr/zalando-newsletter/'
    print('eseguo codenow')
    await user.send(embed=discord.Embed(title='**YOUR CODE IS COMING**'))
    link_code = code(PATH, link_newsletter, 1)
    embed = discord.Embed(title='**YOU WILL FIND YOUR CODE HERE** :flag_ifr:' + link_code)
    await user.send(embed=embed)
    try:
        mes = discord.Embed(title='**YOUR CODE** :flag_fr:\n' + fcode(PATH, link_code))
        await user.send(embed=mes)
    except:
        mes2 = discord.Embed(title='*Ops I was unable to print the code ... you will find it by clicking the link above*')
        await user.send(embed=mes2)
        pass

@client.command()
async def nlnow(ctx, user: discord.Member, *, message=None):
    link_newsletter = 'https://www.zalando.nl/zalando-newsletter/'
    print('eseguo codenow') #log
    await user.send(embed=discord.Embed(title='**YOUR CODE IS COMING**'))
    link_code = code(PATH, link_newsletter, 1)
    embed = discord.Embed(title='**YOU WILL FIND YOUR CODE HERE** :flag_nl:' + link_code)
    await user.send(embed=embed)
    try:
        mes = discord.Embed(title='**YOUR CODE** :flag_nl:\n' + fcode(PATH, link_code))
        await user.send(embed=mes)
    except:
        mes2 = discord.Embed(title='*Ops I was unable to print the code ... you will find it by clicking the link above*')
        await user.send(embed=mes2)
        pass

@client.command()
async def esnow(ctx, user: discord.Member, *, message=None):
    link_newsletter = 'https://www.zalando.es/zalando-newsletter/'
    print('eseguo codenow') #log
    await user.send(embed=discord.Embed(title='**YOUR CODE IS COMING**'))
    link_code = code(PATH, link_newsletter, 1)
    embed = discord.Embed(title='**YOU WILL FIND YOUR CODE HERE** :flag_es:' + link_code)
    await user.send(embed=embed)
    try:
        mes = discord.Embed(title='**YOUR CODE** :flag_es:\n' + fcode(PATH, link_code))
        await user.send(embed=mes)
    except:
        mes2 = discord.Embed(title='*Ops I was unable to print the code ... you will find it by clicking the link above*')
        await user.send(embed=mes2)
        pass


@client.command()
async def benow(ctx, user: discord.Member, *, message=None):
    link_newsletter = 'https://www.zalando.be/zalando-newsletter/'
    print('eseguo codenow') #log
    await user.send(embed=discord.Embed(title='**YOUR CODE IS COMING**'))
    link_code = code(PATH, link_newsletter, 1)
    embed = discord.Embed(title='**YOU WILL FIND YOUR CODE HERE** :flag_be:' + link_code)
    await user.send(embed=embed)
    try:
        mes = discord.Embed(title='**YOUR CODE** :flag_be:\n' + fcode(PATH, link_code))
        await user.send(embed=mes)
    except:
        mes2 = discord.Embed(title='*Ops I was unable to print the code ... you will find it by clicking the link above*')
        await user.send(embed=mes2)
        pass

@client.command()
@commands.is_owner()
async def shutdown(ctx):
    print('stopBot')
    await ctx.send('Bot shutdown')
    await ctx.bot.logout()

client.run(token)
