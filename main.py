import tkinter as tk
from tkinter import messagebox

# FUNÇÃO DOS NÚMEROS
def adicionar(x, y):
    return x + y

# Esta função subtrai dois números
def subtrair(x, y):
    return x - y

# Esta função multiplica dois números
def multiplicar(x, y):
    return x * y

# Esta função divide dois números
def dividir(x, y):
    return x / y

# CRIANDO A PARTE DE INTERFACE DA CALCULADORA COM TKINTER
def main():
    root = tk.Tk()
    root.title("Calculadora")
    root.geometry("400x550")
    root.configure(bg="black")

    num1_var = tk.StringVar()
    num2_var = tk.StringVar()
    result_var = tk.StringVar()
    operator_var = tk.StringVar()

    def calcular(operacao):
        resultado = None
         
        try:
            num1 = float(num1_var.get())
            num2 = float(num2_var.get())

            if operacao == "Soma":
                resultado = adicionar(num1, num2)
            elif operacao == "Subtrair":
                resultado = subtrair(num1, num2)
            elif operacao == "Dividir":
                resultado = dividir(num1, num2)
            elif operacao == "Multiplicar":
                resultado = multiplicar(num1, num2)

        except ValueError:
            messagebox.showerror("Erro", "Digite números válidos.")
        
        if resultado is not None:
            result_var.set(f"Resultado: {resultado}")

    def calcular_e_exibir():
        operacao = operator_var.get()
        calcular(operacao)

    def limpar_entradas():
        num1_var.set("")
        num2_var.set("")
        result_var.set("")      

    # INTERFACE GRÁFICA 
    tk.Label(root, text="CALCULADORA", font=("Helvetica", 16), bg="black", fg="white").pack()

    tk.Label(root, text="Número 1:", font=("Helvetica", 12), bg="black", fg="white").pack()
    entry_num1 = tk.Entry(root, textvariable=num1_var, font=("Helvetica", 12))
    entry_num1.pack()

    tk.Label(root, text="Número 2:", font=("Helvetica", 12), bg="black", fg="white").pack()
    entry_num2 = tk.Entry(root, textvariable=num2_var, font=("Helvetica", 12))
    entry_num2.pack()

    tk.Label(root, text="", bg="black").pack()

    tk.Button(root, text="+", command=lambda: calcular("Soma"), bg="black", fg="white").pack(side=tk.LEFT, padx=5) 
    tk.Button(root, text="-", command=lambda: calcular("Subtrair"), bg="black", fg="white").pack(side=tk.LEFT, padx=5) 
    tk.Button(root, text="/", command=lambda: calcular("Dividir"), bg="black", fg="white").pack(side=tk.LEFT, padx=5) 
    tk.Button(root, text="x", command=lambda: calcular("Multiplicar"), bg="black", fg="white").pack(side=tk.LEFT, padx=5) 

    tk.Label(root, text="", bg="black").pack()
    
    # BOTÃO DE CALCULAR E LIMPAR 
    tk.Button(root, text="Calcular", command=calcular_e_exibir, font=("Helvetica", 12)).pack(side=tk.LEFT, padx=5)
    tk.Button(root, text="Limpar", command=limpar_entradas, font=("Helvetica", 12)).pack(side=tk.LEFT, padx=5)

    tk.Label(root, text="", bg="black").pack()
    
    # BOTÃO DE RESULTADO
    tk.Label(root, textvariable=result_var, font=("Helvetica", 14), bg="black", fg="white").pack()
    tk.Label(root, text="", bg="black").pack()  # Espaço

    # BOTÃO DE SAIR
    tk.Button(root, text="Sair", command=root.destroy, font=("Helvetica", 12)).pack(side=tk.LEFT, padx=5)
    tk.Label(root, text="", bg="black").pack()

    root.mainloop()

if __name__ == "__main__":
    main()