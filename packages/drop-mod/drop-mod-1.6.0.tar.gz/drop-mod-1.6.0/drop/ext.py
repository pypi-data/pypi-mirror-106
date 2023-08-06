"""Extra functions for drop-mod that I didn't think would fit anywhere else."""

import re
from datetime import datetime

from drop.errors import InvalidTimeParsed, PastTimeError, PresentTimeError
import parsedatetime
cal = parsedatetime.Calendar()

owofy_letters = {'r': 'w',
                 'l': 'w',
                 'R': 'W',
                 'L': 'W',
                 'na': 'nya',  # please stop.
                 'ne': 'nye',
                 'ni': 'nyi',
                 ' no ': ' nu ',
                 ' nO ': ' nU ',
                 ' NO ': ' NU ',
                 ' No ': ' Nu ',
                 'no': 'nyo',
                 'nu': 'nyu',
                 'Na': 'Nya',  # oh no the capitalization
                 'Ne': 'Nye',
                 'Ni': 'Nyi',
                 'No': 'Nyo',
                 'Nu': 'Nyu',
                 'nA': 'nyA',  # aaaaaaaaaaaaaaaaaaaaaaaaaa
                 'nE': 'nyE',
                 'nI': 'nyI',
                 'nO': 'nyO',
                 'nU': 'nyU',
                 'NA': 'NYA',  # this is mental torture.
                 'NE': 'NYE',
                 'NI': 'NYI',
                 'NO': 'NYO',
                 'NU': 'NYU',  # I f***ing hate myself.
                 'the ': 'de ',
                 'THE ': 'DE ',
                 'THe ': 'De ',
                 'The ': 'De ',
                 'tHE ': 'dE ',
                 'thE ': 'dE ',  # you seem to have found the exact line where i lose motivation
                 'tt': 'dd',
                 'ock': 'awk',
                 'uck': 'ek',
                 'ou': 'u',
                 'tT': 'dD',
                 'Tt': 'Dd',
                 'TT': 'DD',
                 'ocK': 'awK',
                 'oCK': 'aWK',
                 'OCK': 'AWK',
                 'OCk': 'AWk',
                 'Ock': 'Awk',
                 'ucK': 'eK',
                 'uCK': 'eK',
                 'UCK': 'EK',
                 'UCk': 'Ek',
                 'Uck': 'Ek',
                 'oU': 'U',
                 'OU': 'U',
                 'Ou': 'u'}  # removed stuff because... well, some didn't even work right.
owofy_exclamations = [' OwO', ' @w@', ' #w#', ' UwU', ' ewe', ' -w-', ' \'w\'', ' ^w^', ' >w<',
                      ' ~w~', ' ¬w¬', ' o((>ω< ))o', ' (p≧w≦q)', ' ( •̀ ω •́ )y', ' ✪ ω ✪',
                      ' (。・ω・。)', ' (^・ω・^ )']
# Why'd I put so many here?


to_replace = {
    '<b>': '**',
    '</b>': '**',
    '<p>': '\n**',
    '</p>': '**\n',
    '</li>': '\n'
}

protondb_colors = {"Platinum": 0xB7C9DE, "Gold": 0xCFB526, "Silver": 0xC1C1C1, "Bronze": 0xCB7F22,
                   "Borked": 0xF90000}  # freaking pylint, man.


def format_html(str_input: str):
    """Removes any HTML formatting from a string."""
    for old, new in to_replace.items():
        str_input = str_input.replace(old, new)
    regex_thing = re.compile(r'<.*?>')
    return regex_thing.sub('', str_input)


def format_names(name_list: list):
    """
    Takes a list and returns a string formatting every string inside said list.

    For example, ['john', 'jane', 'joe'] would become "john, jane and joe"
    """
    name_count = len(name_list) - 1
    names = ""
    for idx, name in enumerate(name_list):
        if idx == 0:
            # First name
            names = name
        elif idx == name_count:
            # Last name
            names = names + " and " + name
        else:
            # A name.
            names = names + ", " + name
    return names


def parse_times(datetime_to_parse: str):
    """
    Parses strings containing time formats and returns a string format
    used for temporary punishments such as mute or temp-ban.
    """
    dt_obj = cal.parseDT(datetimeString=datetime_to_parse)
    now_dt = datetime.now()
    list_dt_obj = str(dt_obj[0]).split(":")
    list_now_dt = str(now_dt).split(":")

    str_now_dt = f'{list_now_dt[0]}:{list_now_dt[1]}'
    str_dt_obj = f'{list_dt_obj[0]}:{list_dt_obj[1]}'
    if dt_obj[1] == 0:
        raise InvalidTimeParsed(f"Time string {datetime_to_parse} could not be parsed")
    if dt_obj[0] <= now_dt:
        raise PastTimeError(f"Time {str(dt_obj)} is in the past: "
                            f"there's no logical way to unban them that way")
    if dt_obj[0] == now_dt or str_dt_obj == str_now_dt:
        raise PresentTimeError(f"Time {str(dt_obj)} is the same as now ({str(now_dt)})")
    return str_dt_obj
