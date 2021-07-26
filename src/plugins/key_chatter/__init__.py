# import nonebot
from nonebot import get_driver
from linnian.apps.chatter import utils as ct
from linnian.apps.chatter import Chatter
from nonebot import on_message
from nonebot.adapters.cqhttp.bot import Bot
from nonebot.adapters.cqhttp.event import Event, GroupMessageEvent
from nonebot.plugin import on, on_command
from nonebot.typing import T_State
import random

from .config import Config
chatter = Chatter("data/chatlib.json", "data/chat_backup")
global_config = get_driver().config
config = Config(**global_config.dict())
parser = on_message()
add = on_command("add re ")
remover = on_command("remove re ")

@parser.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    key = ct.easy_key(event.get_plaintext(), event.group_id)
    resp = await chatter.get_reply(key)
    if resp:
        await bot.send(event, random.choice(resp.content.text))
    return


@add.handle()
async def _(bot: Bot, event: GroupMessageEvent, state: T_State):
    msg = event.get_plaintext()
    if not msg:
        await add.finish("这不是纯文本消息qwq")
        return 
    key = ct.easy_key(msg, event.group_id)
    state["key"] = key


@add.got("qwq", "你想让小霖念回复什么捏？")
async def _(bot: Bot, event: GroupMessageEvent, state: T_State):
    key = state["key"]
    reply = await chatter.get_reply(key)
    # 判断是否存在此触发词
    if reply:     
        text_list = reply.content.text
        text_list.append(event.get_plaintext())
    else:
        text_list = [event.get_plaintext()]
    reply = ct.easy_reply(event.sender.user_id, text=text_list)
    await chatter.set(ct.easy_chat(state["key"], reply))
    await chatter.save()
    await add.finish("完成 ~")

@remover.handle()
async def _(bot: Bot,event :GroupMessageEvent,state: T_State):
    msg = event.get_plaintext()
    if not msg:
        await remover.finish("这不是纯文本消息qwq")
        return 
    key = ct.easy_key(msg, event.group_id)
    if not await chatter.get_reply(key):
        await remover.finish("这个词条不存在嗷qwq")
        return 
    else:
        await chatter.remove(key)
        await chatter.save()
        await remover.finish("完成 ~")
    
