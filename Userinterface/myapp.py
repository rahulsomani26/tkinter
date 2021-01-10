import tkinter as tk
from tkinter import PhotoImage


class MainScreen(tk.Frame):

    HEIGHT = 800
    WIDTH = 800

    def __init__(self, master):

        self.master = master
        self.master.title('Student form')
        tk.Frame.__init__(self, self.master)
        self.create_gui()

    def create_gui(self):

        self.entryString = tk.StringVar()

        self.canvas = tk.Canvas(
            self.master, width=self.WIDTH, height=self.HEIGHT)

        self.canvas.pack()   # side, expand, fill ( arguments )

        self.backgroundImg = tk.PhotoImage(
            file=r'C:\Users\aayush\Desktop\python-tkinter\weather app\weathergui\logo.png')

        self.backgroundContainer = tk.Label(
            self.canvas, image=self.backgroundImg)
        self.backgroundContainer.place(
            relx=0.1, rely=0.1, relwidth=0.58, relheight=0.2)

        self.frame = tk.Frame(self.master, bg='#2fa6aa', bd=5)
        self.frame.place(relx=0.34, rely=0.7, relwidth=0.2, relheight=0.1)

        self.enterButton = tk.Button(
            self.frame, text="Click", command=self.testMe)
        self.enterButton.place(x=0, y=0, relwidth=1, relheight=1)

        self.entry = tk.Entry(
            self.frame, textvariable=self.entryString, font=40)
        # self.entry.place(relx=0.05, rely=0.2, relwidth=0.4, relheight=0.5)
        self.entry.pack()
        self.button = tk.Button(self.frame, text='click')
        self.button.place(relx=0.65, rely=0.2, relwidth=0.3, relheight=0.5)

        self.output_frame = tk.Frame(self.master, bg='#2fa6aa', bd=10)
        self.output_frame.place(
            relx=0.1, rely=0.3, relwidth=0.7, relheight=0.5)

        # message = tk.Message(output_frame)
        # message.place(relx=0.1, rely=0.1, relwidth=0.6, relheight=0.45)

        self.label = tk.Label(self.output_frame)
        self.label.place(relwidth=1, relheight=1)

    def testMe(self):
        print(' Working')


if __name__ == '__main__':
    root = tk.Tk()
    app = MainScreen(root)
    app.mainloop()
