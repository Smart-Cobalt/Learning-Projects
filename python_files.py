import sys
def read():
    with open('text.txt', 'r') as file:
        text = file.read()
        if text != "":
            print(text)
            options()
        else:
            print("The file is empty.")
            options()
def write(write_input):
    with open('text.txt', 'w') as file:
        file.write(str(write_input))
def append(append_input):
    with open('text.txt', 'a') as file:
        file.write(f"\n" + append_input)
def clear():
    with open('text.txt', 'w') as file:
        file.write('')
        options()
def options():
    type = input('Read or Write or Append or Quit or Clear').strip().lower()
    if type == 'read':
        print('The file contents are:')
        read()
    elif type == 'write':
        x = input('What do you want to write to the file?')
        write(x)
        print('The new file contents are:')
        read()
        options()
    elif type == 'append':
        x = input('What do you want to stick onto the end of the file?')
        append(x)
        print('The new file contents are:')
        read()
        options()
    elif type == 'quit':
        sys.exit()
    elif type == 'clear':
        clear()
    else:
        print('Invalid option.')
        options()
options()
