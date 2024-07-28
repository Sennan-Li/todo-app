import tkinter as tk

root = tk.Tk()

root.geometry('500x500')
root.title('My To-do App')

label = tk.Label(root, text='test')
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=2)
textbox.pack(padx=20)

button = tk.Button(root, text='click me')
button.pack(padx=20, pady=20)




root.mainloop()
