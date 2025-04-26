from tkinter import *
class Gui:
    def __init__(self):
        self.root = Tk()
        self.root.wm_title("Calculator")
        self.root.wm_geometry("400x520+50+50")
        self.root.configure(background='gold')

        self.active_entry = "en1"

        self.en1 = Entry(master=self.root, font=('Consolas', 18, 'bold'), background="ivory")
        self.en1.place(x=20, y=20, width=80, height=50)
        self.en1.bind("<FocusIn>", lambda event: self.set_active_entry("en1"))

        self.en2 = Entry(master=self.root, font=('Consolas', 18, 'bold'), background="ivory")
        self.en2.place(x=150, y=20, width=80, height=50)
        self.en2.bind("<FocusIn>", lambda event: self.set_active_entry("en2"))

        self.en3 = Entry(master=self.root, font=('Consolas', 18, 'bold'), background="ivory")
        self.en3.place(x=280, y=20, width=80, height=50)

        for i in range(10):
            if i == 0:
                x, y = 35, 270 
            else:
                x = 35 + ((i - 1) % 3) * 130 
                y = 90 + ((i - 1) // 3) * 60  
            
            Button(master=self.root, text=str(i), font=('Consolas', 18, 'bold'), background="lightcyan",
                   command=lambda num=i: self.number_click(num)).place(x=x, y=y, width=50, height=50)

        self.btclr = Button(master=self.root, text="All Clear", font=('Consolas', 18, 'bold'),
                            background="paleturquoise", command=self.clear)
        self.btclr.place(x=165, y=270, width=180, height=50)

        self.btadd = Button(master=self.root, text="+", font=('Consolas', 18, 'bold'), command=self.add, background="lightcyan")
        self.btadd.place(x=35, y=330, width=50, height=50)

        self.btsub = Button(master=self.root, text="-", font=('Consolas', 18, 'bold'), command=self.sub, background="lightcyan")
        self.btsub.place(x=165, y=330, width=50, height=50)

        self.btmul = Button(master=self.root, text="x", font=('Consolas', 18, 'bold'), command=self.mul, background="lightcyan")
        self.btmul.place(x=295, y=330, width=50, height=50)

        self.btdiv = Button(master=self.root, text="/", font=('Consolas', 18, 'bold'), command=self.div, background="lightcyan")
        self.btdiv.place(x=35, y=390, width=50, height=50)

        self.btmodulo = Button(master=self.root, text="%", font=('Consolas', 18, 'bold'), command=self.modulo, background="lightcyan")
        self.btmodulo.place(x=165, y=390, width=50, height=50)

        self.btfloor = Button(master=self.root, text="//", font=('Consolas', 18, 'bold'), command=self.floor, background="lightcyan")
        self.btfloor.place(x=295, y=390, width=50, height=50)

    def set_active_entry(self, entry_name):
        self.active_entry = entry_name

    def number_click(self, number):
        if self.active_entry == "en1":
            self.en1.insert(END, str(number))
        elif self.active_entry == "en2":
            self.en2.insert(END, str(number))

    def add(self):
        try:
            num1 = float(self.en1.get())
            num2 = float(self.en2.get())
            self.en3.delete(0, END)
            self.en3.insert(0, str(num1 + num2))
        except ValueError:
            self.en3.delete(0, END)
            self.en3.insert(0, "Error")

    def sub(self):
        try:
            num1 = float(self.en1.get())
            num2 = float(self.en2.get())
            self.en3.delete(0, END)
            self.en3.insert(0, str(num1 - num2))
        except ValueError:
            self.en3.delete(0, END)
            self.en3.insert(0, "Error")

    def mul(self):
        try:
            num1 = float(self.en1.get())
            num2 = float(self.en2.get())
            self.en3.delete(0, END)
            self.en3.insert(0, str(num1 * num2))
        except ValueError:
            self.en3.delete(0, END)
            self.en3.insert(0, "Error")

    def div(self):
        try:
            num1 = float(self.en1.get())
            num2 = float(self.en2.get())
            if num2 == 0:
                self.en3.delete(0, END)
                self.en3.insert(0, "Error")
            else:
                self.en3.delete(0, END)
                self.en3.insert(0, str(num1 / num2))
        except ValueError:
            self.en3.delete(0, END)
            self.en3.insert(0, "Error")

    def modulo(self):
        try:
            num1 = float(self.en1.get())
            num2 = float(self.en2.get())
            self.en3.delete(0, END)
            self.en3.insert(0, str(num1 % num2))
        except ValueError:
            self.en3.delete(0, END)
            self.en3.insert(0, "Error")

    def floor(self):
        try:
            num1 = float(self.en1.get())
            num2 = float(self.en2.get())
            self.en3.delete(0, END)
            self.en3.insert(0, str(num1 // num2))
        except ValueError:
            self.en3.delete(0, END)
            self.en3.insert(0, "Error")

    def clear(self):
        self.en1.delete(0, END)
        self.en2.delete(0, END)
        self.en3.delete(0, END)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Gui()
    app.run()