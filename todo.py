import PySimpleGUI as sg

# Choose a Theme for the Layout
sg.theme('DarkBlue')

# Button colours
statecolor = ['lightgray', 'tan', 'yellow', 'lightblue', 'orange', 'limegreen', 'pink', 'red', 'darkgray']	

# Initialise state for button	
buttonstate = 0
		
tasks = [ ]

layout = [
    [sg.Text('To Do List')],#Title of Window
    
    [sg.InputText('Enter To Do Item', key='todo_item'), #Assigning  Space for Writting ToDo 
     
     sg.Button(button_text='Add',button_color = ('black', statecolor[2]), key="add_save")], #Assigning  Add Button
    
    [sg.Button('Delete',button_color = ('white', statecolor[-2])),sg.Button('Edit')], #Assigning Delete Button & Edit Button
    
    [sg.Listbox(values=tasks, size=(50, 20), key="items")]  
]

window = sg.Window('To-Do List App', layout)
while True:  # Event Loop
    event, values = window.Read()
    #Saving The Task
    if event == "add_save": #when User Click On Add,Typed Item Will Save
        tasks.append(values['todo_item']) #Value Will Add in Existing list
        window.FindElement('items').Update(values=tasks)
        window.FindElement('add_save').Update("Add")
    #Deleting The Item From List
    elif event == "Delete": #when User Click On Delete,Selected Item Will Deleted From List
        tasks.remove(values["items"][0]) #Value Will Removed in Existing list
        window.FindElement('items').Update(values=tasks)
    #Editting The Existing Item
    elif event == "Edit":
        edit_val = values["items"][0]
        tasks.remove(values["items"][0])
        window.FindElement('items').Update(values=tasks)
        window.FindElement('todo_item').Update(value=edit_val)
        window.FindElement('add_save').Update("Save")
    elif event == None:
        break

window.Close()