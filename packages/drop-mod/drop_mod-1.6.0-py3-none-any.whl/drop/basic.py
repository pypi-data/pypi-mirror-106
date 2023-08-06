"""
Simple-to-use set of functions/commands that don't have a specific goal,
but still are great commands that every bot should have.
"""
import random

import duckduckpy
import lyricsgenius
from requests.exceptions import HTTPError

import drop.ext as ext

GENIUS = None


def owofy(string: str):
    """
    Applies an "owospeak" filter over a passed string. God I hate myself.
    """
    for old, new in ext.owofy_letters.items():
        string = string.replace(old, new)
    while '!' in string:
        string = string.replace('!', random.choice(ext.owofy_exclamations), 1)
    return string


def search(to_search: str):
    """
    Does a DuckDuckPy query. NOTE: does not return search results, only returns queries.
    I don't know how I can really explain this.
    """
    response = duckduckpy.query(to_search, user_agent=u'duckduckpy 0.2', no_redirect=False,
                                no_html=True, skip_disambig=True, container='dict')
    if response['abstract']:
        infobox = []
        is_infobox = False
        image = None
        if response.get('infobox'):
            infobox = response['infobox']['content']
            is_infobox = True
        if response['image']:
            response_image = response['image']
            image = f'https://duckduckgo.com{response_image}' \
                if response_image.startswith('/') else response_image
        result = {
            "title": response['heading'],
            "description": ext.format_html(response.get('abstract_text')),
            "url": response['abstract_url'],
            "source": response['abstract_source'],
            "image": image,
            "fields": [{
                'name': x['label'],
                'value': ''.join(list(x['value'])[:253]) + '...' if len(x) >= 256 else x['value']
            } for x in infobox],
            "infobox": is_infobox
        }
    elif response.get('abstract_text'):
        result = {
            "title": response['heading'],
            "description": response.get('abstract_text'),
            "url": response.get('abstract_url'),
            "source": response['abstract_source'],
            "fields": [],
            "image": None,
            "infobox": False
        }
        for topic in response['related_topics'][:5]:
            if topic.get('topics'):
                pass  # not really what we're looking for
            else:
                name = topic.get('text')
                if len(name) >= 256:
                    name = ''.join(list(name)[:253]) + '...'
                if ' - ' in name:
                    things = name.split(' - ')
                    name = things[0]
                    description = ' - '.join(things[1:]) + '\n' + f"({topic.get('first_url')})"
                else:
                    description = topic.get('first_url')
                result["fields"].append({
                    "name": name,
                    "value": description
                })
    else:
        result = None
    return result


def init_genius(token):
    """
    Initializes Genius' lyrics command (such as get_lyrics() or get_artist()).
    """
    global GENIUS
    GENIUS = lyricsgenius.Genius(token, verbose=False, remove_section_headers=True,
                                 skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"])


# noinspection PyUnresolvedReferences
def get_lyrics(artist, title):
    """
    Obtains lyrics for a song using lyricsgenius.
    NOTE: requires init_genius() to have been used! or... how do i explain things.
    """
    if GENIUS:
        try:
            song = GENIUS.search_song(title=title, artist=artist)
            # Fun fact: that's how I discovered that GHOST by Camellia
            # (the song every beat saber player hates the most) has lyrics, and that they lead to
            # youtu.be/DkrzV5GIQXQ! how the actual fuck did i get here
            # I am now in shock and terrified. If anyone's into ARGs and reading this,
            # well here you go. It appears to be in Japanese though.
        except HTTPError:
            song = None
            print("FIXME: Genius API token probably not working")
        if song:
            return song
    # no genius, woopsies
    return None


# noinspection PyUnresolvedReferences
def get_artist(artist):
    """
    Obtains an artist's most popular songs using lyricsgenius.
    NOTE: requires init_genius() to have been used!
    """
    if GENIUS:
        try:
            songs = GENIUS.search_artist(artist, max_songs=5, sort='popularity').songs
        except HTTPError:
            songs = None
            print("FIXME: Genius API token probably not working")
        except AttributeError:
            songs = None
        if songs:
            lyrics = []
            for song in songs:
                lyric = song.lyrics.split('\n')
                lyrics.append([song.title, lyric[:5], song.url])
            artist_name = songs[0].artist
            return ['Genius', [artist_name, lyrics]]
    return ['nothing', []]
