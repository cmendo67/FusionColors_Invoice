from tkinter import *
from ClientData import ClientData
# Creating tkinter window 
root = Tk()

#creating title for application
root.title('Fusion Colors Invoice')

# creating fixed geometry of the
# tkinter window with dimensions 1280 x 720
root.geometry('1280x720')
backgroundColor = 'green'

class GuiInterface():

    client_entries = []

    def createClientEntries(self):
        for i in range(8):
            clientEntry = Entry(root)
            clientEntry.grid(row = 0, column = i, pady = 5, padx = 0)
            if i == 0:
                clientEntry.insert(END, 'FirstName')
            elif i == 1:

                clientEntry.insert(END, 'LastName')
            elif i == 2:
                clientEntry.insert(END, 'phoneWorkCell')
            elif i == 3:
                clientEntry.insert(END, 'phoneHome')
            elif i == 4:
                clientEntry.insert(END, 'address')
            elif i == 5:
                clientEntry.insert(END, 'city')
            elif i == 6:
                clientEntry.insert(END, 'state')
            else:
                clientEntry.insert(END, 'zip')

        GuiInterface().client_entries.append(clientEntry)
    
    def clientInfo():
        client_entry_list = ''
        
        for i in GuiInterface().client_entries:
            client_entry_list = client_entry_list + str(i.get()) + '\n'
            GuiInterface().client_label.config(text=client_entry_list)

        clientInfo = ClientData(GuiInterface().client_entries[0].get(), GuiInterface().client_entries[1].get(), GuiInterface().client_entries[2].get(), GuiInterface().client_entries[3].get(),
        GuiInterface().client_entries[4].get(), GuiInterface().client_entries[5].get(), GuiInterface().client_entries[6].get(), GuiInterface().client_entries[7].get())
        print(clientInfo.get_firstName(), " ", clientInfo.get_lastName())
    
    clientButton = Button(root, text="Button", command=clientInfo)
    clientButton.grid(row = 9, column = 0, pady = 0)

    client_label = Label(root, text ='')
    client_label.grid(row = 2, column = 0, pady = 0)


GuiInterface().createClientEntries()
#exexute tkinter 
root.mainloop()