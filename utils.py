import json


def load_candidates_from_json(path='candidates.json'):
    file = open(path, encoding='utf-8')
    data_json = json.load(file)
    file.close()
    candidates_dict = {}
    for candidate in data_json:
        candidates_dict[candidate['id']] = candidate
    return data_json


def get_candidate(candidate_id, data_candidates):
    for candidate in data_candidates:
        if candidate_id == candidate['id']:
            return candidate


def get_candidates_by_name(candidate_name, data_candidates):
    correct_candidates = []
    for candidate in data_candidates:
        if candidate_name in candidate['name']:
            correct_candidates.append(candidate)
    return correct_candidates


def get_candidates_by_skill(skill_name, data_candidates):
    correct_candidates = []
    for candidate in data_candidates:
        if skill_name.lower() in candidate['skills'].lower().split(', '):
            correct_candidates.append(candidate)
    return correct_candidates

