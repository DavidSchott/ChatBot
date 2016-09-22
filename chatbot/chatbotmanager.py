import logging
import sys

chatbotPath = '.'
sys.path.append(chatbotPath)

from chatbot import chatbot


logger = logging.getLogger(__name__)


class ChatbotManager:
    """ Manage a single instance of the chatbot shared over the website
    """
    bot = None

    @staticmethod
    def initBot():
        """ Instantiate the chatbot for later use
        Should be called only once
        """
        if not ChatbotManager.bot:
            logger.info('Initializing bot...')
            ChatbotManager.bot = chatbot.Chatbot()
            ChatbotManager.bot.main(['--modelTag', 'server', '--test', 'daemon', '--rootDir', chatbotPath])
        else:
            logger.info('Bot already initialized.')

    @staticmethod
    def callBot(sentence):
        """ Use the previously instantiated bot to predict a response to the given sentence
        Args:
            sentence (str): the question to answer
        Return:
            str: the answer
        """
        if ChatbotManager.bot:
            return ChatbotManager.bot.get_response(sentence)
        else:
            logger.error('Error: Bot not initialized!')
