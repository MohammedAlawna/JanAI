import discord
import openai
import os
from dotenv import load_dotenv
from discord.ext import commands


#Load Env Variables (Bot, OpenAI API):
load_dotenv()
DISCORD_BOT_TOKEN=os.getenv("DISCORD_BOT_TOKEN")
OPENAI_API_KEY= os.getenv("OPENAI_API_KEY")

#OpenAI Key Configuration:
openai.api_key = OPENAI_API_KEY

#Bot Command Specifications:
