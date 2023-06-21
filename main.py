from utils import display_recent_operations, load_data_from_file

DATAFILE = 'operations.json'

if __name__ == '__main__':
    operations = load_data_from_file(DATAFILE)
    display_recent_operations(operations)
