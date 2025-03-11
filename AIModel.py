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
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!Jan", intents=intents)

#The approach of checking is either by a keyword, or question to AI model.
#Jan AI Model should be specific to YGO Content only:
YGO_KEYWORDS = ["yugioh", "card", "duel", "banlist", "deck", 
                "summon", "trap", "yugioh", "يوغي يو", "أوراق يوغي"]

#Check if Question is related to YuGiOh:
def is_ygo_related(question):
    return any(keyword in question.lower() for keyword in YGO_KEYWORDS)