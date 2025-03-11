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

#Ask Model to Generate YGO-Related Answers:
def ask_jan(question):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "JanAI is an expert in YGO! Scripting."},
                  {"role": "user", "content": question}],
                  max_tokens=300
    )
    return response["choices"][0]["message"]["content"]

#YGO Related Questions:
@bot.command()
async def askygo(ctx, *, question):
    if not is_ygo_related(question):
        await ctx.send("JanAI was tuned to answer only YGO related questions!")
        return

    await ctx.send("JanAI is processing your question...")
    response = ask_jan(question)
    await ctx.send(response)

#OpenAI function to generate LUA Scripts:
def generate_lua_scripts(card_details):
    prompt = f"Generate a LUA script for a Yu-Gi-Oh! custom card based on the following details: {card_details}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        message=[{"role": "system", "content": "You generate LUA scripts for Yu-Gi-Oh! custom cards using JanAI."},
                 {"role": "user", "content": prompt}],
        max_tokens=500

    )
    return response["choices"][0]["message"]["content"]

# Create/Generate LUA Script:
async def genlua(ctx, *, card_details):
    await ctx.send("JanAI is processing and writing your card script..")
    lua_script = generate_lua_scripts(card_details)
    await ctx.send(f"```lua\n{lua_script}\n```")

#Run/Launch The Bot!
bot.run(DISCORD_BOT_TOKEN)