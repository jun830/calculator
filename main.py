"""
設計

表示部分
    数字を出す
数字回り
    front_num   表出用数字
    back_num    計算用内部数字
    back_ope    計算用内部演算子
    memory_num  メモリー用保存数字
ボタン
    数字
        0~9
        .(小数点)
    演算子
        +, -, *, /, //, =
        これの入力が来た時にback_numとback_opeがある
            計算してback_numにいれる。=ならばfront_numにする
        無いときはback_opeに演算子を入れる.次の数字が1つ入ったらback_numにfront_numの数字を移す
    メモリー機能
        M+ memory_num + front_num
        M- memory_num - front_num
        MR memory_numを出力
        MC memory_numを0にする
    その他
        AC  front_numとmemory_numの両方を0
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

        self.display_num = tk.IntVar()
        self.display_num.set(0)
        self.num_box = tk.Entry(self.frame,
                                font=("MSゴシック", 32),
                                textvariable=self.display_num,
                                justify=tk.RIGHT)
        self.num_box.grid(row=0, column=0, columnspan=4)

        self.memory = 0
        self.back_num = 0
        self.back_ope = None
        self.is_decimal = False

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
            pass
        elif x == "M-":
            pass
        elif x == "MR":
            pass
        elif x == "MC":
            self.memory = 0
        elif x == "AC":
            self.display_num = 0
            self.memory = 0
        elif x == "C":
            self.display_num = 0
        elif x == "":pass
        elif x in {"+", "-", "*", "/", "//", "="}:
            pass
        elif x == ".":
            pass
        else:
            pass



if __name__=="__main__":
    main()
