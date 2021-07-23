# import nonebot
from nonebot.plugin import on_command, on_keyword
from nonebot.adapters.cqhttp import Bot, Event
import ujson
import aiofiles
parser = on_keyword("妈")
parser1 = on_command("getma")

async def load_db() -> dict:
    try:
        async with aiofiles.open("data/ma.json", "r") as f:
            data = ujson.loads(await f.read())
        return data
    except:
        return {}


@parser.handle()
async def _(bot: Bot, event: Event):
    data = await load_db()
    if event.get_message().extract_plain_text() == "妈妈":
        return
    if not str(event.sender.user_id) in data.keys():
        data[event.sender.user_id] = 1
    else:
        data[str(event.sender.user_id)] += 1
    async with aiofiles.open("data/ma.json", "w") as f:
        await f.write(ujson.dumps(data))
    await bot.send(event,f"可恶 {event.sender.nickname} 说话带妈字")

@parser1.handle()
async def get(bot: Bot, event: Event):
    data = await load_db()
    if not str(event.sender.user_id) in  data.keys():
        await bot.send(event, f"awa 你说话还没带过妈字")
    else:
        await bot.send(event, f"你说话带了{data[str(event.sender.user_id)]}次妈字")



# 我给谁写的不用说了吧