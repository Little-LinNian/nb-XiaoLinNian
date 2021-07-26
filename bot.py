import nonebot
from nonebot.adapters.cqhttp import Bot as CQHTTPBot

nonebot.init(port=8080,nickname=["小霖念"],superusers=['2544704967'],host="0.0.0.0",command_start=['/','#'],debug=True)
driver = nonebot.get_driver()
driver.register_adapter("cqhttp", CQHTTPBot)
nonebot.load_builtin_plugins()
# nonebot.load_plugin("nonebot_plugin_picsearcher")
nonebot.load_plugin("src.plugins.yingyu")
# nonebot.load_plugin("nonebot_plugin_analysis_bilibili")
nonebot.load_plugin("src.plugins.cy2")
nonebot.load_plugin("src.plugins.shouyu")
nonebot.load_plugin("src.plugins.group_to_group")
nonebot.load_plugin("src.plugins.sign_in")
# nonebot.load_plugin("src.plugins.ma")
nonebot.load_plugin("src.plugins.getweb")
nonebot.load_plugin("src.plugins.owo")
nonebot.load_plugin("src.plugins.key_chatter")


if __name__ == "__main__":
        nonebot.run()
