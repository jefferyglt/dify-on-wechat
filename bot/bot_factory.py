"""
channel factory
"""
from common import const


def create_bot(bot_type):
    """
    创建机器人对象
    :param bot_type: bot type code
    :return: bot instance
    """
    if bot_type == const.ZHIPU_AI:
        from bot.zhipuai.zhipuai_bot import ZHIPUAIBot
        return ZHIPUAIBot()



    raise RuntimeError
