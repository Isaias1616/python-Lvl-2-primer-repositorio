import discord
from discord.ext import commands
from bot_logic import gen_pass


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def command(ctx):
    await ctx.send("Los comandos disponibles son: hello, heh, clave, reciclar, recyclabes y meme (TODOS USANDO EL SIMBOLO $)")

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def clave(ctx):
    await ctx.send(gen_pass(10))
@bot.command()
async def reciclar(ctx):
    await ctx.send("Reciclar ayuda a disminuir la contaminacion en el planeta. Sin reducir la contaminacion se vera afectada cosas como el el aire que respiramos o la agua que bebemos. Es muy importante para mantener nuestra Tierra saludable para futuras generaciomes.")

    
@bot.command()
async def recyclables(ctx):
    await ctx.send("Papel y cartón — cajas, libretas, sobres, periódicos." 
    " Plásticos — botellas, envases, bolsas (según tipo). " 
    "Vidrio — botellas, frascos Metales — aluminio, latas, acero. "  
    "Orgánicos - Frutas, vegetales, etc.")

@bot.command()
async def meme(ctx):
    archivos = os.listdir()
    enviar = random.choice(archivos)
    with open(enviar, 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("Token")
