import json


def load_candidates_from_json():
    with open('candidates.json', 'r', encoding='UTF-8') as file:
        return json.load(file)


def get_candidates_all():
    return load_candidates_from_json()


def get_candidate(candidate_id):
    for id in load_candidates_from_json():
        if candidate_id == id['id']:
            return id

    return None


def get_candidates_by_name(candidate_name):
    suitable_candidate = []

    for name in load_candidates_from_json():
        if candidate_name in name['name']:
            suitable_candidate.append(name)

    return suitable_candidate


def get_candidates_by_skill(skill_name):
    suitable_candidate = []

    for skill in load_candidates_from_json():
        if skill_name.lower() in skill['skills'].lower().split(', '):
            suitable_candidate.append(skill)

    return suitable_candidate
