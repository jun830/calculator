import tkinter as tk

root = tk.Tk()
root.title("計算機")
# root.geometry("400x400")


stack = tk.StringVar()
stack.set("")

ent = tk.Entry(root, textvariable=stack)
ent.grid(row=0, columnspan=4)

# [row, column, number , command]
Definition_Button = [[1, 0, "7"], [1, 1, "8"], [1, 2, "9"], [1, 3, "÷"],
                     [2, 0, "4"], [2, 1, "5"], [2, 2, "6"], [2, 3, "×"],
                     [3, 0, "1"], [3, 1, "2"], [3, 2, "3"], [3, 3, "-"],
                     [4, 0, "0"], [4, 1, "C"], [4, 2, "="], [4, 3, "+"]]

for r, c, label in Definition_Button:
    button = tk.Button(text=label, font=("Times", 20), height=1, width=2)
    button.grid(row=r, column=c)

root.mainloop()
