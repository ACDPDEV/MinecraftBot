from src.classes.MinecraftBot import MinecraftBot

ARGS = {
    "host": "mc.servermc.xyz",
    "port": 16126,
    "username": "demo.py",
    "version": "1.18.2",
    "hideErrors": False
}

PLUGINS_ARGS = {
    "needLogin": False,
    "needRegister": False,
    "password": "incorrecta"
}

RECONNECT = True

bot = MinecraftBot(ARGS, PLUGINS_ARGS, RECONNECT)
