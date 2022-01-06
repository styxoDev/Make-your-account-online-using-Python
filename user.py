import os, server_start
import discord
from discord.ext import commands

user = commands.Bot(
  command_prefix='-',
  self_bot=True
)

async def on_ready():
  print("Successfully connected")

server_start.server_start()
user.run(os.getenv("token"), bot=False)
