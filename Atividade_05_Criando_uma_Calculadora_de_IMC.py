import tkinter as tk
from tkinter import messagebox

class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de IMC")
        
        self.create_widgets()
        
    def create_widgets(self):
        self.height_label = tk.Label(self.root, text="Altura (m):")
        self.height_label.grid(row=0, column=0, padx=10, pady=5)
        
        self.weight_label = tk.Label(self.root, text="Peso (kg):")
        self.weight_label.grid(row=1, column=0, padx=10, pady=5)
        
        self.height_entry = tk.Entry(self.root)
        self.height_entry.grid(row=0, column=1, padx=10, pady=5)
        
        self.weight_entry = tk.Entry(self.root)
        self.weight_entry.grid(row=1, column=1, padx=10, pady=5)
        
        self.calculate_button = tk.Button(self.root, text="Calcular IMC", command=self.calculate_bmi)
        self.calculate_button.grid(row=2, columnspan=2, pady=10)
        
        self.result_label = tk.Label(self.root, text="Resultado do IMC:")
        self.result_label.grid(row=3, columnspan=2, pady=5)
    
    def calculate_bmi(self):
        try:
            height = float(self.height_entry.get())
            weight = float(self.weight_entry.get())
            
            if height <= 0 or weight <= 0:
                raise ValueError("Valores devem ser positivos e diferentes de zero.")
                
            bmi = weight / (height ** 2)
            self.show_bmi_category(bmi)
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
    
    def show_bmi_category(self, bmi):
        if bmi < 18.5:
            category = "Abaixo do peso"
        elif 18.5 <= bmi < 24.9:
            category = "Peso normal"
        elif 25 <= bmi < 29.9:
            category = "Sobrepeso"
        else:
            category = "Obesidade"
        
        self.result_label.config(text=f"Resultado do IMC: {bmi:.2f} ({category})")

if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()
