from tkinter import *
import subprocess 
import re

repeat = r"^repeat"
id = r"([a-z][a-z0-9]*) :=|:= ([a-z][a-z0-9]*)"
until  = r"^until"


root = Tk()
root.title("DFA Visulization")
root.geometry("500x500")
txt = Text(root, width=20, height=5, font=("Ubuntu", 20))
txt.pack()

def generate_tokens():
    with open("input.txt", 'r') as f:
        lines = f.readlines()
        print(lines)
        for line in lines:
            if re.match(repeat, line):
                l1 = re.findall(repeat, line)
                for s in l1:
                    label1 = Label(root,text=s + " : " + "Reserved word")
                    label1.config(font=("Ubuntu", 30))
                    label1.pack()
            if ":=" in line:
                label2 = Label(root,text=":=" + " : " + "Assignment operator")
                label2.config(font=("Ubuntu", 30))
                label2.pack()
            for c in line:
                if c == ";":
                    label3= Label(root,text=";" + " : " + "Semi Colon")
                    label3.config(font=("Ubuntu", 30))
                    label3.pack()
            if re.match(id, line):
                l2 = re.findall(id, line)
                for s in l2:
                    label4 = Label(root,text=s[0] + " : " + "ID")
                    label4.config(font=("Ubuntu", 30))
                    label4.pack()
            if re.match(until, line):
                l3 = re.findall(until, line)
                for s in l3:
                    label5 = Label(root,text=s + " : " + "Reserved word")
                    label5.config(font=("Ubuntu", 30))
                    label5.pack()
        
def invoke_click():
    with open("input.txt", "w") as f:
        f.write(txt.get(1.0, END))
    subprocess.run(["manim", "-psqh", "Tiny-compiler.py"])

button1 = Button(root, text="Play animation", padx= 10, pady=10, command=invoke_click)
button1.pack()
button2 = Button(root, text="generate token list", padx = 8, pady =10,command=generate_tokens)
button2.pack()
label=Label(root, text='')
label.pack(pady=20)

root.mainloop()
