from email import message
from discord.ext import commands
import discord
import os
import random
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
import time
from utils import *
from functions import *

kisi_sayac = 1
toplam = 0

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(":", intents=intents)

@client.event
async def on_ready():
    activity = discord.Game(name="İnstagram = @valinn17", type=3)
    await client.change_presence(status=discord.Status.do_not_disturb, activity=activity)
    print('Bot Aktif !')

@client.event
async def on_member_join(member):
    toplam = kisi_sayac + 1
    channel = await member.create_dm()
    channel2 = discord.utils.get(member.guild.text_channels, name="hosgeldiniz")
    await channel2.send(f'@{member} Adlı Kullanıcı Sunucuya Giriş Yaptı Hoşgeldin, Seninle Birlikte **{toplam}** Olduk')
    await channel.send("Selam Değerli Kullanıcı 'VALİN' Adlı Sunucumuza Hoşgeldin https://discord.gg/krYvwPBn")

@client.event
async def on_member_remove(member):
   toplam = kisi_sayac - 1
   channel = discord.utils.get(member.guild.text_channels, name="gidenler")
   await channel.send('@%s Adlı Kullanıcı Sunucudan Çıkış Yaptı !' % member)
   print(f'{member} Adlı Kullanıcı Sunucudan Çıkış Yaptı !')
    


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    some_sinan_engin_jokes = [
        (
            'Sinan Engin OSTURUYOR '
            '||https://www.youtube.com/watch?v=P0LYaHnuvg0||'
        ),
        
        ('Ben Buna Cevap Bile Vermiyorum '
        '||https://www.youtube.com/watch?v=EI3hFr7qfUA||'),

        ('Sinan Engin Falan Filan '
        '||https://www.youtube.com/watch?v=Pmuj-UQvGsg||')
    ]

    if message.content == 'sinan engin':
        response = random.choice(some_sinan_engin_jokes)
        await message.channel.send(response)

    elif message.content == 'raise-exception':
        raise discord.DiscordException









client.run(TOKEN)
