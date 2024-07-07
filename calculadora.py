import tkinter as tk

#Funciones

#Funcion suma toma dos numeros y retorna la suma entre ambos
def suma(a,b):
  return a + b

#Funcion resta toma dos numeros y retorna la resta entre ambos
def resta(a,b):
  return a - b

#Funcion toma dos numeros y retorna la multiplicacion entre ambos
def multiplicacion(a,b):
  return a * b

#Funcion toma dos numeros y retorna la division entre ambos, con excepcion en caso que el segundo numero sea cero
def division(a,b):
  if b == 0:
    return "Error: No se puede dividir por cero"
  
  else:
    return a / b
  

#Instancia grafica
root = tk.Tk()

root.title("Calculadora Básica")

#Diseño grafico

#Funcion al tocar los botones
def button_click(value):
  current = entry.get()
  entry.delete(0, tk.END)
  entry.insert(tk.END, current + str(value))

#Funcion para limpiar el cuadro de texto
def clear_entry():
  entry.delete(0, tk.END)

def evaluate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

input_text = tk.StringVar()

entry = tk.Entry(root, textvariable=input_text, font=("Helvetica", 16))

#Dimensiones de la calculadora
entry.grid(row=0, column=0, columnspan=4)

buttons = [

  "7", "8", "9", "/",
  "4", "5", "6", "*",
  "1", "2", "3", "-",
  "0", ".", "=", "+"
]

row_val = 1
col = 0
#Botones para numeros y operaciones
for button in buttons:
  tk.Button(root, text=button, font=("Helvetica", 12),
            command=lambda item=button: button_click(item) if item != "=" else evaluate()
            ).grid(row=row_val, column=col, padx=5, pady=5)
  
  col += 1
  if col > 3:
    col = 0
    row_val += 1
#Boton para limpiar el cuadro de texto
tk.Button(root, text="C", padx=5, pady=5, font=("Helvetica", 12),
          command=clear_entry).grid(row=row_val, column=col, padx=5, pady=5)

root.mainloop()