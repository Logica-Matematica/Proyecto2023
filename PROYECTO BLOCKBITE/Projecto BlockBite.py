import tkinter as tk
from PIL import ImageTk, Image
import os
import time as t
import random
import math
from tkinter import messagebox
from tkinter import simpledialog
from functools import partial

#login mal
def creacionDeDatos():
    if os.path.isfile("BaseDeDatos.txt"):
        BaseDeDatos=open("BaseDeDatos.txt")
        NombreDelUsuario=input("introduce el nombre")
        contraseña=input("introduce la contraseña")
        lineasTexto=BaseDeDatos.readlines()
        nombre=False
        password=False
        for elementos in lineasTexto:
            if elementos==NombreDelUsuario:
                nombre=True
                
            if elementos==contraseña:
                password=True
            print(elementos)
        if nombre==True and password==True:
            print("bien")
        else:
            print("mal")
        
    
    else:
        NombreDelUsuario=input("crea el nombre")
        contraseña=input("crea la contraseña")
        Datos=open("BaseDeDatos.txt","w")
        Datos.write(NombreDelUsuario + " ")
        Datos.write(contraseña)
        Datos.close()
        

#mancilla TRIVI
preguntas=[]
opciones=[]
respuestas=[]
def ResultadoDeEleccion(Trivia,i,a):
    
    resultado=False
    for respuestasCorrectas in respuestas:
        if opciones[i][a]==respuestasCorrectas:
            resultado=True
            
    if resultado==True:
        listaBotones[a].config(text="CORRECTO",bg="green")
        
    else:
        listaBotones[a].config(text="INCORRECTO",bg="red")
        RespuestaCorrecta=tk.Label(Trivia, text="Respuesta: " + respuestas[i],bg="green", fg="black", font="arial 18").place(x=20,y=650)
    for i in listaBotones:
        i.config(state="disable")

    
def Preguntaas(i,Trivia,animal):
    global preguntas,opciones,respuestas
    if animal == "Ratas":
        preguntas=preguntasRatas
        opciones=opcionesRatas
        respuestas=respuestasRatas
    elif animal == "Caninos":
        preguntas=preguntasCaninos
        opciones=opcionesCaninos
        respuestas=respuestasCaninos
    elif animal == "Serpientes":
        preguntas=preguntasSerpientes
        opciones=opcionesSerpientes
        respuestas=respuestasSerpientes
       
    elif animal == "Alacranes":
        preguntas=preguntasAlacranes
        opciones=opcionesAlacranes
        respuestas=respuestasAlacranes
        
    elif animal == "Arácnidos":
        preguntas=preguntasAracnidos
        opciones=opcionesAracnidos
        respuestas=respuestasAracnidos
   
   
   
    color="#646464"
    pregunta=tk.Label(Trivia, text=preguntas[i],bg="#646464", fg="white", font="arial, 30").place(x=330,y=10)
    acierto=tk.StringVar()
    opcion1=tk.Button(Trivia, font=("Arial", 15), bg=color, fg="white", text=opciones[i][0],command=lambda:ResultadoDeEleccion(Trivia,i,0))
    listaBotones.append(opcion1)
    opcion1.place(x=100,y=posicion[0])
    opcion2=tk.Button(Trivia, font=("Arial", 15), bg=color, fg="white", text=opciones[i][1],command=lambda:ResultadoDeEleccion(Trivia,i,1))
    listaBotones.append(opcion2)
    opcion2.place(x=100,y=posicion[1])
    opcion3=tk.Button(Trivia, font=("Arial", 15), bg=color, fg="white", text=opciones[i][2],command=lambda:ResultadoDeEleccion(Trivia,i,2))
    listaBotones.append(opcion3)
    opcion3.place(x=100,y=posicion[2])
    opcion4=tk.Button(Trivia, font=("Arial", 15), bg=color, fg="white", text=opciones[i][3],command=lambda:ResultadoDeEleccion(Trivia,i,3))
    listaBotones.append(opcion4)
    opcion4.place(x=100,y=posicion[3])
    siguiente=tk.Button(Trivia, font=("Arial", 20), bg="#646464", fg="white", text="NEXT ➤", command=lambda:cambio(i,Trivia,root,animal)).place(x=1000,y=700)
  
def cambio(i,Trivia,root,animal):
    Trivia.destroy()
    suma.append(1)
    if sum(suma)==4:
        suma.clear()
        on_start()
    else:
        listaBotones.clear()
        trivia(root,animal)
        
 
    
    
def trivia(root,animal):
    Trivia=tk.Toplevel(root)
    Trivia.title("Trivia")
    Trivia.geometry("1300x1100")
    Trivia.config(bg="#9b9b9b")
    #listas       O.M.
    random.shuffle(posicion)
    #-----------
    i=sum(suma)
    Preguntaas(i,Trivia,animal)
 
    
    
preguntasCaninos=["¿Qué debes hacer antes de acariciar\n a un perro que no conoces?", "¿Qué debes evitar hacer con un\nperro que está durmiendo, comiendo\n o cuidando a sus cachorros?", "¿Qué tipo de juegos pueden provocar\n que un perro te muerda?", "¿Qué debes hacer si un perro se\n comporta de manera amenazante \ncontigo?", "   ¿Qué debes hacer si un perro te   \nmuerde?"]
opcionesCaninos=[["Pedir permiso al dueño y dejar que\n el perro te olfatee", "Correr hacia el perro y abrazarlo", "Gritarle al perro y tirarle piedras", "Darle comida al perro sin preguntar"], ["Cantarle una canción al perro", "Molestarlo o fastidiarlo", "Acariciarlo suavemente", "Mirarlo a los ojos"], ["Tira y afloja o lucha libre", "Saltar la cuerda o el aro", "Escondite o pilla-pilla", "Hacer burbujas o volar cometas"], ["Mantener la calma, evitar el contacto\n visual y alejarte lentamente.", "Gritar, correr y patear al perro.", "Quedarte quieto y mirarlo fijamente.", "Tirarte al suelo y hacer el muerto."], ["Lavar la herida con agua y jabón y buscar\n atención médica.", "Morder al perro de vuelta y vengarte.", "Ignorar la herida y esperar que se cure sola.", "Ponerle alcohol o vinagre a la herida \ny taparla con una venda."]]
respuestasCaninos=["Pedir permiso al dueño y dejar que\n el perro te olfatee", "Molestarlo o fastidiarlo", "Tira y afloja o lucha libre", "Mantener la calma, evitar el contacto\n visual y alejarte lentamente.", "Lavar la herida con agua y jabón y buscar\n atención médica."]
listaBotones=[]
posicion=[200,300,400,500]
preguntasSerpientes=["¿Qué debes usar al caminar por el campo\n para evitar las picaduras de serpientes?", "¿Qué debes evitar hacer con las piedras y\n los troncos que encuentres en el campo?", "¿Qué debes hacer si ves una\n serpiente en el campo?", "¿Qué debes hacer para evitar que\n las serpientes entren en tu casa?", "¿Qué debes hacer para tapar los agujeros o\n grietas por donde puedan entrar las serpientes?"]    
opcionesSerpientes=[["Ropa y calzado adecuados", "Un sombrero y unas gafas de sol.", "Un traje de baño y unas chanclas.", "Un disfraz de serpiente y una máscara."],["Levantarlos o moverlos con manos\n y pies desprotegidos.", "Pintarlos o dibujarlos con colores.", "Contarlos o clasificarlos por tamaños.", "Saltar sobre ellos  o hacer equilibrio."],["Acercarte a ella y hacerle caricias.", "Gritarle y tirarle piedras.", "No acercarte a ella ni hacer\n movimientos bruscos.", "Invitarla a jugar contigo y darle un nombre."],["Dejar la puerta abierta y la luz encendida.", "Mantener la casa limpia y libre\n de roedores.", "Poner música a todo volumen y bailar.", "Colgar carteles que digan “Prohibido el paso a las serpientes.”"],["Usar plastilina o masilla.", "Usar cemento o yeso.", "Usar papel o cartón.",  "Usar flores o plantas."]]
respuestasSerpientes=["Ropa y calzado adecuados.", "Levantarlos o moverlos con manos\n y pies desprotegidos.", "No acercarte a ella ni hacer\n movimientos bruscos.", "Mantener la casa limpia y libre\n de roedores.", "Usar cemento o yeso."]  



preguntasAlacranes=["¿Qué insectos debes eliminar para que\n los alacranes no se alimenten de ellos?", "¿En qué época del año debes tener más\n cuidado con los alacranes?",  "¿Qué debes hacer con la ropa y los\n zapatos antes de ponértelos?",  "¿Qué debes poner en las alcantarillas y resumideros\n para evitar que entren los alacranes?",  "¿Qué debes hacer si te pica un alacrán?"]
opcionesAlacranes=[["Grillos y cucarachas", "Moscas y mosquitos", "Hormigas y arañas", "Abejas y avispas."],["Invierno", "Primavera", "Verano", "Otoño."],["Lavarlos", "Plancharlos", "Sacudirlos",  "Doblarlos."],["Papel",  "Plástico", "Malla metálica",  "Cartón."],["Rascarte", "Llorar", "Ir al médico",  "Dormir."]]
respuestasAlacranes=["Grillos y cucarachas", "Verano", "Sacudirlos", "Malla metálica",  "Ir al médico"]

preguntasAracnidos=["¿Qué debes hacer con las ventanas y las puertas para evitar que entren las arañas?", 
"¿Qué tipo de calzado debes usar al caminar por zonas donde puedan haber arañas o serpientes?",
"¿Qué vegetal puedes usar para aliviar la picadura de un arácnido?",
"¿Qué debes evitar colgar en las paredes para prevenir las picaduras de arañas?",
"¿Qué debes hacer si te pica una araña venenosa?"]

opcionesAracnidos=["Abrirlas", "Cerrarlas", "Instalar mosquiteros", "Pintarlas."],["Zapatillas", "Sandalias", "Botas", "Ojotas"],["Zanahoria", "Rábano", "Lechuga", "Tomate"],["Cuadros", "Espejos", "Ropa", "Relojes"],["Rascarte", "Llorar", "Ir al médico", "Dormir."]
respuestasAracnidos=["Instalar mosquiteros", "Botas", "Rábano", "Ropa", "Ir al médico"]

preguntasRatas=["¿Qué debes hacer para evitar que las ratas entren en tu casa?",
"¿Qué debes hacer si ves una rata en tu casa?",
"¿Qué debes hacer si tocas algo que ha estado en contacto con las ratas?",
"¿Qué debes hacer si te sientes mal después de haber estado cerca de las ratas?",
"¿Qué debes evitar hacer con las ratas o sus excrementos?"]
opcionesRatas=[["Dejar la puerta abierta y la luz encendida.", "Tapar los agujeros o grietas por donde puedan entrar.","Poner música a todo volumen y bailar.","Colgar carteles que digan “Prohibido el paso a las ratas”"],
["Correr hacia ella y abrazarla.", "Gritar y esconderte debajo de la cama.",  "Usar una trampa o un veneno para eliminarla.",  "Darle de comer queso y hacerle una caricia."],
["Lavar bien las manos y la ropa.",  "Pintar las uñas y ponerse perfume.",  "Comer un dulce y beber un refresco.",  "Nada, no pasa nada."],
["Acudir al médico.", "Tomar una siesta.",  "Jugar a la videoconsola.",  "Llamar a un amigo."],
["Tocarlos o acercarte a ellos.", "Mirarlos o fotografiarlos.", "Olerlos o escucharlos., Cantarles o dibujarlos."]]
respuestasRatas=["Tapar los agujeros o grietas por donde puedan entrar.",  "Usar una trampa o un veneno para eliminarla.", "Lavar bien las manos y la ropa.", "Acudir al médico.",  "Tocarlos o acercarte a ellos."]





suma=[0]
t=[]


#MANCILLA TRIVIA


#LOGIN


def BaseDeDatos(NombreDelUsuario,contraseña):
    Datos=open("Datos.txt","w")
    Datos.write(NombreDelUsuario + " ")
    Datos.write(contraseña)
    Datos.close()
 
def LoginDeCuenta(root):
    global login,NombreDelUsuario
    login=tk.Toplevel(root)
    login.title("Login")
    login.geometry("400x400+400+50")
    login.config(bg="#9b9b9b")
    
    tk.Label(login, text="Bienvenido a BlockBite por\n favor ingrese sus datos", font=("Arial Black", 17), bg="#646464", fg="white").place(x=30, y=10)

    tk.Label(login, text="Nombre:", font=("Sanchez", 14),bg="#646464", fg="white").place(x=70, y=100)
    NombreDelUsuario = tk.StringVar()
    NombreDelUsuario = tk.Entry(login, textvariable="Nombre",font=("Sanchez", 15),justify=tk.CENTER).place(x=70, y=130)

    tk.Label(login, text="contraseña:", font=("Sanchez", 14),bg="#646464", fg="white").place(x=70, y=170)
    contraseña= tk.StringVar()
    contraseña = tk.Entry(login, textvariable="contraseña ",font=("Sanchez", 15), show= '•', justify=tk.CENTER).place(x=70, y=195)
    tk.Button(login, text="Login", width=10, height=1, bg="#646464", font=("Arial Black", 15),fg="white", command=lambda:on_start()).place(x=150, y=280)



#LOGIN FIN


#TRES EN RAYA
nombreJugador1=""
nombreJugador2=""

def bloqueo():
    for i in range (0,9):
        listaBotones[i].config(state="disable")
        
def Inciar(root,ventana):
    global turno,nombreJugador1,nombreJugador2,turnoJugador
    for i in range (0,9):
        listaBotones[i].config(bg="lightgrey",text="",state="normal")
        t[i]="N"
    try:
        while nombreJugador1=="":
            nombreJugador1=simpledialog.askstring("Jugador","Por favor introduzca el nombre del jugador 1 (🕷)")
        while nombreJugador2=="":
            nombreJugador2=simpledialog.askstring("Jugador","Por favor introduzca el nombre del jugador 2 (🕸)")
        turnoJugador.set("Turno: " + nombreJugador1)
        turno=0
    except:
        bloqueo()  
    
def cambiar(num):
    global turno,nombreJugador1,nombreJugador2
    if t[num]=="N" and turno==0:
        listaBotones[num].config(text="🕷",bg="white") #cambio de color
        turno=1
        t[num]="🕷"
        turnoJugador.set("Turno: "+nombreJugador2)
    elif t[num]=="N" and turno==1:
        listaBotones[num].config(text="🕸",bg="blue")
        turno=0
        t[num]="🕸"
        turnoJugador.set("Turno: "+ nombreJugador1)
    listaBotones[num].config(state="disable")
    ganador()


def ganador():
    if (t[0]=="🕷" and t[1]=="🕷" and t[2]=="🕷")or(t[3]=="🕷" and t[4]=="🕷" and t[5]=="🕷")or(t[6]=="🕷" and t[7]=="🕷" and t[8]=="🕷"):
        bloqueo()
        messagebox.showinfo("GANADOR",nombreJugador1+" Gano el juego")
    if (t[0]=="🕷" and t[4]=="🕷" and t[8]=="🕷")or(t[2]=="🕷" and t[4]=="🕷" and t[6]=="🕷"):
        bloqueo()
        messagebox.showinfo("GANADOR",nombreJugador1+" Gano el juego")
    if (t[0]=="🕷" and t[3]=="🕷" and t[6]=="🕷")or(t[1]=="🕷" and t[4]=="🕷" and t[7]=="🕷")or(t[2]=="🕷" and t[5]=="🕷" and t[8]=="🕷"):
        bloqueo()
        messagebox.showinfo("GANADOR",nombreJugador1+" Gano el juego")
    if (t[0]=="🕸" and t[1]=="🕸" and t[2]=="🕸")or(t[3]=="🕸" and t[4]=="🕸" and t[5]=="🕸")or(t[6]=="🕸" and t[7]=="🕸" and t[8]=="🕸"):
        bloqueo()
        messagebox.showinfo("GANADOR",nombreJugador2+" Gano el juego")
    if (t[0]=="🕸" and t[4]=="🕸" and t[8]=="🕸")or(t[2]=="🕸" and t[4]=="🕸" and t[6]=="🕸"):
        bloqueo()
        messagebox.showinfo("GANADOR",nombreJugador2+" Gano el juego")
    if (t[0]=="🕸" and t[3]=="🕸" and t[6]=="🕸")or(t[1]=="🕸" and t[4]=="🕸" and t[7]=="🕸")or(t[2]=="🕸" and t[5]=="🕸" and t[8]=="🕸"):
        bloqueo()
        messagebox.showinfo("GANADOR",nombreJugador2+" Gano el juego")


def tresEnRaya(root):
    ventana=tk.Toplevel(root)
    ventana.title("TRES EN RAYA")
    ventana.geometry("370x500+400+100")
    ventana.resizable(width=False, height=False)
    ventana.config(bg="#9b9b9b")

    
    for i in range (0,9):
        t.append("N")
    boton0=tk.Button(ventana,width=9,height=3,command=lambda: cambiar(0))
    listaBotones.append(boton0)
    boton0.place(x=50,y=50)
    
    boton1=tk.Button(ventana,width=9,height=3,command=lambda: cambiar(1))
    listaBotones.append(boton1)
    boton1.place(x=150,y=50)
    
    boton2=tk.Button(ventana,width=9,height=3,command=lambda: cambiar(2))
    listaBotones.append(boton2)
    boton2.place(x=250,y=50)
    
    boton3=tk.Button(ventana,width=9,height=3,command=lambda: cambiar(3))
    listaBotones.append(boton3)
    boton3.place(x=50,y=150)
    
    boton4=tk.Button(ventana,width=9,height=3,command=lambda: cambiar(4))
    listaBotones.append(boton4)
    boton4.place(x=150,y=150)
    
    boton5=tk.Button(ventana,width=9,height=3,command=lambda: cambiar(5))
    listaBotones.append(boton5)
    boton5.place(x=250,y=150)
    
    boton6=tk.Button(ventana,width=9,height=3,command=lambda: cambiar(6))
    listaBotones.append(boton6)
    boton6.place(x=50,y=250)
    
    boton7=tk.Button(ventana,width=9,height=3,command=lambda: cambiar(7))
    listaBotones.append(boton7)
    boton7.place(x=150,y=250)
    
    boton8=tk.Button(ventana,width=9,height=3,command=lambda: cambiar(8))
    listaBotones.append(boton8)
    boton8.place(x=250,y=250)
    bloqueo()
    TurnDe=tk.Label(ventana,textvariable=turnoJugador).place(x=120,y=20)
    botonInicio=tk.Button(ventana,bg="#646464",fg="white",text="Iniciar Juego",width=15,height=3,command=lambda:Inciar(root,ventana)).place(x=130,y=350)
    Marca=tk.Label(ventana,bg="#2F4F4F",text="O.M.",width=5,height=1).place(x=300,y=450)


#TRES EN RAYA FIN
    
    
current_window = None


    
def on_select(value):
    print(f"Has seleccionado {value}")

def play(animal):
    print(f"Seleccionaste jugar con {animal}")

def show_animal_info(animal):
    global current_window
    if current_window is not None:
        current_window.destroy()
    info_window = tk.Toplevel(root)
    info_window.geometry("1300x1100")
    info_window.config(bg="#9b9b9b")
    if animal == "Ratas":
        info_text = """Existe una causa directa entre la aparición de ratas y ratones y la suciedad de una casa sin limpieza, ¡¡Así que no se lo pongamos fácil!!
Las ratas como cualquier animal prefiere tener su madriguera en un lugar más seguro y cómodo para las crías, y dónde el alimento esté garantizado.
Le recomendamos:
-Mantener la casa limpia y ordenada: La acumulación de suciedad y de trastos, ropas, papel … de manera incontrolada puede servir de fuentes de alimentación y refugio a roedores.
-Guardar los alimentos en recipientes resistente cerrados o alacenas, limpiando y eliminando los restos de alimentos desparramados.
-Almacenar basuras en recipientes resistentes, cerrados, herméticos.
-Revisar fuentes de calor como calefacción, calentadores de agua, cocina.
-Diseño y mantenimiento adecuado de desagües y sistema de saneamiento para evitar la atracción de roedores.
-Colocar barreras a lo largo de cables y tuberías para evitar el paso de roedores."""
    elif animal == "Caninos":
        info_text = """¿Cómo evitar ser mordido?
Si te confronta un perro, lo primero que debes de intentar hacer es permanecer calmado. El miedo y ansiedad es lo último que debes darle, mucho menos gritarle o golpearlo, eso solo empeorará la situación. Evita el contacto directo con sus ojos y ponte de pie de lado pues así te conviertes en un blanco más delgado. Una vez que notes al perro más calmado, usa cualquier objeto que tengas (bastón, sombrilla, cartera) a tu favor para parecer más grande de lo que eres y le comunicará al animal que ese espacio en el que estás es tuyo y que no estás interesado en su espacio. Eso probablemente haga que pierda interés en ti. Claro que no siempre es el caso."""
    elif animal == "Serpientes":
        info_text = """¿Cómo prevenir las mordeduras de serpiente?
Algunos consejos prácticos, útiles para minimizar las probabilidades de una mordedura son:
Utilizar siempre calzado (botas) preferiblemente hasta la altura de la rodilla, pueden ser de hule o de cuero.
Las serpientes muerden cuando se sienten amenazadas. La mayoría de las mordeduras por serpientes venenosas ocurren en los pies o las piernas cuando las personas accidentalmente las pisa.
No introducir las manos ni los pies directamente en huecos de árboles, cuevas o debajo de piedras o ramas.
Utilizar algún instrumento para remover escombros y malezas, debido a que las serpientes acostumbran esconderse en estos lugares.
Tratar de ir siempre acompañado de otra persona, ya que si ocurre algún accidente esta le pueda auxiliar.
Tener cuidado en la recolección de frutos, pues algunas serpientes viven o se pueden encontrar en los árboles y arbustos."""
    elif animal == "Alacranes":
        info_text = """¿Cómo prevenir las picaduras?
Medidas para evitar el ingreso de alacranes a las viviendas y prevenir accidentes en zonas con presencia de alacranes:
Revisar y sacudir prendas de vestir y calzados.
Sacudir la ropa de cama antes de acostarse o acostar un bebe o niño.
Evitar caminar descalzo.
Tener precaución cuando se examinan cajones o estantes.
Utilizar rejillas en desagües, cañerías y otras aberturas.
Colocar burletes o alambre tejido (mosquiteros) en puertas y ventanas.
Revocar las paredes, reparar grietas en pisos, paredes y techos.
Mantener limpia y ordenada la vivienda y alrededores. Evitar la acumulación de materiales de construcción, escombros, leña porque suelen ser lugares donde se alojan."""
    elif animal == "Arácnidos":
        info_text = """Algunos consejos para evitar las picaduras de arañas:
Usar guantes si trabaja en un área donde es probable que haya arañas.
Evitae las pilas de madera o de piedras y zonas oscuras donde habitan las arañas.
Fijarse si hay arañas en telarañas cerca del suelo, en garajes, parrillas para barbacoa, alrededor de piscinas (albercas) y en pilas de madera.
Deshágase de muebles viejos, neumáticos, objetos innecesarios, diarios y ropa vieja. Esto eliminará los lugares donde las arañas prefieren habitar.
Tapone aberturas y grietas en la casa.
Aparte su cama de las paredes de modo que sea menos probable que las arañas se trepen a su cama.
Sacudir y revisar las sábanas,mantas,ropa y zapatos para ver si tienen arañas
No dejar juguetes de su hijo al aire libre."""
    else:
        info_text = ""
    label = tk.Label(info_window, text=info_text, font=("Arial", 20), bg="#646464", fg="white", wraplength=850)
    label.pack(fill=tk.X)
    play_button = tk.Button(info_window, text="Jugar", command=lambda: trivia(root,animal), font=("Arial Black", 25), bg="#646464", fg="white", bd=0)
    play_button.pack(pady=10)
    button_volver = tk.Button(info_window, text="Volver", command=on_start, font=("Arial Black", 15), bg="#646464", fg="white", bd=0)
    button_volver.place(x=1100,y=700)
    current_window = info_window

def on_start():
 
    global current_window,preguntas,opciones,respuestas

    preguntas.clear()
    opciones.clear()
    respuestas.clear()
    listaBotones.clear()
    if current_window is not None:
        current_window.destroy()
    top = tk.Toplevel(root)
    top.geometry("1300x1100")
    top.config(bg="#9b9b9b")
    label = tk.Label(top, text="ACERCA DE QUE ANIMAL QUIERES APRENDER HOY", font=("Arial black", 28), bg="#646464", fg="white")
    label.pack(fill=tk.X)
    button1 = tk.Button(top, text="Caninos", command=lambda: show_animal_info("Caninos"), font=("Arial black", 28), bg="#646464", fg="white", bd=0)
    button1.pack(pady=20)
    button2 = tk.Button(top, text="Serpientes", command=lambda: show_animal_info("Serpientes"), font=("Arial black", 28), bg="#646464", fg="white", bd=0)
    button2.pack(pady=20)
    button3 = tk.Button(top, text="Alacranes", command=lambda: show_animal_info("Alacranes"), font=("Arial black", 28), bg="#646464", fg="white", bd=0)
    button3.pack(pady=20)
    button4 = tk.Button(top, text="Arácnidos", command=lambda: show_animal_info("Arácnidos"), font=("Arial black", 28), bg="#646464", fg="white", bd=0)
    button4.pack(pady=20)
    button5 = tk.Button(top, text="Ratas", command=lambda: show_animal_info("Ratas"), font=("Arial black", 28), bg="#646464", fg="white", bd=0)
    button5.pack(pady=20)
    current_window = top


   
root = tk.Tk()
root.withdraw()
start_window = tk.Toplevel(root)
start_window.title("BLOCKBITE")
start_window.geometry("1300x1100")
start_window.config(bg="#9b9b9b")
label = tk.Label(start_window, text="Bienvenido A", font=("Arial Black", 30), bg="#646464", fg="white")
label.pack(fill=tk.X)

imagen = Image.open("LogoBB.png")
imagen = imagen.resize((800, 300), Image.LANCZOS)

img = ImageTk.PhotoImage(imagen)
lbl_img = tk.Label(start_window, image=img)
lbl_img.pack()

button = tk.Button(start_window, text="EMPEZAR", comman=lambda: LoginDeCuenta(root), font=("Arial Black", 25), bg="#646464", fg="white", bd=0)
button.pack(pady=30)
juegoo = tk.Button(start_window, text="TRES EN RAYA", command=lambda: tresEnRaya(root), font=("Arial Black", 20), bg="#646464", fg="white", bd=0)
juegoo.pack(pady=70)
current_window = start_window

turnoJugador=tk.StringVar()
root.mainloop()