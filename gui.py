import functions
import PySimpleGUI as sg
import time

sg.theme("Black")

clock = sg.Text('', key='-CLOCK-')
label = sg.Text('Type in a to-do:')
input_box = sg.InputText(tooltip="Enter todo:", key='-INPUT-', do_not_clear=False)
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.load_data(), key='-OUTPUT-',
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
done_button = sg.Button("Done")


window = sg.Window("Rog's TODO App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box],
                            [edit_button, complete_button, done_button ]],
                   font=('Helvetica',20))

while True:
    event, values = window.read(timeout=200)
    window['-CLOCK-'].update(value=time.strftime("%b, %d, %Y %H.%M.%S"))
    #print(event, values)
    match event:
        case "Add" :
            text_input = values['-INPUT-'].strip()
            if input == '': continue
            todos = functions.load_data()
            todos.append(text_input)
            functions.save_data(todos)
            window['-OUTPUT-'].update(values=todos)
        case "Edit" :
            todos = functions.load_data()
            if not todos: continue
            text_input = values['-INPUT-'].strip()
            selected = values['-OUTPUT-'][0]
            if not text_input or not selected: continue
            index = todos.index(selected)
            if index < 0: continue
            todos[index] = text_input
            functions.save_data(todos)
            window['-OUTPUT-'].update(values=todos)
        case "Complete" :
            todos = functions.load_data()
            if not todos: continue
            selected = values['-OUTPUT-'][0]
            if not selected: continue
            index = todos.index(selected)
            if index < 0: continue
            del todos[index]
            functions.save_data(todos)
            window['-OUTPUT-'].update(values=todos)
        case sg.WINDOW_CLOSED | "Done" :
            break

window.close()