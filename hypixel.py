# /api new를 입력하여 API 키를 받을수 있습니다.

import requests, math

Key = "INPUT_YOUR_KEYYYY"

BASE = 10_000
GROWTH = 2_500
REVERSE_PQ_PREFIX = -(BASE - 0.5 * GROWTH) / GROWTH
REVERSE_CONST = REVERSE_PQ_PREFIX
GROWTH_DIVIDES_2 = 2 / GROWTH

def get_level(name):
    url = f"https://api.hypixel.net/player?key={Key}&name={name}"
    res = requests.get(url)
    data = res.json()
    if data["player"] is None:
        return None
    exp = int(data["player"]["networkExp"])
    return math.floor(1 + REVERSE_PQ_PREFIX + math.sqrt(REVERSE_CONST + GROWTH_DIVIDES_2 * exp))