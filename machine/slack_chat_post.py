from typing import Dict

from slackbot.slack_bot import SlackBot
from utils.configs.setting import Setting
from workflow.consumer import Consumer


class SlackChatPost(Consumer):
    def __init__(
        self,
    ) -> None:
        self.bot = SlackBot()
        self.setting = Setting()

    def process(self, item: Dict) -> None:
        raise NotImplementedError
