# import nonebot
from nonebot import get_driver
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event
from .config import Config
from nonebot.typing import T_State

global_config = get_driver().config
config = Config(**global_config.dict())
global lib
lib = {}
bind_parser = on_command("send bind",rule=to_me(),priority=2)
@bind_parser.got("group","你想绑定哪个群捏?")
async def handle_city(bot: Bot, event: Event):
    msg = event.get_message().extract_plain_text()
    try:
        group = int(msg)
        lib[event.get_user_id()] = group
        await bot.send(event,"成功")
    except:
        await bind_parser.reject("不对,这不是一个群号")

send_parser = on_command("send ",rule=to_me(),priority=1)
@send_parser.handle()
async def handle_first_receive(bot: Bot, event: Event):
    if not event.get_user_id() in lib.keys():
        await bot.send(event,"你还没绑定嗷,发送 小霖念/send bind")
        return 
    else:
        await bot.call_api("send_group_msg",
                group_id=lib[event.get_user_id()],
                message=event.get_message(),
                auto_escape=True
                )
# Export something for other plugin
# export = nonebot.export()
# export.foo = "bar"

# @export.xxx
# def some_function():
#     pass
