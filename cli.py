import time

from functions import *

def main():
    """ Main loop """
    print("Rog's TODO app.")
    now = time.strftime("%A %B %d, %Y %H:%M:%S")
    print(now)
    while True:
        user_action = input("Type add, show, edit, complete or exit: ")
        if command(user_action): break
    print('Bye')

if __name__== "__main__" :
    main()

