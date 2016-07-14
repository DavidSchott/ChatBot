from nltk.chat.eliza import eliza_chat
from nltk.chat.iesha import iesha_chat
from nltk.chat.rude import rude_chat
from nltk.chat.suntsu import suntsu_chat
from nltk.chat.zen import zen_chat
import sys

nltk_bot_lookup = {"suntsu": suntsu_chat,"eliza":eliza_chat,"teen":iesha_chat,"rude":rude_chat,"zen":zen_chat}

try:
    bot_type = sys.argv.pop()
except IndexError:
    raise IndexError("No bot type specified.")

if not bot_type.lower() in nltk_bot_lookup.keys():
    raise ValueError("Unknown bot-type {0}. Please select from the following:".format(bot_type))


print("Hi, you are chatting to NLTK's {0} Chatbot.\n"
      "Simply press Ctrl-D to exit.\n".format(bot_type))

nltk_bot_lookup.get(bot_type)()
