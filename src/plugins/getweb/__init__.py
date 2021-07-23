# import nonebot
from pathlib import Path
from nonebot import get_driver
import imgkit
from nonebot.adapters.cqhttp.message import MessageSegment
from .config import Config
import os
# import threading

from nonebot.plugin import on_command, on_keyword
from nonebot.adapters.cqhttp import Bot, Event

global_config = get_driver().config
config = Config(**global_config.dict())



path_wkimg = rf"{os.getcwd()}/src/plugins/getweb/wkhtmltox/bin/wkhtmltoimage.exe"
cfg = imgkit.config(wkhtmltoimage=path_wkimg)
def getweb(url: str, time: str):
    imgkit.from_url(url,"cache/" + str(time)+".png",config=cfg)


# import nonebot


parser = on_command("getweb ")

@parser.handle()
async def _(bot: Bot, event: Event):
    ctx = event.get_message().extract_plain_text()
    qid = event.sender.user_id
    time  = str(event.time)
    #thread = threading.Thread(target=getweb,args=(ctx,time))
    #thread.setDaemon(True)
    #thread.start()
    try:
        getweb(ctx,time)
        msg = MessageSegment.image(Path(os.getcwd() + "/cache/" + time + ".png").absolute().as_uri())
        await bot.send(event,msg)
    except Exception as e:
        if len(str(e)) > 30:
            e = "报错过长。。。嘤嘤嘤,发不出来了"
        else:
            pass
        await bot.send(event,str(e))
        msg = MessageSegment.image(Path(os.getcwd() + "/cache/" + time + ".png").absolute().as_uri())
        await bot.send(event,msg)