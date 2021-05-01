# import nonebot
from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, Event
import yinglish


parser = on_command("yingyu ")

@parser.handle()
async def _(bot: Bot,event: Event):
    msg = str(event.get_message().extract_plain_text())
    resp = yinglish.chs2yin(msg , 1.0)
    await bot.send(event=event,message=resp)
# Export something for other plugin
# export = nonebot.export()
# export.foo = "bar"

# @export.xxx
# def some_function():
#     pass
