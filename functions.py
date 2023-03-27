import os, time

DATA_FILE = '/home/rdubar/projects/todo-app/data.txt'

def get_data_index(data, x):
    """ Return the index of an item in list given a number, or text to search for in the list """
    print(123,type(x), x)
    if type(x) == str: x = x.strip()
    if x.isdigit():
        return int(x) - 1
    elif x in data:
        return data.index(x)
    else:
        return -1

def save_data(data, path=DATA_FILE):
    """ Save the list """
    try:
        with open(path, 'w') as f:
            f.write('\n'.join(data))
        print(f"Saved {len(data):,} items to: {path}")
    except Exception as e:
        print(f"Save of {len(data):,} items to {path} failed: {e}.")

def load_data(path=DATA_FILE):
    """ Load a list from a path """
    if not os.path.exists(DATA_FILE):
        print("No data file to load.")
        return []
    try:
        with open(path, 'r') as f:
            data = f.read().splitlines()
        print(f"Loaded {len(data):,} items from: {path}")
        return data
    except Exception as e:
        print(f"Load from {path} failed: {e}.")

def confirm():
    """ Confirm yes/no! """
    answer = input("Are you sure? (enter yes to confirm): ")
    if answer == 'yes': return True
    else: return False

def command(text):
    """ given text input, executes the requested command using the argument given """

    text = text.strip()
    data = load_data()
    exit_program = False

    if ' ' in text:
        command, argument = text.split(' ', 1)
    else:
        command = text
        argument = None

    match command.lower():
        case 'add' | 'a' :
            if argument == None:
                argument = input("Enter a data: ")
            data.append(argument)
        case 'show' | 's' :
            for index, item in enumerate(data):
                row = f'{index+1:>4}    {item}'
                print(row)
        case 'edit' | 'e':
            if argument == None:
                argument = input("Number of the data to edit: ")
            number = get_data_index(argument)
            if number >= 0 and number < len(data):
                number = input("Enter new data: ")
                data[number] = new_data.strip()
            else:
                print(f'Unknown item: {argument}')
        case 'complete' | 'c' | 'remove' | 'r':
            if argument == None:
                argument = input("Number of the data to mark complete: ")
            number = get_data_index(argument)
            if number >= 0 and number < len(data):
                del data[number]
                print(f'{argument} Marked complete.')
            else:
                print(f'Unknown item: {argument}')
        case 'save':
            save_list(data)
        case 'clear':
            if confirm():
                print('List cleared.')
                data = []
        case 'exit' | 'x' | 'q'  | 'quit':
            exit_program = True

    save_data(data)
    return exit_program

def main():
    """ Main loop """
    now = time.strftime("%A %B %d, %Y %H:%M:%S")
    print(now)
    print("Rog's TODO functions")

if __name__== "__main__" :
    main()

