import tkinter as tk #importing tkinter and shortening it to tk 
import csv #importing csv for data handling


root = tk.Tk() #Making the GUI
root.geometry("600x300")  # Setting window size
root.title("Login")  # Setting window title

def login(): #Login confirmation function
    entered_username = username_entry.get()
    entered_password = password_entry.get() #Getting the inputted username and password and assigning them to variables.

    with open("D:\\Python\\SDLC assignment\\users.csv", 'r') as file: #Open and read the users.csv file
        csvreader = csv.DictReader(file) #file reader

        for row in csvreader:
            if row["username"] == entered_username and row["password"] == entered_password: #In CSV file there are 2 rows (username and password). Checks to match with the entered ones.
                result_label.config(text = "Login Success") # Ifthey match print login success onto the screen
                return
    result_label.config(text = "Login Failed") # If they dont match then the password is wrong and it prints login failed onto the scree.

frame = tk.Frame(root) #puts the login area into a frame
frame.place(relx = 0.5, rely = 0.5, anchor = "center") #centres the frame into the middle of the screen

#Creating all labels and entrys needed for the login
login_label = tk.Label(frame, text = "Login")
username_label = tk.Label(frame, text = "Username")
username_entry = tk.Entry(frame)
password_label = tk.Label(frame, text = "Password")
password_entry = tk.Entry(frame, show = "*") #Shows * to hide password when entering
login_button = tk.Button(frame, text = "Login", command = login) #command will make it run the login function
result_label = tk.Label(frame, text="")

font_size = ("Arial", 16) # sets font_size to 16 which is bigger

#Setting all the labels and entrys to have a bigger font size to make it easier to see.
login_label.config(font = font_size)
username_entry.config(font = font_size)
username_label.config(font = font_size)
password_entry.config(font = font_size)
password_label.config(font = font_size)
login_button.config(font = font_size)
result_label.config(font = font_size)

#Displays the labels onto the screen.
login_label.grid(row = 0, column = 0, columnspan = 2)
username_label.grid(row = 1, column = 0)
username_entry.grid(row = 1, column = 1)
password_label.grid(row = 2, column = 0)
password_entry.grid(row = 2, column = 1)
login_button.grid(row = 3, column = 0, columnspan = 2)
result_label.grid(row = 4, column = 0, columnspan = 2)

root.mainloop() # Runs the main loop