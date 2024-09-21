from javascript import require, On, off
from src.components.okCard import okCard
from src.components.errorCard import errorCard
from src.components.infoCard import infoCard
from src.components.inputCard import inputCard
from src.constants.SETTINGS import *
from threading import Thread
import json
import time

mineflayer = require("mineflayer")

class MinecraftBot:
    def __init__(self, args: dict, plugins_args: dict, reconnect: bool = False):
        self.args = args
        self.host = self.args.get("host")
        self.port = self.args.get("port")
        self.username = self.args.get("username")
        self.version = self.args.get("version")
        self.plugins_args = plugins_args
        self.need_login = self.plugins_args.get("needLogin")
        self.need_register = self.plugins_args.get("needRegister")
        self.password = self.plugins_args.get("password")
        self.reconnect = reconnect
        
        self.start()
        
        time.sleep(.5)
        
        self.messageSubprocess = Thread(target=self.sendMessage)
        self.messageSubprocess.start()
        
    def start(self):
        self.bot = mineflayer.createBot(self.args)
        self.listeningEvents()
        time.sleep(1)

    def listeningEvents(self):
        @On(self.bot, "login")
        def login(this):
            okCard(
                title=f"{APP_NAME} - {self.username.upper()}",
                content=[
                    f"Logged in as {self.username}",
                    f"Host: {self.host}",
                    f"Port: {self.port}",
                    f"Version: {self.version}"
                ]
            )

        @On(self.bot, "spawn")
        def spawn(this):
            okCard(
                title=f"{APP_NAME} - {self.username.upper()}",
                content=[
                    f"Spawned in {this.entity.position.toString()}",
                ]
            )
            if self.need_login:
                self.bot.chat(f"/login {self.password}")
            if self.need_register:
                self.bot.chat(f"/register {self.password} {self.password}")

        @On(self.bot, "messagestr")
        def messagestr(this, message, messagePosition, jsonMsg, sender, verified=None):
            infoCard(
                title=f"[{messagePosition.upper()}] {APP_NAME}",
                content=[message]
            )

        @On(self.bot, "kicked")
        def kicked(this, reason, loggedIn):
            reason = json.loads(reason)
            errorCard(
                title="Kicked from server",
                content=[f"Reason: {reason.get('text')}"]
            )

        @On(self.bot, "end")
        def end(this, reason):
            infoCard(
                title=f"{APP_NAME} - {self.username.upper()}",
                content=[f"Disconnected: {reason}"]
            )
            
            off(self.bot, "login", login)
            off(self.bot, "kicked", kicked)
            off(self.bot, "messagestr", messagestr)
            self.is_thread_online = False
            
            if self.reconnect and not self.is_thread_online:
                infoCard(
                    title=f"{APP_NAME} - {self.username.upper()}",
                    content=["Trying to reconnect..."]
                )
                self.start()

            off(self.bot, "end", end)

    def sendMessage(self):
        while True:
            message = inputCard(title=f"SEND - {APP_NAME}")
            self.bot.chat(message)
            time.sleep(.5)
