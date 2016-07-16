import nltk.chat.eliza as el
import nltk.chat.iesha as ie
import nltk.chat.suntsu as sun
import nltk.chat.zen as zen
import nltk.chat.rude as rude
from nltk.chat import util
import sys


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
            self._greetings = "Wow, I look cool today. Hey!"
            self._name = "Chad"
        else:
            self._bot = util.Chat(el.pairs, el.reflections)
            self._greetings = "Hello.  How are you feeling today?"
            self._name = "Eliza"

    def respond(self, query):
        return self._bot.respond(query)

    def greet(self):
        return self._greetings

    def name(self):
        return self._name


def main():
    nltk_bot_lookup = {"sun": sun.suntsu_chat, "eliza": el.eliza_chat, "iesha": ie.iesha_chat, "rude": rude.rude_chat,
                       "zen": zen.zen_chat}
    try:
        bot_type = sys.argv.pop()
    except IndexError:
        raise IndexError("No bot type specified.")
    if not bot_type.lower() in nltk_bot_lookup.keys():
        raise KeyError("Unknown bot-type {0}".format(bot_type))  # TODO: Please select from the following items?
    print("Hi, you are chatting to NLTK's {0} Chatbot.\n"
          "Simply press Ctrl-D to exit.\n".format(bot_type))
    nltk_bot_lookup.get(bot_type)()

if __name__ == '__main__':
    main()