from tkinter import *
class MyLabelFrame(Tk):
    def __init__(self):
        super().__init__()
        # labelframe is defined and the text is assigned to be dis-played by the frame.
        self.mylf1 = LabelFrame(self, text="I am Label-Frame", font = ('Calibri',12), bg = 'LightBlue', labelanchor = N)
        self.mylf1.pack(fill="both", expand="yes")
        #Label is defined and created
        self.myl1 = Label(self.mylf1, text="I am Label", bg = 'Magenta')
        self.myl1.pack(side = LEFT)
    
if __name__ == '__main__':
    myroot = MyLabelFrame() # creating an instance of Scrollbar_En-try
    myroot.geometry('400x150')
    myroot.mainloop() # infinite loop to run the application