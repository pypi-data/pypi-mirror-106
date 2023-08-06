#!/usr/bin/env python3

import discord #To make a discord file
from os import write #To write to sample.png
import requests #To request an image

#class noodle_wrapper(commands.Cog):
 #   """Image-modifying commands."""
baseurl = 'https://frenchnoodles.xyz/api/endpoints/'

def writeFile(res):
    file = open("sample.png", "wb")
    file.write(res.content)
    file.close


def worthless(text):
    url = f'{baseurl}worthless?&text={text}'
    res = requests.get(url)
    writeFile(res)
    imageFile = discord.File(fp="sample.png",filename="worthless.png")
    return imageFile


def drake(text1, text2):
    url = f'{baseurl}drake?text1={text1}&text2={text2}'
    res = requests.get(url)
    writeFile(res)    
    imageFile = discord.File(fp="sample.png",filename="drake.png")
    return imageFile

def presidential(text):
    url = f'{baseurl}presidentialalert?text={text}'
    res = requests.get(url)
    writeFile(res)
    imageFile = discord.File(fp="sample.png",filename="presidential.png")
    return imageFile

def spongebobburn(text):
    url = f'{baseurl}spongebobburnpaper?text={text}'
    res = requests.get(url)
    writeFile(res)    
    imageFile = discord.File(fp="sample.png",filename="spongebobburn.png")
    return imageFile

def lisastage(text):
    url = f'{baseurl}lisastage?text={text}'
    res = requests.get(url)
    writeFile(res)    
    imageFile = discord.File(fp="sample.png",filename="lisastage.png")
    return imageFile

def changemind(text):
    url = f'{baseurl}changemymind?text={text}'
    res = requests.get(url)
    writeFile(res)    
    imageFile = discord.File(fp="sample.png",filename="changemind.png")
    return imageFile

def awkwardmonkey(text):
    url = f'{baseurl}awkwardmonkey?text={text}'
    res = requests.get(url)
    writeFile(res)    
    imageFile = discord.File(fp="sample.png",filename="awkwardmonkey.png")
    return imageFile

def blur(link):
    url = f'{baseurl}blur?image={link}'
    res = requests.get(url)
    writeFile(res)    
    imageFile = discord.File(fp="sample.png",filename="blur.png")
    return imageFile

def invert(link):
    url = f'{baseurl}invert?image={link}'
    res = requests.get(url)
    writeFile(res)    
    imageFile = discord.File(fp="sample.png",filename="invert.png")
    return imageFile

def edge(link):
    url = f'{baseurl}edges?image={link}'
    res = requests.get(url)
    writeFile(res)    
    imageFile = discord.File(fp="sample.png",filename="edge.png")
    return imageFile

def circle(link):
    url = f'{baseurl}circle?image={link}'
    res = requests.get(url)
    writeFile(res)    
    imageFile = discord.File(fp="sample.png",filename="circle.png")
    return imageFile

def wide(link):
    url = f'{baseurl}wide?image={link}'
    res = requests.get(url)
    writeFile(res)    
    imageFile = discord.File(fp="sample.png",filename="wide.png")
    return imageFile

def uglyupclose(link):
    url = f'{baseurl}uglyupclose?image={link}'
    res = requests.get(url)
    writeFile(res)    
    imageFile = discord.File(fp="sample.png",filename="uglyupclose.png")
    return imageFile

def clown(link):
    url = f'{baseurl}clown?image={link}'
    res = requests.get(url)
    writeFile(res)    
    imageFile = discord.File(fp="sample.png",filename="clown.png")
    return imageFile

def restpeace(link):
    url = f'{baseurl}rip?image={link}'
    res = requests.get(url)
    writeFile(res)    
    imageFile = discord.File(fp="sample.png",filename="restpeace.png")
    return imageFile

def affectbaby(link):
    url = f'{baseurl}affectbaby?image={link}' #This was fixed in the release of 0.1.5
    res = requests.get(url)
    writeFile(res)    
    imageFile = discord.File(fp="sample.png",filename="acceftbaby.png")
    return imageFile

def trash(link):
    url = f'{baseurl}trash?image={link}'
    res = requests.get(url)
    writeFile(res)    
    imageFile = discord.File(fp="sample.png",filename="trash.png")
    return imageFile

def welcomebanner(background, avatar, title, subtitle, textcolor):
    url = f'{baseurl}welcomebanner?background={background}&avatar={avatar}&title={title}&subtitle={subtitle}&textcolor={textcolor}'
    res = requests.get(url)
    writeFile(res)    
    imageFile = discord.File(fp="sample.png",filename="welcomebanner.png")
    return imageFile

def boostercard(link):
    url = f'{baseurl}boostercard?image={link}'
    res = requests.get(url)
    writeFile(res)    
    imageFile = discord.File(fp="sample.png",filename="boostercard.png")
    return imageFile

def balancecard(background, avatar, title, top, bottom, textcolor):
    url = f'{baseurl}balancecard?background={background}&avatar={avatar}&title={title}&text1={top}&text2={bottom}&textcolor={textcolor}'
    res = requests.get(url)
    writeFile(res)    
    imageFile = discord.File(fp="sample.png",filename="balancecard.png")
    return imageFile

#python3 setup.py bdist_wheel --universal