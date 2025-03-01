import functions
import FreeSimpleGUI as sg

label1 = sg.Text('Type a todo in:')
input_box = sg.Input(tooltip="Enter a todo", key="todo")
button_convert = sg.Button('add')
button_complete = sg.Button('complete')
button_exit = sg.Button('exit')
list_box = sg.Listbox(values=functions.get_todos(),key="items-list",
                      size=[45,10],
                      highlight_background_color='purple',
                        enable_events=True)

button_edit = sg.Button('edit',)

window = sg.Window('My project todo app',size=(1000, 500),
                   layout=[
                       [label1],
                       [input_box, button_convert],
                       [list_box,button_edit,button_complete],
                       [button_exit]],
                    font=('Helvetica',20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'add':
            todos = functions.get_todos()
            todos.append(values['todo'] + '\n')
            functions.write_todos(todos)
            window['items-list'].update(values=todos)
        case 'edit':
            
            todo_to_edit = values['items-list'][0]
            new_todo = values['todo'] + '\n'
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['items-list'].update(values=todos) #Update the todos list
            window['todo'].update(value='')
        
        case 'complete':
            print('complete is alive')
            to_delete = values['items-list'][0]
            print(f'item to delete ==>> {to_delete}')
            todos = functions.get_todos()
            todos.remove(to_delete)
            functions.write_todos(todos)
            window['items-list'].update(values=todos)
            window['todo'].update(value='')

        case 'items-list':
            window['todo'].Update(value=values['items-list'][0].strip('\n'))

        case 'exit'| sg.WIN_CLOSED:
            break
          
window.close()

