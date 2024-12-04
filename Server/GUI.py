import customtkinter
import random
from datetime import datetime, timedelta

user = "Admin"

 # STATUS NEEDS ADMIN OR BACKEND INTEGRATION
 # |
 # v

status = True

date_and_time = datetime.now()
time = date_and_time.strftime("%H:%M")
date = date_and_time.strftime("%d/%m/%Y")

def get_date (days_ago):
    today = datetime.now()
    target_date = today - timedelta(days=days_ago)
    return target_date.strftime("%d/%m/%Y")

def get_error (error_num):
    return "#" + str(error_num) + " Error"

def get_status (boolean):
    if boolean == True:
        return "ONLINE"
    else:
        return "OFFLINE"

def report_click ():
    global status
    if status == True:
        status = False
    else:
        status = True

class errorLog_Frame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Widgets
        self.errorLabel1 = customtkinter.CTkLabel(self, font=("Consolas" ,11), text_color="#FF2222", text=get_error(1))
        self.errorLabel1.grid(row=0, column=0, padx=20, pady=(8), sticky="nw")
        
        self.errorLabel2 = customtkinter.CTkLabel(self, font=("Consolas" ,11), text_color="#FF2222", text=get_error(2))
        self.errorLabel2.grid(row=1, column=0, padx=20, pady=(8), sticky="nw")

        self.errorLabel3 = customtkinter.CTkLabel(self, font=("Consolas" ,11), text_color="#FF2222", text=get_error(3))
        self.errorLabel3.grid(row=2, column=0, padx=20, pady=(8), sticky="nw")
        
        self.errorLabel4 = customtkinter.CTkLabel(self, font=("Consolas" ,11), text_color="#FF2222", text=get_error(4))
        self.errorLabel4.grid(row=3, column=0, padx=20, pady=(8), sticky="nw")

        self.errorLabel5 = customtkinter.CTkLabel(self, font=("Consolas" ,11), text_color="#FF2222", text=get_error(5))
        self.errorLabel5.grid(row=4, column=0, padx=20, pady=(8), sticky="nw")

class userCard_Frame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.loggedInLabel = customtkinter.CTkLabel(
            self,
            font=("Consolas", 10),
            text_color="#A3A3A3",
            text="You are logged in as:",
            anchor="w"
        )
        self.loggedInLabel.grid(row=0, column=0, padx=20, pady=(15,0), sticky="nsew")

        self.nameLabel = customtkinter.CTkLabel(
            self,
            font=("Consolas", 14),
            text_color="#FFFFF0",
            text=user,
            anchor="w"
        )
        self.nameLabel.grid(row=1, column=0, padx=20, pady=(0, 15), sticky="nsew")

        #self.profilePicture = customtkinter.CTkImage("Icon2.ico")
        #self.profilePicture.grid(row=0, column=1, padx=20, pady=(15,0), sticky="e")

class status_Frame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.statusLabel = customtkinter.CTkLabel(
            self,
            font=("Consolas", 12),
            text_color="#FFFFF0",
            text="Powergrid Status: " + get_status(status),
            anchor="w"
        )
        self.statusLabel.grid(row=0, column=0, padx=20, pady=(10, 10), sticky="nsew")

        self.update_status()

    def update_status(self):
        self.statusLabel.configure(text="Powergrid Status: " + get_status(status))
        self.after(1000, self.update_status)

class button_Frame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.reportButton = customtkinter.CTkButton(
            self,
            text="Report Issue",
            font=("Consolas", 12),
            text_color="#FFFFF0",
            command=report_click
        )
        self.reportButton.grid(row=0, column=0, padx=20, pady=(10, 10), sticky="nsew")

        self.update_status()

    def get_button_text(self):
        if status == True:
            return "Report Issue"
        else:
            return "Report Fixed"
        
    def update_status(self):
        self.reportButton.configure(text=self.get_button_text())
        self.after(1000, self.update_status)

class mainWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("616x254")
        self.title("Smart Meter: Admin")
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=3)
        self.grid_rowconfigure(1, weight=1)
        self.resizable(False, False)

        self.errorLog = errorLog_Frame(self)
        self.errorLog.grid(row=0, column=0, rowspan=3, padx=10, pady=(10), sticky="nsew")

        self.userCard = userCard_Frame(self)
        self.userCard.grid(row=0, column=1, padx=(0,10), pady=(10,10), sticky="nsew")

        self.statusWidget = status_Frame(self)
        self.statusWidget.grid(row=1, column=1, padx=(0,10), pady=(0,10), sticky="nsew")

        self.buttonWidget = button_Frame(self)
        self.buttonWidget.grid(row=2, column=1, padx=(0,10), pady=(0,10), sticky="nsew")


    # Add Methods to app
    def button_callback(self):
        print("Text output")

mainWindow = mainWindow()
<<<<<<< HEAD
mainWindow.mainloop()
=======
mainWindow.mainloop()
>>>>>>> 09ec160 (Finalised the code.)
