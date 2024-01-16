import PySimpleGUI as sg
import functions

# Creates a text variable
label = sg.Text("Please enter a to-do")
# Creates and InputText box
input_box = sg.InputText(tooltip="Enter todo", key="todo")
# Creates a button containing "Add"
add_button = sg.Button("Add")
#
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
#
edit_button = sg.Button("Edit")

# Creates a gui window and sets the details
window = sg.Window('My To-Do App',
                   # Presents label on 1st ine, followed by input_box and add_button on 2nd
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   # Sets font type and size
                   font=('Helvetica', 20))

running = True

while running:
    # Reads the content of the window and returns label of event
    # and a kv pair of the input
    event, values = window.read()
    # Verify the event and values
    print(f"event = {event}")
    print(f"values = {values}")
    print(f"values todos = {values['todos']}")
    # Display todo items

    # Event cases
    match event:
        # Add to-do to todos.txt
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

            # update in real-time
            window['todos'].update(values=todos)
        #
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + '\n'
            functions.write_todos(todos)

            # update in real-time
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        # Handles quitting program
        case sg.WIN_CLOSED:
            running = False

window.close()
