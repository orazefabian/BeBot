import requests

url = "https://football-prediction-api.p.rapidapi.com/api/v2/"
prediction = "predictions"
performance = "performance-stats"
head_to_head = "head-to-head"

querystring = {"market": "classic", "federation": "UEFA"}
querystring_market = {"market": "classic"}

headers = {
    'x-rapidapi-key': "88c6e9c30cmsh3d1f271990cf02fp135d81jsnba68844f15ef",
    'x-rapidapi-host': "football-prediction-api.p.rapidapi.com"
}


def load_prev_stats():
    response = requests.request("GET", url + performance, headers=headers, params=querystring_market)
    # with open("../data/prev_stats.json", "w") as outfile:
    #     json.dump(response.json(), outfile)
    return response.json()


def load_predictions():
    response = requests.request("GET", url + prediction, headers=headers, params=querystring)
    # with open("../data/data.json", "w") as outfile:
    #     json.dump(response.json(), outfile)
    return response.json()


def update_stats():
    """Update local data, downloads the stats of the last predictions as well as the prediction stats for games
    within the next 48 hours"""
    load_predictions()
    load_prev_stats()


def get_details_to_prediction(id):
    id_url = url + prediction + "/" + str(id)
    response = requests.request("GET", id_url, headers=headers)
    # with open("data/single_data_" + str(id) + ".json", "w") as outfile:
    #     json.dump(response.json(), outfile)
    return response.json()


def get_head_to_head_details(match_ID):
    final_url = url + head_to_head + "/" + str(match_ID)
    response = requests.request("GET", final_url, headers=headers)
    # with open("data/head_to_head_data" + str(match_ID) + ".json", "w") as outfile:
    #     json.dump(response.json(), outfile)
    return response.json()


def get_away_last_10(match_ID):
    response = requests.request("GET", url + "away-last-10/" + str(match_ID), headers=headers)
    return response.json()


def get_home_last_10(match_ID):
    response = requests.request("GET", url + "home-last-10/" + str(match_ID), headers=headers)
    return response.json()
