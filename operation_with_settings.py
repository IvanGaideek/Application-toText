import json


def get_settings_for_splash():  # Path to the gif: main splash screen
    # Open and read the JSON (settings) file
    with open('Settings/cur_settings.json', 'r') as file:
        data = json.load(file)
    path_gif = data["FOR_begin_splash"]["path_to_gif"]
    progressbar_value = data["FOR_begin_splash"]["progressbar_value"]
    return path_gif, progressbar_value
