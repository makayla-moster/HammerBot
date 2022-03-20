![](.github/images/HammerBot_Header_noborder.png)

![GitHub Contributors](https://img.shields.io/github/contributors/makayla-moster/HammerBot.svg?style=flat-square) ![GitHub top language](https://img.shields.io/github/languages/top/makayla-moster/HammerBot?style=flat-square) ![GitHub issues](https://img.shields.io/github/issues/makayla-moster/HammerBot?style=flat-square) ![License](https://img.shields.io/github/license/makayla-moster/HammerBot.svg?style=flat-square) 

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

<!-- ## Contributing to HammerBot --> 
![](.github/images/Contributing_Header-02.png)
---

### Issues & Bugs
If a bug or any unintended behavior is discovered, please report it by creating an issue [here](https://github.com/makayla-moster/HammerBot/issues).  

### HammerBot Development
If you'd like to contribute code to HammerBot, please:
1. Fork the repository 
2. Make any contributions in your fork       
3. Create a [pull request](https://github.com/makayla-moster/HammerBot/pulls)  

Your pull request will then be reviewed. Please read the [Contributing Guidelines](https://github.com/makayla-moster/HammerBot/blob/main/CONTRIBUTING.md) before creating your first pull request.  

### Setting Up HammerBot
After forking the repository:
1. `git clone` HammerBot, and `cd` into the `HammerBot` directory
2. Make a new file called `.env` and fill in the fields based off the `.env.example` file
3. Use [poetry](https://python-poetry.org) to install the necessary dependencies with `poetry install`
4. Run HammerBot with either `poetry run python3 hammerbot.py` (mac/linux) or `poetry run py hammerbot.py` (windows)
