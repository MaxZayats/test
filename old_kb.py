from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import x, messages, news_url


def create_inline_keyboard(key):
    kb = InlineKeyboardMarkup()
    if key == 'Main_Screen':
        kb.add(InlineKeyboardButton('Новости', url=news_url))
        kb.row()
        kb.add(InlineKeyboardButton('О боте', callback_data='Info1'))
        kb.insert(InlineKeyboardButton('Меню', callback_data='Menu1'))
        kb.row()
        kb.add(InlineKeyboardButton('Xiaomi [A1]', callback_data='[A1]'))
        kb.add(InlineKeyboardButton('Huawei [B1]', callback_data='[B1]'))
        kb.add(InlineKeyboardButton('iPhone [C1]', callback_data='[C1]'))
        kb.add(InlineKeyboardButton('iPad [D1]', callback_data='[D1]'))
        kb.add(InlineKeyboardButton('PS5 [F1]', callback_data='[F1]'))
        kb.add(InlineKeyboardButton('Xbox [Q1]', callback_data='[Q1]'))
        kb.add(InlineKeyboardButton('Nintendo Switch [S1]', callback_data='[S1]'))
    elif key == 'News':
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == 'Info1':
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == 'Menu1':
        kb.add(InlineKeyboardButton('История покупок', callback_data='History1'))
        kb.add(InlineKeyboardButton('Выигранные бонусы', callback_data='Win1'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == 'History1':
        kb.add(InlineKeyboardButton('Назад', callback_data='Menu1'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == 'Win1':
        kb.add(InlineKeyboardButton('Назад', callback_data='Menu1'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))

    elif key == '[A1]':
        kb.add(InlineKeyboardButton('Xiaomi Redmi 10X Pro [A1.1]', callback_data='[A1.1]'))
        kb.add(InlineKeyboardButton('Бонус 1', callback_data=f'[P1]-{key}'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[A1.1]':
        kb.add(InlineKeyboardButton(f"4/64 Gb ({x['[A1.1]']['Button1']})", callback_data=f"x-{x['[A1.1]']['Button1']}-{key}"))
        kb.add(InlineKeyboardButton(f"6/120 Gb ({x['[A1.1]']['Button2']})", callback_data=f"x-{x['[A1.1]']['Button2']}-{key}"))
        kb.add(InlineKeyboardButton(f"8/256 Gb ({x['[A1.1]']['Button3']})", callback_data=f"x-{x['[A1.1]']['Button3']}-{key}"))
        kb.add(InlineKeyboardButton('Назад', callback_data='[A1]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))

    elif key == '[B1]':
        kb.add(InlineKeyboardButton('Бонус 1', callback_data=f'[P1]-{key}'))
        kb.add(InlineKeyboardButton('HUAWEI P40 Pro [B1.1]', callback_data='[B1.1]'))
        kb.add(InlineKeyboardButton('HUAWEI P40 [B1.2]', callback_data='[B1.2]'))
        kb.add(InlineKeyboardButton('Бонус 8', callback_data=f'[P8]-{key}'))
        kb.insert(InlineKeyboardButton('Бонус 2', callback_data=f'[P2]-{key}'))
        kb.add(InlineKeyboardButton('HUAWEI P30 LITE [B1.3]', callback_data='[B1.3]'))
        kb.add(InlineKeyboardButton('HUAWEI P30 PRO [B1.4]', callback_data='[B1.4]'))
        kb.add(InlineKeyboardButton('HUAWEI P SMART Z [B1.5]', callback_data='[B1.5]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[B1.1]':
        kb.add(InlineKeyboardButton('Синий [B1.1.1]', callback_data='[B1.1.1]'))
        kb.add(InlineKeyboardButton('Бонус 8', callback_data=f'[P8]-{key}'))
        kb.insert(InlineKeyboardButton('Бонус 9', callback_data=f'[P9]-{key}'))
        kb.add(InlineKeyboardButton('Чёрный [B1.1.2]', callback_data='[B1.1.2]'))
        kb.add(InlineKeyboardButton('Красный [B1.1.3]', callback_data='[B1.1.3]'))
        kb.add(InlineKeyboardButton('Бонус 1', callback_data=f'[P1]-{key}'))
        kb.add(InlineKeyboardButton('Розовый [B1.1.4]', callback_data='[B1.1.4]'))
        kb.add(InlineKeyboardButton('Зелёный [B1.1.5]', callback_data='[B1.1.5]'))
        kb.add(InlineKeyboardButton('Назад', callback_data='[B1]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[B1.1.1]':
        kb.add(InlineKeyboardButton(f"4/64 Gb ({x['[B1.1.1]']['Button1']})", callback_data=f"x-{x['[B1.1.1]']['Button1']}-{key}"))
        kb.add(InlineKeyboardButton(f"6/120 Gb ({x['[B1.1.1]']['Button2']})", callback_data=f"x-{x['[B1.1.1]']['Button2']}-{key}"))
        kb.add(InlineKeyboardButton('Назад', callback_data='[B1.1]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[B1.1.2]':
        kb.add(InlineKeyboardButton(f"4/64 Gb ({x['[B1.1.2]']['Button1']})", callback_data=f"x-{x['[B1.1.2]']['Button1']}-{key}"))
        kb.add(InlineKeyboardButton(f"6/120 Gb ({x['[B1.1.2]']['Button2']})", callback_data=f"x-{x['[B1.1.2]']['Button2']}-{key}"))
        kb.add(InlineKeyboardButton('Назад', callback_data='[B1.1]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[B1.1.3]':
        kb.add(InlineKeyboardButton(f"4/64 Gb ({x['[B1.1.3]']['Button1']})", callback_data=f"x-{x['[B1.1.3]']['Button1']}-{key}"))
        kb.add(InlineKeyboardButton(f"6/120 Gb ({x['[B1.1.3]']['Button2']})", callback_data=f"x-{x['[B1.1.3]']['Button2']}-{key}"))
        kb.add(InlineKeyboardButton('Назад', callback_data='[B1.1]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[B1.1.4]':
        kb.add(InlineKeyboardButton(f"4/64 Gb ({x['[B1.1.4]']['Button1']})", callback_data=f"x-{x['[B1.1.4]']['Button1']}-{key}"))
        kb.add(InlineKeyboardButton(f"6/120 Gb ({x['[B1.1.4]']['Button2']})", callback_data=f"x-{x['[B1.1.4]']['Button2']}-{key}"))
        kb.add(InlineKeyboardButton('Назад', callback_data='[B1.1]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[B1.1.5]':
        kb.add(InlineKeyboardButton(f"4/64 Gb ({x['[B1.1.5]']['Button1']})", callback_data=f"x-{x['[B1.1.5]']['Button1']}-{key}"))
        kb.add(InlineKeyboardButton(f"6/120 Gb ({x['[B1.1.5]']['Button2']})", callback_data=f"x-{x['[B1.1.5]']['Button2']}-{key}"))
        kb.add(InlineKeyboardButton('Назад', callback_data='[B1.1]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))

    elif key == '[B1.2]':
        kb.add(InlineKeyboardButton('Синий [B1.2.1]', callback_data='[B1.2.1]'))
        kb.add(InlineKeyboardButton('Чёрный [B1.2.2]', callback_data='[B1.2.2]'))
        kb.add(InlineKeyboardButton('Красный [B1.2.3]', callback_data='[B1.2.3]'))
        kb.add(InlineKeyboardButton('Бонус 1', callback_data=f'[P1]-{key}'))
        kb.add(InlineKeyboardButton('Розовый [B1.2.4]', callback_data='[B1.2.4]'))
        kb.add(InlineKeyboardButton('Бонус 8', callback_data=f'[P8]-{key}'))
        kb.insert(InlineKeyboardButton('Бонус 9', callback_data=f'[P9]-{key}'))
        kb.add(InlineKeyboardButton('Зелёный [B1.2.5]', callback_data='[B1.2.5]'))
        kb.add(InlineKeyboardButton('Назад', callback_data='[B1]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[B1.2.1]':
        kb.add(InlineKeyboardButton(f"4/64 Gb ({x['[B1.2.1]']['Button1']})", callback_data=f"x-{x['[B1.2.1]']['Button1']}-{key}"))
        kb.add(InlineKeyboardButton(f"6/120 Gb ({x['[B1.2.1]']['Button2']})", callback_data=f"x-{x['[B1.2.1]']['Button2']}-{key}"))
        kb.add(InlineKeyboardButton('Назад', callback_data='[B1.2]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[B1.2.2]':
        kb.add(InlineKeyboardButton(f"4/64 Gb ({x['[B1.2.2]']['Button1']})", callback_data=f"x-{x['[B1.2.2]']['Button1']}-{key}"))
        kb.add(InlineKeyboardButton(f"6/120 Gb ({x['[B1.2.2]']['Button2']})", callback_data=f"x-{x['[B1.2.2]']['Button2']}-{key}"))
        kb.add(InlineKeyboardButton('Назад', callback_data='[B1.2]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[B1.2.3]':
        kb.add(InlineKeyboardButton(f"4/64 Gb ({x['[B1.2.3]']['Button1']})", callback_data=f"x-{x['[B1.2.3]']['Button1']}-{key}"))
        kb.add(InlineKeyboardButton(f"6/120 Gb ({x['[B1.2.3]']['Button2']})", callback_data=f"x-{x['[B1.2.3]']['Button2']}-{key}"))
        kb.add(InlineKeyboardButton('Назад', callback_data='[B1.2]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[B1.2.4]':
        kb.add(InlineKeyboardButton(f"4/64 Gb ({x['[B1.2.4]']['Button1']})", callback_data=f"x-{x['[B1.2.4]']['Button1']}-{key}"))
        kb.add(InlineKeyboardButton(f"6/120 Gb ({x['[B1.2.4]']['Button2']})", callback_data=f"x-{x['[B1.2.4]']['Button2']}-{key}"))
        kb.add(InlineKeyboardButton('Назад', callback_data='[B1.2]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[B1.2.5]':
        kb.add(InlineKeyboardButton(f"4/64 Gb ({x['[B1.2.5]']['Button1']})", callback_data=f"x-{x['[B1.2.5]']['Button1']}-{key}"))
        kb.add(InlineKeyboardButton(f"6/120 Gb ({x['[B1.2.5]']['Button2']})", callback_data=f"x-{x['[B1.2.5]']['Button2']}-{key}"))
        kb.add(InlineKeyboardButton('Назад', callback_data='[B1.2]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))

    elif key == '[B1.3]':
        kb.add(InlineKeyboardButton("4/64 Gb [B1.3.1]", callback_data='[B1.3.1]'))
        kb.add(InlineKeyboardButton("6/120 Gb [B1.3.2]", callback_data='[B1.3.2]'))
        kb.add(InlineKeyboardButton('Бонус 1', callback_data=f'[P1]-{key}'))
        kb.insert(InlineKeyboardButton('Бонус 10', callback_data=f'[P10]-{key}'))
        kb.add(InlineKeyboardButton('Назад', callback_data='[B1]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[B1.3.1]':
        kb.add(InlineKeyboardButton(f"4/64 Gb ({x['[B1.3.1]']['Button1']})", callback_data=f"x-{x['[B1.3.1]']['Button1']}-{key}"))
        kb.add(InlineKeyboardButton(f"6/120 Gb ({x['[B1.3.1]']['Button2']})", callback_data=f"x-{x['[B1.3.1]']['Button2']}-{key}"))
        kb.add(InlineKeyboardButton('Назад', callback_data='[B1.3]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[B1.3.2]':
        kb.add(InlineKeyboardButton(f"4/64 Gb ({x['[B1.3.2]']['Button1']})", callback_data=f"x-{x['[B1.3.2]']['Button1']}-{key}"))
        kb.add(InlineKeyboardButton(f"6/120 Gb ({x['[B1.3.2]']['Button2']})", callback_data=f"x-{x['[B1.3.2]']['Button2']}-{key}"))
        kb.add(InlineKeyboardButton('Назад', callback_data='[B1.3]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))

    elif key == '[B1.4]':
        kb.add(InlineKeyboardButton(f"4/64 Gb ({x['[B1.4]']['Button1']})", callback_data=f"x-{x['[B1.4]']['Button1']}-{key}"))
        kb.add(InlineKeyboardButton('Бонус 10', callback_data=f'[P10]-{key}'))
        kb.insert(InlineKeyboardButton('Бонус 11', callback_data=f'[P11]-{key}'))
        kb.add(InlineKeyboardButton(f"6/120 Gb ({x['[B1.4]']['Button2']})", callback_data=f"x-{x['[B1.4]']['Button2']}-{key}"))
        kb.add(InlineKeyboardButton('Назад', callback_data='[B1]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))

    elif key == '[B1.5]':
        kb.add(InlineKeyboardButton('Бонус 1', callback_data=f'[P1]-{key}'))
        kb.insert(InlineKeyboardButton('Бонус 9', callback_data=f'[P9]-{key}'))
        kb.add(InlineKeyboardButton(f"3/32 Gb ({x['[B1.5]']['Button1']})", callback_data=f"x-{x['[B1.5]']['Button1']}-{key}"))
        kb.add(InlineKeyboardButton(f"6/120 Gb ({x['[B1.5]']['Button2']})", callback_data=f"x-{x['[B1.5]']['Button2']}-{key}"))
        kb.add(InlineKeyboardButton('Назад', callback_data='[B1]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))

    elif key == '[C1]':
        kb.add(InlineKeyboardButton('iPhone 12 [C1.1]', callback_data='[C1.1]'))
        kb.add(InlineKeyboardButton('iPhone 11 [C1.2]', callback_data='[C1.2]'))
        kb.add(InlineKeyboardButton('Бонус 4', callback_data=f'[P4]-{key}'))
        kb.insert(InlineKeyboardButton('Бонус 1', callback_data=f'[P1]-{key}'))
        kb.add(InlineKeyboardButton('iPhone SE [C1.3]', callback_data='[C1.3]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))

    elif key == '[C1.1]':
        kb.add(InlineKeyboardButton('Бонус 1', callback_data=f'[P1]-{key}'))
        kb.add(InlineKeyboardButton('12 Max [C1.1.1]', callback_data='[C1.1.1]'))
        kb.add(InlineKeyboardButton('Бонус 5', callback_data=f'[P5]-{key}'))
        kb.insert(InlineKeyboardButton('Бонус 4', callback_data=f'[P4]-{key}'))
        kb.add(InlineKeyboardButton('12 Pro [C1.1.2]', callback_data='[C1.1.2]'))
        kb.add(InlineKeyboardButton('12 Pro Max [C1.1.3]', callback_data='[C1.1.3]'))
        kb.add(InlineKeyboardButton('12 [C1.1.4]', callback_data='[C1.1.4]'))
        kb.add(InlineKeyboardButton('Назад', callback_data='[C1]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[C1.1.1]':
        kb.add(InlineKeyboardButton(f"128 Gb ({x['[C1.1.1]']['Button1']})", callback_data=f"x-{x['[C1.1.1]']['Button1']}-{key}"))
        kb.add(InlineKeyboardButton(f"256 Gb ({x['[C1.1.1]']['Button2']})", callback_data=f"x-{x['[C1.1.1]']['Button2']}-{key}"))
        kb.add(InlineKeyboardButton('Назад', callback_data='[C1.1]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[C1.1.2]':
        kb.add(InlineKeyboardButton('128 Gb [C1.1.2.1]', callback_data='[C1.1.2.1]'))
        kb.add(InlineKeyboardButton('Бонус 1', callback_data=f'[P1]-{key}'))
        kb.add(InlineKeyboardButton('Назад', callback_data='[C1.1]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[C1.1.2.1]':
        kb.add(InlineKeyboardButton(f"4 Gb RAM ({x['[C1.1.2.1]']['Button1']})", callback_data=f"x-{x['[C1.1.2.1]']['Button1']}-{key}"))
        kb.add(InlineKeyboardButton(f"6 Gb RAM ({x['[C1.1.2.1]']['Button2']})", callback_data=f"x-{x['[C1.1.2.1]']['Button2']}-{key}"))
        kb.add(InlineKeyboardButton('Назад', callback_data='[C1.1.2]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))    
    elif key == '[C1.1.3]':
        kb.add(InlineKeyboardButton(f"128 Gb ({x['[C1.1.3]']['Button1']})", callback_data=f"x-{x['[C1.1.3]']['Button1']}-{key}"))
        kb.add(InlineKeyboardButton(f"256 Gb ({x['[C1.1.3]']['Button2']})", callback_data=f"x-{x['[C1.1.3]']['Button2']}-{key}"))
        kb.add(InlineKeyboardButton('Назад', callback_data='[C1.1]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[C1.1.4]':
        kb.add(InlineKeyboardButton('Текст кнопки 1 [C1.1.4.1]', callback_data='[C1.1.4.1]'))
        kb.add(InlineKeyboardButton('Бонус 2', callback_data=f'[P2]-{key}'))
        kb.add(InlineKeyboardButton('Текст кнопки 2 [C1.1.4.2]', callback_data='[C1.1.4.2]'))
        kb.add(InlineKeyboardButton('Назад', callback_data='[C1.1]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[C1.1.4.1]':
        kb.add(InlineKeyboardButton(f"128 Gb ({x['[C1.1.4.1]']['Button1']})", callback_data=f"x-{x['[C1.1.4.1]']['Button1']}-{key}"))
        kb.add(InlineKeyboardButton('Бонус 2', callback_data=f'[P2]-{key}'))
        kb.insert(InlineKeyboardButton('Бонус 1', callback_data=f'[P1]-{key}'))
        kb.add(InlineKeyboardButton(f"256 Gb ({x['[C1.1.4.1]']['Button2']})", callback_data=f"x-{x['[C1.1.4.1]']['Button2']}-{key}"))
        kb.add(InlineKeyboardButton('Назад', callback_data='[C1.1.4]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[C1.1.4.2]':
        kb.add(InlineKeyboardButton(f"128 Gb ({x['[C1.1.4.2]']['Button1']})", callback_data=f"x-{x['[C1.1.4.2]']['Button1']}-{key}"))
        kb.add(InlineKeyboardButton('Бонус 2', callback_data=f'[P2]-{key}'))
        kb.insert(InlineKeyboardButton('Бонус 1', callback_data=f'[P1]-{key}'))
        kb.add(InlineKeyboardButton(f"256 Gb ({x['[C1.1.4.2]']['Button2']})", callback_data=f"x-{x['[C1.1.4.2]']['Button2']}-{key}"))
        kb.add(InlineKeyboardButton('Назад', callback_data='[C1.1.4]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))

    elif key == '[C1.2]':
        kb.add(InlineKeyboardButton('Бонус 1', callback_data=f'[P1]-{key}'))
        kb.add(InlineKeyboardButton('11 Max [C1.2.1]', callback_data='[C1.2.1]'))
        kb.add(InlineKeyboardButton('11 Pro [C1.2.2]', callback_data='[C1.2.2]'))
        kb.add(InlineKeyboardButton('11 Pro Max [C1.2.3]', callback_data='[C1.2.3]'))
        kb.add(InlineKeyboardButton('11 [C1.2.4]', callback_data='[C1.2.4]'))
        kb.add(InlineKeyboardButton('Бонус 2', callback_data=f'[P2]-{key}'))
        kb.insert(InlineKeyboardButton('Бонус 6', callback_data=f'[P6]-{key}'))
        kb.add(InlineKeyboardButton('Назад', callback_data='[C1]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[C1.2.1]':
        kb.add(InlineKeyboardButton(f"128 Gb ({x['[C1.2.1]']['Button1']})", callback_data=f"x-{x['[C1.2.1]']['Button1']}-{key}"))
        kb.add(InlineKeyboardButton(f"256 Gb ({x['[C1.2.1]']['Button2']})", callback_data=f"x-{x['[C1.2.1]']['Button2']}-{key}"))
        kb.add(InlineKeyboardButton(f"512 Gb ({x['[C1.2.1]']['Button3']})", callback_data=f"x-{x['[C1.2.1]']['Button3']}-{key}"))
        kb.add(InlineKeyboardButton(f"128 Gb ({x['[C1.2.1]']['Button4']})", callback_data=f"x-{x['[C1.2.1]']['Button4']}-{key}"))
        kb.add(InlineKeyboardButton(f"256 Gb ({x['[C1.2.1]']['Button5']})", callback_data=f"x-{x['[C1.2.1]']['Button5']}-{key}"))
        kb.add(InlineKeyboardButton(f"512 Gb ({x['[C1.2.1]']['Button6']})", callback_data=f"x-{x['[C1.2.1]']['Button6']}-{key}"))
        kb.add(InlineKeyboardButton(f"128 Gb ({x['[C1.2.1]']['Button7']})", callback_data=f"x-{x['[C1.2.1]']['Button7']}-{key}"))
        kb.add(InlineKeyboardButton(f"256 Gb ({x['[C1.2.1]']['Button8']})", callback_data=f"x-{x['[C1.2.1]']['Button8']}-{key}"))
        kb.add(InlineKeyboardButton(f"512 Gb ({x['[C1.2.1]']['Button9']})", callback_data=f"x-{x['[C1.2.1]']['Button9']}-{key}"))
        kb.add(InlineKeyboardButton('Бонус 1', callback_data=f'[P1]-{key}'))
        kb.add(InlineKeyboardButton('Назад', callback_data='[C1.2]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[C1.2.2]':
        kb.add(InlineKeyboardButton(f"128 Gb ({x['[C1.2.2]']['Button1']})", callback_data=f"x-{x['[C1.2.2]']['Button1']}-{key}"))
        kb.add(InlineKeyboardButton(f"256 Gb ({x['[C1.2.2]']['Button2']})", callback_data=f"x-{x['[C1.2.2]']['Button2']}-{key}"))
        kb.add(InlineKeyboardButton(f"512 Gb ({x['[C1.2.2]']['Button3']})", callback_data=f"x-{x['[C1.2.2]']['Button3']}-{key}"))
        kb.add(InlineKeyboardButton('Назад', callback_data='[C1.2]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[C1.2.3]':
        kb.add(InlineKeyboardButton('Бонус 7', callback_data=f'[P7]-{key}'))
        kb.insert(InlineKeyboardButton('Бонус 2', callback_data=f'[P2]-{key}'))
        kb.add(InlineKeyboardButton('Синий [C1.2.3.1]', callback_data='[C1.2.3.1]'))
        kb.add(InlineKeyboardButton('Красный [C1.2.3.2]', callback_data='[C1.2.3.2]'))
        kb.add(InlineKeyboardButton('Зелёный [C1.2.3.3]', callback_data='[C1.2.3.3]'))
        kb.add(InlineKeyboardButton('Назад', callback_data='[C1.2]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[C1.2.3.1]':
        kb.add(InlineKeyboardButton(f"128 Gb ({x['[C1.2.3.1]']['Button1']})", callback_data=f"x-{x['[C1.2.3.1]']['Button1']}-{key}"))
        kb.add(InlineKeyboardButton(f"256 Gb ({x['[C1.2.3.1]']['Button2']})", callback_data=f"x-{x['[C1.2.3.1]']['Button2']}-{key}"))
        kb.add(InlineKeyboardButton('Назад', callback_data='[C1.2.3]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[C1.2.3.2]':
        kb.add(InlineKeyboardButton(f"1281 Gb ({x['[C1.2.3.2]']['Button1']})", callback_data=f"x-{x['[C1.2.3.2]']['Button1']}-{key}"))
        kb.add(InlineKeyboardButton(f"2561 Gb ({x['[C1.2.3.2]']['Button2']})", callback_data=f"x-{x['[C1.2.3.2]']['Button2']}-{key}"))
        kb.add(InlineKeyboardButton('Бонус 1', callback_data=f'[P1]-{key}'))
        kb.add(InlineKeyboardButton('Назад', callback_data='[C1.2.3]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[C1.2.3.3]':
        kb.add(InlineKeyboardButton(f"128 Gb ({x['[C1.2.3.3]']['Button1']})", callback_data=f"x-{x['[C1.2.3.3]']['Button1']}-{key}"))
        kb.add(InlineKeyboardButton(f"256 Gb ({x['[C1.2.3.3]']['Button2']})", callback_data=f"x-{x['[C1.2.3.3]']['Button2']}-{key}"))
        kb.add(InlineKeyboardButton(f"512 Gb ({x['[C1.2.3.3]']['Button3']})", callback_data=f"x-{x['[C1.2.3.3]']['Button3']}-{key}"))
        kb.add(InlineKeyboardButton(f"128 Gb ({x['[C1.2.3.3]']['Button4']})", callback_data=f"x-{x['[C1.2.3.3]']['Button4']}-{key}"))
        kb.add(InlineKeyboardButton(f"256 Gb ({x['[C1.2.3.3]']['Button5']})", callback_data=f"x-{x['[C1.2.3.3]']['Button5']}-{key}"))
        kb.add(InlineKeyboardButton(f"512 Gb ({x['[C1.2.3.3]']['Button6']})", callback_data=f"x-{x['[C1.2.3.3]']['Button6']}-{key}"))
        kb.add(InlineKeyboardButton('Назад', callback_data='[C1.2.3]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))

    elif key == '[C1.2.4]':
        kb.add(InlineKeyboardButton(f"128 Gb ({x['[C1.2.4]']['Button1']})", callback_data=f"x-{x['[C1.2.4]']['Button1']}-{key}"))
        kb.add(InlineKeyboardButton('Бонус 2', callback_data=f'[P2]-{key}'))
        kb.add(InlineKeyboardButton(f"256 Gb ({x['[C1.2.4]']['Button2']})", callback_data=f"x-{x['[C1.2.4]']['Button2']}-{key}"))
        kb.add(InlineKeyboardButton('Назад', callback_data='[C1.2]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))

    elif key == '[C1.3]':
        kb.add(InlineKeyboardButton('Бонус 1', callback_data=f'[P1]-{key}'))
        kb.add(InlineKeyboardButton('iPhone SE 2020 [C1.3.1]', callback_data='[C1.3.1]'))
        kb.add(InlineKeyboardButton('iPhone SE 1991 [C1.3.2]', callback_data='[C1.3.2]'))
        kb.add(InlineKeyboardButton('Назад', callback_data='[C1]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[C1.3.1]':
        kb.add(InlineKeyboardButton(f"100$ ({x['[C1.3.1]']['Button1']})", callback_data=f"x-{x['[C1.3.1]']['Button1']}-{key}"))
        kb.add(InlineKeyboardButton(f"110$ ({x['[C1.3.1]']['Button2']})", callback_data=f"x-{x['[C1.3.1]']['Button2']}-{key}"))
        kb.add(InlineKeyboardButton(f"120$ ({x['[C1.3.1]']['Button3']})", callback_data=f"x-{x['[C1.3.1]']['Button3']}-{key}"))
        kb.add(InlineKeyboardButton(f"130$ ({x['[C1.3.1]']['Button4']})", callback_data=f"x-{x['[C1.3.1]']['Button4']}-{key}"))
        kb.add(InlineKeyboardButton(f"140$ ({x['[C1.3.1]']['Button5']})", callback_data=f"x-{x['[C1.3.1]']['Button5']}-{key}"))
        kb.add(InlineKeyboardButton('Назад', callback_data='[C1.3]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[C1.3.2]':
        kb.add(InlineKeyboardButton(f"150$ ({x['[C1.3.2]']['Button1']})", callback_data=f"x-{x['[C1.3.2]']['Button1']}-{key}"))
        kb.add(InlineKeyboardButton(f"100$ ({x['[C1.3.2]']['Button2']})", callback_data=f"x-{x['[C1.3.2]']['Button2']}-{key}"))
        kb.add(InlineKeyboardButton('Назад', callback_data='[C1.3]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))

    elif key == '[D1]':
        kb.add(InlineKeyboardButton('iPad Pro 3 11 [D1.1]', callback_data='[D1.1]'))
        kb.add(InlineKeyboardButton('iPad Pro 3 12.9 [D1.2]', callback_data='[D1.2]'))
        kb.add(InlineKeyboardButton('Бонус 3', callback_data=f'[P3]-{key}'))
        kb.add(InlineKeyboardButton('iPad 2020 [D1.3]', callback_data='[D1.3]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[D1.1]':
        kb.add(InlineKeyboardButton('LTE [D1.1.1]', callback_data='[D1.1.1]'))
        kb.add(InlineKeyboardButton('5G [D1.1.2]', callback_data='[D1.1.2]'))
        kb.add(InlineKeyboardButton('Бонус 7', callback_data=f'[P7]-{key}'))
        kb.add(InlineKeyboardButton('Wi-Fi [D1.1.3]', callback_data='[D1.1.3]'))
        kb.add(InlineKeyboardButton('Назад', callback_data='[D1]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[D1.1.1]':
        kb.add(InlineKeyboardButton('512 Gb [D1.1.1.1]', callback_data='[D1.1.1.1]'))
        kb.add(InlineKeyboardButton('1 Tb [D1.1.1.2]', callback_data='[D1.1.1.2]'))
        kb.add(InlineKeyboardButton('Назад', callback_data='[D1.1]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[D1.1.1.1]':
        kb.add(InlineKeyboardButton(f"С клавиатурой ({x[key]['Button1']})", callback_data=f"x-{x[key]['Button1']}-{key}"))
        kb.add(InlineKeyboardButton(f"Без клавиатуры ({x[key]['Button2']})", callback_data=f"x-{x[key]['Button2']}-{key}"))
        kb.add(InlineKeyboardButton('Назад', callback_data='[D1.1.1]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[D1.1.1.2]':
        kb.add(InlineKeyboardButton(f"С клавиатурой ({x[key]['Button1']})", callback_data=f"x-{x[key]['Button1']}-{key}"))
        kb.add(InlineKeyboardButton(f"Без клавиатуры ({x[key]['Button2']})", callback_data=f"x-{x[key]['Button2']}-{key}"))
        kb.add(InlineKeyboardButton('Назад', callback_data='[D1.1.1]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[D1.1.2]':
        kb.add(InlineKeyboardButton('С клавиатурой [D1.1.2.1]', callback_data='[D1.1.2.1]'))
        kb.add(InlineKeyboardButton('Без клавиатуры [D1.1.2.2]', callback_data='[D1.1.2.2]'))
        kb.add(InlineKeyboardButton('Бонус 1', callback_data=f'[P1]-{key}'))
        kb.insert(InlineKeyboardButton('Бонус 2', callback_data=f'[P2]-{key}'))
        kb.add(InlineKeyboardButton('Назад', callback_data='[D1.1]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[D1.1.2.1]':
        kb.add(InlineKeyboardButton(f"512 Gb ({x['[D1.1.2.1]']['Button1']})", callback_data=f"x-{x['[D1.1.2.1]']['Button1']}-{key}"))
        kb.add(InlineKeyboardButton(f"1 Tb ({x['[D1.1.2.1]']['Button2']})", callback_data=f"x-{x['[D1.1.2.1]']['Button2']}-{key}"))
        kb.add(InlineKeyboardButton('Назад', callback_data='[D1.1.2]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[D1.1.2.2]':
        kb.add(InlineKeyboardButton(f"512 Gb ({x['[D1.1.2.2]']['Button1']})", callback_data=f"x-{x['[D1.1.2.2]']['Button1']}-{key}"))
        kb.add(InlineKeyboardButton(f"1 Tb ({x['[D1.1.2.2]']['Button2']})", callback_data=f"x-{x['[D1.1.2.2]']['Button2']}-{key}"))
        kb.add(InlineKeyboardButton('Назад', callback_data='[D1.1.2]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[D1.1.3]':
        kb.add(InlineKeyboardButton(f"256 Gb ({x[key]['Button1']})", callback_data=f"x-{x[key]['Button1']}-{key}"))
        kb.add(InlineKeyboardButton(f"512 Gb ({x[key]['Button2']})", callback_data=f"x-{x[key]['Button2']}-{key}"))
        kb.add(InlineKeyboardButton(f"1 Tb ({x[key]['Button3']})", callback_data=f"x-{x[key]['Button3']}-{key}"))
        kb.add(InlineKeyboardButton('Назад', callback_data='[D1.1]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[D1.2]':
        kb.add(InlineKeyboardButton(f"512 Gb ({x[key]['Button1']})", callback_data=f"x-{x[key]['Button1']}-{key}"))
        kb.add(InlineKeyboardButton(f"1 Tb ({x[key]['Button2']})", callback_data=f"x-{x[key]['Button2']}-{key}"))
        kb.add(InlineKeyboardButton('Назад', callback_data='[D1]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[D1.3]':
        kb.add(InlineKeyboardButton(f"512 Gb ({x[key]['Button1']})", callback_data=f"x-{x[key]['Button1']}-{key}"))
        kb.add(InlineKeyboardButton(f"1 Tb ({x[key]['Button2']})", callback_data=f"x-{x[key]['Button2']}-{key}"))
        kb.add(InlineKeyboardButton('Назад', callback_data='[D1]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))

    elif key == '[F1]':
        kb.add(InlineKeyboardButton(f"Slim ({x[key]['Button1']})", callback_data=f"x-{x[key]['Button1']}-{key}"))
        kb.add(InlineKeyboardButton(f"Pro ({x[key]['Button2']})", callback_data=f"x-{x[key]['Button2']}-{key}"))
        kb.add(InlineKeyboardButton('Бонус 1', callback_data=f'[P1]-{key}'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))

    elif key == '[Q1]':
        kb.add(InlineKeyboardButton('1 Tb [Q1.1]', callback_data='[Q1.1]'))
        kb.add(InlineKeyboardButton('2 Tb [Q1.2]', callback_data='[Q1.2]'))
        kb.add(InlineKeyboardButton('Бонус 8', callback_data=f'[P8]-{key}'))
        kb.add(InlineKeyboardButton('Бонус 1', callback_data=f'[P1]-{key}'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))

    elif key == '[Q1.1]':
        kb.add(InlineKeyboardButton(f"Pro ({x[key]['Button1']})", callback_data=f"x-{x[key]['Button1']}-{key}"))
        kb.add(InlineKeyboardButton(f"Slim ({x[key]['Button2']})", callback_data=f"x-{x[key]['Button2']}-{key}"))
        kb.add(InlineKeyboardButton(f"Pro ({x[key]['Button3']})", callback_data=f"x-{x[key]['Button3']}-{key}"))
        kb.add(InlineKeyboardButton('Бонус 1', callback_data=f'[P1]-{key}'))
        kb.insert(InlineKeyboardButton('Бонус 8', callback_data=f'[P8]-{key}'))
        kb.add(InlineKeyboardButton(f"Pro ({x[key]['Button4']})", callback_data=f"x-{x[key]['Button4']}-{key}"))
        kb.add(InlineKeyboardButton(f"Slim ({x[key]['Button5']})", callback_data=f"x-{x[key]['Button5']}-{key}"))
        kb.add(InlineKeyboardButton(f"Pro ({x[key]['Button6']})", callback_data=f"x-{x[key]['Button6']}-{key}"))
        kb.add(InlineKeyboardButton('Бонус 2', callback_data=f'[P2]-{key}'))
        kb.add(InlineKeyboardButton(f"Pro ({x[key]['Button7']})", callback_data=f"x-{x[key]['Button7']}-{key}"))
        kb.add(InlineKeyboardButton(f"Slim ({x[key]['Button8']})", callback_data=f"x-{x[key]['Button8']}-{key}"))
        kb.add(InlineKeyboardButton('Назад', callback_data='[Q1]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))

    elif key == '[Q1.2]':
        kb.add(InlineKeyboardButton('Full [Q1.2.1]', callback_data='[Q1.2.1]'))
        kb.add(InlineKeyboardButton('No Full [Q1.2.2]', callback_data='[Q1.2.2]'))
        kb.add(InlineKeyboardButton('Бонус 1', callback_data=f'[P1]-{key}'))
        kb.insert(InlineKeyboardButton('Бонус 8', callback_data=f'[P8]-{key}'))
        kb.add(InlineKeyboardButton('No Controller [Q1.2.3]', callback_data='[Q1.2.3]'))
        kb.add(InlineKeyboardButton('Назад', callback_data='[Q1]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[Q1.2.1]':
        kb.add(InlineKeyboardButton(f"Game edition ({x[key]['Button1']})", callback_data=f"x-{x[key]['Button1']}-{key}"))
        kb.add(InlineKeyboardButton(f"No ({x[key]['Button2']})", callback_data=f"x-{x[key]['Button2']}-{key}"))
        kb.add(InlineKeyboardButton('Назад', callback_data='[Q1.2]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[Q1.2.2]':
        kb.add(InlineKeyboardButton(f"Game edition ({x[key]['Button1']})", callback_data=f"x-{x[key]['Button1']}-{key}"))
        kb.add(InlineKeyboardButton(f"No ({x[key]['Button2']})", callback_data=f"x-{x[key]['Button2']}-{key}"))
        kb.add(InlineKeyboardButton('Назад', callback_data='[Q1.2]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[Q1.2.3]':
        kb.add(InlineKeyboardButton(f"Game edition ({x[key]['Button1']})", callback_data=f"x-{x[key]['Button1']}-{key}"))
        kb.add(InlineKeyboardButton(f"No ({x[key]['Button2']})", callback_data=f"x-{x[key]['Button2']}-{key}"))
        kb.add(InlineKeyboardButton('Назад', callback_data='[Q1.2]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))

    elif key == '[S1]':
        kb.add(InlineKeyboardButton('Бонус 12', callback_data=f'[P12]-{key}'))
        kb.add(InlineKeyboardButton('Бонус 1', callback_data=f'[P1]-{key}'))
        kb.add(InlineKeyboardButton('1 Tb [S1.1]', callback_data='[S1.1]'))
        kb.add(InlineKeyboardButton('2 Tb [S1.2]', callback_data='[S1.2]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))

    elif key == '[S1.1]':
        kb.add(InlineKeyboardButton('Бонус 12', callback_data=f'[P12]-{key}'))
        kb.add(InlineKeyboardButton(f"Pro ({x[key]['Button1']})", callback_data=f"x-{x[key]['Button1']}-{key}"))
        kb.add(InlineKeyboardButton(f"Slim ({x[key]['Button2']})", callback_data=f"x-{x[key]['Button2']}-{key}"))
        kb.add(InlineKeyboardButton(f"Pro ({x[key]['Button3']})", callback_data=f"x-{x[key]['Button3']}-{key}"))
        kb.add(InlineKeyboardButton(f"Slim ({x[key]['Button4']})", callback_data=f"x-{x[key]['Button4']}-{key}"))
        kb.add(InlineKeyboardButton(f"Pro ({x[key]['Button5']})", callback_data=f"x-{x[key]['Button5']}-{key}"))
        kb.add(InlineKeyboardButton(f"Slim ({x[key]['Button6']})", callback_data=f"x-{x[key]['Button6']}-{key}"))
        kb.add(InlineKeyboardButton('Бонус 2', callback_data=f'[P2]-{key}'))
        kb.add(InlineKeyboardButton(f"Pro ({x[key]['Button7']})", callback_data=f"x-{x[key]['Button7']}-{key}"))
        kb.add(InlineKeyboardButton('Назад', callback_data='[S1]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    elif key == '[S1.2]':
        kb.add(InlineKeyboardButton('Бонус 12', callback_data=f'[P12]-{key}'))
        kb.add(InlineKeyboardButton(f"Pro ({x[key]['Button1']})", callback_data=f"x-{x[key]['Button1']}-{key}"))
        kb.add(InlineKeyboardButton(f"Slim ({x[key]['Button2']})", callback_data=f"x-{x[key]['Button2']}-{key}"))
        kb.add(InlineKeyboardButton(f"Pro ({x[key]['Button3']})", callback_data=f"x-{x[key]['Button3']}-{key}"))
        kb.add(InlineKeyboardButton(f"Slim ({x[key]['Button4']})", callback_data=f"x-{x[key]['Button4']}-{key}"))
        kb.add(InlineKeyboardButton(f"Pro ({x[key]['Button5']})", callback_data=f"x-{x[key]['Button5']}-{key}"))
        kb.add(InlineKeyboardButton('Назад', callback_data='[S1]'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))

    elif key == 'Fin':
        # kb.add(InlineKeyboardButton('Поделиться с друзьями', callback_data='Fren1'))
        kb.add(InlineKeyboardButton('Новости', callback_data='News'))
        kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))

    elif key == 'Fren1':
        kb.add(InlineKeyboardButton(messages[key]['text'], url=messages[key]['url']))

    elif key in ('[P1.1]', '[P2.1]'):
        kb.add(InlineKeyboardButton('Отмена', callback_data='Main_Screen'))

    return kb


def create_special_keyboard(key, back_key):
    kb = InlineKeyboardMarkup()
    if key == '[P1]':
        kb.add(InlineKeyboardButton('Предложить', callback_data='[P1.1]'))
        kb.add(InlineKeyboardButton('Назад', callback_data=back_key))
    elif key == '[P2]':
        kb.add(InlineKeyboardButton('Предложить', callback_data='[P2.1]'))
        kb.add(InlineKeyboardButton('Назад', callback_data=back_key))
    elif key in ('[P3]', '[P4]', '[P5]', '[P6]', '[P7]', '[P8]', '[P9]', '[P10]', '[P11]', '[P12]'):
        kb.add(InlineKeyboardButton('Назад', callback_data=back_key))
    elif key == '[Ввод]':
        kb.add(InlineKeyboardButton('Назад', callback_data=back_key))
    return kb


def create_payment_keyboard(url):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton('Оплатить', url=url))
    kb.add(InlineKeyboardButton('Проверить оплату', callback_data='Check_pay'))
    kb.add(InlineKeyboardButton('Главный экран', callback_data='Main_Screen'))
    return kb
