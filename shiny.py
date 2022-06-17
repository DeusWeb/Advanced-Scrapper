from googlesearch import search 
from colorama import Fore
from pystyle import *
import os
import requests
import urllib.request
import time

banneranonfile = f"""{Fore.LIGHTBLACK_EX}
     ╔═╗╔╗╔╔═╗╔╗╔╔═╗╦╦  ╔═╗  ╔═╗╔═╗╦═╗╔═╗╔═╗╔═╗╔═╗╦═╗
     ╠═╣║║║║ ║║║║╠╣ ║║  ║╣   ╚═╗║  ╠╦╝╠═╣╠═╝╠═╝║╣ ╠╦╝
     ╩ ╩╝╚╝╚═╝╝╚╝╚  ╩╩═╝╚═╝  ╚═╝╚═╝╩╚═╩ ╩╩  ╩  ╚═╝╩╚═
           github.com/{Fore.RED}deusweb{Fore.RESET} discord.gg/{Fore.RED}vecna
"""

bannerhastebin = f"""{Fore.LIGHTBLACK_EX}
     ╦ ╦╔═╗╔═╗╔╦╗╔═╗╔╗ ╦╔╗╔  ╔═╗╔═╗╦═╗╔═╗╔═╗╔═╗╔═╗╦═╗
     ╠═╣╠═╣╚═╗ ║ ║╣ ╠╩╗║║║║  ╚═╗║  ╠╦╝╠═╣╠═╝╠═╝║╣ ╠╦╝
     ╩ ╩╩ ╩╚═╝ ╩ ╚═╝╚═╝╩╝╚╝  ╚═╝╚═╝╩╚═╩ ╩╩  ╩  ╚═╝╩╚═
           github.com/{Fore.RED}deusweb{Fore.RESET} discord.gg/{Fore.RED}vecna
"""

banner = f"""{Fore.LIGHTBLACK_EX}
        ┌─┐┬ ┬┬┌┐┌┬ ┬  ┌─┐┌─┐┬─┐┌─┐┌─┐┌─┐┌─┐┬─┐
        └─┐├─┤││││└┬┘  └─┐│  ├┬┘├─┤├─┘├─┘├┤ ├┬┘
        └─┘┴ ┴┴┘└┘ ┴   └─┘└─┘┴└─┴ ┴┴  ┴  └─┘┴└─
          github.com/{Fore.RED}deusweb{Fore.RESET} discord.gg/{Fore.RED}vecna
"""

bannergithub = f"""{Fore.LIGHTBLACK_EX}
      ╔═╗╦╔╦╗╦ ╦╦ ╦╔╗   ╔═╗╔═╗╦═╗╔═╗╔═╗╔═╗╔═╗╦═╗
      ║ ╦║ ║ ╠═╣║ ║╠╩╗  ╚═╗║  ╠╦╝╠═╣╠═╝╠═╝║╣ ╠╦╝
      ╚═╝╩ ╩ ╩ ╩╚═╝╚═╝  ╚═╝╚═╝╩╚═╩ ╩╩  ╩  ╚═╝╩╚═
          github.com/{Fore.RED}deusweb{Fore.RESET} discord.gg/{Fore.RED}vecna
"""

bannerpastebin = f"""{Fore.LIGHTBLACK_EX}
    ╔═╗╔═╗╔═╗╔╦╗╔═╗╔╗ ╦╔╗╔  ╔═╗╔═╗╦═╗╔═╗╔═╗╔═╗╔═╗╦═╗
    ╠═╝╠═╣╚═╗ ║ ║╣ ╠╩╗║║║║  ╚═╗║  ╠╦╝╠═╣╠═╝╠═╝║╣ ╠╦╝
    ╩  ╩ ╩╚═╝ ╩ ╚═╝╚═╝╩╝╚╝  ╚═╝╚═╝╩╚═╩ ╩╩  ╩  ╚═╝╩╚═
          github.com/{Fore.RED}deusweb{Fore.RESET} discord.gg/{Fore.RED}vecna
"""
bannergoogle = f"""{Fore.LIGHTBLACK_EX}
    ╔═╗╔═╗╔═╗╔═╗╔╗ ╔═╗╔═╗╦╔═  ╔═╗╔═╗╦═╗╔═╗╔═╗╔═╗╔═╗╦═╗
    ╠╣ ╠═╣║  ║╣ ╠╩╗║ ║║ ║╠╩╗  ╚═╗║  ╠╦╝╠═╣╠═╝╠═╝║╣ ╠╦╝
    ╚  ╩ ╩╚═╝╚═╝╚═╝╚═╝╚═╝╩ ╩  ╚═╝╚═╝╩╚═╩ ╩╩  ╩  ╚═╝╩╚═
             github.com/{Fore.RED}deusweb{Fore.RESET} discord.gg/{Fore.RED}vecna
"""

choosebanner = f"""
\n                     {Fore.LIGHTRED_EX}[{Fore.LIGHTBLACK_EX}1{Fore.LIGHTRED_EX}] {Fore.LIGHTWHITE_EX}-{Fore.LIGHTYELLOW_EX} Anonfile scrapper
\n                     {Fore.LIGHTRED_EX}[{Fore.LIGHTBLACK_EX}2{Fore.LIGHTRED_EX}] {Fore.LIGHTWHITE_EX}-{Fore.LIGHTWHITE_EX} Github scrapper
\n                     {Fore.LIGHTRED_EX}[{Fore.LIGHTBLACK_EX}3{Fore.LIGHTRED_EX}] {Fore.LIGHTWHITE_EX}-{Fore.LIGHTCYAN_EX} Pastebin scrapper
\n                     {Fore.LIGHTRED_EX}[{Fore.LIGHTBLACK_EX}4{Fore.LIGHTRED_EX}] {Fore.LIGHTWHITE_EX}-{Fore.LIGHTMAGENTA_EX} Facebook scrapper
\n                     {Fore.LIGHTRED_EX}[{Fore.LIGHTBLACK_EX}5{Fore.LIGHTRED_EX}] {Fore.LIGHTWHITE_EX}-{Fore.LIGHTRED_EX} Hastebin scrapper
"""

def githubscrap():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Center.XCenter (bannergithub))
    dorks = input(Center.XCenter (f"{Fore.LIGHTBLACK_EX}\n\nYour search {Fore.LIGHTRED_EX}-> "))
    query = f""" "site:"github.com" "{dorks}" """
    for j in search(query, tld="com", num=40, stop=40, pause=2): 
        print(Center.XCenter (j)) 

def hastebin():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Center.XCenter (bannerhastebin))
    dorks = input(Center.XCenter (f"{Fore.LIGHTBLACK_EX}\n\nYour search {Fore.LIGHTRED_EX}-> "))
    query = f""" site:"http://bin.shortbin.eu" "{dorks}" """
    for j in search(query, tld="com", num=40, stop=40, pause=2): 
        print(Center.XCenter (j)) 


def anonscrap():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Center.XCenter (banneranonfile))
    dorks = input(Center.XCenter (f"{Fore.LIGHTBLACK_EX}\n\nYour search {Fore.LIGHTRED_EX}-> "))
    query = f""" "site:"anonfiles.com" "{dorks}" """
    for j in search(query, tld="com", num=40, stop=40, pause=2): 
        print(Center.XCenter (j)) 

def pastebinscrap():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Center.XCenter (bannerpastebin))
    dorks = input(Center.XCenter (f"{Fore.LIGHTBLACK_EX}\n\nYour search {Fore.LIGHTRED_EX}-> "))
    query = f""" "site:"pastebin.com" "{dorks}" """
    for j in search(query, tld="com", num=40, stop=40, pause=2): 
        print(Center.XCenter (j)) 

def facebookscrap():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Center.XCenter (bannergoogle))
    dorks = input(Center.XCenter (f"{Fore.LIGHTBLACK_EX}\n\nPrénom Nom {Fore.LIGHTRED_EX}-> "))
    query = f""" "facebook.com" "{dorks}" """
    for j in search(query, tld="com", num=40, stop=40, pause=2): 
        print(Center.XCenter (j)) 

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Center.XCenter (banner))
    print(Center.XCenter (choosebanner))
    choice = input(Center.XCenter (f"{Fore.LIGHTBLACK_EX}\n\nYour choice {Fore.LIGHTRED_EX}-> "))
    if choice == "1":
        anonscrap()
    if choice == "2":
        githubscrap()
    if choice == "3":
        pastebinscrap()
    if choice == "4":
        facebookscrap()
    if choice == "5":
        hastebin()
menu()