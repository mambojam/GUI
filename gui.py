import PySimpleGUI as sg
import functions

# Creates a text variable
label = sg.Text("Please enter a to-do")
# Creates and InputText box
input_box = sg.InputText(tooltip="Enter todo", key="todo")
# Creates a button containing "Add"
add_button = sg.Button("Add")

# Creates a gui window and sets the details
window = sg.Window('My To-Do App',
                   # Presents label on 1st ine, followed by input_box and add_button on 2nd
                   layout=[[label], [input_box, add_button]],
                   # Sets font type and size
                   font=('Helvetica', 20))

running = True

while running:
    # Reads the content of the window and returns label of event
    # and a kv pair of the input
    event, values = window.read()
    # Verify the event and values
    print(event)
    print(values)
    # Event cases
    match event:
        # Add to-do to todos.txt
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        # Handles quitting program
        case sg.WIN_CLOSED:
            running = False





window.close()
