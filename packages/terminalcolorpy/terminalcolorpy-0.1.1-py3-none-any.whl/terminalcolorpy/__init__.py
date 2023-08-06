__version__ = '0.1.1'

import typing
import random
import time

"""
2021-2021 AmmarSys
Open Sourse License: Apache 2.0
Built with: Python 3
Long description: This is a simple package to print colored messages using ASCI to the terminal built with python 3.
Short description: A module to markup text
"""


# each dictionary has a PARENT key, this is used to tell what sort of dict is being sent. this way i dont have to make
# 3 different parsers
end = '\033[0m'
class colors:
    highlight_dicts = {
        'gray': '\x1b[7m',
        'pink': '\x1b[45m',
        'black': '\x1b[40m',
        'yellow': '\x1b[43m',
        'green': '\x1b[42m',
        'blue': '\x1b[44m',
        'red': '\x1b[41m',
        'PARENT': 'highlight'
    }

    color_dict = {
        'pink': '\033[95m',
        'blue': '\033[94m',
        'cyan': '\033[96m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'red': '\033[91m',
        'black': '\x1b[30m',
        'orange': '\033[38;2;255;69;0m',
        'PARENT': 'color'
    }

    text_markup_dict = {
        'bold': '\033[1m',
        'underline': '\033[4m',
        'italic': '\x1B[3m',
        'striked': '\033[9m',
        'framed': '\033[52m',
        'flipped': '',
        'PARENT': 'markup'
    }


def flipText(text):
    return text.translate(str.maketrans(r"""abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""",
                                        r"""ɐqɔpǝɟƃɥᴉɾʞꞁɯuodbɹsʇnʌʍxʎzⱯᗺƆᗡƎᖵ⅁HIᒋ⋊ꞀWNOԀꝹᴚS⊥∩ɅMX⅄Z0ІᘔƐᔭ59Ɫ86¡„#$%⅋,)(*+'-˙/:؛>=<¿@]\[ᵥ‾`}|{~"""))[::-1]


def hex_to_rgb(hexcode: str) -> list:
    hexcode = hexcode.lstrip('#')
    hlen = len(hexcode)
    return list(int(hexcode[i:i + hlen // 3], 16) for i in range(0, hlen, hlen // 3))


def rgb_to_ansii(rgb: typing.Union[list, tuple], NUM: int) -> str:
    return f"\033[{NUM};2;{rgb[0]};{rgb[1]};{rgb[2]}m"


def parse(color: typing.Union[list, tuple, str], DICT) -> str:
    try:
        try:
            return DICT[color]
        except (KeyError, TypeError):
            if DICT['PARENT'] == 'markup':
                return "".join([DICT[i] for i in color])

            if '#' in color:
                return rgb_to_ansii(hex_to_rgb(color), 38 if DICT['PARENT'] == 'color' else 48)

            if type(color) in [list, tuple]:
                if any(i > 255 or i < 0 for i in color):
                    raise TypeError
                return rgb_to_ansii(color, 38 if DICT['PARENT'] == 'color' else 48)
            else:
                return ''
    except TypeError:
        return ''


def prainbow(text: str) -> str:
    return ''.join([rgb_to_ansii((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)), 38) + i
                    for i in text]) + end


def blink(message: str, lenght: float = 1.0, newMessage: str = ' ') -> None:
    print(message, end='')
    time.sleep(lenght)
    return print(f'\r{newMessage}')


def pcolor(
        text: str,
        color: typing.Union[list, tuple, str],
        highlight: typing.Union[list, tuple, str] = None,
        markup: typing.Union[list] = None
) -> str:
    if not markup:
        markup = []
    try:
        color = color.lower() if isinstance(color, str) else color
        highlight = highlight.lower() if isinstance(highlight, str) else highlight
        try:
            markup = list(map(lambda i: i.lower(), list(markup)))
        except TypeError:
            pass
        expression = f'{parse(highlight, colors.highlight_dicts)}' \
                     f'{parse(color, colors.color_dict)}{parse(markup, colors.text_markup_dict)}{text}'

        if 'flipped' in markup:
            return expression.split(text)[0] + flipText(text) + '\u0336' + end

        return expression + end

    except (KeyError, ValueError, IndexError, AttributeError):
        raise KeyError('You\'re proving a invalid argument, please look at the acceptable options at '
                       'https://www.github.com/ammar-sys/terminalcolorpy')


pc, pr, b = pcolor, prainbow, blink
