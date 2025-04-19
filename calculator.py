import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("图形计算器")
        
        # 输入框
        self.entry = tk.Entry(root, width=20, font=('Arial', 16), borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # 按钮
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', 'C', '=', '+'
        ]
        
        row = 1
        col = 0
        for button in buttons:
            tk.Button(root, text=button, width=5, height=2, 
                     command=lambda b=button: self.on_button_click(b),
                     font=('Arial', 14)).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1
    
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