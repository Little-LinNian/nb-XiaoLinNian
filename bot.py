import nonebot
from nonebot.adapters.cqhttp import Bot as CQHTTPBot

nonebot.init(port=5050)
driver = nonebot.get_driver()
driver.register_adapter("cqhttp", CQHTTPBot)
nonebot.load_builtin_plugins()
nonebot.load_plugin("nonebot_plugin_status")

if __name__ == "__main__":
        nonebot.run()
