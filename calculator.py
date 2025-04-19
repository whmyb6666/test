import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("图形计算器")
        
        # 输入框
        self.entry = tk.Entry(root, width=20, font=('Arial', 16), borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # 数字按钮
        buttons = [
            '7', '8', '9',
            '4', '5', '6',
            '1', '2', '3',
            '0', '.', 'C'
        ]
        
        # 运算符按钮
        operators = ['+', '-', '*', '/', '%']
        
        # 数字按钮布局
        row = 1
        col = 0
        for button in buttons:
            tk.Button(root, text=button, width=5, height=2,
                     command=lambda b=button: self.on_button_click(b),
                     font=('Arial', 14)).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 2:
                col = 0
                row += 1
        
        # 运算符按钮布局(右侧)
        col_op = 3
        row_op = 1
        for op in operators:
            tk.Button(root, text=op, width=5, height=2,
                     command=lambda o=op: self.on_button_click(o),
                     font=('Arial', 14)).grid(row=row_op, column=col_op, padx=5, pady=5)
            row_op += 1
        
        # 等号按钮(单独放在底部)
        tk.Button(root, text='=', width=5, height=2,
                 command=lambda: self.on_button_click('='),
                 font=('Arial', 14)).grid(row=5, column=0, columnspan=3, padx=5, pady=5, sticky='we')
    
    def on_button_click(self, button):
        current = self.entry.get()
        if button == 'C':
            self.entry.delete(0, tk.END)
        elif button == '=':
            try:
                result = eval(current)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except:
                messagebox.showerror("错误", "无效的表达式")
        elif button == '.':
            if '.' not in current:
                self.entry.insert(tk.END, '.')
        else:
            self.entry.insert(tk.END, button)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()