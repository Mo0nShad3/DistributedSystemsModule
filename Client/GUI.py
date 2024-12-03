<<<<<<< HEAD
import customtkinter
import random
from datetime import datetime, timedelta

user = "Customer"

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

 # PRICE NEEDS BACKEND INTEGRATION
 # |
 # v

def get_price (days_ago_price):
    return "£ " + str(days_ago_price) + "d ago"

def get_status (boolean):
    if boolean == True:
        return "ONLINE"
    else:
        return "OFFLINE"

class billLog_Frame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Widgets
        self.dateLabel1 = customtkinter.CTkLabel(self, font=("Consolas" ,11), text=get_date(4))
        self.dateLabel1.grid(row=0, column=0, padx=20, pady=(15,0), sticky="nw")
        self.priceLabel1 = customtkinter.CTkLabel(self, font=("Consolas" ,14), text_color="#636fe3", text=get_price(4))
        self.priceLabel1.grid(row=1, column=0, padx=20, pady=(0, 15), sticky="sw")

        self.dateLabel2 = customtkinter.CTkLabel(self, font=("Consolas" ,11), text=get_date(3))
        self.dateLabel2.grid(row=0, column=1, padx=20, pady=(15,0), sticky="nw")
        self.priceLabel2 = customtkinter.CTkLabel(self, font=("Consolas" ,14), text_color="#636fe3", text=get_price(3))
        self.priceLabel2.grid(row=1, column=1, padx=20, pady=(0,15), sticky="sw")

        self.dateLabel3 = customtkinter.CTkLabel(self, font=("Consolas" ,11), text=get_date(2))
        self.dateLabel3.grid(row=0, column=2, padx=20, pady=(15,0), sticky="nw")
        self.priceLabel3 = customtkinter.CTkLabel(self, font=("Consolas" ,14), text_color="#636fe3", text=get_price(2))
        self.priceLabel3.grid(row=1, column=2, padx=20, pady=(0,15), sticky="sw")

        self.dateLabel4 = customtkinter.CTkLabel(self, font=("Consolas" ,11), text=get_date(1))
        self.dateLabel4.grid(row=0, column=3, padx=20, pady=(15,0), sticky="nw")
        self.priceLabel4 = customtkinter.CTkLabel(self,  font=("Consolas" ,14), text_color="#636fe3", text=get_price(1))
        self.priceLabel4.grid(row=1, column=3, padx=20, pady=(0,15), sticky="sw")

        self.dateLabel5 = customtkinter.CTkLabel(self, font=("Consolas" ,11), text=get_date(0))
        self.dateLabel5.grid(row=0, column=4, padx=20, pady=(15,0), sticky="nw")
        self.priceLabel5 = customtkinter.CTkLabel(self, font=("Consolas" ,14), text_color="#636fe3", text=get_price(0))
        self.priceLabel5.grid(row=1, column=4, padx=20, pady=(0,15), sticky="sw")

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


class timeCard_Frame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.timeLabel = customtkinter.CTkLabel(
            self,
            font=("Helvetica", 60),
            text_color="#555555",
            text="",
            anchor="center"
        )
        self.timeLabel.grid(row=0, column=0, padx=(10, 10), pady=20, sticky="nsew")

        self.update_time()

    def update_time(self):
        current_time = datetime.now().strftime("%H:%M")
        self.timeLabel.configure(text=current_time)
        self.after(1000, self.update_time)

class mainWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("616x254")
        self.title("Smart Meter: User")
        #self.wm_iconbitmap("Icon2.ico")
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure((0,1), weight=1)
        self.resizable(False, False)

        # Add widgets to app
        # ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
        self.billLog = billLog_Frame(self)
        self.billLog.grid(row=0, column=0, padx=10, pady=(10,0), sticky="nsew", columnspan=2)

        self.userCard = userCard_Frame(self)
        self.userCard.grid(row=1, column=1, padx=(0,10), pady=(10,10), sticky="ew")

        self.statusWidget = status_Frame(self)
        self.statusWidget.grid(row=2, column=1, padx=(0,10), pady=(0,10),sticky="ew")

        self.timeCard = timeCard_Frame(self)
        self.timeCard.grid(row=1, column=0, padx=10,pady=(10,10),sticky="nsew", rowspan=2)

        #self.button = customtkinter.CTkButton(self, command=self.button_callback)
        #self.button.grid(row=4, column=0, padx=20, pady=10, sticky="ew")

    # Add Methods to app
    def button_callback(self):
        print("Text output")

mainWindow = mainWindow()
=======
import customtkinter
import random
from datetime import datetime, timedelta

user = "User"

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

 # PRICE NEEDS BACKEND INTEGRATION
 # |
 # v

def get_price (days_ago_price):
    return "£ " + str(days_ago_price) + "d ago"

def get_status (boolean):
    if boolean == True:
        return "ONLINE"
    else:
        return "OFFLINE"

class billLog_Frame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Widgets
        self.dateLabel1 = customtkinter.CTkLabel(self, font=("Consolas" ,11), text=get_date(4))
        self.dateLabel1.grid(row=0, column=0, padx=20, pady=(15,0), sticky="nw")
        self.priceLabel1 = customtkinter.CTkLabel(self, font=("Consolas" ,14), text_color="#636fe3", text=get_price(4))
        self.priceLabel1.grid(row=1, column=0, padx=20, pady=(0, 15), sticky="sw")

        self.dateLabel2 = customtkinter.CTkLabel(self, font=("Consolas" ,11), text=get_date(3))
        self.dateLabel2.grid(row=0, column=1, padx=20, pady=(15,0), sticky="nw")
        self.priceLabel2 = customtkinter.CTkLabel(self, font=("Consolas" ,14), text_color="#636fe3", text=get_price(3))
        self.priceLabel2.grid(row=1, column=1, padx=20, pady=(0,15), sticky="sw")

        self.dateLabel3 = customtkinter.CTkLabel(self, font=("Consolas" ,11), text=get_date(2))
        self.dateLabel3.grid(row=0, column=2, padx=20, pady=(15,0), sticky="nw")
        self.priceLabel3 = customtkinter.CTkLabel(self, font=("Consolas" ,14), text_color="#636fe3", text=get_price(2))
        self.priceLabel3.grid(row=1, column=2, padx=20, pady=(0,15), sticky="sw")

        self.dateLabel4 = customtkinter.CTkLabel(self, font=("Consolas" ,11), text=get_date(1))
        self.dateLabel4.grid(row=0, column=3, padx=20, pady=(15,0), sticky="nw")
        self.priceLabel4 = customtkinter.CTkLabel(self,  font=("Consolas" ,14), text_color="#636fe3", text=get_price(1))
        self.priceLabel4.grid(row=1, column=3, padx=20, pady=(0,15), sticky="sw")

        self.dateLabel5 = customtkinter.CTkLabel(self, font=("Consolas" ,11), text=get_date(0))
        self.dateLabel5.grid(row=0, column=4, padx=20, pady=(15,0), sticky="nw")
        self.priceLabel5 = customtkinter.CTkLabel(self, font=("Consolas" ,14), text_color="#636fe3", text=get_price(0))
        self.priceLabel5.grid(row=1, column=4, padx=20, pady=(0,15), sticky="sw")

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


class timeCard_Frame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.timeLabel = customtkinter.CTkLabel(
            self,
            font=("Helvetica", 60),
            text_color="#555555",
            text="",
            anchor="center"
        )
        self.timeLabel.grid(row=0, column=0, padx=(10, 10), pady=20, sticky="nsew")

        self.update_time()

    def update_time(self):
        current_time = datetime.now().strftime("%H:%M")
        self.timeLabel.configure(text=current_time)
        self.after(1000, self.update_time)

class mainWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("616x254")
        self.title("Smart Meter: User")
        #self.wm_iconbitmap("Icon2.ico")
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure((0,1), weight=1)
        self.resizable(False, False)

        # Add widgets to app
        # ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
        self.billLog = billLog_Frame(self)
        self.billLog.grid(row=0, column=0, padx=10, pady=(10,0), sticky="nsew", columnspan=2)

        self.userCard = userCard_Frame(self)
        self.userCard.grid(row=1, column=1, padx=(0,10), pady=(10,10), sticky="ew")

        self.statusWidget = status_Frame(self)
        self.statusWidget.grid(row=2, column=1, padx=(0,10), pady=(0,10),sticky="ew")

        self.timeCard = timeCard_Frame(self)
        self.timeCard.grid(row=1, column=0, padx=10,pady=(10,10),sticky="nsew", rowspan=2)

        #self.button = customtkinter.CTkButton(self, command=self.button_callback)
        #self.button.grid(row=4, column=0, padx=20, pady=10, sticky="ew")

    # Add Methods to app
    def button_callback(self):
        print("Text output")

mainWindow = mainWindow()
>>>>>>> 09ec160 (Finalised the code.)
mainWindow.mainloop()