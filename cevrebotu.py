import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f"a")

@bot.command()
async def atik_ayirma(ctx, atik_turu:str):
    atik_mesajlari = {"plastik": "plastik geri dönüşüm kutusuna atınız",
                      "kağıt": "kağıt geri dönüşüm kutusuna atınız",
                      "cam": "cam geri dönüşüm kutusuna atınız",
                      "organik": "bu atıklardan kompost yapabilirsiniz",
                      "metal": "metal geri dönüşüm kutusuna atınız"}
    mesaj = atik_mesajlari.get(atik_turu.lower(), "Böyle bir atık türü bulunamadı plastik, kağıt, cam, organik, metal tarzında atıklar için yardımcı olabilirim.")
    await ctx.send(mesaj)

@bot.command()
async def yok_olma_suresi(ctx, atiklar:str):
    atik = {"pet_şişe": "450 yılda yok olur.",
            "muz_kabuğu": "2-5 haftada yok olur.",
            "naylon_poşet": "en az 1000 yılda yok olur.",
            "cam_şişe": "en az 4000 yılda yok olur.",
            "metal_kutular": "10-100 yılda yok olur."}
    mesaj = atik.get(atiklar.lower(), "Böyle bir atık bulunamadı pet şişe, muz kabuğu, naylon poşet, cam şişe, metal kutular hakkında yardımcı olabilirim.")
    await ctx.send(mesaj)

bot.run("TOKEN")
