'''
1)Look for the assets folder for the respective images.
2)Download the font Salsa it looks really nice, Here's the link

Download font from here - https://fonts.google.com/specimen/Salsa

3)Make sure your server is working and change the credentials as required.
4)Make sure you have the required libraries
5)Change the required data within these <>
6) Finally if you like my work then you may buy me a coffee.

https://www.buymeacoffee.com/sourish

'''

#importing libraries
import tkinter as tk
from pathlib import Path
import mysql.connector
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from PIL import Image
#------------------Path------------------
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#------------------Login Page-------------
window = Tk()
window.geometry("800x500")
window.title('EMS')
ico = PhotoImage(
    file=relative_to_assets("db.png"))
window.iconphoto(False,ico)
window.configure(bg = "#FFFFFF")

con = mysql.connector.connect(host="localhost",user="----------<Give your Username>------"
,password="---<Password>---",database="----<DatabaseName>----")
cur = con.cursor()

lframe = Frame(window,height = 500,width = 800)
lframe.place(x=0,y=0)

logcnv = Canvas(
    lframe,
    bg = "#FFFFFF",
    height = 500,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

logcnv.place(x = 0, y = 0)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = logcnv.create_image(
    594.0,
    304.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#C4C4C4",
    show='*',
    highlightthickness=0
)
entry_1.place(
    x=446.0,
    y=279.0+19,
    width=296.0,
    height=28.0
)

logcnv.create_text(
    438.0,
    279.0,
    anchor="nw",
    text="Password",
    fill="#000000",
    font=("Salsa", 12 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = logcnv.create_image(
    594.0,
    194.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#C4C4C4",
    font=("Salsa", 15 * -1),
    highlightthickness=0
)
entry_2.place(
    x=446.0,
    y=169.0+19,
    width=296.0,
    height=28.0
)

logcnv.create_text(
    438.0,
    169.0,
    anchor="nw",
    text="Username",
    fill="#000000",
    font=("Salsa", 12 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print('Button Clicked'),
    relief="flat"
)
button_1.place(
    x=526.0,
    y=389.0,
    width=136.0,
    height=45.0
)

logcnv.create_rectangle(
    0.0,
    0.0,
    395.0,
    500.0,
    fill="#5D5FEF",
    outline="")

logcnv.create_text(
    21.0,
    45.0,
    anchor="nw",
    text="Login into",
    fill="#FFFFFF",
    font=("Salsa", 48 * -1)
)

logcnv.create_text(
    21.0,
    104.0,
    anchor="nw",
    text="your",
    fill="#FFFFFF",
    font=("Salsa", 48 * -1)
)

logcnv.create_text(
    21.0,
    163.0,
    anchor="nw",
    text="Account",
    fill="#FFFFFF",
    font=("Salsa", 48 * -1)
)

logcnv.create_text(
    414.0,
    22.0,
    anchor="nw",
    text="Enter your Username",
    fill="#000000",
    font=("Salsa", 36 * -1)
)

logcnv.create_text(
    414.0,
    75.0,
    anchor="nw",
    text="and Password",
    fill="#000000",
    font=("Salsa", 36 * -1)
)
window.resizable(False, False)


def login():
 if entry_2.get()=="" or entry_1.get()=="":
  messagebox.showerror("Error","Enter User Name And Password",parent=window)	
 else:
  try:
   cur.execute("select * from <TABLE NAME> where <USERNAME COLUMN NAME>=%s and <PASSWORD COLUMN NAME> = %s",(entry_2.get(),entry_1.get()))
   row = cur.fetchone()   
   if row == None:
    	   messagebox.showinfo("Error","Invalid Username and Password",parent=window)
   else:
       messagebox.showinfo("Success" , "Authentication Succeded" , parent = window)                 
  except Exception as es:
   messagebox.showerror("Error",f"Error Due to : {str(es)}",parent = window)
