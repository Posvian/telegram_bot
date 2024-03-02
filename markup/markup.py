from telebot.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, \
    InlineKeyboardMarkup
from settings import config
from data_base.dbalchemy import DBManager


class Keyboards:
    def __init__(self):
        self.markup = None
        self.DB = DBManager()

    def set_btn(self, name, step=0, quantity=0):
        return KeyboardButton(config.KEYBOARD[name])

    def start_menu(self):
        self.markup = ReplyKeyboardMarkup(True, True)
        item_button_1 = self.set_btn('CHOOSE_GOODS')
        item_button_2 = self.set_btn('INFO')
        item_button_3 = self.set_btn('SETTINGS')

        self.markup.row(item_button_1)
        self.markup.row(item_button_2, item_button_3)
        return self.markup

    def info_menu(self):
        self.markup = ReplyKeyboardMarkup(True, True)
        item_button_1 = self.set_btn('<<')
        self.markup.row(item_button_1)
        return self.markup

    def settings_menu(self):
        self.markup = ReplyKeyboardMarkup(True, True)
        item_button_1 = self.set_btn('<<')
        self.markup.row(item_button_1)
        return self.markup

    @staticmethod
    def remove_menu():
        return ReplyKeyboardRemove()

    @staticmethod
    def set_inline_btn(name):
        return InlineKeyboardButton(str(name), callback_data=str(name.id))

    def set_select_category(self, category):
        self.markup = InlineKeyboardMarkup(row_width=1)
        for item in self.DB.select_all_products_category(category):
            self.markup.add(self.set_inline_btn(item))
        return self.markup

    def category_menu(self):
        self.markup = ReplyKeyboardMarkup(True, True)
        self.markup.add(self.set_btn('SEMIPRODUCT'))
        self.markup.add(self.set_btn('GROCERY'))
        self.markup.add(self.set_btn('ICE_CREAM'))
        self.markup.row(self.set_btn('<<'), self.set_btn('ORDER'))
        return self.markup

