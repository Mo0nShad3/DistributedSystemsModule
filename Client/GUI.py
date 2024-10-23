import customtkinter
import random

date = "21.10.24"
time = "14:34"

price = "£24.05"

class billLog_Frame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Widgets
        self.dateLabel1 = customtkinter.CTkLabel(self, font=("Consolas" ,11), text=date)
        self.dateLabel1.grid(row=0, column=0, padx=20, pady=(15,0), sticky="nw")
        self.priceLabel1 = customtkinter.CTkLabel(self, font=("Consolas" ,14), text_color="#636fe3", text=price)
        self.priceLabel1.grid(row=1, column=0, padx=20, pady=(0, 15), sticky="sw")

        self.dateLabel2 = customtkinter.CTkLabel(self, font=("Consolas" ,11), text=date)
        self.dateLabel2.grid(row=0, column=1, padx=20, pady=(15,0), sticky="nw")
        self.priceLabel2 = customtkinter.CTkLabel(self, font=("Consolas" ,14), text_color="#636fe3", text=price)
        self.priceLabel2.grid(row=1, column=1, padx=20, pady=(0,15), sticky="sw")

        self.dateLabel1 = customtkinter.CTkLabel(self, font=("Consolas" ,11), text=date)
        self.dateLabel1.grid(row=0, column=2, padx=20, pady=(15,0), sticky="nw")
        self.priceLabel1 = customtkinter.CTkLabel(self, font=("Consolas" ,14), text_color="#636fe3", text=price)
        self.priceLabel1.grid(row=1, column=2, padx=20, pady=(0,15), sticky="sw")

        self.dateLabel1 = customtkinter.CTkLabel(self, font=("Consolas" ,11), text=date)
        self.dateLabel1.grid(row=0, column=3, padx=20, pady=(15,0), sticky="nw")
        self.priceLabel1 = customtkinter.CTkLabel(self,  font=("Consolas" ,14), text_color="#636fe3", text=price)
        self.priceLabel1.grid(row=1, column=3, padx=20, pady=(0,15), sticky="sw")

        self.dateLabel1 = customtkinter.CTkLabel(self, font=("Consolas" ,11), text=date)
        self.dateLabel1.grid(row=0, column=4, padx=20, pady=(15,0), sticky="nw")
        self.priceLabel1 = customtkinter.CTkLabel(self, font=("Consolas" ,14), text_color="#636fe3", text=price)
        self.priceLabel1.grid(row=1, column=4, padx=20, pady=(0,15), sticky="sw")

class userCard_Frame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Widgets
        self.loggedInLabel = customtkinter.CTkLabel(self, font=("Consolas" ,10), text_color="#A3A3A3", text="You are logged in as:")
        self.loggedInLabel.grid(row=0, column=0, padx=20, pady=(15,0), sticky="nw")
        self.nameLabel = customtkinter.CTkLabel(self, font=("Consolas" ,14), text_color="#FFFFF0", text="Temitope Adeosun")
        self.nameLabel.grid(row=1, column=0, padx=20, pady=(0, 15), sticky="sw")

        #self.profilePicture = customtkinter.CTkImage("Icon2.ico")
        #self.profilePicture.grid(row=0, column=1, padx=20, pady=(15,0), sticky="e")

class status_Frame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Widgets
        self.statusLabel = customtkinter.CTkLabel(self, font=("Consolas" ,10), text_color="#FFFFF0", text="Powergrid Status: ONLINE")
        self.statusLabel.grid(row=0, column=0, padx=20, pady=(15,0), sticky="nw")

class timeCard_Frame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Widgets
        self.timeLabel = customtkinter.CTkLabel(self, font=("Consolas" ,40), text_color="#FFFFF0", text=time)
        self.timeLabel.grid(row=0, column=0, padx=(10,50), pady=40, sticky="nsew")

class mainWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("616x254")
        self.title("Smart Meter")
        #self.wm_iconbitmap("Icon2.ico")
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure((0,1), weight=1)

        # Add widgets to app
        # ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
        self.billLog = billLog_Frame(self)
        self.billLog.grid(row=0, column=0, padx=10, pady=(10,0), sticky="nsew", columnspan=2)

        self.userCard = userCard_Frame(self)
        self.userCard.grid(row=1, column=1, padx=10, pady=(10,10), sticky="ew")

        self.statusWidget = status_Frame(self)
        self.statusWidget.grid(row=2, column=1, padx=10, pady=(0,10),sticky="ew")

        self.timeCard = timeCard_Frame(self)
        self.timeCard.grid(row=1, column=0, padx=10,pady=(10,10),sticky="nsew", rowspan=2)

        #self.button = customtkinter.CTkButton(self, command=self.button_callback)
        #self.button.grid(row=4, column=0, padx=20, pady=10, sticky="ew")

    # Add Methods to app
    def button_callback(self):
        print("Text output")

mainWindow = mainWindow()
mainWindow.mainloop()