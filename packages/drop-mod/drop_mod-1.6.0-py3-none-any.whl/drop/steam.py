"""General functions for Steam-related stuff."""

import re
import requests

import drop.ext as ext
from drop.errors import GameNotFound

# steam_api_token = None

# def init_steam(token):
#     global steam_api_token
#     steam_api_token = token


def search_game(query: str):
    """Searches a game on Steam using a query string, and returns any app IDs found."""
    return re.findall('appid="(.*?)"', requests.get(
        f"https://store.steampowered.com/search/suggest?term={query}&f=games&cc=CA&l=english").text)


def get_protondb_summary(app_id: int):
    """Gets ProtonDB's summary about any game, using a Steam AppID."""
    request = requests.get(f"https://www.protondb.com/api/v1/reports/summaries/{app_id}.json")
    if request.status_code == 404:
        raise GameNotFound(f"Could not find any reports for app ID {app_id}")

    received = request.json()

    tier = received.get("tier").title()
    confidence = received.get("confidence").title()
    score = received.get("score")
    total = received.get("total")
    trending_tier = received.get("trendingTier").title()
    best_reported_tier = received.get("bestReportedTier").title()

    string_result = f"{confidence} confidence, {total} reports, " \
                    f"recently trending tier is {trending_tier}" \
                    f", best reported tier ever is {best_reported_tier}, score is {score}"

    if tier.lower() == "pending":
        string_result = string_result + f', provisional tier is ' \
                                        f'{received.get("provisionalTier").title()}'

    color = 0xf00055
    supposed_color = ext.protondb_colors.get(tier)
    if supposed_color:
        color = supposed_color
    received["string_result"] = string_result
    received["tier_color"] = color
    return received


def get_steam_app_info(app_id: int):
    """Simple HTTP request that returns the JSON data for a Steam AppID."""
    return requests.get(f"https://store.steampowered.com/api/appdetails?appids={app_id}").json()
