# import our required library TK Interface
import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.label_1 = tkinter.Label(self.main_window, text='This is some type of text that is suppose to be seasonal')
        self.label_2 = tkinter.Label(self.main_window, text='Extra words to get a better grade right ?')
        self.label_3 = tkinter.Label(self.main_window, text='What else should I say ?')
        self.label_4 = tkinter.Label(self.main_window, text='Well I think I wasted enough of both of our times !')

        # package lable to make it referancable to the main window
        self.label_1.pack()
        self.label_2.pack()
        self.label_3.pack(side = 'right')
        self.label_4.pack(side = 'left')

        # enter the main loop of Tkinter()
        tkinter.mainloop()

my_gui = MyGUI()
