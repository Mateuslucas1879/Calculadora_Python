import tkinter as tk
from tkinter import messagebox

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry("400x550")
        self.configure(bg="black")

        self.result_var = tk.StringVar()
        self.result_var.set("")

        self.create_widgets()

    def create_widgets(self):
        entry_frame = tk.Frame(self, bg="black")
        entry_frame.pack(padx=10)

        entry = tk.Entry(entry_frame, textvariable=self.result_var, font=("Helvetica", 24), bd=10, relief=tk.SOLID, justify="right", insertbackground="white")
        entry.grid(row=0, column=0, columnspan=4, ipady=8)

        buttons_frame = tk.Frame(self, bg="black")
        buttons_frame.pack()

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (text, row, col) in buttons:
            button = tk.Button(buttons_frame, text=text, font=("Helvetica", 18), width=5, height=2, bg="gray", fg="black", command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, button_text):
        current_text = self.result_var.get()

        if button_text == 'C':
            self.result_var.set('')
        elif button_text == '=':
            try:
                result = self.evaluate_expression(current_text)
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Erro", f"Erro na expressão: {e}")
                self.result_var.set('')
        else:
            self.result_var.set(current_text + button_text)

    def evaluate_expression(self, expression):
        try:
            result = eval(expression)
            return round(result, 4)  # Arredonde para 4 casas decimais
        except Exception as e:
            raise ValueError(f"Erro na expressão: {e}")

if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()
