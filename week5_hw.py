from tkinter import *
from tkinter import ttk
from tkinter import messagebox
def add_user():
    user_id = entry_user_id.get()
    user_name = entry_user_name.get()
    email = entry_email.get()
    birth_year = entry_birth_year.get()
    if user_id and user_name and email and birth_year:
        tree.insert("", "end", values=(user_id, user_name, email, birth_year))
        entry_user_id.delete(0, END)
        entry_user_name.delete(0, END)
        entry_email.delete(0, END)
        entry_birth_year.delete(0, END)
        messagebox.showinfo("성공", "데이터 입력 성공")
    else:
        messagebox.showerror("오류", "데이터 입력 오류가 발생함")
def search_user():
    search_text = entry_user_id.get()
    if not search_text:
        messagebox.showerror("오류", "데이터 입력 오류가 발생함")
        return
    found_items = []
    for item in tree.get_children():
        values = tree.item(item, 'values')
        if search_text.lower() == str(values[0]).lower():
            found_items.append(item)
    if found_items:
        tree.selection_set(found_items)
    else:
        messagebox.showinfo("오류", "데이터 입력 오류가 발생함")
def on_tree_select(event):
    selected_item = tree.selection()
    if selected_item:
        values = tree.item(selected_item, 'values')
        entry_user_id.delete(0, END)
        entry_user_name.delete(0, END)
        entry_email.delete(0, END)
        entry_birth_year.delete(0, END)
        entry_user_id.insert(0, values[0])
        entry_user_name.insert(0, values[1])
        entry_email.insert(0, values[2])
        entry_birth_year.insert(0, values[3])
window = Tk()
window.title("GUI 데이터 입력")
label_user_id = Label(window, text="")
entry_user_id = Entry(window)
label_user_name = Label(window, text="")
entry_user_name = Entry(window)
label_email = Label(window, text="")
entry_email = Entry(window)
label_birth_year = Label(window, text="")
entry_birth_year = Entry(window)
btn_add = Button(window, text="입력", command=add_user)
btn_search = Button(window, text="조회", command=search_user)
tree = ttk.Treeview(window, columns=("UserID", "UserName", "Email", "BirthYear"))
tree.heading("#0", text="ID")
tree.heading("#1", text="사용자ID")
tree.heading("#2", text="사용자이름")
tree.heading("#3", text="이메일")
tree.heading("#4", text="출생년도")
tree.bind("<ButtonRelease-1>", on_tree_select)
label_user_id.grid(row=0, column=0, padx=10, pady=4, sticky="w")
entry_user_id.grid(row=0, column=0, padx=10, pady=4)
label_user_name.grid(row=0, column=1, padx=10, pady=4, sticky="w")
entry_user_name.grid(row=0, column=1, padx=10, pady=4)
label_email.grid(row=0, column=2, padx=10, pady=4, sticky="w")
entry_email.grid(row=0, column=2, padx=10, pady=4)
label_birth_year.grid(row=0, column=3, padx=10, pady=4, sticky="w")
entry_birth_year.grid(row=0, column=3, padx=10, pady=4)
btn_add.grid(row=0, column=4, columnspan=3, pady=10, sticky="w")
btn_search.grid(row=0, column=5, columnspan=3, pady=10, sticky="w")
tree.grid(row=2, column=0, columnspan=8, padx=10, pady=10)
window.mainloop()