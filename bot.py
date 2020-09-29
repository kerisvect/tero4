from discord.ext import commands
import config
import server

bot = commands.Bot(command_prefix=config.prefix)
bot.remove_command('help')

@bot.event
async def on_ready():
    print ('Tero4 online.')
    print ('Username: ' + bot.user.name)
    print ('ID: ' + str(bot.user.id))

@bot.command()
async def core(ctx, sub=None):
    if sub == None:
        await ctx.send(config.help)
    elif sub == 'stop':
        if ctx.message.author.id == config.creatorID:
            await ctx.send('Bot stopping.')
            await bot.logout()
        else:
            await ctx.send('Invalid perms!')
    else:
        await ctx.send(notOption)

@bot.command()
async def serv(ctx, sub=None, sub2=None):
    if sub == None:
        await ctx.send(server.info())
    elif sub == 'status':
        await ctx.send(server.status())
    elif sub == 'temp':
        await ctx.send(server.temp())
    elif sub == 'clock':
        await ctx.send(server.clock())
    elif sub == 'voltage':
        await ctx.send(server.voltage())
    else:
        await ctx.send(config.notOption)

bot.run(config.token)