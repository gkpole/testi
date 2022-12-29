# Copyright ©️ 2022 Sanila Ranatunga. All Rights Reserved
# You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [YouTube-Bot](https://github.com/sanila2007/YouTube_bot_telegram)

# Read GNU General Public License v3.0: https://github.com/sanila2007/YouTube_bot_telegram/blob/mai/LICENSE
# Don't forget to follow github.com/sanila2007 because I am doing these things for free and open source
# Star, fork, enjoy!

import os

class Config(object):
    API_ID = int(os.environ.get("10475996", 10475996))
    API_HASH = os.environ.get("59e438d2b2ba12ab84b9c2ae57d624c9")
    BOT_TOKEN = os.environ.get("5485921311:AAGrDW4nhOtnvfMluzFdPsrsPLvOLNEfs4I")
