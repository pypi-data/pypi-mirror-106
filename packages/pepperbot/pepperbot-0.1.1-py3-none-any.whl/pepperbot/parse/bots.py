from pepperbot.types import API_Caller_T
from pepperbot.Mixins.Mixins import *


class BotBase:
    pass


class GroupCommonBot(BotBase, GroupMessageMixin, GroupMemberMixin):
    def __init__(self, event: Dict[str, Any], api: API_Caller_T) -> None:
        self.api: API_Caller_T = api
        self.groupId = event["group_id"]


class AddGroupBot(GroupCommonBot, AddGroupMixin):
    def __init__(self, event: Dict[str, Any], api: API_Caller_T) -> None:
        self.api: API_Caller_T = api
        self.flag = event["flag"]
