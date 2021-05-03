# import nonebot
from nonebot import get_driver
import ujson
from nonebot.adapters.cqhttp import Bot, Event
from nonebot import on_command

from .config import Config

global_config = get_driver().config
config = Config(**global_config.dict())
f = open("./src/plugins/cy2/cy2db.json")
data = ujson.loads(f.read())

parser = on_command("cy2 find ")

@parser.handle()
async def _(bot: Bot,event: Event):
    msg = event.get_message().extract_plain_text()
    try:
        resp = data[msg]
        msg = "Cy2 Song Info\n{}\n角色 {}\nEasy难度等级 y{}\nNote数 {}\nHard难度等级 {}\nNote数 {}\nChaos难度等级 {}\nNote数 {}"
        msg = msg.format(
            resp["title"],
            resp["character"],
            resp["EasyLevel"],
            resp["EasyNote"],
            resp["HardLevel"],
            resp["HardNote"],
            resp["ChaosLevel"],
            resp["ChaosNote"]
        )


        await bot.send(event,msg)
    except Exception as e:
        await bot.send(event,f"查询失败，请注意大小写qwq\n{e}")
# Export something for other plugin
# export = nonebot.export()
# export.foo = "bar"

# @export.xxx
# def some_function():
#     pass
