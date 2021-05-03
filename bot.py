import nonebot
from nonebot.adapters.cqhttp import Bot as CQHTTPBot

nonebot.init(port=8080,nickname=["小霖念"],superusers=['2544704967'])
driver = nonebot.get_driver()
driver.register_adapter("cqhttp", CQHTTPBot)
nonebot.load_builtin_plugins()
nonebot.load_plugin("nonebot_plugin_picsearcher")
nonebot.load_plugin("src.plugins.yingyu")
nonebot.load_plugin("nonebot_plugin_analysis_bilibili")
nonebot.load_plugin("src.plugins.cy2")
nonebot.load_plugin("src.plugins.shouyu")
nonebot.load_plugin("nonebot_plugin_arcaea")
nonebot.load_plugin("src.plugins.group_to_group")

if __name__ == "__main__":
        nonebot.run()
