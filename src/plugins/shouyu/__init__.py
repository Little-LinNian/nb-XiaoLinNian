# import nonebot
from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, Event
from .beast import encode, decode


parser = on_command("兽语 ")
parser_de = on_command("解兽语 ")

@parser.handle()
async def _(bot: Bot,event: Event):
    msg = str(event.get_message().extract_plain_text())
    resp = encode(msg)
    await bot.send(event=event,message=resp)

@parser_de.handle()
async def _(bot: Bot, event: Event):
    msg = event.get_message().extract_plain_text()
    resp = decode(msg)
    await bot.send(event=event,message=resp)
# Export something for other plugin
# export = nonebot.export()
# export.foo = "bar"

# @export.xxx
# def some_function():
#     pass
