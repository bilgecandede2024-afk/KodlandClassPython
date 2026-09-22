import discord
from logic import sifre_olusturucu
from logic import emoji_olusturucu
from logic import yazi_tura

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak biz de girdik abi, biraz harçlık verir misin?')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('merhaba'):
        await message.channel.send("Merhaba Abi, işte okuyoruz öyle böyle.")
    elif message.content.startswith('Nasılsın'):
        await message.channel.send("İyi işte, sadece biraz para iyi olurdu, ibanımı atsam verir misin")
    elif message.content.startswith('pass'):
        await message.channel.send(sifre_olusturucu(10))
    elif message.content.startswith('Yazı Tura'):
        await message.channel.send(yazi_tura())
    elif message.content.startswith("Emoji oluştur"):
        await message.channel.send(emoji_olusturucu())
    elif message.content.startswith("Şuan ne yapıyorsun"):
        await message.channel.send("Ya ben bilgisayar dili bilmiyorum ama şuan yanlışlıkla pentagonu hekledim sanırım")
    elif message.content.startswith("Kumru ai"):
        await message.channel.send("Üfff çok zekidir abi o, bizim mahallenin kuşu o")
    elif message.content.startswith("Tsar Bomba"):
        await message.channel.send("Aman abi, Allah göstermesin")
    elif message.content.startswith("Nerelisin"):
        await message.channel.send("Valla ben bir Maçkali, biraz Adanalıyım")
    elif message.content.startswith("Abdürrezzak"):
        await message.channel.send("Abdürrezzak Savurdur, bizim mahallenin bakkalcısı abi.")
    elif message.content.startswith('bye'):
        await message.channel.send("\U0001f642")
    else:
        await message.channel.send(message.content)

client.run("Your Token Here")
