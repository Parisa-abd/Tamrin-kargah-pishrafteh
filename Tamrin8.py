import tkinter as tk
from tkinter import messagebox

def calc():
    try:
        total = float(e_total.get())
        people = int(e_people.get())
        share = total / people
        messagebox.showinfo("Result", f"Each: {share:.2f} Toman")
    except:
        messagebox.showwarning("Error", "Enter valid numbers!")

root = tk.Tk()
root.title("Dong Calculator")

tk.Label(root, text="Total Bill").grid(row=0, column=0)
e_total = tk.Entry(root); e_total.grid(row=0, column=1)

tk.Label(root, text="People").grid(row=1, column=0)
e_people = tk.Entry(root); e_people.grid(row=1, column=1)

tk.Button(root, text="Calculate", command=calc).grid(row=2, columnspan=2)

root.mainloop()
