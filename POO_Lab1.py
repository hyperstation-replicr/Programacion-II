import tkinter as tk

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.__edad = edad
    
    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Edad: {self.__edad}"
        
    def presentarse(self):
        return f"Hola, soy {self.nombre}."

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera
    
    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Edad: {self._Persona__edad}, Carrera: {self.carrera}"
        
    def presentarse(self):
        return f"Hola, soy {self.nombre} y estudio {self.carrera}."

class Profesor(Persona):
    def __init__(self, nombre, edad, materia, titulo):
        super().__init__(nombre, edad)
        self.materia = materia
        self.titulo = titulo
    
    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Edad: {self._Persona__edad}, Materia: {self.materia}, Título: {self.titulo}"
    
    def presentarse(self):
        return f"Hola, soy {self.nombre}, profesor de {self.materia}, con título de {self.titulo}."

lista_objetos = []

def actualizar_campos(*args):
    tipo = tipo_var.get()
    if tipo == "Persona":
        label_carrera.config(text="Carrera / Materia:")
        entry_carrera.pack_forget()
        label_carrera.pack_forget()
        label_carrera.pack_forget()
        entry_carrera.pack_forget()
        entry_carrera.delete(0, tk.END)
        entry_carrera.pack_forget()

        entry_carrera.pack_forget()
        label_carrera.pack_forget()
        label_titulo.pack_forget()
        entry_titulo.pack_forget()

    elif tipo == "Estudiante":
        label_carrera.config(text="Carrera:")
        label_carrera.pack()
        entry_carrera.pack()
        label_titulo.pack_forget()
        entry_titulo.pack_forget()
    elif tipo == "Profesor":
        label_carrera.config(text="Materia:")
        label_carrera.pack()
        entry_carrera.pack()
        label_titulo.pack()
        entry_titulo.pack()
    else:
        label_carrera.pack_forget()
        entry_carrera.pack_forget()
        label_titulo.pack_forget()
        entry_titulo.pack_forget()

def crear_objeto():
    nombre = entry_nombre.get().strip()
    edad = entry_edad.get().strip()
    if not nombre or not edad:
        label_resultado.config(text="Error: Debes ingresar Nombre y Edad.", fg="red")
        return
    
    tipo = tipo_var.get()
    try:
        edad_int = int(edad)
    except ValueError:
        label_resultado.config(text="Error: Edad debe ser un número entero.", fg="red")
        return
    
    if tipo == "Persona":
        obj = Persona(nombre, edad_int)
        lista_objetos.append(obj)
        label_resultado.config(text=obj.mostrar_info() + "\n" + obj.presentarse(), fg="blue")
    elif tipo == "Estudiante":
        carrera = entry_carrera.get().strip()
        if not carrera:
            label_resultado.config(text="Error: Debes ingresar la carrera.", fg="red")
            return
        obj = Estudiante(nombre, edad_int, carrera)
        lista_objetos.append(obj)
        label_resultado.config(text=obj.mostrar_info() + "\n" + obj.presentarse(), fg="green")
    elif tipo == "Profesor":
        materia = entry_carrera.get().strip()
        titulo = entry_titulo.get().strip()
        if not materia or not titulo:
            label_resultado.config(text="Error: Debes ingresar materia y título.", fg="red")
            return
        obj = Profesor(nombre, edad_int, materia, titulo)
        lista_objetos.append(obj)
        label_resultado.config(text=obj.mostrar_info() + "\n" + obj.presentarse(), fg="purple")
    else:
        label_resultado.config(text="Selecciona un tipo válido.", fg="red")
        return
    
    limpiar_campos()

def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_carrera.delete(0, tk.END)
    entry_titulo.delete(0, tk.END)

def limpiar_texto():
    label_resultado.config(text="")

# --- Interfaz ---
root = tk.Tk()
root.title("Laboratorio POO")

tk.Label(root, text="Seleccione tipo de objeto:").pack(pady=(10, 0))
tipo_var = tk.StringVar(value="Persona")
opciones = ["Persona", "Estudiante", "Profesor"]
menu_tipo = tk.OptionMenu(root, tipo_var, *opciones, command=lambda _: actualizar_campos())
menu_tipo.pack()

tk.Label(root, text="Nombre:").pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack()

tk.Label(root, text="Edad:").pack()
entry_edad = tk.Entry(root)
entry_edad.pack()

label_carrera = tk.Label(root, text="Carrera / Materia:")
label_carrera.pack()
entry_carrera = tk.Entry(root)
entry_carrera.pack()

label_titulo = tk.Label(root, text="Título (solo para Profesor):")
entry_titulo = tk.Entry(root)

tk.Button(root, text="Crear", command=crear_objeto).pack(pady=5)
tk.Button(root, text="Limpiar Texto", command=limpiar_texto).pack(pady=5)

label_resultado = tk.Label(root, text="", fg="blue")
label_resultado.pack(pady=10)

actualizar_campos()  # Para ajustar los campos al inicio según el valor por defecto

root.mainloop()
