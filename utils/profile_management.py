import json

def load_profiles():
    try:
        with open('data/user_profiles.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_profiles(profiles):
    with open('data/user_profiles.json', 'w') as f:
        json.dump(profiles, f)

def update_user_profile(user_id, toxic_word, toxicity_label, comment):
    user_profiles = load_profiles()
    if user_id not in user_profiles:
        user_profiles[user_id] = {'toxic_word_usage': {}, 'comments': [], 'toxicity_labels': []}
    if toxic_word:
        if toxic_word not in user_profiles[user_id]['toxic_word_usage']:
            user_profiles[user_id]['toxic_word_usage'][toxic_word] = 0
        user_profiles[user_id]['toxic_word_usage'][toxic_word] += 1
    user_profiles[user_id]['comments'].append(comment)
    user_profiles[user_id]['toxicity_labels'].append(toxicity_label)
