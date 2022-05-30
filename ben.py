import discord
import random
client = discord.Client()
TOKEN = 'OTgwNDA5OTAwMDc1MjA0NjQ4.GzZypS.UVR1GdzR9sVScwfb7rAIJhOBYEz6kqvsQGnMT8'
answer = ['yes','no']
answer_joke = ['ho-ho-ho','bruh']
@client.event
async def on_message(message):
    channel = client.get_channel(980411282148708372)
    if message.content.lower().startswith('?'):
        a = random.choice(answer)
        if a == 'no':
            with open('no.gif', 'rb') as file:
                await channel.send(file=discord.File(file, 'new_no.gif'))
        else:
            with open('yes.gif', 'rb') as file:
                await channel.send(file=discord.File(file, 'new_yes.gif'))
        await channel.send(a)
    if message.content.lower().startswith('+'):
        b = random.choice(answer_joke)
        if b == 'ho-ho-ho':
            with open('ho-ho.gif', 'rb') as file:
                await channel.send(file=discord.File(file, 'new_ho-ho.gif'))
        else:
            with open('bruh.gif', 'rb') as file:
                await channel.send(file=discord.File(file, 'new_bruh.gif'))
        await channel.send(b)
    if message.content.lower()=='-':
        with open('-.gif', 'rb') as file:
            await channel.send(file=discord.File(file, 'new_-.gif'))
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
client.run(TOKEN)