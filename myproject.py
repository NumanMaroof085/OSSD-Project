import tkinter as tk
from tkinter import ttk
import dbfile as db
import Encryption as en

theme = True
def theme1():
    frame2.config(bg="#1e1e1e")
    top_bar.config(bg="#1e1e1e")
    sidebar.config(bg="#2e2e2e")
    main_area.config(bg="#2e2e2e")
    hframe.config(bg="#2e2e2e")
    h1frame.config(bg="#2e2e2e")
    h2frame.config(bg="#2e2e2e")
    h3frame.config(bg="#2e2e2e")
    sframe.config(bg="#2e2e2e")
    cpframe.config(bg="#2e2e2e")
    lframe.config(bg="#2e2e2e")
    nframe.config(bg="#2e2e2e")
    for i in range(0, 4):
        tbbutn[i].config(bg="#3a3a3a",fg="White")
    h2t1.config(bg="#2e2e2e",fg="White")
    h2b1.config(bg="#3a3a3a",fg="White")
    h2b2.config(bg="#3a3a3a",fg="White")
    hl1.config(bg="#2e2e2e",fg="White")
    h3l1.config(background="#2e2e2e",foreground="White")
    h3e1.config(background="#2e2e2e",foreground="White")
    h3b1.config(bg="#3a3a3a",fg="White")
    dropdown.config(bg="#3a3a3a",fg="White")
    nl1.config(background="#2e2e2e",foreground="White")
    ne1.config(background="#2e2e2e",foreground="White")
    nl2.config(background="#2e2e2e",foreground="White")
    ne2.config(bg="#2e2e2e",fg="White")
    nb1.config(bg="#3a3a3a",fg="White")
    sb1.config(bg="#3a3a3a",fg="White")
    sb2.config(bg="#3a3a3a",fg="White")
    cpl1.config(background="#2e2e2e",foreground="White")
    cpe1.config(background="#2e2e2e",foreground="White")
    cpb1.config(bg="#3a3a3a",fg="White")
    cpb2.config(bg="#3a3a3a",fg="White")
    lb1.config(bg="#3a3a3a",fg="White")
    for i in range(0, len(categories)):
        sbbtn[i].config(bg="#3a3a3a",fg="White")

def theme2():
    frame2.config(bg="SystemButtonFace")
    top_bar.config(bg="#F5F5F5")
    sidebar.config(bg="#D9D9D9")
    main_area.config(bg="SystemButtonFace")
    hframe.config(bg="SystemButtonFace")
    h1frame.config(bg="SystemButtonFace")
    h2frame.config(bg="SystemButtonFace")
    h3frame.config(bg="SystemButtonFace")
    sframe.config(bg="SystemButtonFace")
    cpframe.config(bg="SystemButtonFace")
    lframe.config(bg="SystemButtonFace")
    nframe.config(bg="SystemButtonFace")
    for i in range(0, 4):
        tbbutn[i].config(bg="#D9D9D9",fg="Black")
    h2t1.config(bg="SystemButtonFace",fg="Black")
    h2b1.config(bg="#D9D9D9",fg="Black")
    h2b2.config(bg="#D9D9D9",fg="Black")
    hl1.config(bg="SystemButtonFace",fg="Black")
    h3l1.config(background="SystemButtonFace",foreground="Black")
    h3e1.config(background="SystemButtonFace",foreground="Black")
    h3b1.config(bg="#D9D9D9",fg="Black")
    dropdown.config(bg="SystemButtonFace",fg="Black")
    nl1.config(background="SystemButtonFace",foreground="Black")
    ne1.config(background="SystemButtonFace",foreground="Black")
    nl2.config(background="SystemButtonFace",foreground="Black")
    ne2.config(bg="SystemButtonFace",fg="Black")
    nb1.config(bg="#D9D9D9",fg="Black")
    sb1.config(bg="#D9D9D9",fg="Black")
    sb2.config(bg="#D9D9D9",fg="Black")
    cpl1.config(background="SystemButtonFace",foreground="Black")
    cpe1.config(background="SystemButtonFace",foreground="Black")
    cpb1.config(bg="#D9D9D9",fg="Black")
    cpb2.config(bg="#D9D9D9",fg="Black")
    lb1.config(bg="#D9D9D9",fg="Black")
    for i in range(0, len(categories)):
        sbbtn[i].config(bg="#D9D9D9",fg="Black")

# fetching categories
categories = db.fetch_all_notes("categories")
categories.insert(0,"All")
categories.insert(len(categories),"Add Category")
# fetching all notes from the Data base
notes = []
notes = db.fetch_all_notes("notes")
# fetching key 
key = db.read_pass(2)
key1 = key[0][1].encode()

def pw_check():
    pas = f1e1.get()
    check = db.read_pass(1)
    if pas == check[0][1]:
        frame1.pack_forget()
        frame2.place(relheight=1, relwidth=1)
        f1e1.delete(0, tk.END)
#  setting functions
def setting():
    lframe.place_forget()
    sframe.place(relheight=1 , relwidth=1)
    sb1.place(relx=0.3,rely=0.3)
    sb2.place(relx=0.3,rely=0.5)
    hframe.place_forget()

def goto_cpframe():
    main_area.place_forget()
    cpframe.place(relheight=1, relwidth=1)

def change_pass():
    new_pass = cpe1.get()
    db.change_pass(new_pass)
    cpframe.place_forget()
    frame2.place(relheight=1, relwidth=1)

def change_theme():
    global theme
    if(theme == True):
        theme2()
        theme = False
    else:
        theme1()
        theme = True

def goto_sframe():
    cpframe.place_forget()
    sframe.place(relheight=1, relwidth=1)

# logout functions
def logout():
    main_area.place_forget()
    lframe.place(relheight=1,relwidth=1)
    lb1.place(relx=0.3,rely=0.4)

def goto_frame1():
    main_area.place_forget()
    frame2.place_forget()
    frame1.place(relheight=1,relwidth=1)

# home button functions

def home():
    sidebar.place_forget()
    hframe.place(relheight=1,relwidth=1)
    main_area.place_forget()
    h1frame.place(relwidth=1,relheight=1)
    filter_notes("All")
    sframe.place_forget()
    lframe.place_forget()
    nframe.place_forget()
    h2frame.place_forget()
    h3frame.place_forget()

def filter_notes(cat):
    tree.delete(*tree.get_children())  # Clear current rows
    for note in notes:
        if cat == "All" or note["category"] == cat:
            tree.insert("", "end", values=(note["title"], note["category"]))
            h1frame.place(relheight=1,relwidth=1)
            h3frame.place_forget()
        if cat == "Add Category":
            h3frame.place(relheight=1,relwidth=1)
    h2frame.place_forget()

def on_select(event):
    selected = tree.focus()  # Get selected item ID
    if selected:
        values = tree.item(selected, "values")
        note = db.read_data(values[1],values[0])
        note1 = en.decrypt_text(note[0][1], key1)
        h2t1.delete("1.0","end")
        h2t1.insert("1.0", note1)
        # h2t1.config(state="disabled")
        h1frame.place_forget()
        h2frame.place(relheight=1,relwidth=1)  

def delete_note():
    global notes
    selected = tree.focus()  # Get selected item ID
    if selected:
        values = tree.item(selected, "values")
        db.delete_data(values[1], values[0])
        notes = [note for note in notes if note["title"] != values[0]]
        h2frame.place_forget()
        h1frame.place(relheight=1,relwidth=1)

def edit_note():
    selected = tree.focus()  # Get selected item ID
    if selected:
        values = tree.item(selected, "values")
        text = h2t1.get("1.0", "end")
        text = en.encrypt_text(text,key1)
        db.update_data(values[1], values[0], text)

def add_cat():
    cat = h3e1.get()
    categories.insert(-1, cat)
    db.create_table(cat)
    h3frame.place_forget()
    h3e1.delete(0, tk.END)
# Add notes button functions
def addnotes():
    hframe.place_forget()
    h1frame.place_forget()
    lframe.place_forget()
    sframe.place_forget()
    nframe.place(relheight=1,relwidth=1)
    
def save_note():
    cat = dropdown_var.get()
    title = ne1.get()
    note = ne2.get("1.0", "end-1c")
    db.create_table(cat)
    note = en.encrypt_text(note,key1)
    db.insert_data(cat, title,note)
    notes.append({
        "title": title,
        "category" : cat
    })
    ne1.delete(0, tk.END)
    ne2.delete("1.0","end")
    dropdown_var.set(value="Select a Category")

# mian code
root = tk.Tk()
root.title("Secure Notes Manager")
root.geometry("400x300")

# frame 1 
frame1 = tk.Frame(root)
frame1.place(relwidth=1, relheight=1)

f1l1= ttk.Label(frame1, text="Input Password to Enter", font=("Arial", 14)).place(relx=0.5, rely=0.4, anchor="center")
f1e1 = ttk.Entry(frame1, show="*")
f1e1.place(relx=0.5, rely=0.5, anchor="center")
f1b1 = ttk.Button(frame1, text="Enter", command=pw_check)
f1b1.place(relx=0.5, rely=0.6, anchor="center")

# frame 2
frame2 = tk.Frame(root, bg="#1e1e1e")

#  top bar menu
top_bar = tk.Frame(frame2, bg="#1e1e1e", height=50)
top_bar.pack(fill="x", side="top")
#  => top bar buttons
tbbutn = []
buttons = ["Home", "Add Note", "Settings", "Logout"]
for b in buttons:
    btn = tk.Button(top_bar, text=b, bg="#2e2e2e", fg="white",cursor="hand2", bd=0, padx=10)
    btn.pack(side="left", padx=10)
    tbbutn.append(btn)

# sidebar menu
sidebar = tk.Frame(frame2, width=100, bg="#2e2e2e")
sidebar.pack(fill="y", side="left", pady=5)

# main area for data display
main_area = tk.Frame(frame2, bg="#2e2e2e")
main_area.pack(fill="both", expand=True, padx=5, pady=5)

# Home button code
tbbutn[0].config(command=home)
hframe = tk.Frame(sidebar,bg="#2e2e2e")
h1frame = tk.Frame(main_area,bg="#2e2e2e")
h2frame = tk.Frame(main_area, bg="#2e2e2e")
h3frame = tk.Frame(main_area, bg="#2e2e2e")
# => Treeview code
tree = ttk.Treeview(h1frame, columns=("Title", "Category"), show="headings")
tree.heading("Title", text="Title")
tree.heading("Category", text="Category")
tree.pack(fill="both", expand=True)
tree.column("Title", width=150, anchor="w")
tree.column("Category", width=100, anchor="w")

for n in notes:
    tree.insert("", tk.END, values=n)
tree.bind("<<TreeviewSelect>>", on_select)
# => inside the note
h2t1 = tk.Text(h2frame, height= 13, width=40,bg="#3a3a3a",fg="White", font=("Times New Roman", 10))
h2t1.place(relx=0.0,rely=0.0)

h2b1 = tk.Button(h2frame, text="Save Updates",width=10, height=1, bg="#3a3a3a", fg="white",cursor="hand2", command=edit_note)
h2b1.place(relx=0.3, rely=0.8)
h2b2 = tk.Button(h2frame, text="Delete Note",width=10, height=1, bg="#3a3a3a", fg="white",cursor="hand2",command=delete_note)
h2b2.place(relx=0.3, rely=0.9)
# => sidebar menu code
hl1=tk.Label(hframe, text="Categories",bg="#3a3a3a", fg="white" ,font=("Arial", 12, "bold"))
hl1.pack(pady=10)
sbbtn = []
for cat in categories:
    btn = tk.Button(hframe, text=cat, bg="#3a3a3a", fg="white", bd=0,cursor="hand2",command=lambda c=cat: filter_notes(c))
    btn.pack(fill="x", padx=10, pady=5)
    sbbtn.append(btn)
# => add category code
h3l1 = ttk.Label(h3frame, text="Enter the New Category",background="#2e2e2e",foreground="White", font=("Times New Roman", 12))
h3l1.place(relx=0.2, rely=0.3)
h3e1 = tk.Entry(h3frame, background="#2e2e2e", foreground="White")
h3e1.place(relx=0.25,rely=0.44)
h3b1 = tk.Button(h3frame, text="Save Category",relief="sunken", bg="#3a3a3a", fg="white",cursor="hand2",command=add_cat)
h3b1.place(relx=0.3, rely=0.6)
# Add notes button code
tbbutn[1].config(command=addnotes)
nframe = tk.Frame(main_area, bg="#2e2e2e")
# => option menu for category choice
dropdown_var = tk.StringVar(value="Select a Category")
options = categories[1:-1]
dropdown = tk.OptionMenu(nframe, dropdown_var, *options)
dropdown.config(bg="#3a3a3a", fg="white" , 
    activebackground="#2e2e2e",  
    activeforeground="White",           
    bd=2,                      
    highlightthickness=0,
    cursor="hand2")
dropdown.place(relx=0.3, rely=0.1)
#  => labels and entry to get data
nl1 = ttk.Label(nframe,text="Enter the title: ",background="#2e2e2e",foreground="White", font=("Times New Roman", 12))
nl1.place(relx=0.0,rely=0.3)
ne1 = tk.Entry(nframe,font=("Times New Roman", 12),background="#2e2e2e",foreground="White", width=15)
ne1.place(relx=0.4,rely=0.3)
nl2 = ttk.Label(nframe,text="Enter the notes: ",background="#2e2e2e",foreground="White", font=("Times New Roman", 12))
nl2.place(relx=0.0,rely=0.4)
ne2 = tk.Text(nframe, height=5, width=15,background="#2e2e2e",foreground="White", font=("Times New Roman", 12))
ne2.place(relx=0.4,rely=0.4)
#  => button to submit
nb1 = tk.Button(nframe, text="Save",relief="sunken",width=10, height=1, bg="#3a3a3a", fg="white",cursor="hand2", command=save_note)
nb1.place(relx=0.3, rely=0.85)

# Setting button code
sframe = tk.Frame(main_area, bg="#2e2e2e")
tbbutn[2].config(command=setting)
# => setting->theme
sb1 = tk.Button(sframe, text="Change Theme",relief="sunken", width=13, height=2, bg="#3a3a3a", fg="white",cursor="hand2",command=change_theme)
# => setting ->password
sb2 = tk.Button(sframe, text="Change Password",width=13, height=2, bg="#3a3a3a", fg="white",cursor="hand2",command=goto_cpframe)
cpframe = tk.Frame(sframe, bg="#2e2e2e")
cpl1 = ttk.Label(cpframe, text="Enter the new password: ",background="#2e2e2e",foreground="White", font=("Times New Roman", 12))
cpl1.place(relx=0.18, rely=0.3)
cpe1 = tk.Entry(cpframe, background="#2e2e2e", foreground="White")
cpe1.place(relx=0.23,rely=0.45)
cpb1 = tk.Button(cpframe, text="Change",width=10, height=1, bg="#3a3a3a", fg="white",cursor="hand2",command=change_pass)
cpb1.place(relx=0.3, rely=0.6)
cpb2 = tk.Button(cpframe, text="Back",width=10, height=1, bg="#3a3a3a", fg="white",cursor="hand2",command=goto_sframe)
cpb2.place(relx=0.3, rely=0.75)

# logout button code
tbbutn[3].config(command= logout)
lframe = tk.Frame(main_area, bg="#2e2e2e")
lb1 = tk.Button(lframe, text="Logout",relief="sunken", width=13, height=2, bg="#3a3a3a", fg="white",cursor="hand2", command=goto_frame1)

# theme1()
root.mainloop()