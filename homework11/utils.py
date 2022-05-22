import json
from pprint import pprint as pp

DATA_PATH = 'candidates.json'


def load_candidates_from_json(path=DATA_PATH):
    """Возвращает список всех кандидатов """
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_candidate(candidate_id):
    """Возвращает одного кандидата по его id"""
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate['id'] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):
    """Возвращает кандидатов по имени"""
    candidates = load_candidates_from_json()
    candidates_found = []

    for candidate in candidates:
        if candidate_name.lower() in candidate['name'].lower():
            candidates_found.append(candidate)

    return candidates_found


def get_candidates_by_skill(skill_name):
    """Возвращает кандидатов по навыку"""
    skill_candidates = []
    skill_name_lower = skill_name.lower()
    candidates = load_candidates_from_json()
    for candidate in candidates:
        skills = candidate['skills'].lower().strip().split(', ')
        if skill_name_lower in skills:
            skill_candidates.append(candidate)
            continue
    return skill_candidates

#pp(get_candidates_by_skill(''))




