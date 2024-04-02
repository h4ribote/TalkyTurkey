import discord
from discord import app_commands
import ai
import time

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
    print ('成功しました')
    print(f'" {client.user} "としてログイン中')
    await client.change_presence(activity=discord.Game(name="Made by h4ribote"))
    await tree.sync()


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('tu'):
        count_now = int(time.time())
        with open("db/cooldown.txt", 'r') as file:
            count_last = int(file.read())
        if (count_now - count_last) < 30:
            res = "cooldown..."
        else:
            msg = message.content.replace('tu','')
            try:
                res = ai.talk(msg)
            except:
                res = "error/エラーが発生しました"
            with open("db/cooldown.txt", 'w') as file:
                count_now = int(time.time())
                file.write(str(int(count_now)))
        await message.channel.send(res)


client.run("Paste Token here")
