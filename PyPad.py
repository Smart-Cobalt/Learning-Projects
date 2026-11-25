import sys
import tkinter as tk
def saveFile():
    contents = textBox.get("1.0", "end-1c")
    with open(fileName, 'w') as file:
        file.write(contents)
    print(f'Saved {fileName}')
def undo():
    try:
        textBox.edit_undo()
    except:
        print('It looks like there\'s nothing to undo.')
def options():
    print('Welcome to PyPad!')
    option = input('New, or edit, or exit:  ').strip().lower()
    if option == 'new':
        global fileName
        fileName = input('Add filename with extension (supports html, python, ect):  ')
        if "." not in fileName:
                print('Please use a valid extension')
                fileName = input('Add filename with extension (supports html, python, ect):  ')
        print(f"Making {fileName}:")
        try:
            with open(fileName, 'r') as file:
                contents = file.read()
                print('This file already exists. Edit it instead. Program crashing...')
                return
        except FileNotFoundError:
            pass
        global window
        global textBox
        window = tk.Tk()
        window.bind("<Control-s>", lambda event: saveFile())
        saveButton = tk.Button(window, text="Save",command=saveFile)
        saveButton.pack(side="left", anchor = 'ne')
        undoButton = tk.Button(window, text="Undo", command = undo)
        undoButton.pack(side="left", anchor = 'ne')
        window.title(f"PyPad - open: {fileName}")
        window.geometry("600x400")
        textBox = tk.Text(window, undo=True)
        textBox.pack(expand=True, fill="both")
        window.mainloop()
        options()
    elif option == 'edit':
        fileName = input('Add filename with extension (supports html, python, ect):  ')
        if "." not in fileName:
            print('Please use a valid extension')
            fileName = input('Add filename with extension (supports html, python, ect):  ')
        print(f"Opening {fileName}:")
        try:
            with open(fileName, 'r') as file:
                oldContent = file.read()
        except FileNotFoundError:
            print('File Does not Exist.')
            options()
        except:
            print('An error occured. It cannot  be fixed without changing the code.')
        window = tk.Tk()
        window.bind("<Control-s>", lambda event: saveFile())
        saveButton = tk.Button(window, text="Save",command=saveFile)
        saveButton.pack(side="left", anchor = 'ne')
        undoButton = tk.Button(window, text="Undo", command = undo)
        undoButton.pack(side="left", anchor = 'ne')
        window.title(f"PyPad - open: {fileName}")
        window.geometry("600x400")
        textBox = tk.Text(window, undo = True)
        textBox.insert('1.0',oldContent)
        textBox.pack(expand=True, fill="both")
        window.mainloop()
        options()
    elif option == 'exit':
        sys.exit()
    else: 
        print('Invalid Option.')
options()
