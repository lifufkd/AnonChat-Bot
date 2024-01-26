#################################################
#                 created by                    #
#                     ZZS                       #
#                     SBR                       #
#################################################
from telebot import types


class Bot_buttons:
    def __init__(self):
        super(Bot_buttons, self).__init__()
        self.__markup = types.InlineKeyboardMarkup(row_width=2)

    def start_buttons(self):
        btn1 = types.InlineKeyboardButton('Поиск T2T', callback_data='t2t_search')
        btn2 = types.InlineKeyboardButton('Поиск GROUP', callback_data='group_search')
        btn3 = types.InlineKeyboardButton('Профиль', callback_data='profile')
        self.__markup.add(btn1, btn2, btn3)
        return self.__markup


class Bot_phrase:
    def __init__(self):
        super(Bot_phrase, self).__init__()
        self.__ru = {'global': ['Приветствую в RED ROOM👋\nЗдесь Вы можете анонимно общаться со случайными людьми.',
                                'Выберите действие✅']}
        self.__en = {}

    def get_phrase_pac(self, language, _type):
        phrases = self.chose_language(language)
        return phrases[_type]

    def chose_language(self, language):
        if language == 'RU':
            phrases = self.__ru
        elif language == 'EN':
            phrases = self.__en
        return phrases
