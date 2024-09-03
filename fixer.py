import json
import os
import sys

def clocktower_json_fixer(new_char_file, replacements, filename):
    # getting the names of the characters that need to be replaced
    with open(new_char_file, 'r', encoding='utf-8') as fh:
        new_characters = [line.strip() for line in fh if line.strip()]

    # getting the jsons into a list
    with open(replacements, 'r', encoding='utf-8') as fh:
        json_data = [line.strip() for line in fh if line.strip()]

    open_brackets = [i for i, char in enumerate(''.join(json_data)) if char == '{']
    close_brackets = [i for i, char in enumerate(''.join(json_data)) if char == '}']

    jsons = [''.join(json_data)[open_brackets[x]:close_brackets[x]+1] for x in range(len(new_characters))]

    # replacing the phrase
    with open(filename, 'r', encoding='utf-8') as fh:
        script = ''.join([line for line in fh])

    for x in range(len(new_characters)):
        character = f'"{new_characters[x].lower()}"'
        text = jsons[x]
        script = script.replace(character, text)

    # exporting the file
    part = filename.split(".")[1].split("\\")[2]
    new_filename = f".\\out\\{part}_fixed.json"
    with open(new_filename, 'w', encoding='utf-8') as fh:
        fh.write(script)
    print("Writing to",new_filename)

clocktower_json_fixer('.\\roles.txt','.\\roles.json',sys.argv[1])