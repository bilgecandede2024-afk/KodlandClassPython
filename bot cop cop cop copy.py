import discord
import random
import os
import requests
from discord.ext import commands
from dataclasses import dataclass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event  # bot belirli bir olay gerçekleştiğinde tetiklensin.
async def on_ready():  # bot başarılı bir şekilde Discord'a bağlandığında tetiklenir
    print(f'{bot.user} olarak giriş yaptık')

@dataclass
class struct:
    StructName:str
    print(StructName)


struct("Selam")

cevre_ipuclari = [
    "Geri dönüşüm makinelerini kullanabilirsin, hem dünya kurtulur, hem para kazanırsın",
    "Atıkları dışarı atmaktan ziyade evde tutabilir, çöp kamyonlarını bekleyebilirsin",
    "Sakın yere atma, dünyayı kirletmek senin de pişman olacağın bir hareket",
    "Plastik doğada 100 yılda çok küçük çözünür, ama dert etme, bizim okulda plastik yiyen bir arkadaş var, ona senin evin adresini verebilirim istersen",
    "PET plastikle beslenen bir bakteri türü var, eğer bunu artırır, üremesine izin verirsek, plastik sıkıntımızı çözebilir.",
    "Ya şimdi atıklardan kurtulma için çok kolay yöntem var biliyor musun, at, öğüt, kurtul geç, hallet",
]

cevre_sorunlari = {
    "Plastikler": "Ya bunlar çok sıkıntılı, çok gidik, en beteri bunlar, hem çok var, hem kolay çözünmüyor, oh mis, dünya yok etme 101 resmen!",
    "Muzlar":"Dert etme yav bunları, meyve bunlar, doğanın, çözülür, hallolur",
    "Kağıtlar":"Sıkıntı ama plastik kadar değil, bu yüzden o kadar da dert etme, ama gene de israfı kötü",
    "Cam":"Camlar güneş ışığını yansıttığı için orman yangınlarına sebep olabilmektedir, bu yüzden doğaya atmamak gerekir",
    "Pil":" Piller de biraz sıkkıntılı, tıprağı zehirleyip daha pek çok soruna öncü oluyor",
    "Yiyecek atıkları":"at toprağa çözünsün, ama görüntü kirliliği oluşturmadan, işte bu kadar basit",
    "Elektronik atıklar":"Çok tezgah bunlar, sıkıntısız gibi görünürler ama sıkıntılılar yarışması olsa ikinci olurlar"
}



@bot.command()
async def geri_donusum(ctx):
    await ctx.send("Geri dönüştürülebilir malzemeler: Cam, kağıt, plastik ve metal. Unutmayın, geri dönüşüm önemlidir!" )

@bot.command()
async def yardim_et(ctx):
    await ctx.send("Tabii, evdeki atıkları geri dönüşüm makinelerine atman yeterli olacaktır dostum")

@bot.command()
async def baska(ctx):
    await ctx.send("Tamam, yardım için yerli ve milli yapay zekamız kumru ai'dan yardım alabilirsin")

@bot.command()
async def ipuclari(ctx):
    await ctx.send(random.choice(cevre_ipuclari))

@bot.command()
async def buyukresim(ctx):
    await ctx.send("Şimdi bir dünya kadar cismi sıkıştırıp (para kadar), klaradelik yapar ve her atığı içeri atarsak, atığımız olmaz, evet, saçma ama mümkün")

@bot.command()
async def cevresorunlari(ctx):
    await ctx.send(random.choice(list(cevre_sorunlari.items())))
# Bu özellik, botun kendisine gönderilen komutları tanıması için bir ön ek tanımlar.
# $ işareti komut ön eki olarak belirlenmiştir. Yani bot sadece $ ile başlayan komutları algılar.


bot.run("Your Token Here")