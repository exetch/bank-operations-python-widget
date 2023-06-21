import json
from utils import display_recent_operations

DATAFILE = 'operations.json'

with open(DATAFILE, 'r', encoding='utf-8') as file:
    operations = json.load(file)
if __name__ == '__main__':
    display_recent_operations(operations)
