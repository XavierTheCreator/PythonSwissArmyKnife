from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfile,asksaveasfile, asksaveasfilename

#Variables, setting window 
window = Tk()
menubar = Menu(window)


window.config(menu=menubar)
window.title("Text Editor")
blank = Text(window,font=("arail",10))
blank.pack()

#Methods
def open_file():
    blank.delete("1.0",END)
    file = askopenfile(mode="r", filetypes=[("text files","*.txt")])
    if file is not None:
        text = file.read()
        blank.insert("1.0",text)

def save_file():
    text = blank.get("1.0","end-1c")
    file = asksaveasfilename(title="Save",filetypes=[("text files", "*.txt")])
    with open(file,"w")as data:
        data.write(text)

#File menu setup
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "File", menu=filemenu)
filemenu.add_command(label = "Open", command = open_file)
filemenu.add_command(label = "Save",command= save_file)
filemenu.add_command(label = "Exit", command = window.destroy)

if __name__ == "__main__":
    window.mainloop()
 