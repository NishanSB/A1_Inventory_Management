import tkinter as tk # Importing tkinter and shortening it to tk 
from tkinter import ttk # Importing ttk for treeview.
import csv # Importing csv for data handling


root = tk.Tk() # Making the GUI
root.geometry("600x300")  # Setting window size
root.title("Login")  # Setting window title

font_size = ("Arial", 16) # sets font_size to 16 which is bigger as it was too small

def login(): # Login confirmation function
    entered_username = username_entry.get()
    entered_password = password_entry.get() #G etting the inputted username and password and assigning them to variables.

    with open("D:\\Python\\SDLC assignment\\users.csv", 'r', newline = '') as file: # Open and read the users.csv file
        csvreader = csv.DictReader(file) # File reader

        for row in csvreader:
            if row["username"] == entered_username and row["password"] == entered_password: # In CSV file there are 2 rows (username and password). Checks to match with the entered ones.
                result_label.config(text = "Login Success") # If they match print login success onto the screen
                openInvManager()
                return
    result_label.config(text = "Login Failed") # If they dont match then the password is wrong and it prints login failed onto the scree.

frame = tk.Frame(root) # Puts the login area into a frame
frame.place(relx = 0.5, rely = 0.5, anchor = "center") # Centres the frame into the middle of the screen

# Creating all labels and entrys needed for the login
login_label    = tk.Label(frame, text  = "Login")
username_label = tk.Label(frame, text  = "Username")
username_entry = tk.Entry(frame)
password_label = tk.Label(frame, text  = "Password")
password_entry = tk.Entry(frame, show  = "*") # Shows * to hide password when entering
login_button   = tk.Button(frame, text = "Login", command = login) # Command will make it run the login function
result_label   = tk.Label(frame, text  = "")

# Setting all the labels and entrys to have a bigger font size to make it easier to see.
login_label.config(font    = font_size)
username_entry.config(font = font_size)
username_label.config(font = font_size)
password_entry.config(font = font_size)
password_label.config(font = font_size)
login_button.config(font   = font_size)
result_label.config(font   = font_size)

# Displays the labels onto the screen.
login_label.grid(row    = 0, column = 0, columnspan = 2)
username_label.grid(row = 1, column = 0)
username_entry.grid(row = 1, column = 1)
password_label.grid(row = 2, column = 0)
password_entry.grid(row = 2, column = 1)
login_button.grid(row   = 3, column = 0, columnspan = 2)
result_label.grid(row   = 4, column = 0, columnspan = 2)

# Function to open a new window after login
def openInvManager(): 
    window = tk.Toplevel(root) # root is the main window and this is a side window.
    window.title("Inventory Management")
    window.geometry("600x600")

    # Loading the inventory csv file.
    def loadInventory():
        tree.delete(*tree.get_children()) # * will separate get_children() into different arguments to delete to clear the table.
        with open("D:\\Python\\SDLC assignment\\inventory.csv", 'r', newline = '') as file:
            reader = csv.DictReader(file)
            for row in reader:
                tree.insert("", "end", values = (row["Item Name"], row ["SKU"], row["Quantity"])) # "" means theres no parent and end is at the end of the list and it just adds those row items.

    # Adds item into inventory(csv).
    def addItem():
        name     = item_entry.get()
        sku      = sku_entry.get()
        quantity = quantity_entry.get()
        if not name or not sku or not quantity: # If all fields aren't given
            message_label.config(text = "All fields required.") # Changes message_label to say All fields required
            return
        with open("D:\\Python\\SDLC assignment\\inventory.csv", 'a', newline = '') as file:
            writer = csv.writer(file)
            writer.writerow([name, sku, quantity]) #Adds the new name,sku and quantity to the csv
        message_label.config(text = "Added Item.")
        loadInventory() # Reloads the table to see the new item

    # Uses the SKU to only display a certain item.
    def searchItem():
        sku = sku_entry.get()
        if not sku:
            message_label.config(text = "Enter SKU to search.")
            return
        tree.delete(*tree.get_children()) # * will separate get_children() into different arguments to delete to clear the table.
        with open("D:\\Python\\SDLC assignment\\inventory.csv", 'r', newline = '') as file:
            reader = csv.DictReader(file)
            itemFound = False # Has the item been found
            for row in reader:
                if row["SKU"] == sku: #If the SKU in the row is the same one that is given
                    tree.insert("", "end", values = (row["Item Name"], row ["SKU"], row["Quantity"])) #Then insert give all the data for that row
                    itemFound = True # Then it has found the item.
            if itemFound:
                message_label.config(text = "Item Found.") # Display Purposes
            else:
                message_label.config(text = "Item Not Found.")

    # Removes an item from the inventory using the SKU.
    def removeItem():
        sku = sku_entry.get()
        if not sku:
            message_label.config(text = "Enter SKU to remove.")
            return
        rows = [] # This list of SKUs to keep.
        itemRemoved = False
        with open("D:\\Python\\SDLC assignment\\inventory.csv", 'r', newline = '') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["SKU"] != sku:
                    rows.append(row) #If the SKU is not the one the use inputted to be deleted, its added to the list to keep.
                else:
                    itemRemoved = True
        with open("D:\\Python\\SDLC assignment\\inventory.csv", 'w', newline = '') as file:
            writer = csv.DictWriter(file, fieldnames=["Item Name", "SKU", "Quantity"])
            writer.writeheader() 
            writer.writerows(rows) # Overwrites the CSV and adds all the rows besides the one which we wanted to remove.
        if itemRemoved:
            message_label.config(text = "Item Removed.") # Display Purposes
        else:
            message_label.config(text = "Item Not Removed.") # Display Purposes
        loadInventory() # Reloads the inventory manager without the removed item.


    # Adds Inventory Manager to the new window and pads it down slightly.
    label = tk.Label(window, text = "Inventory Manager", font = ("Arial", 16))
    label.pack(pady = 10)

    # Making a new frame for the inputs.
    inputFrame = tk.Frame(window)
    inputFrame.pack(pady = 10)

    # Adding the add, remove and search buttons to the new window.
    add_button    = tk.Button(inputFrame, text = "Add Item", font    = font_size, command = addItem)  
    remove_button = tk.Button(inputFrame, text = "Remove Item", font = font_size, command = removeItem)
    search_button = tk.Button(inputFrame, text = "Search Item", font = font_size, command = searchItem)

    # Creating the labels and entries to add data to database.
    item_label     = tk.Label(inputFrame, text = "Item Name", font = font_size)
    item_entry     = tk.Entry(inputFrame, font = font_size)
    sku_label      = tk.Label(inputFrame, text = "SKU ", font = font_size)
    sku_entry      = tk.Entry(inputFrame, font = font_size)
    quantity_label = tk.Label(inputFrame, text = "Quantity", font = font_size)
    quantity_entry = tk.Entry(inputFrame, font = font_size)

    # Displaying all necessary buttons, entries and labels.
    item_label.grid(row     = 0, column = 0)
    item_entry.grid(row     = 0, column = 1)    
    sku_label.grid(row      = 1, column = 0)
    sku_entry.grid(row      = 1, column = 1)
    quantity_label.grid(row = 2, column = 0)
    quantity_entry.grid(row = 2, column = 1)
    add_button.grid(row     = 3, column = 0)
    remove_button.grid(row  = 3, column = 1)
    search_button.grid(row  = 3, column = 2)

    # Error message
    message_label = tk.Label(window, text = "", font = font_size)
    message_label.pack()

    # Sets up a tree using treeview for handling and displaying the data.
    tree = ttk.Treeview(window, columns = ("Item Name", "SKU", "Quantity"), show = "headings")
    for column in ("Item Name", "SKU", "Quantity"):
        tree.heading(column, text = column)
        tree.column(column, width = 200)
    tree.pack(pady = 10, fill = "both", expand = True)

    loadInventory() # Loads the inventory up.

root.mainloop() # Runs the main loop