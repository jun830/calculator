import tkinter as tk

def main():
    root = tk.Tk()
    root.title("電卓")
    calc = Calculator(root)
    root.mainloop()

class Calculator:
    def __init__(self, root):
        self.frame = tk.Frame(root)
        self.frame.grid(row=0, column=0, padx=15, pady=15)

        self.calc_str = ""
        self.stack = tk.StringVar()
        self.stack.set("0")
        self.num_box = tk.Entry(self.frame, font=("MSゴシック", 32),
                                textvariable=self.stack, justify=tk.RIGHT)
        self.num_box.grid(row=0, column=0, columnspan=4)

        self.memory = tk.StringVar()
        self.memory.set("0")
        # [row, column, number, command]
        Definition_Button = [["M+","M-","MR","MC"],
                             ["AC", "C",  "", "/"],
                             [ "7", "8", "9", "*"],
                             [ "4", "5", "6", "-"],
                             [ "1", "2", "3", "+"],
                             [ "0", ".","DEL","="]]

        for r, d_i in enumerate(Definition_Button, 1):
            for c, label in enumerate(d_i):
                button = tk.Button(self.frame, text=label, font=("ＭＳゴシック", 28))
                button.grid(row=r, column=c, sticky="news")
                button.bind("<ButtonPress>", self.push_command)

    def push_command(self, e):
        x = e.widget.cget("text")
        if x == "M+":
            pass
        elif x == "M-":
            pass
        elif x == "MR":
            pass
        elif x == "MC":
            self.memory.set("0")
        elif x == "AC":
            self.stack.set("0")
            self.memory.set("0")
        elif x == "C":
            self.stack.set("0")
        elif x == "":pass
        else:
            if x == "=":
                try:
                    self.calc_str = str(eval(self.calc_str))
                except:
                    pass
            elif x in "+-x/.":
                self.calc_str += x
            else:
                if self.calc_str == "0":
                    self.calc_str = x
                else:
                    self.calc_str += x
            self.stack.set(self.calc_str)


if __name__=="__main__":
    main()
