import discord
import random
TOKEN='OTIxMjg1NDI1MzE2ODkyNjkz.Ybwr6g.Myu6BExCRQ3EI-AGNU-N1lmYSh8'
client=discord.Client()
@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
@client.event
async def on_message(message):
    username=str(message.author).split("#")[0]
    user_message=str(message.content)
    channel=str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')
    if message.author==client.user:
        return
    if message.channel.name=='國際貿易清流':
        if user_message.lower()=='hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower()=='bye':
            await message.channel.send(f"See toy later {username}!")
        elif user_message.lower()=='!random':
            response=f'This is your random number: {random.randrange(1000000)}'
            await message.channel.send(response)
            return
    if user_message.lower()=='!anywhere':
        await message.channel.send(f'This can be used anywhere!')
        return
client.run(TOKEN)