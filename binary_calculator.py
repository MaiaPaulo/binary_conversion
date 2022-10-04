from tkinter import *

class Application:
    def __init__(self, master=None):
        self.standardFont = ("Arial", "15")
        self.firstContainer = Frame(master)
        self.firstContainer["pady"] = 20
        self.firstContainer.pack()

        self.secondContainer = Frame(master)
        self.secondContainer["padx"] = 30
        self.secondContainer.pack()

        self.thirdContainer = Frame(master)
        self.thirdContainer['padx'] = 30
        self.thirdContainer['pady'] = 10
        self.thirdContainer.pack()

        self.fourthContainer = Frame(master)
        self.fourthContainer['padx'] = 30
        self.fourthContainer['pady'] = 10
        self.fourthContainer.pack()

        self.title = Label(self.firstContainer, text="Decimal into Binary")
        self.title["font"] = ("Arial", "25", "bold")
        self.title.pack()

        self.decimalLabel = Label(self.secondContainer, text="Decimal", font=self.standardFont)
        self.decimalLabel.pack(side=LEFT)

        self.decimal = Entry(self.secondContainer)
        self.decimal["width"] = 20
        self.decimal["font"] = self.standardFont
        self.decimal.pack(side=LEFT)

        self.convert = Button(self.thirdContainer)
        image_bt = PhotoImage(file="C:\\Users\maiap\Documents\pythonProject\icon\click_me.png")
        self.convert.config(image=image_bt)
        self.convert.image_bt = image_bt
        #self.convert["width"] = 50
        #self.convert["height"] = 50
        self.convert["command"] = self.convertion
        self.convert.pack()

        self.byteLabel = Label(self.fourthContainer, text="The result is =", font=self.standardFont)
        self.byteLabel.pack(side=LEFT)

        self.byte = Label(self.fourthContainer, text="")
        self.byte["font"] = ("Arial", "17", "bold")
        self.byte.pack()

    # function to convert the number to binary
    def convertion(self):
        num = int(self.decimal.get())
        x = 1
        aux = []
        while num >= x:
            x = num % 2
            num //= 2
            aux.append(x)
        aux.reverse()
        self.byte["text"] = aux

root = Tk()
Application(root)
button_img = PhotoImage(file="C:\\Users\maiap\Documents\pythonProject\icon\click_me.png")
root.title("Decimal - Binary")
root.geometry("450x250")
root.iconbitmap("C:\Documents and Settings\maiap\Documents\pythonProject\icon\math.ico")
root.mainloop()