import random
import json
import re
import random_responses
from epicstore_api import EpicGamesStoreAPI
import jp2

# Load JSON data
def load_json(file):
    with open(file) as bot_responses:
        print(f"Loaded '{file}' successfully!")
        return json.load(bot_responses)


def load_text(file):
    with open(file, encoding='utf-8') as f:
        print(f"Loaded '{file}' successfully!")
        return str(f.read())


# Store JSON data
response_data = load_json("responses.json")
# '` '

def handle_response(message) -> str:
    p_message = message.lower()
    if message == 'roll':
        return str(random.randint(1, 6))
    if message == 'hello there!':
        return 'General Kenobi!'
    if message == 'inwokacja':
        return load_text("inwokacja.txt")
    if message == 'epic':
        api = EpicGamesStoreAPI()
        data = api.get_free_games()
        # print(data)
        # print(data['data']['Catalog']['searchStore']['elements'][0]['title'])
        # print(type(data))
        r = []
        for el in data['data']['Catalog']['searchStore']['elements']:
            r.append(el['title'])
        # d = json.dumps(data)
        # json_regex = re.compile(r'\"title\": \"([\w ]+)\"')
        # r = json_regex.findall(d)
        return ', '.join(r)
    if message == 'jp2':
        return jp2.jp2_quote(random.randint(0, 150))
    return get_response(p_message)


def get_response(input_string):
    split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
    score_list = []

    # Check all the responses
    for response in response_data:
        response_score = 0
        required_score = 0
        required_words = response["required_words"]

        # Check if there are any required words
        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score += 1

        # Amount of required words should match the required score
        if required_score == len(required_words):
            # print(required_score == len(required_words))
            # Check each word the user has typed
            for word in split_message:
                # If the word is in the response, add to the score
                if word in response["user_input"]:
                    response_score += 1

        # Add score to list
        score_list.append(response_score)
        # Debugging: Find the best phrase
        # print(response_score, response["user_input"])

    # Find the best response and return it if they're not all 0
    best_response = max(score_list)
    response_index = score_list.index(best_response)

    # Check if input is empty
    if input_string == "":
        return "Please type something so we can chat :("

    # If there is no good response, return a random one.
    if best_response != 0:
        return response_data[response_index]["bot_response"]
    return
