import os
from dotenv import load_dotenv

import discord
from discord.ext import commands
# from discord_slash import SlashCommand
import requests


load_dotenv()
discord_bot_token = os.getenv("DISCORD_BOT_TOKEN")

description = '''A general purpose research agent.'''

# Specify intents
intents = discord.Intents.default()

# client = discord.Client(intents=intents)

bot = discord.Client(command_prefix="/", description=description, intents=intents)
# slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# @bot.command(
#     name="research",
#     description="Conducts research based on the provided query.",
# )
# async def research(ctx, query):
#     print('Research requested: ', query)
#     response = requests.post('https://research-agent-gpt.onrender.com', json={"query": query})
#     response_json = response.json()
#     if response.status_code == 200:
#         print('Response: ', response_json)
#         await ctx.send(content=response_json)
#     else:
#         await ctx.send(content='An error occurred.')

@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # Define the command prefix (e.g., "/research")
    if message.content.startswith('/research'):
        # Extract the research query from the message
        query = message.content[len('/research '):]
        print('Research requested: ', query)

        # Send the query to your API
        response = requests.post('https://research-agent-gpt.onrender.com', json={"query": query})
        response_json = response.json()

        # Check for a successful response
        if response.status_code == 200:
            # Format and send the research results to Discord
            print('Response: ', response_json)
            await message.channel.send(response_json)
        else:
            # Handle any errors that occur
            await message.channel.send('An error occurred.')

# Run the bot
bot.run(discord_bot_token)