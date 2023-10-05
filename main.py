"""version
Python 3.9.4
tkinter 8.6
"""
"""設計

表示部分
    num_box 数字を出す
内部数字回り
    front_num   表出用数字
    back_num    計算用内部数字
    back_ope    計算用内部演算子
    memory_num  メモリー用保存数字
    last_is_ope 最後に入力されたのが演算子だったかどうか
ボタン
    数字
        0~9 .(小数点)
        直前が演算子のとき back_num = front_num, front_num = 0
        else:front_num に入力を追加
    演算子
        +, -, *, /, //, =
        直前の入力が演算子のとき    back_ope を書き換え
        else:
            back_numがあるとき   front_num = back_num back_ope front_num
                            　　back_num = back_ope = None
                    無いとき     back_ope = 入力
    メモリー機能
        M+ memory_num + front_num
        M- memory_num - front_num
        MR memory_numを出力
        MC memory_numを0にする
    その他
        AC  front_numとback_numの両方を0
        C   front_numのみを0
        DEL front_numの末尾1桁を消す
"""
import tkinter as tk

def main():
    root = tk.Tk()
    root.title("電卓")
    Calculator(root)
    root.mainloop()

class Calculator:
    def __init__(self, root):
        self.frame = tk.Frame(root)
        self.frame.grid(row=0, column=0, padx=15, pady=15)

        self.display_num = tk.StringVar()
        self.display_num.set(0)
        self.num_box = tk.Entry(self.frame,
                                readonlybackground="white",
                                font=("MSゴシック", 32),
                                textvariable=self.display_num,
                                justify=tk.RIGHT)
        self.num_box.config(state="readonly")
        self.num_box.grid(row=0, column=0, columnspan=4)

        self.memory_num = 0
        self.front_num = "0"
        self.back_num = None
        self.back_ope = None
        self.is_decimal = False
        self.last_is_ope = False

        Definition_Button = [["M+","M-","MR","MC"],
                             ["AC", "C","//", "/"],
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
            self.memory_num = eval(str(self.memory_num)+ "+" + self.num_box.get())
            self.front_num = "0"

        elif x == "M-":
            self.memory_num = eval(str(self.memory_num) + "-" + self.num_box.get())
            self.front_num = "0"

        elif x == "MR":
            self.front_num = str(self.memory_num)
            self.display_num.set(self.front_num)

        elif x == "MC":
            self.memory_num = 0

        elif x == "AC":
            self.front_num = "0"
            self.back_num = None
            self.back_ope = None
            self.is_decimal = False
            self.last_is_ope = False
            self.display_num.set("0")

        elif x == "C":
            self.front_num = "0"
            self.is_decimal = False
            self.display_num.set("0")

        elif x == "DEL":
            if len(self.front_num) == 1:
                self.front_num = "0"
            else:
                if self.front_num[-1] == ".":
                    self.is_decimal = False
                self.front_num = self.front_num[:-1]
            self.display_num.set(self.front_num)

        elif x in {"+", "-", "*", "/", "//", "="}:
            if self.last_is_ope:
                self.back_ope = x
            elif self.back_num is None:
                self.last_is_ope = True
                self.back_num, self.front_num = self.front_num, "0"
                self.back_ope = x
                self.is_decimal = False
                self.display_num.set(self.back_num)
            else:
                try:
                    self.back_num = str(eval(self.back_num + self.back_ope + self.front_num))
                    self.last_is_ope = True
                    self.front_num = "0"
                    self.back_ope = x
                    self.is_decimal = False
                    self.display_num.set(self.back_num)
                except ZeroDivisionError:
                    self.display_num.set("0で割ってはいけません")
                    self.memory_num = 0
                    self.front_num = "0"
                    self.back_num = None
                    self.back_ope = None
                    self.is_decimal = False
                    self.last_is_ope = False

        elif x == ".":
            if self.is_decimal:
                pass
            else:
                self.is_decimal = True
                if self.front_num is None:
                    self.front_num = "0."
                else:
                    self.front_num += "."
                self.display_num.set(self.front_num)

        elif x in "0123456789":
            if self.last_is_ope:
                self.last_is_ope = False
                if self.back_ope == "=":
                    self.back_num, self.back_ope = None, None

            if self.front_num is None or self.front_num == "0":
                self.front_num = x
            else:
                self.front_num += x
            self.display_num.set(self.front_num)

        else:
            pass

        # print(x, self.front_num, self.back_num, self.back_ope, self.is_decimal,self.last_is_ope, self.memory_num)

if __name__=="__main__":
    main()
