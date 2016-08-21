import nltk.chat.eliza as el
import nltk.chat.iesha as ie
import nltk.chat.suntsu as sun
import nltk.chat.zen as zen
import nltk.chat.rude as rude
from chatterbot import ChatBot
from chatterbot.training.trainers import ChatterBotCorpusTrainer
from chatterbot.utils import clean
from nltk.chat import util
import sys

nltk_bot_lookup = {"Sun Tsu": sun.suntsu_chat, "Eliza": el.eliza_chat, "*iesha*": ie.iesha_chat, "Chad": rude.rude_chat,
                   "Zen Master": zen.zen_chat}


class Bot:
    def __init__(self, bot_name="eliza"):
        if bot_name.lower() == "sun":
            self._bot = util.Chat(sun.pairs, sun.reflections)
            self._greetings = "Welcome, my child. Do you seek enlightenment?"
            self._name = "Sun Tsu"
        elif bot_name.lower() == "iesha":
            self._bot = util.Chat(ie.pairs, ie.reflections)
            self._greetings = "hi!! i'm iesha! who r u??!"
            self._name = "*iesha*"
        elif bot_name.lower() == "zen":
            self._bot = util.Chat(zen.responses, zen.reflections)
            self._greetings = "Look beyond mere words and letters - look into your mind"
            self._name = "Zen Master"
        elif bot_name.lower() == "rude":
            self._bot = util.Chat(rude.pairs, rude.reflections)
            self._greetings = "Wow, I look real fresh today. Hey!"
            self._name = "Chad"
        elif bot_name.lower() == "eliza":
            self._bot = util.Chat(el.pairs, el.reflections)
            self._greetings = "Hello.  How are you feeling today?"
            self._name = "Eliza"
            # TODO: Integrate with DeepQA bot somehow...
        elif bot_name.lower() == "laura":
            self._bot = ""
            self._greetings = "Hi."
        else:
            self._corpus_path = "CopyCat.db"
            self._bot = ChatBot(bot_name,
                                storage_adapter="chatterbot.adapters.storage.JsonDatabaseAdapter",
                                logic_adapters=["chatterbot.adapters.logic.ClosestMatchAdapter"],
                                input_adapter="chatterbot.adapters.input.VariableInputTypeAdapter",
                                output_adapter="chatterbot.adapters.output.OutputFormatAdapter",
                                database=self._corpus_path)
            self._bot.set_trainer(ChatterBotCorpusTrainer)
            self._name = bot_name
            self._greetings = "You are speaking to " + bot_name + "."

    def respond(self, query):
        query = clean.clean(clean.clean_whitespace(query))
        if self._name in nltk_bot_lookup.keys():
            return self._bot.respond(query)
        else:
            return str(self._bot.get_response(query))

    def greet(self):
        return self._greetings

    def setup(self, corpus="chatterbot.corpus.english"):
        if self._name not in nltk_bot_lookup.keys():
            self._bot.train(corpus)

    def name(self):
        return self._name

    def location(self):
        return self._corpus_path


def main():
    """Speak to an NLTK ChatBot through CLI."""
    try:
        bot_type = sys.argv.pop()
    except IndexError:
        raise IndexError("No bot type specified.")
    if bot_type.lower() in nltk_bot_lookup.keys():
        print("Hi, you are chatting to NLTK's {0} Chatbot.\n"
              "Simply press Ctrl-D to exit.\n".format(bot_type))
        nltk_bot_lookup.get(bot_type)() # init NLTK-bot

if __name__ == '__main__':
    main()