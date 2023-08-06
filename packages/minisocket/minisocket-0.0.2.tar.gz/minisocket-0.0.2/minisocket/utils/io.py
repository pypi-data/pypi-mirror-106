import json
import os
def load_json(filename):
    with open(filename, "r") as f:
        return json.load(f)

def append_to_txt(ori_file, new_lines):
    with open(ori_file, 'a') as f:
        f.write(new_lines+'\n')

def save_json(filename, content):
    with open(filename, "w") as f:
        json.dump(content, f)

def check_path(path):
    if not os.path.exists(path):
        os.makedirs(path)