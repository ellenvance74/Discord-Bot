import discord
import random
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the token from the environment variable
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord. Intents.default() 
intents.message_content = True

client = discord.Client (intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$teams'):
        # Example command format: $teams name1, name2, name3, name4 / 2
        try:
            # Split the message content to extract names and number of teams
            content = message.content[len('$teams '):]
            names_part, teams_part = content.split('/')
            names = [name.strip() for name in names_part.split(',')]
            num_teams = int(teams_part.strip())

            if num_teams <= 0 or num_teams > len(names):
                await message.channel.send('Invalid number of teams.')
                return

            # Shuffle the names
            random.shuffle(names)

            # Create the teams
            teams = [[] for _ in range(num_teams)]
            for i, name in enumerate(names):
                teams[i % num_teams].append(name)

            # Prepare the response
            response = 'Teams:\n'
            for i, team in enumerate(teams, start=1):
                response += f'Team {i}: {", ".join(team)}\n'

            await message.channel.send(response)
        except Exception as e:
            await message.channel.send('Error: Please use the correct format: $teams name1, name2, name3, ... / number_of_teams')

client.run(TOKEN)
