![](.github/images/HammerBot_Header_noborder.png)
<div align="center">
  
![GitHub Contributors](https://img.shields.io/github/contributors/makayla-moster/HammerBot.svg?style=flat-square) ![GitHub top language](https://img.shields.io/github/languages/top/makayla-moster/HammerBot?style=flat-square) ![GitHub issues](https://img.shields.io/github/issues/makayla-moster/HammerBot?style=flat-square) ![License](https://img.shields.io/github/license/makayla-moster/HammerBot.svg?style=flat-square) 
  
</div>

HammerBot is a discord bot built for an Age of Empire II streamer's discord server. HammerBot features Age of Empires II specific commands, such as `!whichciv <techName>` which returns a list of civs that get that specific technology in-game.  

  
Specific features include:
- Team civilization randomizer for 2v2s, 3v3s, and 4v4s that takes into account pocket or flank positions
- Finding out if a civilization has a specific technology or unit
- Returning in-game [taunts](https://ageofempires.fandom.com/wiki/Taunts)
- Player rank and match commands with info pulled from the [aoe2.net](https://aoe2.net/#api) API
- And more!


![](.github/images/Packages_Header_2.png)
---
<!-- ## Python Packages & Software -->        
![Python Package](https://img.shields.io/badge/made%20with-python%203.9+-blue.svg?style=flat-square&logo=Python)

HammerBot is built with [Disnake](https://github.com/DisnakeDev/disnake), an API wrapper for Discord.

Other packages/libraries used inclue:
- asyncio
- aiohttp
- poetry

HammerBot currently has a very simple setup, where all features are split into their own cogs. 

We currently have cogs for:  
- Age of Empires 2 player info
- Age of Empires 2 taunts
- Error handling
- Bot services (help and info commands)

<!-- ## Contributing to HammerBot --> 
![](.github/images/Contributing_Header-02.png)
---

### Issues & Bugs
If a bug or any unintended behavior is discovered, please report it by creating an issue [here](https://github.com/makayla-moster/HammerBot/issues).  

### HammerBot Development
If you'd like to contribute code to HammerBot, please:
1. Follow the setup guidelines & fork the repository 
2. Make any contributions in your fork       
3. Create a [pull request](https://github.com/makayla-moster/HammerBot/pulls)  

Your pull request will then be reviewed. Please read the [Contributing Guidelines](https://github.com/makayla-moster/HammerBot/blob/main/CONTRIBUTING.md) before creating your first pull request.  

### Setting Up HammerBot
#### Get a Discord Bot Token
1. Get a Discord bot token by going to the [Discord Developers](https://discordapp.com/developers/applications) website (you'll have to login)
2. Create an Application & click `Bot` in the left sidebar
3. Create a bot - the name you put will be seen in the servers
4. Copy the token from this page and hold onto it
#### Prepare your Bot for your Server Connection
5. Click `OAuth2` from the left sidebar
6. Under `Scopes`, check `bot`
7. In `Bot Permissions` select `administrator` under `General Permissions`
8. Copy the link from the `Scopes` section and open it in a new tab
9. Select the server you want to add the bot to
#### Prepare your Repository
10. Fork this repository
11. `git clone` HammerBot, and `cd` into the `HammerBot` directory
12. Make a new file called `.env` and fill in the fields based off the `.env.example` file
#### Setup & Run your HammerBot
13. Setup venv with `pip3 install virtualenv` (mac/linux) or  `py -m pip install --user virtualenv` (windows)
14. Then run `virtualenv venv` (mac/linux) or `py -m venv venv` (windows)
15. Enter the virtual environment with `source venv/bin/activate` (mac/linux) or `.\venv\Scripts\activate` (windows)
16. Then let pip get the latest libraries with `pip3 install -r requirements.txt` (mac/linux) or `py -m pip install -r requirements` (windows)
17. Then test run your HammerBot with `python3 -m hammerbot.py` (mac/linux) or `py -m hammerbot.py` (windows) in the main directory
18. The bot should show up in your server and respond to commands such as `11`

<!-- After forking the repository:
1. `git clone` HammerBot, and `cd` into the `HammerBot` directory
2. Make a new file called `.env` and fill in the fields based off the `.env.example` file
3. Get a Discord bot token by going to the [Discord Developers](https://discordapp.com/developers/applications) website (you'll have to login)
4. Create an Application & click `Bot` in the left sidebar
5. Create a bot - the name you put will be seen in the servers
6. Copy the token from this page and hold onto it
7. Click `OAuth2` from the left sidebar
8. Under `Scopes`, check `bot`
9. In `Bot Permissions` select `administrator` under `General Permissions`
10. Copy the link from the `Scopes` section and open it in a new tab
11. Select the server you want to add the bot to
12. Setup venv with `pip3 install virtualenv` (mac/linux) or  `py -m pip install --user virtualenv` (windows)
13. Then run `virtualenv venv` (mac/linux) or `py -m venv venv` (windows)
14. Enter the virtual environment with `source venv/bin/activate` (mac/linux) or `.\venv\Scripts\activate` (windows)
15. Then let pip get the latest libraries with `pip3 install -r requirements.txt` (mac/linux) or `py -m pip install -r requirements` (windows)
16. Then test run your HammerBot with `python3 -m hammerbot.py` (mac/linux) or `py -m hammerbot.py` (windows) in the main directory
17. The bot should show up in your server and respond to commands such as `!11` -->
<!-- 3. Use [poetry](https://python-poetry.org) to install the necessary dependencies with `poetry install`
4. Run HammerBot with either `poetry run python3 hammerbot.py` (mac/linux) or `poetry run py hammerbot.py` (windows) -->
