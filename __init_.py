import tkinter as tk
from tkinter import messagebox

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title=("Calculadora")
        self.geometry=("350x400")
        self.result_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        entry = tk.Entry(self, textvariable=self.result_var, font=('Helvetica', 14), bd=10, insertwidth=4, width=14,
                         justify='right')
        entry.grid(row=0, column=0, columnspan=4)


        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]
        
        for(text,row,column) in buttons:
            button = tk.Button(self, text=text, font=('Helvetica', 14), height=2, width=5, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=column, sticky="nsew")
        
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
            self.columnconfigure(i,weight=1)
        
    
    def on_button_click(self,value):
        try:
            if value == "C":
                self.clear_entry()
            if value == "=":
                self.calculate_result()
            else:
                self.update_entry(value)
        except Exception as e:
                messagebox.showerror("Erro", "Erro na expressão")


    def clear_entry(self):
        self.result_var.set('')

    def calculate_result(self):
        try:
            result = eval(self.result_var.get())
            self.result_var.set(result)
        except Exception as e:
            messagebox.showerror("Erro", "Erro na expressão")

    def update_entry(self, value):
        current_value = self.result_var.get()
        current_value += value
        self.result_var.set(current_value)

if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()





