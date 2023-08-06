"""This module handles generation of static badges read from pyproject.toml or
from command line parameters
"""
from .badges_json import json_badge, print_json


def to_snake_case(value: str) -> str:
    """Convert the label from a badge to snake case"""
    return "_".join(value.lower().split())


def convert_list_json_badge(badges_list: list) -> list:
    """Converts the list of badges list to json format to be printed in the json file"""
    json_list = []
    try:
        for badge in badges_list:
            if isinstance(badge, list):
                json_item = print_json(badge[0], badge[1], badge[2])
                json_list.append(json_item)
            else:
                raise TypeError
        return json_list
    except (KeyError, SyntaxError, TypeError):
        return []


def print_static_badges(directory: str, badges_list: list):
    """Call functions to perform actions in order to write a file with json badge information"""
    badges = convert_list_json_badge(badges_list)
    for badge in badges:
        json_badge(directory, to_snake_case(badge['label']), badge)
