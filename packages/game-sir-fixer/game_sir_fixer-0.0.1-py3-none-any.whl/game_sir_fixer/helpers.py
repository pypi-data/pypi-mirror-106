from functools import lru_cache

import pygame


def ToPercent(Value, Min=0, Max=100):
    '''
    This function will take the Value, Min and Max and return a percentage
    :param Value: float
    :param Min: float
    :param Max: float
    :return: float from 0.0 to 100.0
    '''
    try:
        if Value < Min:
            return 0
        elif Value > Max:
            return 100

        TotalRange = Max - Min
        # print('TotalRange=', TotalRange)

        FromMinToValue = Value - Min
        # print('FromMinToValue=', FromMinToValue)

        Percent = FromMinToValue / TotalRange

        return Percent
    except Exception as e:
        # print(e)
        # ProgramLog('gs_tools ToPercent Erorr: {}'.format(e), 'error')
        return 0


MAX_VAL = 32768


@lru_cache(maxsize=32768)
def ScaleFloatToHex(f):
    '''

    :param f: float from -1 to +1
    :return: hex from 0x1 to 0x8000
    '''
    p = ToPercent(f, -1, 1)
    i = int(32768 * p) + 1
    i = max(1, i)
    i = min(32768, i)
    return i


@lru_cache(maxsize=32768)
def ScaleFloatToHexInvert(f):
    '''

    :param f: float from -1 to +1
    :return: hex from 0x1 to 0x8000
    '''
    p = ToPercent(f, -1, 1)
    i = int(32768 * p) + 1
    i = max(1, i)
    i = min(32768, i)
    i = 32768 - i
    return i


@lru_cache
def HandleJoyButton(type, button):
    return (
               button + 1,
               1 if type == pygame.JOYBUTTONDOWN else 0
           ), {}


@lru_cache
def HandleJoyHatMotion(value):
    STARTING = 9
    LEFT = STARTING
    RIGHT = LEFT - 1
    UP = RIGHT - 1
    DOWN = UP - 1

    if value[0] == -1:
        return [(LEFT, 1)]
    elif value[0] == 0:
        return [
            (LEFT, 0),
            (RIGHT, 0)
        ]
    elif value[0] == 1:
        return [(RIGHT, 1)]

    if value[1] == -1:
        return [(DOWN, 1)]
    elif value[1] == 0:
        return [
            (DOWN, 0),
            (UP, 0)
        ]
    elif value[1] == 1:
        return [(UP, 1)]
