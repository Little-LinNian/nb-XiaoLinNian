from nonebot.plugin import on_command, on_keyword
from nonebot.adapters.cqhttp import Bot, Event
import ujson
import loguru
import random

db = ujson.load(open('data/chat.json', 'r',encoding='utf-8'))
loguru.logger.success("OWO DB LOAD SUCCESS")
parser = on_command("t ")

@parser.handle()
async def t(bot: Bot, event: Event):
    try:
        resp = db[event.get_message().extract_plain_text()]
        result = random.choice(resp)
        await bot.send(event, result)
    except KeyError:
        await bot.send(event, "No such word OWO")
