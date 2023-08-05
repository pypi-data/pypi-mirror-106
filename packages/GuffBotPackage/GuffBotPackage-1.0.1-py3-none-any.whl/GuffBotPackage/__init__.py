import fortnitepy
import json
import os
import requests
import BenBotAsync
import asyncio
import sys
import time
from datetime import datetime
from functools import partial
import random as rand
from colorama import Fore, Back, Style, init
init(autoreset=True)
import aiohttp
import sanic
from sanic.response import text
from sanic import Sanic
from termcolor import colored
import sanic
import aioconsole
from sanic import Sanic
import os
from sanic.response import text, html
from flask import Flask, render_template
from threading import Thread
import discord
from fortnitepy.ext import commands
from fortnitepy.ext import commands as fortnite_commands
from discord.ext import commands as discord_commands

#config
with open('settings.json') as f:
    try:
        data = json.load(f)
    except json.decoder.JSONDecodeError as e:
        print(Fore.RED + 'File Error:' + Fore.RESET + "Please Check (settings.json).")
        print(Fore.LIGHTRED_EX + f'\n {e}')
        exit(1)
#define get device auth
def get_device_auth_details():
    if os.path.isfile('auths.json'):
        with open('auths.json', 'r') as fp:
            return json.load(fp)
    else:
        with open('auths.json', 'w+') as fp:
            json.dump({}, fp)
    return {}

def store_device_auth_details(email, details):
    existing = get_device_auth_details()
    existing[email] = details

    with open('auths.json', 'w') as fp:
        json.dump(existing, fp)

noteasonadmin = 'noteason'
email = data['email']
password = data['password']
filename = 'auths.json'
discord_bot_token =data['TOKEN']  # the discord bots token
description = 'My discord + fortnite bot!'
creds = "use code noteason #ad •  made with ❤"
fnstatus=data['status']



app = sanic.Sanic('https://pinger.pirxcy.xyz')
discord_bot = discord.Client



os.system('cls||clear')
app = sanic.Sanic(__name__)

url = f'https://{os.getenv("REPL_SLUG")}--{os.getenv("REPL_OWNER")}.repl.co'
requests.post('https://pinger.pirxcy.xyz/api/add', json={'url': url})


botsemail=data['email']

async def get_authorization_code():
    while True:
        response = await aioconsole.ainput(f"Please Get an auth code from https://rebrand.ly/authcode sign  in and enter the response for {botsemail} here: ")
        if "redirectUrl" in response:
            response = json.loads(response)
            if "?code" not in response["redirectUrl"]:
                print(colored("Invalid response.", "red"))
                continue
            code = response["redirectUrl"].split("?code=")[1]
            return code
        else:
            if "https://accounts.epicgames.com/fnauth" in response:
                if "?code" not in response:
                    print(colored("invalid response.", "red"))
                    continue
                code = response.split("?code=")[1]
                return code
            else:
                code = response
                return code

device_auth_details = get_device_auth_details().get(data['email'], {})

prefix = '!'

client = commands.Bot(
    command_prefix=prefix,
    case_insensitive=True,
    auth=fortnitepy.AdvancedAuth(
        prompt_authorization_code=True,
        delete_existing_device_auths=True,
        authorization_code=get_authorization_code,
        **device_auth_details
    ),
    status=f'🐤{fnstatus}🐧',
    platform=fortnitepy.Platform(data['platform']),
)
description = 'GuffBot v2 Help'
discord_bot = discord_commands.Bot(
        command_prefix=data['PREFIXDISCORD'],
        description=description,
        case_insensitive=True,
        help_command=None
    )


@client.event
async def event_friend_message(message):
    print('{0.author.display_name} | Content "{0.content}"'.format(message))


@client.event
async def event_ready():
    os.system('cls||clear')
    print(Fore.LIGHTBLUE_EX + 'Fortnite Client Ready As ' + Fore.LIGHTWHITE_EX + f'{client.user.display_name}')
    coro = app.create_server(
       host='0.0.0.0',
       port=8000,
       return_asyncio_server=True,
    )
    server = await coro
    
    member = client.party.me

    await member.edit_and_keep(
        partial(
            fortnitepy.ClientPartyMember.set_outfit,
            variants = client.party.me.create_variants(material=data['style']),
            asset=data['cid'],
        ),
        partial(
            fortnitepy.ClientPartyMember.set_backpack,
            variants = client.party.me.create_variants(material=data['bidstyle']),
            asset=data['bid'],
        ),
        partial(
            fortnitepy.ClientPartyMember.set_pickaxe,
            asset=data['pid']
        ),
        partial(
            fortnitepy.ClientPartyMember.set_banner,
            icon=data['banner'],
            color=data['banner_color'],
            season_level=data['level']
        ),
        partial(
            fortnitepy.ClientPartyMember.set_battlepass_info,
            has_purchased=True,
            level=data['bp_tier']
        )
    )

    client.set_avatar(fortnitepy.Avatar(asset=data['icon'], background_colors=data['colors']))
    if data['RunDiscordBot'] == 'False':
        print(colored('Discord Bot Was Not Run', 'green'))

    else:
        await discord_bot.start(data['TOKEN'])


@client.event
async def event_party_member_join(member: fortnitepy.PartyMember) -> None:
    
    await client.party.send(
        data['joinmessage']
    )
    await set_and_update_party_prop(
        'Default:RawSquadAssignments_j',
        {
                'RawSquadAssignments': [
                        {
                        'memberId': client.user.id,
                        'absoluteMemberIdx': 1
                }
                ]
        }
        ) 
    await client.party.me.set_emote(asset=data['eid'])
    print(f" [GUFFBOT] {member.display_name} Has Joined The Lobby")


if data['platform'] == 'PS5':
    PLATFORM_web = '<i class="fab fa-playstation fa-2x text-gray-900"></i>'

elif data['platform'] == 'XBL':
   PLATFORM_web = '<i class="fab fa-xbox fa-2x text-gray-900"></i>'

elif data['platform'] == 'MAC':
    PLATFORM_web = '<i class="fab fa-apple fa-2x text-gray-900"></i>'

elif data['platform'] == 'SWT':
    PLATFORM_web = '<i class="fas fa-gamepad fa-2x text-gray-900"></i>'

elif data['platform'] == 'IOS':
    PLATFORM_web = '<i class="fab fa-apple fa-2x text-gray-900"></i>'

elif data['platform'] == 'AND':
    PLATFORM_web = '<i class="fab fa-android fa-2x text-gray-900"></i>'

elif data['platform'] == 'PSN':
    PLATFORM_web = '<i class="fab fa-playstation fa-2x text-gray-900"></i>'    

else:
    data['platform'] == 'WIN'
    PLATFORM_web = '<i class="fab fa-windows fa-2x text-gray-900"></i>'

@app.route('/')
async def index(request):
    friends = [friend.display_name for friend in client.friends]
    currentskin = client.party.me.outfit
    currentpickaxe = client.party.me.pickaxe
    currentbackpack = client.party.me.backpack
    currentemote = client.party.me.emote
    return html(f'''
    <!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<meta name="description" content="use code noteason #ad">
<meta name="author" content="GuffBot">
<title>GuffBot Dashboard</title>
<meta property="og:image" content="https://cdn.noteason.repl.co/images/logo.png">
<link rel="icon" href="https://cdn.noteason.repl.co/images/logo.png">


<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.10.0/css/all.css" type="text/css">
<link href="https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i" rel="stylesheet">

<link href="https://cdn.noteason.repl.co/css/admin-2.css" rel="stylesheet">
<link href="https://cdn.noteason.repl.co/css/style.css" rel="stylesheet">

<script data-ad-client="ca-pub-8899997837601633" async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
</head>
<body id="page-top" class="">

<div id="wrapper">

<ul class="navbar-nav bg-gradient-warning sidebar sidebar-dark accordion">

<a class="sidebar-brand d-flex align-items-center justify-content-center" href="https://discord.gg/HDD8cb9hmm">
                <div class="sidebar-brand-icon rotate-n-0">
                    <i class="fab fa-discord"></i>
                </div>
                <div class="sidebar-brand-text mx-3">GUFF<sup>BOT</sup></div>
            </a>

<hr class="sidebar-divider my-0">
<li class="nav-item active">
<a class="nav-link" href="https://discord.gg/HDD8cb9hmm">
<i class="fas fa-sign-in-alt"></i>
<span>Join Our Discord</span>
</a>
</li>
<div class="sidebar-heading" style="margin-bottom : 1em;"></div>
<li class="nav-item active">
<a class="nav-link" style="margin-top : -1em;" href="/friends">
<i class="fas fa-people-carry"></i>
<span>All Freinds</span>
</a>
</li>
<div class="sidebar-heading" style="margin-bottom : 1em;"></div>
<li class="nav-item active">
<a class="nav-link" style="margin-top : -1em;" href="/shop">
<i class="fas fa-cart-arrow-down"></i>
<span>Item Shop</span>
</a>
</li>



<hr class="sidebar-divider my-0">
<li class="nav-item">
<a class="nav-link" href="/">
<i class=""></i>
<span>use code noteason #ad</span>
</a>
 </li>


 <hr class="sidebar-divider my-0">
<li class="nav-item">
<a class="nav-link" href="https://github.com/noteason/guffbot">
<i class=""></i>
<span>GuffBot v1.1</span>
</a>
 </li>

<hr class="sidebar-divider">

<div class="text-center d-none d-md-inline">
<button class="rounded-circle border-0" id="sidebarToggle"></button>
</div>
</ul>



<hr class="sidebar-divider">

<div class="text-center d-none d-md-inline">
<button class="rounded-circle border-0" id="sidebarToggle"></button>
</div>
</ul>



<div id="content-wrapper" class="d-flex flex-column">

<div id="content">

<nav class="navbar navbar-expand navbar-light bg-white topbar mb-4 static-top shadow">

<button id="sidebarToggleTop" class="btn btn-link d-md-none rounded-circle mr-3"><i class="fa fa-bars"></i></button>

<ul class="navbar-nav ml-auto">

<li class="nav-item dropdown no-arrow mx-1">
<a class="nav-link dropdown-toggle" href="#" id="alertsDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
<i class="fab fa-githu fa-fw"></i>

<img class="img-profile rounded-circle" src="https://fortnite-api.com/images/cosmetics/br/{currentskin}/icon.png?width=450&height=450">
</a>

<span id="alert_count" class="badge badge-danger badge-counter"></span>
</a>

<div class="dropdown-list dropdown-menu dropdown-menu-right shadow animated--grow-in" aria-labelledby="alertsDropdown">
<h6 class="dropdown-header">use code noteason #ad</h6>
                                                                        <a class="dropdown-item d-flex align-items-center" href="#">
        <a class="dropdown-item d-flex align-items-center" href="#">
</a>

</div>
</li>
<div class="topbar-divider d-none d-sm-block"></div>

<li class="nav-item dropdown no-arrow">
<a class="nav-link dropdown-toggle" href="#" id="userDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
<span class="mr-2 d-none d-lg-inline text-gray-600 small">{client.user.display_name}</span>
<img class="img-profile rounded-circle" src="https://cdn.noteason.repl.co/images/logo.png">
</a>


</div>
</li>
</ul>
</nav>


<div class="container-fluid" id="page-content">
<div class="container-fluid">

<div class="d-sm-flex align-items-center justify-content-between mb-4">{client.user.display_name}
<h1 class="h3 mb-0 text-gray-800"></h1>
<a href="/" class="d-none d-sm-inline-block btn btn-sm btn-warning shadow-sm"><i class="fas fa-redo"></i> Refresh</a>
</div>

<div class="row">

<div class="col-xl-3 col-md-6 mb-4">
<div class="card border-left-white shadow h-100 py-2">
<div class="card-body">
<div class="row no-gutters align-items-center">
<div class="col mr-2">
<div class="text-xs font-weight-bold text-warning text-uppercase mb-1">PLATFORM</div>
<div class="h5 mb-0 font-weight-bold text-black">{(str((client.platform))[9:]).lower().capitalize()}</div>
</div>
<div class="col-auto">
{PLATFORM_web}
</div>
</div>
</div>
</div>
</div>

<div class="col-xl-3 col-md-6 mb-4">
<div class="card border-left-white shadow h-100 py-2">
<div class="card-body">
<div class="row no-gutters align-items-center">
<div class="col mr-2">
<div class="text-xs font-weight-bold text-warning text-uppercase mb-1">Party</div>
<div class="h5 mb-0 font-weight-bold text-gray-900">Battle Royale Lobby - {client.party.member_count} / 16</div>
</div>
<div class="col-auto">
<i class="fas fa-users fa-2x text-gray-900"></i>
</div>
</div>
</div>
</div>
</div>

<div class="col-xl-3 col-md-6 mb-4">
<div class="card border-left-white shadow h-100 py-2">
<div class="card-body">
<div class="row no-gutters align-items-center">
<div class="col mr-2">
<div class="text-xs font-weight-bold text-warning text-uppercase mb-1">Friends</div>
<div class="h5 mb-0 font-weight-bold text-gray-900">{len(friends)} / 1000</div>
</div>
<div class="col-auto">
<i class="fas fa-user-friends fa-2x text-gray-900"></i>
</div>
</div>
</div>
</div>
</div>

<div class="col-xl-3 col-md-6 mb-4">
<div class="card border-left-white shadow h-100 py-2">
<div class="card-body">
<div class="row no-gutters align-items-center">
<div class="col mr-2">
<div class="text-xs font-weight-bold text-warning text-uppercase mb-1">CID</div>
<div class="h5 mb-0 font-weight-bold text-gray-900">{client.party.me.outfit}</div>
</div>
<div class="col-auto">
<i class="fas fa-cog fa-2x text-gray-900"></i>
</div>
</div>
</div>
</div>
</div>

<div class="col-xl-3 col-md-6 mb-4">
<div class="card border-left-white shadow h-100 py-2">
<div class="card-body">
<div class="row no-gutters align-items-center">
<div class="col mr-2">
<div class="text-xs font-weight-bold text-info text-uppercase mb-1">Emote</div>
<div class="h5 mb-0 font-weight-bold text-gray-900">{client.party.me.emote}</div>
</div>
<div class="col-auto">
<i class="fas fa-music fa-2x text-gray-900"></i>
</div>
</div>
</div>
</div>
</div>






<div class="row">
<div class="col-lg-6 mb-4">


</div>
</div>
</div>
</div>
<div class="col-lg-6 mb-4">


</tbody>
</table>
</div>
</div>
</div>
</div>
</div>
</div>
</div>

</div>


<footer class="sticky-footer bg-white">
<div class="container my-auto">
<div class="copyright text-center my-auto">
<span></span><br>
<span></span>
</div>
</div>
</footer>

</div>

</div>


<a class="scroll-to-top rounded" href="#page-top"><i class="fas fa-angle-up"></i></a>



<script src="https://cdn.noteason.repl.co/js/jquery.js"></script>
<script src="https://cdn.noteason.repl.co/js/bootstrap.bundle.js"></script>

<script src="https://cdn.noteason.repl.co/js/bootstrap-notify.js"></script>



<script src="https://cdn.noteason.repl.co/js/sb-admin-2.js"></script>









</body>





    ''')

@app.route('/shop')
async def index(request):
    friends = [friend.display_name for friend in client.friends]
    currentskin = client.party.me.outfit
    currentpickaxe = client.party.me.pickaxe
    currentbackpack = client.party.me.backpack
    currentemote = client.party.me.emote
    return html(f'''
    
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<meta name="description" content="use code noteason #ad">
<meta name="author" content="GuffBot">
<title>GuffBot Dashboard</title>
<meta property="og:image" content="https://cdn.noteason.repl.co/images/logo.png">
<link rel="icon" href="https://cdn.noteason.repl.co/images/logo.png">


<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.10.0/css/all.css" type="text/css">
<link href="https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i" rel="stylesheet">

<link href="https://cdn.noteason.repl.co/css/admin-2.css" rel="stylesheet">
<link href="https://cdn.noteason.repl.co/css/style.css" rel="stylesheet">

<script data-ad-client="ca-pub-8899997837601633" async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
</head>
<body id="page-top" class="">

<div id="wrapper">

<ul class="navbar-nav bg-gradient-warning sidebar sidebar-dark accordion">

<a class="sidebar-brand d-flex align-items-center justify-content-center" href="https://discord.gg/HDD8cb9hmm">
                <div class="sidebar-brand-icon rotate-n-0">
                    <i class="fab fa-discord"></i>
                </div>
                <div class="sidebar-brand-text mx-3">GUFF<sup>BOT</sup></div>
            </a>

<hr class="sidebar-divider my-0">
<li class="nav-item active">
<a class="nav-link" href="/">
<i class="fas fa-sign-in-alt"></i>
<span>Back To Home</span>
</a>
</li>



<hr class="sidebar-divider my-0">
<li class="nav-item">
<a class="nav-link" href="/">
<i class=""></i>
<span>use code noteason #ad</span>
</a>
 </li>


 <hr class="sidebar-divider my-0">
<li class="nav-item">
<a class="nav-link" href="https://github.com/noteason/guffbot">
<i class=""></i>
<span>GuffBot v1.0</span>
</a>
 </li>

<hr class="sidebar-divider">

<div class="text-center d-none d-md-inline">
<button class="rounded-circle border-0" id="sidebarToggle"></button>
</div>
</ul>



<hr class="sidebar-divider">

<div class="text-center d-none d-md-inline">
<button class="rounded-circle border-0" id="sidebarToggle"></button>
</div>
</ul>



<div id="content-wrapper" class="d-flex flex-column">

<div id="content">

<nav class="navbar navbar-expand navbar-light bg-white topbar mb-4 static-top shadow">

<button id="sidebarToggleTop" class="btn btn-link d-md-none rounded-circle mr-3"><i class="fa fa-bars"></i></button>

<ul class="navbar-nav ml-auto">

<li class="nav-item dropdown no-arrow mx-1">
<a class="nav-link dropdown-toggle" href="#" id="alertsDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
<i class="fab fa-githu fa-fw"></i>

<img class="img-profile rounded-circle" src="https://fortnite-api.com/images/cosmetics/br/{currentskin}/icon.png?width=450&height=450">
</a>

<span id="alert_count" class="badge badge-danger badge-counter"></span>
</a>

<div class="dropdown-list dropdown-menu dropdown-menu-right shadow animated--grow-in" aria-labelledby="alertsDropdown">
<h6 class="dropdown-header">use code noteason #ad</h6>
                                                                        <a class="dropdown-item d-flex align-items-center" href="#">
        <a class="dropdown-item d-flex align-items-center" href="#">
</a>

</div>
</li>
<div class="topbar-divider d-none d-sm-block"></div>

<li class="nav-item dropdown no-arrow">
<a class="nav-link dropdown-toggle" href="#" id="userDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
<span class="mr-2 d-none d-lg-inline text-gray-600 small">{client.user.display_name}</span>
<img class="img-profile rounded-circle" src="https://cdn.noteason.repl.co/images/logo.png">
</a>


</div>
</li>
</ul>
</nav>


<div class="container-fluid" id="page-content">
<div class="container-fluid">

<div class="d-sm-flex align-items-center justify-content-between mb-4">GuffBot Item Shop
<h1 class="h3 mb-0 text-gray-800"></h1>
<a href="/shop." class="d-none d-sm-inline-block btn btn-sm btn-warning shadow-sm"><i class="fas fa-redo"></i> Refresh</a>
</div>



<div class="row">

<div class="col-xl-3 col-md-6 mb-4">
<div class="card border-left-white shadow h-100 py-2">
<div class="card-body">
<div class="row no-gutters align-items-center">
<div class="col mr-2">
<div class="text-xs font-weight-bold text-black text-uppercase mb-1">RARE</div>
<div class="h5 mb-0 font-weight-bold text-gray-800">Renegade Raider</div>
</div>
<div class="">
        <a href="/shop" class="d-none d-sm-inline-block btn btn-sm btn-warning shadow-sm"><i class="fas fa-circle"></i> Purchase</a>
        <a href="https://cdn.noteason.repl.co/gifs/rickroll.gif" class="d-none d-sm-inline-block btn btn-sm btn-warning shadow-sm"><i class="fas fa-circle"></i> Gift</a>
        <img id="placeholder-project-img" class="card-img-top" src="https://fortnite-api.com/images/cosmetics/br/CID_028_Athena_Commando_F/icon.png" alt="Failed to load the Skin">
</div>
</div>
</div>
</div>
</div>

<div class="col-xl-3 col-md-6 mb-4">
<div class="card border-left-white shadow h-100 py-2">
<div class="card-body">
<div class="row no-gutters align-items-center">
<div class="col mr-2">
<div class="text-xs font-weight-bold text-black text-uppercase mb-1">RARE</div>
<div class="h5 mb-0 font-weight-bold text-gray-800">Aerial Assault Trooper</div>
</div>
<div class="col-auto">
        <a href="/shop" class="d-none d-sm-inline-block btn btn-sm btn-warning shadow-sm"><i class="fas fa-circle"></i> Purchase</a>
        <a href="https://cdn.noteason.repl.co/gifs/rickroll.gif" class="d-none d-sm-inline-block btn btn-sm btn-warning shadow-sm"><i class="fas fa-circle"></i> Gift</a>
        <img id="placeholder-project-img" class="card-img-top" src="https://fortnite-api.com/images/cosmetics/br/CID_017_Athena_Commando_M/icon.png" alt="Failed to load the Skin">
</div>
</div>
</div>
</div>
</div>

<div class="col-xl-3 col-md-6 mb-4">
<div class="card border-left-white shadow h-100 py-2">
<div class="card-body">
<div class="row no-gutters align-items-center">
<div class="col mr-2">
<div class="text-xs font-weight-bold text-black text-uppercase mb-1">RARE</div>
<div class="h5 mb-0 font-weight-bold text-gray-800">The Original Floss</div>
</div>
<div class="col-auto">
        <a href="/shop" class="d-none d-sm-inline-block btn btn-sm btn-warning shadow-sm"><i class="fas fa-circle"></i> Purchase</a>
        <a href="https://cdn.noteason.repl.co/gifs/rickroll.gif" class="d-none d-sm-inline-block btn btn-sm btn-warning shadow-sm"><i class="fas fa-circle"></i> Gift</a>
        <img id="placeholder-project-img" class="card-img-top" src="https://cdn.noteason.repl.co/images/floss.png" alt="Failed to load the Skin">
</div>
</div>
</div>
</div>
</div>



<div class="col-xl-3 col-md-6 mb-4">
<div class="card border-left-white shadow h-100 py-2">
<div class="card-body">
<div class="row no-gutters align-items-center">
<div class="col mr-2">
<div class="text-xs font-weight-bold text-black text-uppercase mb-1">RARE</div>
<div class="h5 mb-0 font-weight-bold text-gray-800">Raiders Revenge</div>
</div>
<div class="col-auto">
        <a href="/shop" class="d-none d-sm-inline-block btn btn-sm btn-warning shadow-sm"><i class="fas fa-circle"></i> Purchase</a>
        <a href="https://cdn.noteason.repl.co/gifs/rickroll.gif" class="d-none d-sm-inline-block btn btn-sm btn-warning shadow-sm"><i class="fas fa-circle"></i> Gift</a>
        <img id="placeholder-project-img" class="card-img-top" src="https://fortnite-api.com/images/cosmetics/br/pickaxe_lockjaw/icon.png" alt="Failed to load the Skin">
</div>
</div>
</div>
</div>
</div>

<div class="col-xl-3 col-md-6 mb-4">
<div class="card border-left-white shadow h-100 py-2">
<div class="card-body">
<div class="row no-gutters align-items-center">
<div class="col mr-2">
<div class="text-xs font-weight-bold text-black text-uppercase mb-1">EXCLUSIVE</div>
<div class="h5 mb-0 font-weight-bold text-gray-800">Ikonik & Scenario</div>
</div>
<div class="col-auto">
        <a href="/shop" class="d-none d-sm-inline-block btn btn-sm btn-warning shadow-sm"><i class="fas fa-circle"></i> Purchase</a>
        <a href="https://cdn.noteason.repl.co/gifs/rickroll.gif" class="d-none d-sm-inline-block btn btn-sm btn-warning shadow-sm"><i class="fas fa-circle"></i> Gift</a>
        <img id="placeholder-project-img" class="card-img-top" src="https://fortnite-api.com/images/cosmetics/br/cid_313_athena_commando_m_kpopfashion/icon.png" alt="Failed to load the Skin">
</div>
</div>
</div>
</div>
</div>

<div class="col-xl-3 col-md-6 mb-4">
<div class="card border-left-white shadow h-100 py-2">
<div class="card-body">
<div class="row no-gutters align-items-center">
<div class="col mr-2">
<div class="text-xs font-weight-bold text-black text-uppercase mb-1">EXCLUSIVE</div>
<div class="h5 mb-0 font-weight-bold text-gray-800">Double Helix</div>
</div>
<div class="col-auto">
        <a href="/shop" class="d-none d-sm-inline-block btn btn-sm btn-warning shadow-sm"><i class="fas fa-circle"></i> Purchase</a>
        <a href="https://cdn.noteason.repl.co/gifs/rickroll.gif" class="d-none d-sm-inline-block btn btn-sm btn-warning shadow-sm"><i class="fas fa-circle"></i> Gift</a>
        <img id="placeholder-project-img" class="card-img-top" src="https://fortnite-api.com/images/cosmetics/br/CID_183_Athena_Commando_M_ModernMilitaryRed/icon.png" alt="Failed to load the Skin">
</div>
</div>
</div>
</div>
</div>
 
<div class="col-xl-3 col-md-6 mb-4">
<div class="card border-left-white shadow h-100 py-2">
<div class="card-body">
<div class="row no-gutters align-items-center">
<div class="col mr-2">
<div class="text-xs font-weight-bold text-black text-uppercase mb-1">EXCLUSIVE</div>
<div class="h5 mb-0 font-weight-bold text-gray-800">Galaxy</div>
</div>
<div class="col-auto">
        <a href="/shop" class="d-none d-sm-inline-block btn btn-sm btn-warning shadow-sm"><i class="fas fa-circle"></i> Purchase</a>
        <a href="https://cdn.noteason.repl.co/gifs/rickroll.gif" class="d-none d-sm-inline-block btn btn-sm btn-warning shadow-sm"><i class="fas fa-circle"></i> Gift</a>
        <img id="placeholder-project-img" class="card-img-top" src="https://fortnite-api.com/images/cosmetics/br/CID_175_Athena_Commando_M_Celestial/icon.png" alt="Failed to load the Skin">
</div>
</div>
</div>
</div>
</div>

<div class="col-xl-3 col-md-6 mb-4">
<div class="card border-left-white shadow h-100 py-2">
<div class="card-body">
<div class="row no-gutters align-items-center">
<div class="col mr-2">
<div class="text-xs font-weight-bold text-black text-uppercase mb-1">EXCLUSIVE</div>
<div class="h5 mb-0 font-weight-bold text-gray-800">Wonder</div>
</div>
<div class="col-auto">
        <a href="/shop" class="d-none d-sm-inline-block btn btn-sm btn-warning shadow-sm"><i class="fas fa-circle"></i> Purchase</a>
        <a href="https://cdn.noteason.repl.co/gifs/rickroll.gif" class="d-none d-sm-inline-block btn btn-sm btn-warning shadow-sm"><i class="fas fa-circle"></i> Gift</a>
        <img id="placeholder-project-img" class="card-img-top" src="https://fortnite-api.com/images/cosmetics/br/CID_434_Athena_Commando_F_StealthHonor/icon.png" alt="Failed to load the Skin">
</div>
</div>
</div>
</div>
</div>
        









<div class="row">
<div class="col-lg-6 mb-4">


</div>
</div>
</div>
</div>
<div class="col-lg-6 mb-4">


</tbody>
</table>
</div>
</div>
</div>
</div>
</div>
</div>
</div>

</div>


<footer class="sticky-footer bg-white">
<div class="container my-auto">
<div class="copyright text-center my-auto">
<span></span><br>
<span></span>
</div>
</div>
</footer>

</div>

</div>


<a class="scroll-to-top rounded" href="#page-top"><i class="fas fa-angle-up"></i></a>



<script src="https://cdn.noteason.repl.co/js/jquery.js"></script>
<script src="https://cdn.noteason.repl.co/js/bootstrap.bundle.js"></script>

<script src="https://cdn.noteason.repl.co/js/bootstrap-notify.js"></script>



<script src="https://cdn.noteason.repl.co/js/sb-admin-2.js"></script>









</body>
    ''')

@app.route('/rickroll')
async def index(request):
    friends = [friend.display_name for friend in client.friends]
    currentskin = client.party.me.outfit
    currentpickaxe = client.party.me.pickaxe
    currentbackpack = client.party.me.backpack
    currentemote = client.party.me.emote
    return html(f'''
    HOW TF DO U RICKROLLL OMG
    ''')




@app.route('/friends')
async def index(request):
    friends = [friend.display_name for friend in client.friends]
    return html(f'''
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.10.0/css/all.css" type="text/css">
<link href="https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i" rel="stylesheet">

<link href="https://cdn.noteason.repl.co/css/admin-2.css" rel="stylesheet">
<link href="https://cdn.noteason.repl.co/css/style.css" rel="stylesheet">

<script data-ad-client="ca-pub-8899997837601633" async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
</head>
<body id="page-top" class="">



</center>
<div class="col-xl-3 col-md-6 mb-4">
<div class="card-body">
<a class="nav-link" href="/">
<i class="fas fa-home"></i>
<span>Back To Main Page</span>
<div class="row no-gutters align-items-center">
<div class="col mr-2">
<div class="text-xs font-weight-bold text-danger text-uppercase mb-1">Friends</div>
<div class="h5 mb-0 font-weight-bold text-gray-800">{friends}</div>

</div>
<div class="col-auto">
<i class="fas fa-users fa-2x text-gray-300"></i>
</div>


    ''')

@client.event
async def event_device_auth_generate(details, email):
    store_device_auth_details(email, details)



@discord_bot.event
async def on_ready():
    print(Fore.LIGHTBLUE_EX + f'Discord Client Ready As {discord_bot.user.name}')
    print(Fore.LIGHTBLUE_EX + f'{discord_bot.user.id}')
    print(Fore.LIGHTGREEN_EX + 'All Clients Ready')
    await discord_bot.change_presence(activity=discord.Streaming(name=data['DiscordStatus'], url=data['TWITCH']))
    


@client.event
async def event_friend_request(request):
    await request.accept()

prefix = discord_bot.command_prefix

@discord_bot.command('botinfo', help='staartbot')
async def botinfo(ctx):
  party_size = "1"
  party_max_size = "16"
  embed = discord.Embed(
    title = f'{client.user.display_name}',
    color=0x2f3136,
    description = f'Battle Royale Lobby - {client.party.member_count} / 16',
  )


  currentskin = client.party.me.outfit
  currentpickaxe = client.party.me.pickaxe
  currentbackpack = client.party.me.backpack
  embed.set_footer(text=f'{creds}')
  embed.set_thumbnail(url=f'https://fortnite-api.com/images/cosmetics/br/{currentskin}/icon.png?width=450&height=450')
  embed.add_field(name = " CID", value = f"{currentskin}", inline=True)
  embed.add_field(name = " BID", value = f"{currentbackpack}", inline=True)
  embed.add_field(name = " PID", value = f"{currentpickaxe}", inline=True)

  await ctx.send(embed=embed)

@client.event
async def event_party_invite(invite):
    if data['joinoninvite'].lower() == 'true':
        try:
            await invite.accept()
            print(Fore.LIGHTYELLOW_EX + '[GUFFBOT] ' + Fore.RESET + f'Accepted party invite from {invite.sender.display_name}')
        except Exception:
            pass
    elif data['joinoninvite'].lower() == 'false':
        if invite.sender.id in (noteasonadmin):
            await invite.accept()
            print(Fore.LIGHTYELLOW_EX + '[GUFFBOT] ' + Fore.RESET + 'Accepted party invite from ' + Fore.LIGHTGREEN_EX + f'{invite.sender.display_name}')
        else:
            print(Fore.LIGHTYELLOW_EX + ' [GUFFBOT] ' + Fore.RESET + f'Never accepted party invite from {invite.sender.display_name}')



@client.event
async def event_friend_request(request):
    if data['friendaccept'].lower() == 'true':
        try:
            await request.accept()
            print(f' [GUFFBOT] Accepted friend request from {request.display_name}' + Fore.LIGHTBLACK_EX + f' ({lenFriends()})')
        except Exception:
            pass
    elif data['friendaccept'].lower() == 'false':
        if request.id in (noteasonadmin):
            try:
                await request.accept()
                print(Fore.LIGHTYELLOW_EX + ' [GUFFBOT] ' + Fore.RESET + 'Accepted friend request from ' + Fore.LIGHTGREEN_EX + f'{request.display_name}' + Fore.LIGHTBLACK_EX + f' ({lenFriends()})')
            except Exception:
                pass
        else:
            print(f' [GUFFBOT] Never accepted friend request from {request.display_name}')





@client.event
async def event_party_member_leave(member):
    if client.user.display_name != member.display_name:
        try:
            if client.user.id in (noteasonadmin):
                print(Fore.LIGHTGREEN_EX + f' [GUFFBOT] {member.display_name}' + Fore.RESET + 'has left the lobby.')
            else:
                await set_and_update_party_prop(
                  'Default:RawSquadAssignments_j',
                  {
                          'RawSquadAssignments':[
                            {
                              'memberId': client.user.id,
                              'absoluteMemberIdx' : 1
                            }
                          ]
                  }
                )
                print(f' [GUFFBOT] {member.display_name} has left the lobby.' + Fore.LIGHTBLACK_EX + f'Left')
        except fortnitepy.HTTPException:
            pass


@client.event
async def event_party_message(message):
    if message.author.id in (noteasonadmin):
        name = Fore.LIGHTGREEN_EX + f'{message.author.display_name}'
    else:
        name = Fore.RESET + f'{message.author.display_name}'
    print(Fore.LIGHTGREEN_EX + ' [Party] ' + f'{name}' + Fore.RESET + f': {message.content}')


@client.event
async def event_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f'That is not a command. Try {prefix}help')
    elif isinstance(error, IndexError):
        pass
    elif isinstance(error, fortnitepy.HTTPException):
        pass
    elif isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have access to that command.")
    elif isinstance(error, TimeoutError):
        await ctx.send("You took too long to respond!")
    else:
        print(error)

@discord_bot.command()
async def poll(ctx, *, message):
  embed=discord.Embed(title="poll")
  embed.add_field(name = f"{message}", value = f"Requested By {ctx.message.author.mention}", inline=True)

  message=await ctx.send(embed=embed)
  await message.add_reaction('👍')
  await message.add_reaction('👎')








@discord_bot.command(name='shop', help='Fortnite Item Shop')
async def shop(ctx):
  embed = discord.Embed(title="Fortnite Item Shop", color=0x2f3136)
  embed.set_image(url="https://fortool.fr/cm/assets/shop/en.png")
  embed.set_footer(text=f"{creds}")
  await ctx.send(embed=embed)

@discord_bot.command(pass_context=True)
async def brnews(ctx, l = None):
 
    response = requests.get(f'https://fortnite-api.com/v2/news/br?language=en')

    geted = response.json()
        
    if response.status_code == 200:

        image = geted['data']['image']

        embed = discord.Embed(title="use code noteason #ad", color=0x2f3136)
        embed.set_image(url=image)
        embed.set_footer(text=f"{creds}")

        await ctx.send(embed=embed)

    elif response.status_code == 400:
 
        error = geted['error']

        embed = discord.Embed(title='Error', 
                description=f'`{error}`')

        await ctx.send(embed=embed)

    elif response.status_code == 404:

        error =geted['error']

        embed = discord.Embed(title='Error', 
        description=f'``{error}``')

        await ctx.send(embed=embed)

@discord_bot.command(name='map', help='Shows Fortnite Map')
async def map(ctx):
    embed = discord.Embed(title="Fortnite Map", color=0x2f3136)
    embed.set_image(url="https://media.fortniteapi.io/images/map.png?showPOI=true")
    embed.set_footer(text=f"{creds}")
    await ctx.send(embed=embed)


@discord_bot.command()
async def ping(ctx):
    embed=discord.Embed(title=f" Current Ping : {round (discord_bot.latency * 1000)} ms", color=0x2f3136)
    embed.set_footer(text=f"{creds}")
    await ctx.send(embed=embed)


@discord_bot.command(name='skin', help='Change LobbyBots Skin')
async def skin(ctx, *, content = None):
    if content is None:
        embed=discord.Embed(title=f"No skin was given, try: {prefix}skin (skin name)", color=0x2f3136)
        embed.set_footer(text=f"{creds}")
        await ctx.send(embed=embed)
    elif content.upper().startswith('CID_'):
        await client.party.me.set_outfit(asset=content.upper())
        embed=discord.Embed(title=f"Set Outfit To {content}", color=0x2f3136)
        embed.set_thumbnail(url=f"https://fortnite-api.com/images/cosmetics/br/{content}/icon.png?width=450&height=450")
        embed.set_footer(text=f"{creds}")
        await ctx.send(embed=embed)
    else:
        try:
            cosmetic = await BenBotAsync.get_cosmetic(
                lang="en",
                searchLang="en",
                name=content,
                backendType="AthenaCharacter"
            )
            await client.party.me.set_outfit(asset=cosmetic.id)
            embed=discord.Embed(title=f"Set Outfit To {cosmetic.name}",description=f'**{cosmetic.id}**', color=0x2f3136)
            embed.set_thumbnail(url=f"https://fortnite-api.com/images/cosmetics/br/{cosmetic.id}/icon.png?width=450&height=450")
            embed.set_footer(text=f"{creds}")
            await ctx.send(embed=embed)
        except BenBotAsync.exceptions.NotFound:
            embed=discord.Embed(title=f"could not find a skin named : {content}", color=0x2f3136)
            embed.set_footer(text=f"{creds}")
            await ctx.send(embed=embed)


@discord_bot.command(name='emote', help='Change LobbyBot Emote')
async def emote(ctx, *, content = None):
    if content is None:
        embed=discord.Embed(title=f"No emote was given, try: {prefix}emote (emote name)", color=0x2f3136)
        embed.set_footer(text=f"{creds}")
        await ctx.send(embed=embed)
    elif content.lower() == 'floss':
        await client.party.me.clear_emote()
        await client.party.me.set_emote(asset='EID_Floss')
        embed=discord.Embed(title="Emote set to: Floss", color=0x2f3136)
        await ctx.send(embed=embed)
    elif content.lower() == 'none':
        await client.party.me.clear_emote()
        embed=discord.Embed(title="Emote set to: None", color=0x2f3136)
        embed.set_footer(text=f"{creds}")
        await ctx.send(embed=embed)
    elif content.upper().startswith('EID_'):
        await client.party.me.clear_emote()
        await client.party.me.set_emote(asset=content.upper())
        embed=discord.Embed(title=f"Emote set to: {content}", color=0x2f3136)
        embed.set_thumbnail(url=f"https://fortnite-api.com/images/cosmetics/br/{content}/icon.png?width=450&height=450")
        embed.set_footer(text=f"{creds}")
        await ctx.send(embed=embed)
    else:
        try:
            cosmetic = await BenBotAsync.get_cosmetic(
                lang="en",
                searchLang="en",
                matchMethod="contains",
                name=content,
                backendType="AthenaDance"
            )
            await client.party.me.clear_emote()
            await client.party.me.set_emote(asset=cosmetic.id)
            embed=discord.Embed(title=f"Emote set to: {cosmetic.name}", color=0x2f3136)
            embed.set_thumbnail(url=f"https://fortnite-api.com/images/cosmetics/br/{cosmetic.id}/icon.png?width=450&height=450")
            embed.set_footer(text=f"{creds}")
            await ctx.send(embed=embed)
        except BenBotAsync.exceptions.NotFound:
            embed=discord.Embed(title=f"Could not find an emote named: {content}", color=0x2f3136)
            embed.set_footer(text=f"{creds}")
            await ctx.send(embed=embed)

@discord_bot.command(name='backbling', help='Change LobbyBot Backbling')
async def backbling(ctx, *, content = None):
    if content is None:
        embed=discord.Embed(title=f"No backbling was given, try: {prefix}backbling (backpack name)", color=0x2f3136)
        embed.set_footer(text=f"{creds}")
        await ctx.send(embed=embed)
    elif content.lower() == 'none':
        await client.party.me.clear_backpack()
        embed=discord.Embed(title="Backbling set to None", color=0x2f3136)
        embed.set_footer(text=f"{creds}")
        await ctx.send(embed=embed)
    elif content.upper().startswith('BID_'):
        await client.party.me.set_backpack(asset=content.upper())
        embed=discord.Embed(title=f"Backbling set to: {content}", color=0x2f3136)
        embed.set_thumbnail(url=f"https://fortnite-api.com/images/cosmetics/br/{content}/icon.png?width=450&height=450")
        embed.set_footer(text=f"{creds}")
        await ctx.send(embed=embed)
    else:
        try:
            cosmetic = await BenBotAsync.get_cosmetic(
                lang="en",
                searchLang="en",
                matchMethod="contains",
                name=content,
                backendType="AthenaBackpack"
            )
            await client.party.me.set_backpack(asset=cosmetic.id)
            embed=discord.Embed(title=f"Backbling set to: {cosmetic.name}", color=0x2f3136)
            embed.set_thumbnail(url=f"https://fortnite-api.com/images/cosmetics/br/{cosmetic.id}/icon.png?width=450&height=450")
            embed.set_footer(text=f"{creds}")
            await ctx.send(embed=embed)
        except BenBotAsync.exceptions.NotFound:
            embed=discord.Embed(title=f"Could not find a backpack named: {content}", color=0x2f3136)
            embed.set_footer(text=f"{creds}")
            await ctx.send(embed=embed)

@discord_bot.command(name='pickaxe', help='Change LobbyBots PickAxe')
async def pickaxe(ctx, *, content = None):
    if content is None:
        embed=discord.Embed(title=f"No pickaxe was given, try: {prefix}pickaxe (pickaxe name)", color=0x2f3136)
        embed.set_footer(text=f"{creds}")
        await ctx.send(embed=embed)
    elif content.upper().startswith('Pickaxe_'):
        await client.party.me.set_pickaxe(asset=content.upper())
        embed=discord.Embed(title=f"Pickaxe set to: {content}", color=0x2f3136)
        embed.set_thumbnail(url=f"https://fortnite-api.com/images/cosmetics/br/{content}/icon.png?width=450&height=450")
        embed.set_footer(text=f"{creds}")
        await ctx.send(embed=embed)
    else:
        try:
            cosmetic = await BenBotAsync.get_cosmetic(
                lang="en",
                searchLang="en",
                matchMethod="contains",
                name=content,
                backendType="AthenaPickaxe"
            )
            await client.party.me.set_pickaxe(asset=cosmetic.id)
            embed=discord.Embed(title=f"Pickaxe set to: {cosmetic.name}", color=0x2f3136)
            embed.set_thumbnail(url=f"https://fortnite-api.com/images/cosmetics/br/{cosmetic.id}/icon.png?width=450&height=450")
            embed.set_footer(text=f"{creds}")
            await ctx.send(embed=embed)
        except BenBotAsync.exceptions.NotFound:
            embed=discord.Embed(title=f"Could not find a pickaxe named: {content}", color=0x2f3136)
            embed.set_footer(text=f"{creds}")
            await ctx.send(embed=embed)

@discord_bot.command(name='banner', help='Change Bots Banner/BannerColor')
async def banner(ctx, args1 = None, args2 = None):
    if (args1 is not None) and (args2 is None):
        if args1.startswith('defaultcolor'):
            await client.party.me.set_banner(
                color = args1
            )
            embed=discord.Embed(title=f"Banner color set to: {args1}", color=0x2f3136)
            embed.set_footer(text=f"{creds}")
            await ctx.send(embed=embed)

        elif args1.isnumeric() == True:
            await client.party.me.set_banner(
                color = 'defaultcolor' + args1
            )
            embed=discord.Embed(title=f"Banner color set to: defaultcolor{args1}", color=0x2f3136)
            embed.set_footer(text=f"{creds}")
            await ctx.send(embed=embed)

        else:
            await client.party.me.set_banner(
                icon = args1
            )
            embed=discord.Embed(title=f"Banner Icon set to: {args1}", color=0x2f3136)
            embed.set_footer(text=f"{creds}")
            await ctx.send(embed=embed)

    elif (args1 is not None) and (args2 is not None):
        if args2.startswith('defaultcolor'):
            await client.party.me.set_banner(
                icon = args1,
                color = args2
            )
            embed=discord.Embed(title=f"Banner icon set to: {args1} -- Banner color set to: {args2}", color=0x2f3136)
            embed.set_footer(text=f"{creds}")
            await ctx.send(embed=embed)
        
        elif args2.isnumeric() == True:
            await client.party.me.set_banner(
                icon = args1,
                color = 'defaultcolor' + args2
            )
            embed=discord.Embed(title=f"Banner icon set to: {args1} -- Banner color set to: defaultcolor{args2}", color=0x2f3136)
            embed.set_footer(text=f"{creds}")
            await ctx.send(embed=embed)

        else:
            embed=discord.Embed(title=f"Not proper format. Try: {prefix}banner (Banner ID) (Banner Color ID)")
            embed.set_footer(text=f"{creds}")
            await ctx.send(embed=embed)


copied_player = ""


@discord_bot.command(name='send', help='send message to party chat')
async def send(ctx, *, message = None):
    if message is not None:
        await client.party.send(message)
        embed=discord.Embed(title=f"Sent 『{message}』  to party chat", color=0x2f3136)
        embed.set_footer(text=f"{creds}")
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title=f"No message was given. Try: {prefix}send (message)", color=0x2f3136)
        embed.set_footer(text=f"{creds}")
        await ctx.send(embed=embed)

@discord_bot.command(name='level', help='Change LobbyBots Level')
async def level(ctx, level = None):
    if level is None:
        embed=discord.Embed(title=f"No level was given. Try: {prefix}level (number)", color=0x2f3136)
        embed.set_footer(text=f"{creds}")
        await ctx.send(embed=embed)
    else:
        await client.party.me.set_banner(season_level=level)
        embed=discord.Embed(title=f"Level set to: {level}", color=0x2f3136)
        embed.set_footer(text=f"{creds}")
        await ctx.send(embed=embed)

@discord_bot.command(name='magic', help='Preforms a magic trick')
async def magic(ctx: fortnitepy.ext.commands.Context):
    await client.party.me.set_emote(asset="EID_Scholar")
    await asyncio.sleep(3.40)
    await client.party.me.set_outfit("CID_dababy") 
    embed=discord.Embed(title="Poof! Magic Trick", color=0x2f3136)
    embed.set_thumbnail(url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/160/apple/271/magic-wand_1fa84.png")
    embed.set_footer(text=f"{creds}")
    await ctx.send(embed=embed) 

@discord_bot.command(name='tonylopez', help='Equips The Unreleased Tony Lopez Locker Bundle')
async def tonylopez(ctx: fortnitepy.ext.commands.Context):
    await client.party.me.set_outfit("CID_991_Athena_Commando_M_Nightmare_NM1C8")

    await asyncio.sleep(1.00)
    await client.party.me.set_emote(asset="EID_RideThePony_Athena")
    embed=discord.Embed(title="Outfit Set To Tony Lopez #ilikekids", color=0x2f3136)
    embed.set_thumbnail(url="https://cdn.noteason.repl.co/images/tonylopez.png")
    embed.set_footer(text=f"{creds}")
    await ctx.send(embed=embed) 
    await asyncio.sleep(1.00) 
    

@discord_bot.command(name='pinkghoul', help='Wears Pink Ghoul Trooper')
async def pinkghoul(ctx):
    variants = client.party.me.create_variants(material=3)

    await client.party.me.set_outfit(
        asset='CID_029_Athena_Commando_F_Halloween',
        variants=variants
    )
    
    embed=discord.Embed(title="Skin set to: Pink Ghoul Trooper", color=0x2f3136)
    embed.set_thumbnail(url="http://www.pngmart.com/files/12/Fortnite-Ghoul-Trooper-PNG-Transparent-Image.png")
    embed.set_footer(text=f"{creds}")
    await ctx.send(embed=embed)



@discord_bot.command(name='purpleskull', help='Equips Purple Skull Trooper')
async def purpleskull(ctx):
    variants = client.party.me.create_variants(clothing_color=1)

    await client.party.me.set_outfit(
        asset='CID_030_Athena_Commando_M_Halloween',
        variants = variants
    )
    
    embed=discord.Embed(title="Skin set to: Purple Skull Trooper", color=0x2f3136)
    embed.set_thumbnail(url="https://i.redd.it/sgnjl7agwdl51.png")
    embed.set_footer(text=f"{creds}")
    await ctx.send(embed=embed)

@discord_bot.command(name='check', help='Equips Checkered Renegade Raider')
async def check(ctx):
    variants = client.party.me.create_variants(material=2)

    await client.party.me.set_outfit(
        asset='CID_028_Athena_Commando_F',
        variants=variants
    )

    embed=discord.Embed(title="Skin set to: Checkered Renegade", color=0x2f3136)
    embed.set_thumbnail(url="https://pbs.twimg.com/media/D1cyc5BWwAARd4g.png")
    embed.set_footer(text=f"{creds}")
    await ctx.send(embed=embed)

@discord_bot.command(name='leave', help='Leave The Party')
async def leave(ctx):
    await client.party.me.leave()
    embed=discord.Embed(title="Left party.", color=0x2f3136)
    embed.set_footer(text=f"{creds}")
    await ctx.send(embed=embed)



@discord_bot.command(name='kick', help='Kick Ass Holes')
async def kick(ctx, *, member = None):
    if member is not None:
        if member.lower() == 'all':
            members = client.party.members

            for m in members:
                try:
                    member = await client.get_user(m)
                    await member.kick()
                except fortnitepy.Forbidden:
                    embed=discord.Embed(title="I am not party leader.", color=0x2f3136)
                    embed.set_footer(text=f"{creds}")
                    await ctx.send(embed=embed)

            embed=discord.Embed(title="Kicked everyone in the party", color=0x2f3136)
            embed.set_footer(text=f"{creds}")
            await ctx.send(embed=embed)

        else:
            try:
                user = await client.fetch_profile(member)
                member = client.party.members.get(user.id)
                if member is None:
                    embed=discord.Embed(title="Couldn't find that user. Are you sure they're in the party?", color=0x2f3136)
                    embed.set_footer(text=f"{creds}")
                    await ctx.send(embed=embed)

                await member.kick()
                embed=discord.Embed(title=f"Kicked: {member.display_name}", color=0x2f3136)
                await ctx.send(embed=embed)
            except fortnitepy.Forbidden:
                embed=discord.Embed(title="I can't kick that user because I am not party leader", color=0x2f3136)
                embed.set_footer(text=f"{creds}")
                await ctx.send(embed=embed)
            except AttributeError:
                embed=discord.Embed(title="Couldn't find that user.", color=0x2f3136)
                embed.set_footer(text=f"{creds}")
                await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title=f"No member was given. Try: {prefix}kick (user)", color=0x2f3136)
        embed.set_footer(text=f"{creds}")
        await ctx.send(embed=embed)

@discord_bot.command(name='block', help='block ass holes')
async def block(ctx, *, user = None):
    if user is not None:
        try:
            user = await client.fetch_profile(user)
            friends = client.friends

            if user.id in friends:
                try:
                    await user.block()
                    embed=discord.Embed(title=f"Blocked {user.display_name}", color=0x2f3136)
                    embed.set_footer(text=f"{creds}", color=0x2f3136)
                    await ctx.send(embed=embed)
                except fortnitepy.HTTPException:
                    embed=discord.Embed(title="Something went wrong trying to block that user.", color=0x2f3136)
                    embed.set_footer(text=f"{creds}")
                    await ctx.send(embed=embed)

            elif user.id in client.blocked_users:
                embed=discord.Embed(title=f"I already have {user.display_name} blocked.", color=0x2f3136)
                embed.set_footer(text=f"{creds}")
                await ctx.send(embed=embed)
        except AttributeError:
            embed=discord.Embed(title=f"I can't find a player with that name.", color=0x2f3136)
            embed.set_footer(text=f"{creds}")
            await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title=f"No user was given. Try: {prefix}block (friend)", color=0x2f3136)
        embed.set_footer(text=f"{creds}")
        await ctx.send(embed=embed)

@discord_bot.command(name='promote', help='Promote Kings / Queens')
async def promote(ctx, *, member = None):
    if member is None:
        user = await client.fetch_profile(ctx.message.author.id)
        member = client.party.members.get(user.id)
    if member is not None:
        user = await client.fetch_profile(member.display_name)
        member = client.party.members.get(user.id)
    try:
        await member.promote()
        embed=discord.Embed(title=f"Promoted: {member.display_name}", color=0x2f3136)
        embed.set_footer(text=f"{creds}")
        await ctx.send(embed=embed)
    except fortnitepy.Forbidden:
        embed=discord.Embed(title="Client is not party leader", color=0x2f3136)
        embed.set_footer(text=f"{creds}")
        await ctx.send(embed=embed)
    except fortnitepy.PartyError:
        embed=discord.Embed(title="That person is already party leader", color=0x2f3136)
        embed.set_footer(text=f"{creds}")
        await ctx.send(embed=embed)
    except fortnitepy.HTTPException:
        embed=discord.Embed(title="Something went wrong trying to promote that member", color=0x2f3136)
        embed.set_footer(text=f"{creds}")
        await ctx.send(embed=embed)
    except AttributeError:
        embed=discord.Embed(title=f"I could not find that user", color=0x2f3136)
        embed.set_footer(text=f"{creds}")
        await ctx.send(embed=embed)


@discord_bot.command(name='hide', help='hides people')
async def hide(ctx, *, user = None):
    if client.party.me.leader:
        if user != None:
            try:
                if user is None:
                    user = await client.fetch_profile(ctx.message.author.id)
                    member = client.party.members.get(user.id)
                else:
                    user = await client.fetch_profile(user)
                    member = client.party.members.get(user.id)

                raw_squad_assignments = client.party.meta.get_prop('Default:RawSquadAssignments_j')["RawSquadAssignments"]

                for m in raw_squad_assignments:
                    if m['memberId'] == member.id:
                        raw_squad_assignments.remove(m)

                await set_and_update_party_prop(
                    'Default:RawSquadAssignments_j',
                    {
                        'RawSquadAssignments': raw_squad_assignments
                    }
                )

                embed=discord.Embed(title=f"Hid {member.display_name}", color=0x2f3136)
                embed.set_footer(text=f"{creds}")
                await ctx.send(embed=embed)
            except AttributeError:
                embed=discord.Embed(title=f"I could not find that user.", color=0x2f3136)
                embed.set_footer(text=f"{creds}")
                await ctx.send(embed=embed)
            except fortnitepy.HTTPException:
                embed=discord.Embed(title=f"I am not party leader.", color=0x2f3136)
                embed.set_footer(text=f"{creds}")
                await ctx.send(embed=embed)
        else:
            try:
                await set_and_update_party_prop(
                    'Default:RawSquadAssignments_j',
                    {
                        'RawSquadAssignments': [
                            {
                                'memberId': client.user.id,
                                'absoluteMemberIdx': 1
                            }
                        ]
                    }
                )

                embed=discord.Embed(title=f"Hid everyone in the party.", color=0x2f3136)
                embed.set_footer(text=f"{creds}")
                await ctx.send(embed=embed)
            except fortnitepy.HTTPException:
                embed=discord.Embed(title=f"I am not party leader.", color=0x2f3136)
                embed.set_footer(text=f"{creds}")
                await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title=f"I need party leader to do this!", color=0x2f3136)
        embed.set_footer(text=f"{creds}")
        await ctx.send(embed=embed)


@discord_bot.command(name='ready', help='Ready Up')
async def ready(ctx):
    await client.party.me.set_ready(fortnitepy.ReadyState.READY)
    embed=discord.Embed(title=f"Ready!", color=0x2f3136)
    embed.set_footer(text=f"{creds}")
    await ctx.send(embed=embed)



@discord_bot.command(name='unready', help='UnReady The Bot')
async def unready(ctx):
    await client.party.me.set_ready(fortnitepy.ReadyState.NOT_READY)
    embed=discord.Embed(title=f"UnReady!", color=0x2f3136)
    embed.set_footer(text=f"{creds}")
    await ctx.send(embed=embed)


@discord_bot.command(name='sitin', help='sits the bot in')
async def sitin(ctx):
    await client.party.me.set_ready(fortnitepy.ReadyState.NOT_READY)
    embed=discord.Embed(title=f"Sitting in!", color=0x2f3136)
    embed.set_footer(text=f"{creds}")
    await ctx.send(embed=embed)


@discord_bot.command(name='sitout', help='Sit Out the bot')
async def sitout(ctx):
    await client.party.me.set_ready(fortnitepy.ReadyState.SITTING_OUT)
    embed=discord.Embed(title=f"Sitting out!", color=0x2f3136)
    embed.set_footer(text=f"{creds}")
    await ctx.send(embed=embed)

@discord_bot.command(name='ingame', help='Puts the bot ingame (visual)')
async def ingame(ctx, players = None):
    time = datetime.utcnow()
    if players is not None:
        if 'auto' in players.lower():
            if client.party.me.in_match():
                left = client.party.me.match_players_left
            else:
                left = 100
            await client.party.me.set_in_match(players_left=left, started_at=time)

            await asyncio.sleep(rand.randint(20, 30))

            while client.party.me.match_players_left > 5 and client.party.me.in_match():
                await client.party.me.set_in_match(players_left=client.party.me.match_players_left - rand.randint(3, 5), started_at=time),

                await asyncio.sleep(rand.randint(8, 18))

            while (client.party.me.match_players_left <= 5) and (client.party.me.match_players_left > 3):
                await client.party.me.set_in_match(players_left=client.party.me.match_players_left - rand.randint(1, 2), started_at=time)

                await asyncio.sleep(rand.randint(12, 20))

            while (client.party.me.match_players_left <= 3) and (client.party.me.match_players_left > 1):
                await client.party.me.set_in_match(players_left=client.party.me.match_players_left - 1, started_at=time)

                await asyncio.sleep(rand.randint(12, 20))

            await asyncio.sleep(6)
            await client.party.me.clear_in_match()

        elif 'leave' in players.lower():
            await client.party.me.clear_in_match()

        else:
            try:
                await client.party.me.set_in_match(players_left=int(players), started_at=time)
            except ValueError:
                embed=discord.Embed(title=f"Invalid Format Please Do !ingame number", color=0x2f3136)
                embed.set_footer(text=f"{creds}")
                await ctx.send(embed=embed)
                pass

    else:
        embed=discord.Embed(title=f"Error", color=0x2f3136)
        embed.set_footer(text=f"{creds}")
        await ctx.send(embed=embed)

@discord_bot.command(name='dababy', help='Equips Unreleased Dababy Locker Bundle')
async def dababy(ctx: fortnitepy.ext.commands.Context):
    await client.party.me.set_outfit("CID_887_Athena_Commando_M_ChOneSpitfire")
    await asyncio.sleep(1.00)
    await client.party.me.set_emote(asset="EID_JanuaryBop")
    embed=discord.Embed(title=f"Outfit Set To DaBaby. LETS GO!", color=0x2f3136)
    embed.set_thumbnail(url=f"https://cdn.noteason.repl.co/images/dababy.png")
    embed.set_footer(text=f"{creds}")
    await ctx.send(embed=embed)

@discord_bot.command(name='join', help='Join Someones Party')
async def join(ctx, *, member = None):
    try:
        if member is None:
            user = await client.fetch_profile(ctx.message.author.id)
            friend = client.get_friend(user.id)
        elif member is not None:
            user = await client.fetch_profile(member)
            friend = client.get_friend(user.id)

        await friend.join_party()
        embed=discord.Embed(title=f"Joined {friend.display_name}'s party.", color=0x2f3136)
        embed.set_footer(text=f"{creds}")
        await ctx.send(embed=embed)
    except fortnitepy.Forbidden:
        embed=discord.Embed(title=f"I can not join that party because it is private.", color=0x2f3136)
        embed.set_footer(text=f"{creds}")
        await ctx.send(embed=embed)
    except fortnitepy.PartyError:
        embed=discord.Embed(title=f"That user is already in the party.", color=0x2f3136)
        embed.set_footer(text=f"{creds}")
        await ctx.send(embed=embed)
    except fortnitepy.HTTPException:
        embed=discord.Embed(title=f"Something went wrong joining the party", color=0x2f3136)
        embed.set_footer(text=f"{creds}")
        await ctx.send(embed=embed)
    except AttributeError:
        embed=discord.Embed(title=f"I can not join that party. Are you sure I have them friended?", color=0x2f3136)
        embed.set_footer(text=f"{creds}")
        await ctx.send(embed=embed)

@discord_bot.command(name='invite', help='Invite Friends To The Party')
async def invite(ctx, *, member = None):
    if member == 'all':
        friends = client.friends
        invited = []

        try:
            for f in friends:
                friend = client.get_friend(f)

                if friend.is_online():
                    invited.append(friend.display_name)
                    await friend.invite()
            
            embed=discord.Embed(title=f"Invited {len(invited)} friends to the party.", color=0x2f3136)
            embed.set_footer(text=f"{creds}")
            await ctx.send(embed=embed)

        except Exception:
            pass

    else:
        try:
            if member is None:
                user = await client.fetch_profile(ctx.message.author.id)
                friend = client.get_friend(user.id)
            if member is not None:
                user = await client.fetch_profile(member)
                friend = client.get_friend(user.id)

            await friend.invite()
            embed=discord.Embed(title=f"Invited {friend.display_name} to the party.", color=0x2f3136)
            embed.set_footer(text=f"{creds}")
            await ctx.send(embed=embed)
        except fortnitepy.PartyError:
            embed=discord.Embed(title=f"That user is already in the party.", color=0x2f3136)
            embed.set_footer(text=f"{creds}")
            await ctx.send(embed=embed)
        except fortnitepy.HTTPException:
            embed=discord.Embed(title=f"Something went wrong inviting that user.", color=0x2f3136)
            embed.set_footer(text=f"{creds}")
            await ctx.send(embed=embed)
        except AttributeError:
            embed=discord.Embed(title=f"I can not invite that user. Are you sure I have them friended?", color=0x2f3136)
            embed.set_footer(text=f"{creds}")
            await ctx.send(embed=embed)
        except Exception:
            pass

@discord_bot.command(name='add', help='Add New Friends')
async def add(ctx, *, member = None):
    if member is not None:
        try:
            user = await client.fetch_profile(member)
            friends = client.friends

            if user.id in friends:
                embed=discord.Embed(title=f"I already have {user.display_name} as a friend", color=0x2f3136)
                embed.set_footer(text=f"{creds}")
                await ctx.send(embed=embed)
            else:
                await client.add_friend(user.id)
                embed=discord.Embed(title=f"Sent a friend request to {user.display_name}", color=0x2f3136)
                embed.set_footer(text=f"{creds}")
                await ctx.send(embed=embed)
                print(Fore.GREEN + ' [GUFFBOT] ' + Fore.RESET + 'Sent a friend request to: ' + Fore.LIGHTBLACK_EX + f'{user.display_name}')

        except fortnitepy.HTTPException:
            await ctx.send("There was a problem trying to add this friend.")
        except AttributeError:
            embed=discord.Embed(title="I can't find a player with that name.", color=0x2f3136)
            embed.set_footer(text=f"{creds}")
            await ctx.send(embed=embed)
    else:
        
        embed=discord.Embed(title=f"No user was given. Try: {prefix}add (user)", color=0x2f3136)
        embed.set_footer(text=f"{creds}")
        await ctx.send(embed=embed)











@discord_bot.command(name='item', help='Get A Cosmetic Detail')
async def item(ctx, cosnamee):
  r = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search/all?name={cosnamee}')
  rr = r.json()
  if rr['status'] == 200:
    for sub_dict in rr['data']:
      embed = discord.Embed(color=0x2f3136)
      embed.add_field(name='Name', value=f"```{sub_dict['name']}```", inline=False)
      embed.add_field(name='ID', value=f"```{sub_dict['id']}```", inline=False)
      embed.add_field(name='Description', value=f"```{sub_dict['description']}```", inline=False)
      embed.add_field(name='Type', value=f"```{sub_dict['type']['value']}```", inline=False)
      embed.add_field(name='Rarity', value=f"```{sub_dict['rarity']['value']}```", inline=False)
      if sub_dict['introduction'] == None:
        pass
      else:
        embed.add_field(name='Introduction', value=f"```{sub_dict['introduction']['text']}```", inline=False)
        embed.add_field(name='Display Asset Path', value=f"```{sub_dict['displayAssetPath']}```", inline=False)
        embed.add_field(name='Save The World', value=f"```{sub_dict['definitionPath']}```", inline=False)
        embed.set_thumbnail(url=f"https://fortnite-api.com/images/cosmetics/br/{sub_dict['id'].lower()}/icon.png")
        embed.set_footer(text=f"{creds}")
        message = await ctx.send(embed=embed)
  else:
    embed = discord.Embed(color=0x2f3136)
    embed.add_field(name='Error', value=f"```{rr['error']}```", inline=False)
    embed.set_footer(text=f"{creds}")
    message = await ctx.send(embed=embed)
    await asyncio.sleep(60)
    await message.delete()

@discord_bot.command('stop', help='kill bot')
async def stop(ctx):
  embed = discord.Embed(
    description = ("You Requested The Bot To Shut Down | Shutting Down"),
    colour = discord.Colour.green()
  )

  await ctx.send(embed=embed)
  sys.exit(1)






@discord_bot.event
async def on_message(message):
    if message.author.bot:
        return

    print(Fore.LIGHTBLUE_EX + '{0.author.display_name} | {0.content}'.format(message))
    await discord_bot.process_commands(message)






















# discord bot commands end





@client.command()
async def skin(ctx, *, content = None):
    if content is None:
        await ctx.send(f'No skin was given, try: {prefix}skin (skin name)')
    elif content.upper().startswith('CID_'):
        await client.party.me.set_outfit(asset=content.upper())
        await ctx.send(f'Skin set to: {content}')
    else:
        try:
            cosmetic = await BenBotAsync.get_cosmetic(
                lang="en",
                searchLang="en",
                name=content,
                backendType="AthenaCharacter"
            )
            await client.party.me.set_outfit(asset=cosmetic.id)
            await ctx.send(f'Skin set to: {cosmetic.name}')
        except BenBotAsync.exceptions.NotFound:
            await ctx.send(f'Could not find a skin named: {content}')


@client.command()
async def backbling(ctx, *, content = None):
    if content is None:
        await ctx.send(f'No backpack was given, try: {prefix}backpack (backpack name)')
    elif content.lower() == 'none':
        await client.party.me.clear_backpack()
        await ctx.send('Backpack set to: None')
    elif content.upper().startswith('BID_'):
        await client.party.me.set_backpack(asset=content.upper())
        await ctx.send(f'Backpack set to: {content}')
    else:
        try:
            cosmetic = await BenBotAsync.get_cosmetic(
                lang="en",
                searchLang="en",
                matchMethod="contains",
                name=content,
                backendType="AthenaBackpack"
            )
            await client.party.me.set_backpack(asset=cosmetic.id)
            await ctx.send(f'Backpack set to: {cosmetic.name}')
        except BenBotAsync.exceptions.NotFound:
            await ctx.send(f'Could not find a backpack named: {content}')


@client.command()
async def emote(ctx, *, content = None):
    if content is None:
        await ctx.send(f'No emote was given, try: {prefix}emote (emote name)')
    elif content.lower() == 'floss':
        await client.party.me.clear_emote()
        await client.party.me.set_emote(asset='EID_Floss')
        await ctx.send(f'Emote set to: Floss')
    elif content.lower() == 'none':
        await client.party.me.clear_emote()
        await ctx.send(f'Emote set to: None')
    elif content.upper().startswith('EID_'):
        await client.party.me.clear_emote()
        await client.party.me.set_emote(asset=content.upper())
        await ctx.send(f'Emote set to: {content}')
    else:
        try:
            cosmetic = await BenBotAsync.get_cosmetic(
                lang="en",
                searchLang="en",
                matchMethod="contains",
                name=content,
                backendType="AthenaDance"
            )
            await client.party.me.clear_emote()
            await client.party.me.set_emote(asset=cosmetic.id)
            await ctx.send(f'Emote set to: {cosmetic.name}')
        except BenBotAsync.exceptions.NotFound:
            await ctx.send(f'Could not find an emote named: {content}')


@client.command()
async def pickaxe(ctx, *, content = None):
    if content is None:
        await ctx.send(f'No pickaxe was given, try: {prefix}pickaxe (pickaxe name)')
    elif content.upper().startswith('Pickaxe_'):
        await client.party.me.set_pickaxe(asset=content.upper())
        await ctx.send(f'Pickaxe set to: {content}')
    else:
        try:
            cosmetic = await BenBotAsync.get_cosmetic(
                lang="en",
                searchLang="en",
                matchMethod="contains",
                name=content,
                backendType="AthenaPickaxe"
            )
            await client.party.me.set_pickaxe(asset=cosmetic.id)
            await ctx.send(f'Pickaxe set to: {cosmetic.name}')
        except BenBotAsync.exceptions.NotFound:
            await ctx.send(f'Could not find a pickaxe named: {content}')


@client.command()
async def pet(ctx, *, content = None):
    if content is None:
        await ctx.send(f'No pet was given, try: {prefix}pet (pet name)')
    elif content.lower() == 'none':
        await client.party.me.clear_pet()
        await ctx.send('Pet set to: None')
    else:
        try:
            cosmetic = await BenBotAsync.get_cosmetic(
                lang="en",
                searchLang="en",
                matchMethod="contains",
                name=content,
                backendType="AthenaPet"
            )
            await client.party.me.set_pet(asset=cosmetic.id)
            await ctx.send(f'Pet set to: {cosmetic.name}')
        except BenBotAsync.exceptions.NotFound:
            await ctx.send(f'Could not find a pet named: {content}')


@client.command()
async def emoji(ctx, *, content = None):
    if content is None:
        await ctx.send(f'No emoji was given, try: {prefix}emoji (emoji name)')
    try:
        cosmetic = await BenBotAsync.get_cosmetic(
            lang="en",
            searchLang="en",
            matchMethod="contains",
            name=content,
            backendType="AthenaEmoji"
        )
        await client.party.me.clear_emoji()
        await client.party.me.set_emoji(asset=cosmetic.id)
        await ctx.send(f'Emoji set to: {cosmetic.name}')
    except BenBotAsync.exceptions.NotFound:
        await ctx.send(f'Could not find an emoji named: {content}')

    

@client.command()
async def current(ctx, setting = None):
    if setting is None:
        await ctx.send(f"Missing argument. Try: {prefix}current (skin, backpack, emote, pickaxe, banner)")
    elif setting.lower() == 'banner':
        await ctx.send(f'Banner ID: {client.party.me.banner[0]}  -  Banner Color ID: {client.party.me.banner[1]}')
    else:
        try:
            if setting.lower() == 'skin':
                    cosmetic = await BenBotAsync.get_cosmetic_from_id(
                        cosmetic_id=client.party.me.outfit
                    )

            elif setting.lower() == 'backpack':
                    cosmetic = await BenBotAsync.get_cosmetic_from_id(
                        cosmetic_id=client.party.me.backpack
                    )

            elif setting.lower() == 'emote':
                    cosmetic = await BenBotAsync.get_cosmetic_from_id(
                        cosmetic_id=client.party.me.emote
                    )

            elif setting.lower() == 'pickaxe':
                    cosmetic = await BenBotAsync.get_cosmetic_from_id(
                        cosmetic_id=client.party.me.pickaxe
                    )

            await ctx.send(f"My current {setting} is: {cosmetic.name}")
        except BenBotAsync.exceptions.NotFound:
            await ctx.send(f"I couldn't find a {setting} name for that.")



@client.command()
async def name(ctx, *, content=None):
    if content is None:
        await ctx.send(f'No ID was given, try: {prefix}name (cosmetic ID)')
    else:
        try:
            cosmetic = await BenBotAsync.get_cosmetic_from_id(
                cosmetic_id=content
            )
            await ctx.send(f'The name for that ID is: {cosmetic.name}')
            print(f' [GUFFBOT] The name for {cosmetic.id} is: {cosmetic.name}')
        except BenBotAsync.exceptions.NotFound:
            await ctx.send(f'Could not find a cosmetic name for ID: {content}')



@client.command()
async def cid(ctx, *, content = None):
    if content is None:
        await ctx.send(f'No skin was given, try: {prefix}cid (skin name)')
    else:
        try:
            cosmetic = await BenBotAsync.get_cosmetic(
                lang="en",
                searchLang="en",
                matchMethod="contains",
                name=content,
                backendType="AthenaCharacter"
            )
            await ctx.send(f'The CID for {cosmetic.name} is: {cosmetic.id}')
            print(f' [GUFFBOT] The CID for {cosmetic.name} is: {cosmetic.id}')
        except BenBotAsync.exceptions.NotFound:
            await ctx.send(f'Could not find a skin named: {content}')
        

@client.command()
async def bid(ctx, *, content):
    if content is None:
        await ctx.send(f'No backpack was given, try: {prefix}bid (backpack name)')
    else:
        try:
            cosmetic = await BenBotAsync.get_cosmetic(
                lang="en",
                searchLang="en",
                matchMethod="contains",
                name=content,
                backendType="AthenaBackpack"
            )
            await ctx.send(f'The BID for {cosmetic.name} is: {cosmetic.id}')
            print(f' [GUFFBOT] The BID for {cosmetic.name} is: {cosmetic.id}')
        except BenBotAsync.exceptions.NotFound:
            await ctx.send(f'Could not find a backpack named: {content}')



@client.command()
async def eid(ctx, *, content):
    if content is None:
        await ctx.send(f'No emote was given, try: {prefix}eid (emote name)')
    elif content.lower() == 'floss':
        await ctx.send(f'The EID for Floss is: EID_Floss')
    else:
        try:
            cosmetic = await BenBotAsync.get_cosmetic(
                lang="en",
                searchLang="en",
                matchMethod="contains",
                name=content,
                backendType="AthenaDance"
            )
            await ctx.send(f'The EID for {cosmetic.name} is: {cosmetic.id}')
            print(f' [GUFFBOT] The EID for {cosmetic.name} is: {cosmetic.id}')
        except BenBotAsync.exceptions.NotFound:
            await ctx.send(f'Could not find an emote named: {content}')


@client.command()
async def pid(ctx, *, content):
    if content is None:
        await ctx.send(f'No pickaxe was given, try: {prefix}pid (pickaxe name)')
    else:
        try:
            cosmetic = await BenBotAsync.get_cosmetic(
                lang="en",
                searchLang="en",
                matchMethod="contains",
                name=content,
                backendType="AthenaPickaxe"
            )
            await ctx.send(f'The PID for {cosmetic.name} is: {cosmetic.id}')
            print(f' [GUFFBOT] The PID for {cosmetic.name} is: {cosmetic.id}')
        except BenBotAsync.exceptions.NotFound:
            await ctx.send(f'Could not find a pickaxe named: {content}')



@client.command()
async def random(ctx, content = None):

    skins = await BenBotAsync.get_cosmetics(
        lang="en",
        backendType="AthenaCharacter"
    )

    skin = rand.choice(skins)

    backpacks = await BenBotAsync.get_cosmetics(
        lang="en",
        backendType="AthenaBackpack"
    )

    backpack = rand.choice(backpacks)

    emotes = await BenBotAsync.get_cosmetics(
        lang="en",
        backendType="AthenaDance"
    )

    emote = rand.choice(emotes)

    pickaxes = await BenBotAsync.get_cosmetics(
        lang="en",
        backendType="AthenaPickaxe"
    )

    pickaxe = rand.choice(pickaxes)

    
    if content is None:
        me = client.party.me
        await me.set_outfit(asset=skin.id)
        await me.set_backpack(asset=backpack.id)
        await me.set_pickaxe(asset=pickaxe.id)

        await ctx.send(f'Loadout randomly set to: {skin.name}, {backpack.name}, {pickaxe.name}')
    else:
        if content.lower() == 'skin':
            await client.party.me.set_outfit(asset=skin.id)
            await ctx.send(f'Skin randomly set to: {skin.name}')

        elif content.lower() == 'backpack':
            await client.party.me.set_backpack(asset=backpack.id)
            await ctx.send(f'Backpack randomly set to: {backpack.name}')

        elif content.lower() == 'emote':
            await client.party.me.set_emote(asset=emote.id)
            await ctx.send(f'Emote randomly set to: {emote.name}')

        elif content.lower() == 'pickaxe':
            await client.party.me.set_pickaxe(asset=pickaxe.id)
            await ctx.send(f'Pickaxe randomly set to: {pickaxe.name}')

        else:
            await ctx.send(f"I don't know that, try: {prefix}random (skin, backpack, emote, pickaxe - og, exclusive, unreleased")



@client.command()
async def point(ctx, *, content = None):
    if content is None:
        await client.party.me.clear_emote()
        await client.party.me.set_emote(asset='EID_IceKing')
        await ctx.send(f'Pointing with: {client.party.me.pickaxe}')
    
    else:
        if content.upper().startswith('Pickaxe_'):
            await client.party.me.set_pickaxe(asset=content.upper())
            await client.party.me.clear_emote()
            asyncio.sleep(0.25)
            await client.party.me.set_emote(asset='EID_IceKing')
            await ctx.send(f'Pointing with: {content}')
        else:
            try:
                cosmetic = await BenBotAsync.get_cosmetic(
                    lang="en",
                    searchLang="en",
                    matchMethod="contains",
                    name=content,
                    backendType="AthenaPickaxe"
                )
                await client.party.me.set_pickaxe(asset=cosmetic.id)
                await client.party.me.clear_emote()
                await client.party.me.set_emote(asset='EID_IceKing')
                await ctx.send(f'Pointing with: {cosmetic.name}')
            except BenBotAsync.exceptions.NotFound:
                await ctx.send(f'Could not find a pickaxe named: {content}')





@client.command()
async def check(ctx):
    variants = client.party.me.create_variants(material=2)

    await client.party.me.set_outfit(
        asset='CID_028_Athena_Commando_F',
        variants=variants
    )

    await ctx.send('Skin set to: Checkered Renegade')

@client.command()
async def surgeon(ctx):
    variants = client.party.me.create_variants(parts=2)

    await client.party.me.set_outfit(
        asset='CID_216_Athena_Commando_F_Medic',
        variants=variants
    )

    await ctx.send('Skin set to: Field Surgeon (No Helmet).')

@client.command()
async def pinkghoul(ctx):
    variants = client.party.me.create_variants(material=3)

    await client.party.me.set_outfit(
        asset='CID_029_Athena_Commando_F_Halloween',
        variants=variants
    )

    await ctx.send('Skin set to: Pink Ghoul Trooper')


@client.command()
async def wildcat(ctx):
    variants = client.party.me.create_variants(material=3)

    await client.party.me.set_outfit(
        asset='CID_757_Athena_Commando_F_WildCat',
        variants=variants
    )

    await ctx.send('Skin set to: wildcat ')


@client.command()
async def purpleskull(ctx):
    variants = client.party.me.create_variants(clothing_color=1)

    await client.party.me.set_outfit(
        asset='CID_030_Athena_Commando_M_Halloween',
        variants = variants
    )

    await ctx.send('Skin set to: Purple Skull Trooper')


@client.command()
async def purpleportal(ctx):
    variants = client.party.me.create_variants(
        item='AthenaBackpack',
        particle_config='Particle',
        particle=1
    )

    await client.party.me.set_backpack(
        asset='BID_105_GhostPortal',
        variants=variants
    )

    await ctx.send('Backpack set to: Purple Ghost Portal')


@client.command()
async def goldpeely(ctx):
    variants = client.party.me.create_variants(progressive=4)

    await client.party.me.set_outfit(
        asset='CID_701_Athena_Commando_M_BananaAgent',
        variants=variants,
        enlightenment=(2, 350)
    )

    await ctx.send('Skin set to: Golden Peely')

@client.command()
async def hatlessrecon(ctx):
    variants = client.party.me.create_variants(parts=2)

    await client.party.me.set_outfit(
        asset='CID_022_Athena_Commando_F',
        variants=variants
    )

    await ctx.send('Skin set to: Hatless Recon Expert')



@client.command()
async def hologram(ctx):
    await client.party.me.set_outfit(
        asset='CID_VIP_Athena_Commando_M_GalileoGondola_SG'
    )
    
    await ctx.send("Skin set to: Hologram")



@client.command()
async def itemshop(ctx):
    previous_skin = client.party.me.outfit

    store = await client.fetch_item_shop()

    await ctx.send("Equipping all item shop skins + emotes")

    for cosmetic in store.featured_items + store.daily_items:
        for grant in cosmetic.grants:
            if grant['type'] == 'AthenaCharacter':
                await client.party.me.set_outfit(asset=grant['asset'])
                await asyncio.sleep(5)
            elif grant['type'] == 'AthenaDance':
                await client.party.me.clear_emote()
                await client.party.me.set_emote(asset=grant['asset'])
                await asyncio.sleep(5)

    await client.party.me.clear_emote()
    
    await ctx.send("Done!")

    await asyncio.sleep(1.5)

    await client.party.me.set_outfit(asset=previous_skin)



@client.command()
async def new(ctx, content = None):
    newSkins = getNewSkins()
    newEmotes = getNewEmotes()

    previous_skin = client.party.me.outfit

    if content is None:
        await ctx.send(f'There are {len(newSkins) + len(newEmotes)} new skins + emotes')

        for cosmetic in newSkins + newEmotes:
            if cosmetic.startswith('CID_'):
                await client.party.me.set_outfit(asset=cosmetic)
                await asyncio.sleep(4)
            elif cosmetic.startswith('EID_'):
                await client.party.me.clear_emote()
                await client.party.me.set_emote(asset=cosmetic)
                await asyncio.sleep(4)

    elif 'skin' in content.lower():
        await ctx.send(f'There are {len(newSkins)} new skins')

        for skin in newSkins:
            await client.party.me.set_outfit(asset=skin)
            await asyncio.sleep(4)

    elif 'emote' in content.lower():
        await ctx.send(f'There are {len(newEmotes)} new emotes')

        for emote in newEmotes:
            await client.party.me.clear_emote()
            await client.party.me.set_emote(asset=emote)
            await asyncio.sleep(4)

    await client.party.me.clear_emote()
    
    await ctx.send('Done!')

    await asyncio.sleep(1.5)

    await client.party.me.set_outfit(asset=previous_skin)

    if (content is not None) and ('skin' or 'emote' not in content.lower()):
        ctx.send(f"Not a valid option. Try: {prefix}new (skins, emotes)")



@client.command()
async def ready(ctx):
    await client.party.me.set_ready(fortnitepy.ReadyState.READY)
    await ctx.send('Ready!')



@client.command()
async def unready(ctx):
    await client.party.me.set_ready(fortnitepy.ReadyState.NOT_READY)
    await ctx.send('Unready!')


@client.command()
async def sitin(ctx):
    await client.party.me.set_ready(fortnitepy.ReadyState.NOT_READY)
    await ctx.send('Sitting in')


@client.command()
async def sitout(ctx):
    await client.party.me.set_ready(fortnitepy.ReadyState.SITTING_OUT)
    await ctx.send('Sitting out')



@client.command()
async def tier(ctx, tier = None):
    if tier is None:
        await ctx.send(f'No tier was given. Try: {prefix}tier (tier number)') 
    else:
        await client.party.me.set_battlepass_info(
            has_purchased=True,
            level=tier
        )

        await ctx.send(f'Battle Pass tier set to: {tier}')



@client.command()
async def level(ctx, level = None):
    if level is None:
        await ctx.send(f'No level was given. Try: {prefix}level (number)')
    else:
        await client.party.me.set_banner(season_level=level)
        await ctx.send(f'Level set to: {level}')



@client.command()
async def banner(ctx, args1 = None, args2 = None):
    if (args1 is not None) and (args2 is None):
        if args1.startswith('defaultcolor'):
            await client.party.me.set_banner(
                color = args1
            )
            
            await ctx.send(f'Banner color set to: {args1}')

        elif args1.isnumeric() == True:
            await client.party.me.set_banner(
                color = 'defaultcolor' + args1
            )

            await ctx.send(f'Banner color set to: defaultcolor{args1}')

        else:
            await client.party.me.set_banner(
                icon = args1
            )

            await ctx.send(f'Banner Icon set to: {args1}')

    elif (args1 is not None) and (args2 is not None):
        if args2.startswith('defaultcolor'):
            await client.party.me.set_banner(
                icon = args1,
                color = args2
            )

            await ctx.send(f'Banner icon set to: {args1} -- Banner color set to: {args2}')
        
        elif args2.isnumeric() == True:
            await client.party.me.set_banner(
                icon = args1,
                color = 'defaultcolor' + args2
            )

            await ctx.send(f'Banner icon set to: {args1} -- Banner color set to: defaultcolor{args2}')

        else:
            await ctx.send(f'Not proper format. Try: {prefix}banner (Banner ID) (Banner Color ID)')


copied_player = ""


@client.command()
async def stop(ctx):
    global copied_player
    if copied_player != "":
        copied_player = ""
        await ctx.send(f'Stopped copying all users.')
        return
    else:
        try:
            await client.party.me.clear_emote()
        except RuntimeWarning:
            pass



@client.command()
async def copy(ctx, *, username = None):
    global copied_player

    if username is None:
        user = await client.fetch_profile(ctx.message.author.id)
        member = client.party.members.get(user.id)

    elif 'stop' in username:
        copied_player = ""
        await ctx.send(f'Stopped copying all users.')
        return

    elif username is not None:
        try:
            user = await client.fetch_profile(username)
            member = client.party.members.get(user.id)
        except AttributeError:
            await ctx.send("Could not get that user.")
            return
    try:
        copied_player = member

        await client.party.me.edit_and_keep(
                partial(
                    fortnitepy.ClientPartyMember.set_outfit,
                    asset=member.outfit,
                    variants=member.outfit_variants
                ),
                partial(
                    fortnitepy.ClientPartyMember.set_backpack,
                    asset=member.backpack,
                    variants=member.backpack_variants
                ),
                partial(
                    fortnitepy.ClientPartyMember.set_pickaxe,
                    asset=member.pickaxe,
                    variants=member.pickaxe_variants
                ),
                partial(
                    fortnitepy.ClientPartyMember.set_banner,
                    icon=member.banner[0],
                    color=member.banner[1],
                    season_level=member.banner[2]
                ),
                partial(
                    fortnitepy.ClientPartyMember.set_battlepass_info,
                    has_purchased=member.battlepass_info[0],
                    level=member.battlepass_info[1]
                )
            )

        await ctx.send(f"Now copying: {member.display_name}")
    except AttributeError:
        await ctx.send("Could not get that user.")

@client.event()
async def event_party_member_outfit_change(member, before, after):
    if member == copied_player:
        await client.party.me.edit_and_keep(
            partial(
                fortnitepy.ClientPartyMember.set_outfit,
                asset=after,
                variants=member.outfit_variants
            )
        )

@client.event()
async def event_party_member_outfit_variants_change(member, before, after):
    if member == copied_player:
        await client.party.me.edit_and_keep(
            partial(
                fortnitepy.ClientPartyMember.set_outfit,
                variants=member.outfit_variants
            )
        )

@client.event()
async def event_party_member_backpack_change(member, before, after):
    if member == copied_player:
        if after is None:
            await client.party.me.clear_backpack()
        else:
            await client.party.me.edit_and_keep(
                partial(
                    fortnitepy.ClientPartyMember.set_backpack,
                    asset=after,
                    variants=member.backpack_variants
                )
            )

@client.event()
async def event_party_member_backpack_variants_change(member, before, after):
    if member == copied_player:
        await client.party.me.edit_and_keep(
            partial(
                fortnitepy.ClientPartyMember.set_backpack,
                variants=member.backpack_variants
            )
        )

@client.event()
async def event_party_member_emote_change(member, before, after):
    if member == copied_player:
        if after is None:
            await client.party.me.clear_emote()
        else:
            await client.party.me.edit_and_keep(
                partial(
                    fortnitepy.ClientPartyMember.set_emote,
                    asset=after
                )
            )

@client.event()
async def event_party_member_pickaxe_change(member, before, after):
    if member == copied_player:
        await client.party.me.edit_and_keep(
            partial(
                fortnitepy.ClientPartyMember.set_pickaxe,
                asset=after,
                variants=member.pickaxe_variants
            )
        )

@client.event()
async def event_party_member_pickaxe_variants_change(member, before, after):
    if member == copied_player:
        await client.party.me.edit_and_keep(
            partial(
                fortnitepy.ClientPartyMember.set_pickaxe,
                variants=member.pickaxe_variants
            )
        )

@client.event()
async def event_party_member_banner_change(member, before, after):
    if member == copied_player:
        await client.party.me.edit_and_keep(
            partial(
                fortnitepy.ClientPartyMember.set_banner,
                icon=member.banner[0],
                color=member.banner[1],
                season_level=member.banner[2]
            )
        )

@client.event()
async def event_party_member_battlepass_info_change(member, before, after):
    if member == copied_player:
        await client.party.me.edit_and_keep(
            partial(
                fortnitepy.ClientPartyMember.set_battlepass_info,
                has_purchased=member.battlepass_info[0],
                level=member.battlepass_info[1]
            )
        )

async def set_and_update_party_prop(schema_key: str, new_value: str):
    prop = {schema_key: client.party.me.meta.set_prop(schema_key, new_value)}
    await client.party.patch(updated=prop)


@client.command()
async def hide(ctx, *, user = None):
    if client.party.me.leader:
        if user != None:
            try:
                if user is None:
                    user = await client.fetch_profile(ctx.message.author.id)
                    member = client.party.members.get(user.id)
                else:
                    user = await client.fetch_profile(user)
                    member = client.party.members.get(user.id)

                raw_squad_assignments = client.party.meta.get_prop('Default:RawSquadAssignments_j')["RawSquadAssignments"]

                for m in raw_squad_assignments:
                    if m['memberId'] == member.id:
                        raw_squad_assignments.remove(m)

                await set_and_update_party_prop(
                    'Default:RawSquadAssignments_j',
                    {
                        'RawSquadAssignments': raw_squad_assignments
                    }
                )

                await ctx.send(f"Hid {member.display_name}")
            except AttributeError:
                await ctx.send("I could not find that user.")
            except fortnitepy.HTTPException:
                await ctx.send("I am not party leader.")
        else:
            try:
                await set_and_update_party_prop(
                    'Default:RawSquadAssignments_j',
                    {
                        'RawSquadAssignments': [
                            {
                                'memberId': bot.user.id,
                                'absoluteMemberIdx': 1
                            }
                        ]
                    }
                )

                await ctx.send("Hid everyone in the party.")
            except fortnitepy.HTTPException:
                await ctx.send("I am not party leader.")
    else:
        await ctx.send("I need party leader to do this!")


@client.command()
async def unhide(ctx):
    if client.party.me.leader:
        user = await client.fetch_profile(ctx.message.author.id)
        member = client.party.members.get(user.id)

        await member.promote()

        await ctx.send("Unhid all players.")

    else:
        await ctx.send("I am not party leader.")



@client.command()
async def avatar(ctx, *, skin = None):
    if skin is None:
        await ctx.send(f'No skin was given. Try: {prefix}avatar (skin name, cid)')
    elif skin.upper().startswith('CID_'):
        try:
            cosmetic = await BenBotAsync.get_cosmetic_from_id(
                cosmetic_id=skin.upper()
            )
            client.set_avatar(fortnitepy.Avatar(asset=cosmetic.id))
            await ctx.send(f'Avatar set to: {cosmetic.id}')
        except BenBotAsync.exceptions.NotFound:
            await ctx.send(f'Could not find the ID: {skin}')
    else:
        try:
            cosmetic = await BenBotAsync.get_cosmetic(
                lang="en",
                searchLang="en",
                name=skin,
                backendType="AthenaCharacter"
            )
            client.set_avatar(fortnitepy.Avatar(asset=cosmetic.id))
            await ctx.send(f'Avatar set to: {cosmetic.name}')
        except BenBotAsync.exceptions.NotFound:
            await ctx.send(f'Could not find a skin named: {skin}')


@commands.dm_only()
@client.command()
async def send(ctx, *, message = None):
    if message is not None:
        await client.party.send(message)
        await ctx.send(f'Sent "{message}" to party chat')
    else:
        await ctx.send(f'No message was given. Try: {prefix}send (message)')



@client.command()
async def whisper(ctx, member = None, *, message = None):
    if (member is not None) and (message is not None):
        try:
            user = await client.fetch_profile(member)
            friend = client.get_friend(user.id)

            if friend.is_online():
                await friend.send(message)
                await ctx.send("Message sent.")
            else:
                await ctx.send("That friend is offline.")
        except AttributeError:
            await ctx.send("I couldn't find that friend.")
        except fortnitepy.HTTPException:
            await ctx.send("Something went wrong sending the message.")
    else:
        await ctx.send(f"Command missing one or more arguments. Try: {prefix}whisper (friend) (message)")



@client.command()
async def match(ctx, players = None):
    time = datetime.utcnow()
    if players is not None:
        if 'auto' in players.lower():
            if client.party.me.in_match():
                left = client.party.me.match_players_left
            else:
                left = 100
            await client.party.me.set_in_match(players_left=left, started_at=time)

            await asyncio.sleep(rand.randint(20, 30))

            while client.party.me.match_players_left > 5 and client.party.me.in_match():
                await client.party.me.set_in_match(players_left=client.party.me.match_players_left - rand.randint(3, 5), started_at=time),

                await asyncio.sleep(rand.randint(8, 18))

            while (client.party.me.match_players_left <= 5) and (client.party.me.match_players_left > 3):
                await client.party.me.set_in_match(players_left=client.party.me.match_players_left - rand.randint(1, 2), started_at=time)

                await asyncio.sleep(rand.randint(12, 20))

            while (client.party.me.match_players_left <= 3) and (client.party.me.match_players_left > 1):
                await client.party.me.set_in_match(players_left=client.party.me.match_players_left - 1, started_at=time)

                await asyncio.sleep(rand.randint(12, 20))

            await asyncio.sleep(6)
            await client.party.me.clear_in_match()

        elif 'leave' in players.lower():
            await client.party.me.clear_in_match()

        else:
            try:
                await client.party.me.set_in_match(players_left=int(players), started_at=time)
            except ValueError:
                await ctx.send(f"Invalid usage. Try: {prefix}match (0-255)")
                pass

    else:
        await ctx.send(f'Incorrect usage. Try: {prefix}match (auto, #, leave)')


@client.command()
async def status(ctx, *, status = None):
    if status is not None:
        await client.set_status(status)
        await ctx.send(f'Set status to: {status}')
        print(Fore.GREEN + ' [GUFFBOT] ' + Fore.RESET + 'Changed status to: ' + Fore.LIGHTBLACK_EX + f'{status}')
    else:
        await ctx.send(f'No status was given. Try: {prefix}status (status message)')


@client.command()
async def leave(ctx):
    await client.party.me.leave()
    await ctx.send('Left party.')



@client.command()
async def kick(ctx, *, member = None):
    if member is not None:
        if member.lower() == 'all':
            members = client.party.members

            for m in members:
                try:
                    member = await client.get_user(m)
                    await member.kick()
                except fortnitepy.Forbidden:
                    await ctx.send("I am not party leader.")

            await ctx.send("Kicked everyone in the party")

        else:
            try:
                user = await client.fetch_profile(member)
                member = client.party.members.get(user.id)
                if member is None:
                    await ctx.send("Couldn't find that user. Are you sure they're in the party?")

                await member.kick()
                await ctx.send(f'Kicked: {member.display_name}')
            except fortnitepy.Forbidden:
                await ctx.send("I can't kick that user because I am not party leader")
            except AttributeError:
                await ctx.send("Couldn't find that user.")
    else:
        await ctx.send(f'No member was given. Try: {prefix}kick (user)')


@client.command()
async def promote(ctx, *, member = None):
    if member is None:
        user = await client.fetch_profile(ctx.message.author.id)
        member = client.party.members.get(user.id)
    if member is not None:
        user = await client.fetch_profile(member.display_name)
        member = client.party.members.get(user.id)
    try:
        await member.promote()
        await ctx.send(f"Promoted: {member.display_name}")
    except fortnitepy.Forbidden:
        await ctx.send("Client is not party leader")
    except fortnitepy.PartyError:
        await ctx.send("That person is already party leader")
    except fortnitepy.HTTPException:
        await ctx.send("Something went wrong trying to promote that member")
    except AttributeError:
        await ctx.send("I could not find that user")



@client.command()
async def privacy(ctx, setting = None):
    if setting is not None:
        try:
            if setting.lower() == 'public':
                await client.party.set_privacy(fortnitepy.PartyPrivacy.PUBLIC)
                await ctx.send(f"Party Privacy set to: Public")
            elif setting.lower() == 'friends':
                await client.party.set_privacy(fortnitepy.PartyPrivacy.FRIENDS)
                await ctx.send(f"Party Privacy set to: Friends Only")
            elif setting.lower() == 'private':
                await client.party.set_privacy(fortnitepy.PartyPrivacy.PRIVATE)
                await ctx.send(f"Party Privacy set to: Private")
            else:
                await ctx.send("That is not a valid privacy setting. Try: Public, Friends, or Private")
        except fortnitepy.Forbidden:
            await ctx.send("I can not set the party privacy because I am not party leader.")
    else:
        await ctx.send(f"No privacy setting was given. Try: {prefix}privacy (Public, Friends, Private)")


@client.command()
async def join(ctx, *, member = None):
    try:
        if member is None:
            user = await client.fetch_profile(ctx.message.author.id)
            friend = client.get_friend(user.id)
        elif member is not None:
            user = await client.fetch_profile(member)
            friend = client.get_friend(user.id)

        await friend.join_party()
        await ctx.send(f"Joined {friend.display_name}'s party.")
    except fortnitepy.Forbidden:
        await ctx.send("I can not join that party because it is private.")
    except fortnitepy.PartyError:
        await ctx.send("That user is already in the party.")
    except fortnitepy.HTTPException:
        await ctx.send("Something went wrong joining the party")
    except AttributeError:
        await ctx.send("I can not join that party. Are you sure I have them friended?")
        


@client.command()
async def invite(ctx, *, member = None):
    if member == 'all':
        friends = client.friends
        invited = []

        try:
            for f in friends:
                friend = client.get_friend(f)

                if friend.is_online():
                    invited.append(friend.display_name)
                    await friend.invite()
            
            await ctx.send(f"Invited {len(invited)} friends to the party.")

        except Exception:
            pass

    else:
        try:
            if member is None:
                user = await client.fetch_profile(ctx.message.author.id)
                friend = client.get_friend(user.id)
            if member is not None:
                user = await client.fetch_profile(member)
                friend = client.get_friend(user.id)

            await friend.invite()
            await ctx.send(f"Invited {friend.display_name} to the party.")
        except fortnitepy.PartyError:
            await ctx.send("That user is already in the party.")
        except fortnitepy.HTTPException:
            await ctx.send("Something went wrong inviting that user.")
        except AttributeError:
            await ctx.send("I can not invite that user. Are you sure I have them friended?")
        except Exception:
            pass



@client.command()
async def add(ctx, *, member = None):
    if member is not None:
        try:
            user = await client.fetch_profile(member)
            friends = client.friends

            if user.id in friends:
                await ctx.send(f"I already have {user.display_name} as a friend")
            else:
                await client.add_friend(user.id)
                await ctx.send(f'Sent a friend request to {user.display_name}')
                print(Fore.GREEN + ' [GUFFBOT] ' + Fore.RESET + 'Sent a friend request to: ' + Fore.LIGHTBLACK_EX + f'{user.display_name}')

        except fortnitepy.HTTPException:
            await ctx.send("There was a problem trying to add this friend.")
        except AttributeError:
            await ctx.send("I can't find a player with that name.")
    else:
        await ctx.send(f"No user was given. Try: {prefix}add (user)")







@client.command()
async def block(ctx, *, user = None):
    if user is not None:
        try:
            user = await client.fetch_profile(user)
            friends = client.friends

            if user.id in friends:
                try:
                    await user.block()
                    await ctx.send(f"Blocked {user.display_name}")
                except fortnitepy.HTTPException:
                    await ctx.send("Something went wrong trying to block that user.")

            elif user.id in client.blocked_users:
                await ctx.send(f"I already have {user.display_name} blocked.")
        except AttributeError:
            await ctx.send("I can't find a player with that name.")
    else:
        await ctx.send(f"No user was given. Try: {prefix}block (friend)")



@client.command()
async def blocked(ctx):

    blockedusers = []

    for b in client.blocked_users:
        user = client.get_blocked_user(b)
        blockedusers.append(user.display_name)
    
    await ctx.send(f'Client has {len(blockedusers)} users blocked:')
    for x in blockedusers:
        if x is not None:
            await ctx.send(x)



@client.command()
async def unblock(ctx, *, user = None):
    if user is not None:
        try:
            member = await client.fetch_profile(user)
            blocked = client.blocked_users
            if member.id in blocked:
                try:
                    await client.unblock_user(member.id)
                    await ctx.send(f'Successfully unblocked {member.display_name}')
                except fortnitepy.HTTPException:
                    await ctx.send('Something went wrong trying to unblock that user.')
            else:
                await ctx.send('That user is not blocked')
        except AttributeError:
            await ctx.send("I can't find a player with that name.")
    else:
        await ctx.send(f'No user was given. Try: {prefix}unblock (blocked user)')




client.run()