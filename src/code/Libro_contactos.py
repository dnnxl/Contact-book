#Autor Danny Xie Li
#Tarea Programada 1
#Instituto Tecnologico de Costa Rica
#Profesor William Mata
#Versión 0.0.1
#Fecha de entrega 25/09/16


#--------------------------------
#Librerías usadas
#--------------------------------

from os import startfile 
import random
import sys
import os
import tkinter.ttk as ttk 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#--------------------------------
#Variables Globales 
#--------------------------------

ListaNumeroModificado = []
NumerosModificar = []
NombreAModificar = []
imagen = ["usuario_1_.gif"]
ListasDeContactos = []
listaNumero = []
listaCorreo = []
sonido = ["Silencio"]
ListaNotasExtras = []

#--------------------------------
#Funciones
#--------------------------------

#Descripción: El siguiente código se utiliza para mandar un mensaje de error.
#Entradas: Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.

def PongaNumero():
    messagebox.showerror("Error","Escriba un número")


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función ordena alfabeticamente los contactos.
#Entradas: Ninguno.
#Salidas: Ninguno.
#Restricciones: Ninguno.

def Alfabético():
    global ListasDeContactos
    if ListasDeContactos == []:
        return
    else:
        ListaAlfabético = []
        for i in ListasDeContactos:
            ListaAlfabético = ListaAlfabético + [i[0]]
        ListaAlfabético.sort()
        ListaConContactos = []
        for i in ListaAlfabético:
            for j in ListasDeContactos:
                if i == j[0]:
                     ListaConContactos = ListaConContactos + [j]
        ListasDeContactos = ListaConContactos
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función abre el manual de usuario.
#Entradas: Ninguno.
#Salidas: Ninguno.
#Restricciones: Ninguno.

def Manual(): 
    startfile("Manual_de_usuario_libro_contactos.pdf")
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función retorna el contenido leído en un archivo en formato string, cuando se le digite la entrada que es el nombre del archivo en formato string.
#Entradas: Un string.
#Salidas: Un string.
#Restricciones: Sólo en formato string.

def leerTodo (nombreArchivo):
       archivo = open (nombreArchivo, "r+")  #Abre el archivo y la operación es sólo escritura.
       contenido = archivo.read ()  #El contenido leído se lo asigna a la variable.
       archivo.close() #Se cierra el archivo.
       return contenido

#--------------------------------------------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función carga los datos que se encuentra en el archivo "AppContactosInfo.txt" y se lo asigna a la variable global.
#Entradas: Ninguno.
#Salidas: Ninguno.
#Restricciones: Ninguno.
    
def CargarListaDeContactos():
    global ListasDeContactos  #Utiliza la variable global ListasDeContactos
    archivo=leerTodo("AppContactosInfo.txt") #Utiliza la función leerTodo del archivo "AppContactosInfo.txt"
    if archivo == "" :
        ListasDeContactos = []
    else:
        ListasDeContactos = eval(archivo) #Se le asigna los datos que se encuentra en la variable a la variable global.
    
#----------------------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función retorna un valor booleano si el nombre está en la variable global ListasDeContactos.
#Entradas: Un string.
#Salidas: Un valor booleano.
#Restricciones: Sólo strings.

def Está(nombre):
       global ListasDeContactos #Utiliza la variable global ListasDeContactos
       for i in ListasDeContactos:
              if i[0] == nombre:
                     return True
       return False

#----------------------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función abre un cuadro de mensaje indicando que no se encuentra el usuario en los contactos.
#Entradas: Ninguno.
#Salidas: Ninguno.
#Restricciones: Ninguno.

def MensajeDeErrorNombres():
       messagebox.showwarning("Error", "Error: No se encuentra este usuario en los contactos")

#----------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función abre un cuadro de mensaje indicando que la información ha sido guardado.
#Entradas: Ninguno.
#Salidas: Ninguno.
#Restricciones: Ninguno.
       
def MensajeDeListo():
       messagebox.showinfo("Guardado", "Su información ha sido guardado")

#------------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función abre un cuadro de mensaje indicando que la información es demasiado largo.
#Entradas: Ninguno.
#Salidas: Ninguno.
#Restricciones: Ninguno.
       
def ErrorNombreMuyLargo():
       messagebox.showerror("Error","Error: Escriba la información más corto")

#------------------------------------------------------------------------------------
#Descripción: La siguiente función cuenta la cantidad de letras que tiene un string.
#Entradas: Un string.
#Salidas: Un entero positivo.
#Restricciones: Sólo strings.
       
def ContarLetras(string):
    cont = 0
    for i in string:
        cont=cont+1
    return cont

#----------------------------------------------------------------------------------------------
#Descripción: La siguiente función convierte listas en tuplas y retorna una lista con tuplas.
#Entradas: Una lista.
#Salidas: Una lista.
#Restricciones: Sólo listas en formato [[],[]].

def TuplaModo(lista):
        tuplas=[]
        for i in lista:
            tuplas=tuplas+[tuple(i)]
        return tuplas
       
#--------------------------------------------------------------------------------------------------------------
#Pantalla de información general de la APP.
#--------------------------------------------------------------------------------------------------------------
#Descripción: El siguiente código representa una pantalla, la pantalla de información general de la aplicación.
#Entradas: Ninguno.
#Salidas: Ninguno.
#Restricciones: Ninguno.

def VentanaAcercaDe():
       ventanaAcercaDe = Toplevel(celular) #Se crea una ventana.
       ventanaAcercaDe.title("DContact") #Titulo de la ventana.
       canvas = Canvas(ventanaAcercaDe,width=300, height=210, bg='white') #Se crea una pantalla canvas en donde se le coloca labels, botones etc.
       canvas.pack(expand=YES, fill=BOTH) #Empaca el canvas y lo exapande en toda la pantalla.
       icono = ventanaAcercaDe.iconbitmap("guia-telefonica.ico") #Icono de la ventana.
       ventanaAcercaDe.geometry("310x550") #Tamano de la ventana.
       ventanaAcercaDe.maxsize(310,550) #El tamano máximo que se puede agrandar o minimizar la pantalla.
       canvas.config(bg = "RoyalBlue4") #Configura el color de la ventana.
       EtiquetaTitulo=Label(canvas,bg="light sea green",width=50,height=4).place(x=0,y=1) #Se le asigna una etiqueta a la variable.
       titulo=Label(canvas,text="Acerca de DContact",fg="white",relief=FLAT,bg="light sea green",font=("ms sans Serif",10,"bold")).place(x=75,y=25) #Se le asigna una etiqueta a la variable.
       titulo2=Label(canvas,text="Actualizaciones",fg="white",relief=FLAT,width=25,height=2,bg="orange",font=("ms sans Serif",10,"bold")).place(x=40,y=100) #Se le asigna una etiqueta a la variable.
       titulo3=Label(canvas,text="Nombre de la APP",fg="white",relief=FLAT,bg="orange",width=25,height=2,font=("ms sans Serif",10,"bold")).place(x=40,y=260) #Se le asigna una etiqueta a la variable.
       title5 =Label(canvas,text="DContact",fg="white",relief=FLAT,width=25,height=2,bg="RoyalBlue4",font=("ms sans Serif",8,"bold")).place(x=70,y=300) #Se le asigna una etiqueta a la variable
       title =Label(canvas,text="Proximamente",fg="white",relief=FLAT,width=25,height=2,bg="RoyalBlue4",font=("ms sans Serif",8,"bold")).place(x=70,y=140) #Se le asigna una etiqueta a la variable.
       titulo4=Label(canvas,text="Versión",fg="white",relief=FLAT,bg="orange",width=25,height=2,font=("ms sans Serif",10,"bold")).place(x=40,y=180) #Se le asigna una etiqueta a la variable.
       title2 =Label(canvas,text="0.0.1",fg="white",relief=FLAT,width=25,height=2,bg="RoyalBlue4",font=("ms sans Serif",8,"bold")).place(x=70,y=220) #Se le asigna una etiqueta a la variable
       titulo5=Label(canvas,text="Fecha de creación",fg="white",relief=FLAT,width=25,height=2,bg="orange",font=("ms sans Serif",10,"bold")).place(x=40,y=340) #Se le asigna una etiqueta a la variable.
       title3 =Label(canvas,text="21 de Septiembre del 2016",fg="white",relief=FLAT,width=25,height=2,bg="RoyalBlue4",font=("ms sans Serif",8,"bold")).place(x=70,y=380) #Se le asigna una etiqueta a la variable
       titulo7=Label(canvas,text="Creador",fg="white",relief=FLAT,bg="orange",width=25,height=2,font=("ms sans Serif",10,"bold")).place(x=40,y=420) #Se le asigna una etiqueta a la variable.
       title4 =Label(canvas,text="Danny Xie Li",fg="white",relief=FLAT,width=25,height=2,bg="RoyalBlue4",font=("ms sans Serif",8,"bold")).place(x=70,y=460) #Se le asigna una etiqueta a la variable
       ventanaAcercaDe.mainloop() #Espera hasta que el usuario haga un evento.              

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Pantalla de selección de imagenes de la APP.
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Descripción: El siguiente código le permite accede a la pantalla de selección de imagenes de la APP.
#Entradas: Ninguna.
#Salidas: Ninguna
#Restricciones: Ninguna.

def VentanaImagenes():

#----------
#Funciones
#----------
#Descripción: La siguiente función se le asigna una imagen a la variable global.
#Entradas:Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.
    
    def AceptarImagen():
        global imagen
        imagen=[StringImagen]

#----------
#Funciones
#----------
#Descripción: La siguiente función se le asigna una imagen a la variable global.
#Entradas:Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.
    
    def AsignarImagenSoldado():
        global imagen
        imagen=["soldado.gif"]
        print(imagen)

#----------
#Funciones
#----------
#Descripción: La siguiente función se le asigna una imagen a la variable global.
#Entradas:Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.

    def AsignarImagensquirtle():
        global imagen
        imagen=["squirtle.gif"]
        print(imagen)

#----------
#Funciones
#----------
#Descripción: La siguiente función se le asigna una imagen a la variable global.
#Entradas:Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.
        
    def AsignarImagenSnolax():
        global imagen
        imagen=["snorlax.gif"]
        print(imagen)

#----------
#Funciones
#----------
#Descripción: La siguiente función se le asigna una imagen a la variable global.
#Entradas:Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.

    def AsignarImageningeniero():
        global imagen
        imagen=["ingeniero.gif"]
        print(imagen)

#----------
#Funciones
#----------
#Descripción: La siguiente función se le asigna una imagen a la variable global.
#Entradas:Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.

    def AsignarImagenPolicia():
        global imagen
        imagen=["policia.gif"]
        print(imagen)

#----------
#Funciones
#----------
#Descripción: La siguiente función se le asigna una imagen a la variable global.
#Entradas:Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.

    def AsignarImagenDj():
        global imagen
        imagen=["dj.gif"]
        print(imagen)

#----------
#Funciones
#----------
#Descripción: La siguiente función se le asigna una imagen a la variable global.
#Entradas:Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.

    def AsignarImagenAdministrador():
        global imagen
        imagen=["hombre-de-negocios.gif"]
        print(imagen)

#----------
#Funciones
#----------
#Descripción: La siguiente función se le asigna una imagen a la variable global.
#Entradas:Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.
        
    def AsignarImagenJuez():
        global imagen
        imagen=["juez.gif"]
        print(imagen)

#----------
#Funciones
#----------
#Descripción: La siguiente función se le asigna una imagen a la variable global.
#Entradas:Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.

    def AsignarImagenLadron():
        global imagen
        imagen=["ladron.gif"]
        print(imagen)

#----------
#Funciones
#----------
#Descripción: La siguiente función cierra la ventana de Imagenes y ademas se le asigna a la variable global el imagen default.
#Entradas:Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.

    def CerrarVentana():
        global imagen
        imagen=["usuario_1_.gif"]
        print(imagen)
        ventanaImagenes.withdraw()

#----------
#Funciones
#----------
#Descripción: La siguiente función abre un mensaje de información indicando que la imagen ha sido guardado.
#Entradas:Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.

    def InfoImagen():
        messagebox.showinfo("Info","La imagen ha sido asignado")

#----------
#Funciones
#----------
#Descripción: La siguiente función abre una ventana de error indicando que seleccione una imagen.
#Entradas:Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.
        
    def ErrorImagen():
        messagebox.showerror("Error","Seleccione una imagen")

#----------
#Funciones
#----------
#Descripción: La siguiente funcion, cuando el usuario le da click en aceptar (de color verde), aparece un mensaje en donde dice que la imagen ha sido asignado o error cuando no se ha sido seleccionado.
#Entradas:Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.
        
    def AceptarVentana():
        global imagen #Utiliza la variable global.
        if imagen == ["usuario_1_.gif"]: 
            return ErrorImagen() #Abre el mensaje de error.
        else:
            InfoImagen() #Abre el mensaje de información.
            ventanaImagenes.withdraw() #Cerrar la ventana.
            
    ventanaImagenes = Toplevel(celular) #Se crea una ventana.
    ventanaImagenes.title("DContact") #Titulo de la ventana.
    icono = ventanaImagenes.iconbitmap("guia-telefonica.ico") #Icono de la ventana.
    ventanaImagenes.geometry("310x400") #Tamano de la ventana.
    ventanaImagenes.maxsize(310,550) #El tamano máximo que se puede agrandar o minimizar la pantalla.
    ventanaImagenes.config(bg = "RoyalBlue4") #Configura el color de la ventana.
    no = PhotoImage(file = "error.gif") #A la imagen de equis o no se le asigna a la variable no.
    si = PhotoImage(file = "exito.gif") #A la imagen de check se le asigna a la variable si.
    ladron = PhotoImage(file = "ladron.gif") #A la imagen se le asigna a la variable ladron.
    squirtle = PhotoImage(file = "squirtle.gif") #A la imagen se le asigna a la variable squitle.
    snolax = PhotoImage(file = "snorlax.gif") #A la imagen se le asigna a la variable snolax.
    usuario = PhotoImage(file = "usuario_1_.gif") #A la imagen se le asigna a la variable usuario.
    ingeniero=PhotoImage(file = "ingeniero.gif")  #A la imagen se le asigna a la variable ingeniero.
    policia =PhotoImage(file = "policia.gif") #A la imagen se le asigna a la variable policia.
    soldado = PhotoImage(file = "soldado.gif") #A la imagen se le asigna a la variable soldado.
    Dj = PhotoImage(file = "dj.gif") #A la imagen se le asigna a la variable Dj.
    Administrador = PhotoImage(file = "hombre-de-negocios.gif") #A la imagen se le asigna a la variable Administrador.
    Juez = PhotoImage(file = "juez.gif") #A la imagen se le asigna a la variable Juez.
    BotonLadron=Button(ventanaImagenes,command=AsignarImagenLadron,image=ladron,relief=FLAT,bg = "RoyalBlue4").place(x=65,y=100) #Se crea un boton con la variable de la imagen ladron.
    BotonSquirtle=Button(ventanaImagenes,image=squirtle,relief=FLAT,command=AsignarImagensquirtle,bg = "RoyalBlue4").place(x=65,y=150) #Se crea un boton con la variable de la imagen Squirtle.    
    BotonSnolax=Button(ventanaImagenes,image=snolax,relief=FLAT,command=AsignarImagenSnolax,bg = "RoyalBlue4").place(x=65,y=200) #Se crea un boton con la variable de la imagen Snolax.
    Botoningeniero=Button(ventanaImagenes,image=ingeniero,relief=FLAT,command= AsignarImageningeniero,bg = "RoyalBlue4").place(x=140,y=200) #Se crea un boton con la variable de la imagen Ingeniero.
    Botonpolicia=Button(ventanaImagenes,command=AsignarImagenPolicia,image=policia,relief=FLAT,bg = "RoyalBlue4").place(x=215,y=200) #Se crea un boton con la variable de la imagen policia.
    Botonsoldado=Button(ventanaImagenes,command=AsignarImagenSoldado,image=soldado,relief=FLAT,bg = "RoyalBlue4").place(x=215,y=150) #Se crea un boton con la variable de la imagen soldado.
    BotonDj=Button(ventanaImagenes,image=Dj,relief=FLAT,command=AsignarImagenDj,bg = "RoyalBlue4").place(x=140,y=150) #Se crea un boton con la variable de la imagen Dj.
    BotonAdministrador=Button(ventanaImagenes,command=AsignarImagenAdministrador,relief=FLAT,image=Administrador,bg = "RoyalBlue4").place(x=215,y=100) #Se crea un boton con la variable de la imagen administrador.
    BotonJuez=Button(ventanaImagenes,command=AsignarImagenJuez,image=Juez,relief=FLAT,bg = "RoyalBlue4").place(x=140,y=100) #Se crea un boton con la variable de la imagen Juez.
    botonSi=Button(ventanaImagenes,command=AceptarVentana,image=si,bg="RoyalBlue4",relief=FLAT).place(x=70,y=300) #Se crea un boton con la variable de la imagen si, aceptar.
    botonNo=Button(ventanaImagenes,image=no,bg="RoyalBlue4",command=CerrarVentana,relief=FLAT).place(x=200,y=300) #Se crea un boton con la variable de la imagen no, de cancelar.
    EtiquetaImagenes = Label(ventanaImagenes,bg="light sea green",width=50,height=4).place(x=0,y=1) #Se le asigna una etiqueta a la variable.
    TextoImagenes = Label(ventanaImagenes,text="Imagenes",fg="white",relief=FLAT,bg="light sea green",font=("ms sans Serif",12,"bold")).place(x=110,y=25) #Se le asigna una etiqueta a la variable.
    ventanaImagenes.mainloop() #La ventana espera hasta que haya interracion con el usuario.

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Pantalla de Notas Extras.
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Descripción: El siguiente código le permite accede a la pantalla de notas extras de la APP.
#Entradas: Ninguna.
#Salidas: Ninguna
#Restricciones: Ninguna.

def VentanaNotasExtras():

#----------
#Funciones
#----------
#Descripción: El siguiente código le permite corregir, validar y recoger la información de las variables.
#Entradas: Ninguna.
#Salidas: Ninguna
#Restricciones: Ninguna.
       
    def NotasExtrasNotes():
           
        global ListaNotasExtras #Utiliza la variable global
        
        Lista = [] #Se le asigna una lista vacía a la variable.
        Familia = FamiliaNotes.get() #Se le asigna el valor recogido a la variable.
        Notas = Notes.get() #Se le asigna el valor recogido a la variable.
        Profesion = ProfesionNotes.get() #Se le asigna el valor recogido a la variable.
        
        dia = dia0.get() #Se le asigna el valor recogido a la variable.
        mes = mes0.get() #Se le asigna el valor recogido a la variable.
        año = año0.get() #Se le asigna el valor recogido a la variable.
        cumple = dia + mes + año #Se cocatenan los strings.
        
        dia2 = dia1.get() #Se le asigna el valor recogido a la variable.
        mes2 = mes1.get() #Se le asigna el valor recogido a la variable.
        año2 = año1.get() #Se le asigna el valor recogido a la variable.
        Matrimonio = dia2 + mes2 + año2 #Se cocatenan los strings.
        
        day = day2.get() #Se le asigna el valor recogido a la variable.
        month = month2.get() #Se le asigna el valor recogido a la variable.
        year = year2.get() #Se le asigna el valor recogido a la variable.
        Trabajo = day + month + year #Se cocatenan los strings.
        Direccion = DireccionNotes.get()  #Se le asigna el valor recogido a la variable.
        Entretenimiento = EntretenimientoNotes.get()  #Se le asigna el valor recogido a la variable.
        Deporte = DeportesNotes.get()  #Se le asigna el valor recogido a la variable.
        
        if Cien(Notas) == False:
            Lista = Lista + [["Notas",Notas]]  #Se le asigna el valor de la lista recogido a la variable.
            
        if Cien(Familia) == False:
            Lista = Lista + [["Acerca de la familia",Familia]]  #Se le asigna el valor de la lista recogido a la variable.
            
        if Cincuenta(Profesion) == False and ContarLetras(Profesion)>3:
            Lista = Lista + [["Profesión",Profesion]]  #Se le asigna el valor de la lista recogido a la variable.
            
        if Fechas(cumple) == False:
            Lista = Lista + [["Cumpleaños",cumple]]  #Se le asigna el valor de la lista recogido a la variable.
            
        if Fechas(Matrimonio) ==False:
            Lista = Lista + [["Matrimonio",Matrimonio]]  #Se le asigna el valor de la lista recogido a la variable.
            
        if Fechas(Trabajo) == False:
            Lista = Lista + [["Trabajo",Trabajo]]  #Se le asigna el valor de la lista recogido a la variable.
            
        if Cincuenta(Direccion) == False:
            Lista = Lista + [["Direccion",Direccion]]  #Se le asigna el valor recogido a la variable.
            
        if Cien(Entretenimiento) == False:
            Lista = Lista + [["Entretenimiento",Entretenimiento]]  #Se le asigna el valor recogido a la variable.
            
        if Cien(Deporte) == False:
            Lista = Lista + [["Deporte",Deporte]]  #Se le asigna el valor recogido a la variable.
            
        ListaNotasExtras = TuplaModo(Lista) #Convierte en tuplas todos los valores anteriores.
        MensajeDeListo() #Retorna el mensaje de listo que ha sido guardado.
        ventanaNotasExtras.withdraw() #Cierra la ventana.

#----------
#Funciones
#----------
#Descripción: El siguiente código cuenta si hay 140 letras o simbolos y puede retornar un mensaje o un valor booleano.
#Entradas: Un string.
#Salidas: Un valor booleano o un mensaje.
#Restricciones: Ninguno.

    def Cien(string):
        if string == "":
            return True
        if ContarLetras(string)>140:
            return ErrorNombreMuyLargo()
        else:
            return False

#----------
#Funciones
#----------
#Descripción: El siguiente código cuenta si hay 50 letras o simbolos y puede retornar un mensaje o un valor booleano.
#Entradas: Un string.
#Salidas: Un valor booleano o un mensaje.
#Restricciones: Ninguno.

    def Cincuenta(string):
        if string == "":
            return True
        if ContarLetras(string) > 50:
            return ErrorNombreMuyLargo()
        else:
            return False

#----------
#Funciones
#----------
#Descripción: El siguiente código cuenta si hay 9 letras o simbolos en las fechas y puede retornar un mensaje o un valor booleano.
#Entradas: Un string.
#Salidas: Un valor booleano o un mensaje.
#Restricciones: Ninguno.
    
    def Fechas(string):
        if string == "":
            return True
        if ContarLetras(string) > 9:
            return ErrorNombreMuyLargo()
        else:
            return False

#----------
#Funciones
#----------
#Descripción: El siguiente código cierra la ventana de NotasExtras.
#Entradas: Ninguno.
#Salidas: Ninguno.
#Restricciones: Ninguno.
       
    def Cerrar3():
        ventanaNotasExtras.withdraw()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Ventana de Notas Extras o Datos Extras
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
    ventanaNotasExtras = Toplevel(celular) #Se crea una ventana dentro de la pantalla ventana1.
    ventanaNotasExtras.title("DContact") #Titulo de la ventana.
    icono4 = ventanaNotasExtras.iconbitmap("guia-telefonica.ico") #Icono
    no = PhotoImage(file = "error.gif") #Se carga la imagen de si o aceptar.
    si = PhotoImage(file = "exito.gif") #Se carga la imagen de no o cancelar.
    ventanaNotasExtras.geometry("305x630") #Tamano de la ventana.
    ventanaNotasExtras.maxsize(305,630) #El tamano maximo de la ventana.
    ventanaNotasExtras.config(bg="RoyalBlue4") #Configura el color de la ventana.
    EtiquetaTitulo = Label(ventanaNotasExtras,bg = "light sea green",width = 50,height = 4).place(x=0,y=1) #Se le asigna una etiqueta a la variable.
    titulo = Label(ventanaNotasExtras,text = "Datos Extras",fg = "white",relief = FLAT,bg = "light sea green",font = ("ms sans Serif",12,"bold")).place(x=100,y=25) #Se le asigna una etiqueta a la variable.
    
    FamiliaNotes = StringVar() #Se le asigna el valor de string a una variable.
    EtiquetaFamilia = Label(ventanaNotasExtras,text = "Familia",fg = "white",bg = "RoyalBlue4",width = 50,height = 4,relief = FLAT,font = ("ms sans Serif",8,"bold")).place(x=-65,y=90) #Se crea una etiqueta y se lo asigna.
    EspacioFamilia = Entry(ventanaNotasExtras,textvariable = FamiliaNotes,fg = "black",bg = "white",width = 15,font = ("ms sans Serif",8,"bold")).place(x=160,y=110) #Se crea  un campo de text y se lo asigna a la variable.

    Notes = StringVar() #Se le asigna el valor de string a una variable.
    EtiquetaNotas = Label(ventanaNotasExtras,text = "Notas",fg = "white",bg = "RoyalBlue4",width = 50,height = 4,relief = FLAT,font = ("ms sans Serif",8,"bold")).place(x=-65,y=140) #Se crea una etiqueta y se lo asigna.
    EspacioNotas = Entry(ventanaNotasExtras,textvariable = Notes,fg = "black",bg = "white",width = 15,font = ("ms sans Serif",8,"bold")).place(x=160,y=160) #Se crea  un campo de text y se lo asigna a la variable.
    
    ProfesionNotes = StringVar() #Se le asigna el valor de string a una variable.
    EtiquetaProfesion = Label(ventanaNotasExtras,text = "Profesión",fg = "white",bg = "RoyalBlue4",width = 50,height = 4,relief = FLAT,font = ("ms sans Serif",8,"bold")).place(x=-65,y=190) #Se crea una etiqueta y se lo asigna. 
    EspacioProfesion = Entry(ventanaNotasExtras,textvariable = ProfesionNotes,fg = "black",bg = "white",width = 15,font = ("ms sans Serif",9,"bold")).place(x=160,y=210) #Se crea  un campo de text y se lo asigna a la variable.

    EtiquetaCumple = Label(ventanaNotasExtras,text = "Cumpleaños",fg = "white",bg = "RoyalBlue4",width = 50,height = 4,relief = FLAT,font = ("ms sans Serif",8,"bold")).place(x=-65,y=240) #Se le asigna una etiqueta a la variable.
    dia0 = StringVar() #Se le asigna el valor de string a una variable.
    mes0 = StringVar() #Se le asigna el valor de string a una variable.
    año0 = StringVar() #Se le asigna el valor de string a una variable.
    OptionDia1 = ttk.Combobox(ventanaNotasExtras,textvariable = dia0,values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],width=2).place(x=160,y=260) #Se le asigna a una variable el option boton
    OptionMes1 = ttk.Combobox(ventanaNotasExtras,textvariable = mes0,values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],width = 2).place(x=200,y=260) #Se le asigna a una variable el option boton
    OptionAño1 = ttk.Combobox(ventanaNotasExtras,textvariable = año0,values = ["1900",'1901', '1902', '1903', '1904', '1905', '1906', '1907', '1908', '1909', '1910', '1911', '1912', '1913', '1914', '1915', '1916', '1917','1918', '1919', '1920', '1921', '1922', '1923', '1924', '1925', '1926', '1927', '1928', '1929', '1930', '1931', '1932', '1933', '1934', '1935', '1936', '1937', '1938', '1939', '1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947', '1948', '1949', '1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016'],width=4).place(x=240,y=260) #Se le asigna a una variable el option boton
    
    EtiquetaMatrimonio = Label(ventanaNotasExtras,text="Matrimonio",fg="white",bg="RoyalBlue4",width=50,height=4,relief=FLAT,font=("ms sans Serif",8,"bold")).place(x=-65,y=290) #Se le asigna la etiqueta a la variable matrimonio.
    dia1 = StringVar()#Se le asigna el valor de string a una variable.
    mes1 = StringVar()#Se le asigna el valor de string a una variable.
    año1 = StringVar()#Se le asigna el valor de string a una variable.
    OptionDia2 = ttk.Combobox(ventanaNotasExtras,textvariable=dia1,values=['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],width=2).place(x=160,y=310)
    OptionMes2 = ttk.Combobox(ventanaNotasExtras,textvariable=mes1,values=['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],width=2).place(x=200,y=310)
    OptionAño2 = ttk.Combobox(ventanaNotasExtras,textvariable=año1,values=["1900",'1901', '1902', '1903', '1904', '1905', '1906', '1907', '1908', '1909', '1910', '1911', '1912', '1913', '1914', '1915','1916', '1917', '1918', '1919', '1920', '1921', '1922', '1923', '1924', '1925', '1926', '1927', '1928', '1929', '1930', '1931', '1932', '1933', '1934', '1935', '1936', '1937', '1938', '1939', '1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947', '1948', '1949', '1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016'],width=4).place(x=240,y=310)

    EtiquetaFechaTrabajo = Label(ventanaNotasExtras,text = "Inicio(Trabajo)",fg = "white",bg = "RoyalBlue4",width = 50,height = 4,relief = FLAT,font = ("ms sans Serif",6,"bold")).place(x=-75,y=340)#Se le asigna la etiqueta a la variable trabajo.
    day2 = StringVar()#Se le asigna el valor de string a una variable.
    month2 = StringVar()#Se le asigna el valor de string a una variable.
    year2 = StringVar()#Se le asigna el valor de string a una variable.
    OptionDia3 = ttk.Combobox(ventanaNotasExtras,textvariable = day2,values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],width=2).place(x=160,y=360)
    OptionMes3 = ttk.Combobox(ventanaNotasExtras,textvariable = month2,values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],width = 2).place(x=200,y=360) #Se le asigna a una variable el option boton
    OptionAño3 = ttk.Combobox(ventanaNotasExtras,textvariable = year2,values = ["1900",'1901', '1902', '1903', '1904', '1905', '1906', '1907', '1908', '1909', '1910', '1911', '1912', '1913', '1914', '1915','1916', '1917', '1918', '1919', '1920', '1921', '1922', '1923', '1924', '1925', '1926', '1927', '1928', '1929', '1930', '1931', '1932', '1933', '1934', '1935', '1936', '1937', '1938', '1939', '1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947', '1948', '1949', '1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016'],width=4).place(x=240,y=360)

    DireccionNotes = StringVar()#Se le asigna el valor de string a una variable.
    EtiquetaDireccionfisicaTrabajo = Label(ventanaNotasExtras,text = "Dónde trabaja",fg = "white",bg = "RoyalBlue4",width = 50,height = 4,relief = FLAT,font = ("ms sans Serif",8,"bold")).place(x=-75,y=390) #Se le asigna una qtiqueta a una variable
    EspacioDireccionfisicaTrabajo = Entry(ventanaNotasExtras,textvariable = DireccionNotes,fg = "RoyalBlue4",bg = "white",width = 15,font = ("ms sans Serif",9,"bold")).place(x=160,y=410) #Se le asigna un campo de texto a la variable.

    EntretenimientoNotes = StringVar() #Se le asigna el valor de string a una variable.
    EtiquetaEntretenimiento = Label(ventanaNotasExtras,text = "Entretenimiento",fg = "white",bg = "RoyalBlue4",width = 50,height = 4,relief = FLAT,font = ("ms sans Serif",8,"bold")).place(x=-65,y=440) #Se le asigna una qtiqueta a una variable
    EspacioEntretenimiento = Entry(ventanaNotasExtras,textvariable = EntretenimientoNotes,fg = "RoyalBlue4",bg = "white",width = 15,font = ("ms sans Serif",9,"bold")).place(x=160,y=460)#Se le asigna un campo de texto a la variable.

    DeportesNotes = StringVar() #Se le asigna el valor de string a una variable.
    EtiquetaDeportes = Label(ventanaNotasExtras,text = "Deportes",fg = "white",bg = "RoyalBlue4",width = 50,height = 4,relief = FLAT,font = ("ms sans Serif",8,"bold")).place(x=-65,y=490)#Se le asigna una qtiqueta a una variable
    EspacioDeportes = Entry(ventanaNotasExtras,textvariable = DeportesNotes,fg = "RoyalBlue4",bg = "white",width = 15,font = ("ms sans Serif",8,"bold")).place(x=160,y=510) #Se le asigna un campo de texto a la variable.
    
    botonSi = Button(ventanaNotasExtras,command = NotasExtrasNotes,image = si,bg = "RoyalBlue4",relief = FLAT).place(x=70,y=560) #Se le asigna a la variable el boton de aceptar.
    botonNo = Button(ventanaNotasExtras,command = Cerrar3,image = no,bg = "RoyalBlue4",relief = FLAT).place(x=200,y=560) #Se le asigna a la variable el boton de no o de cancelar.

    ventanaNotasExtras.mainloop() #La ventana espera hasta que el usuario digite algo.

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Ventana Secundaria (Ventana de Agregar)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Descripción: El siguiente código crea la pantalla secundaria del App Contactos, es la ventana de agregar contacto.
#Entradas: Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.

def VentanaAgregar():

#----------
#Funciones
#----------
#Descripción: El siguiente código se usa para cerrar la ventana de ventana de Agregar.
#Entradas: Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.
    
    def Cerrar():
        ventana.withdraw()
        Principal()

#----------
#Funciones
#----------
#Descripción: El siguiente retorna un valor booleano si el nombre esta en los contactos o no.
#Entradas: Ninguna.
#Salidas: Un valor booleano true o false.
#Restricciones: Ninguna.
        
    def EstaContacto():
        global ListasDeContactos
        for i in ListasDeContactos:
            if i[0] == Name1.get():
                return True
        return False
    
#----------
#Funciones
#----------
#Descripción: El siguiente código se utiliza para agregar números a la variable global, los números que desea.
#Entradas: Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.

    def NumerosAgregar():
       global listaNumero
       listaNum=[]
       numero = Numer1.get()
       TipoNumero = Type1.get()
       try:
              if int(numero)>0:
                   listaNumero = listaNumero +[[TipoNumero,int(numero)]]
       except:
              PongaNumero()

    def prin():
       global listaCorreo 
       print(listaCorreo)

#----------
#Funciones
#----------
#Descripción: La siguiete función se utiliza para determinar si una cadena de string es un correo electronico.
#Entradas: Un string.
#Salidas: Un valor booleano.
#Restricciones: Sólo strings.
       
    def EsCorreo(correo):
       for i in correo:
              if i == "@":
                     return True
       return False

#----------
#Funciones
#----------
#Descripción: La siguinte función abre un mensaje de error indicandole que debe escribir un nombre.
#Entradas: Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.

    def PongaNombre():
       messagebox.showerror("Error","Error: Escriba un nombre")

#----------
#Funciones
#----------
#Descripción: La siguinte función abre un mensaje de error indicandole que debe escribir un correo.
#Entradas: Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.

    def PongaCorreo():
       messagebox.showerror("Error","Error: Escriba un correo")

#----------
#Funciones
#----------
#Descripción: La siguiente función agregar correos a la variable global, la cantidad que desee.
#Entradas: Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.
       
    def CorreosAgregar():
       global listaCorreo
       Mail = Correo.get()
       TipoCorreo = TypeCorreo.get()
       if EsCorreo(Mail):
              listaCorreo = listaCorreo + [[TipoCorreo,Mail]]
       else:
              PongaCorreo()
    def MensajeDeNoEsta():
        messagebox.showerror("Error","El contacto ya esta registrado, escriba otro")
#----------
#Funciones
#----------
#Descripción: La siguiente función agrega el contacto a la variable global cocatenando las listas y los valores del contacto y la información suministrada.
#Entradas: Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.

    def AgregarContactos():
       global ListasDeContactos,imagen,sonido,listaNumero,listaCorreo,ListaNotasExtras,sonido
       if EstaContacto() == False:
           nombre = Name1.get() #Recoge el valor de la variable.
           DireccionCasa = DireccionC1.get() #Recoge el valor de la variable.
           DireccionEstudio = DireccionE1.get() #Recoge el valor de la variable.
           DireccionTrabajo = DireccionT1.get() #Recoge el valor de la variable.
           if nombre == "":
               return PongaNombre()
           if ContarLetras(nombre) > 50:
               return ErrorNombreMuyLargo()
           if ContarLetras(DireccionCasa) > 50:
               return ErrorNombreMuyLargo()
           if ContarLetras(DireccionEstudio) > 50:
               return ErrorNombreMuyLargo()
           if ContarLetras(DireccionTrabajo) > 50:
               return ErrorNombreMuyLargo()
           else:
               ListasDeContactos = [[nombre,imagen,TuplaModo(listaNumero),listaCorreo,sonido,DireccionCasa,DireccionEstudio,DireccionTrabajo,ListaNotasExtras]]+ListasDeContactos
               sonido = ["Silencio"] #Se le asigna el default de sonido
               ventana.withdraw() #Cierra la ventana
               listaNumero=[] #Al variable global se le asigna una lista vacía.
               listaCorreo=[] #Al variable global se le asigna una lista vacía.
               ListaNotasExtras=[] #Al variable global se le asigna una lista vacía.
               print(ListasDeContactos)
               Principal()
       else:
            return MensajeDeNoEsta()
        
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Pantalla de Agregar o ventana de agregar
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    ventana = Toplevel(celular) #Se crea una ventana.
    ventana.title("DContact") #Titulo de la ventana.
    icono1 = ventana.iconbitmap("guia-telefonica.ico") #Icono de la ventana.
    no = PhotoImage(file = "error.gif") #A la imagen de equis o no se le asigna a la variable no.
    si = PhotoImage(file = "exito.gif") #A la imagen de check se le asigna a la variable si.
    Notas = PhotoImage(file = "contrato.gif") #A la imagen se le asigna a la variable.
    Sonido = PhotoImage(file = "anillo.gif") #A la imagen se le asigna a la variable.
    ImagenUsuario = PhotoImage(file = "camara-de-fotos.gif") #A la imagen se le asigna a la variable.
    LlamadaYa = PhotoImage(file = "llamada-telefonica.gif") #A la imagen se le asigna a la variable.
    CorreoYa = PhotoImage(file = "correo.gif") #A la imagen se le asigna a la variable.
    ventana.geometry("305x550") #Tamano de la ventana.
    ventana.maxsize(305, 550) #El tamano máximo que se puede agrandar o minimizar la pantalla.
    ventana.config(bg="RoyalBlue4") #Configura el color de la ventana.
    botonSi = Button(ventana,image = si,command = AgregarContactos,bg = "RoyalBlue4",relief = FLAT).place(x=70,y=480) #Se le asigna al boton a la variable
    botonNo = Button(ventana,image = no,command = Cerrar,bg = "RoyalBlue4",relief = FLAT).place(x=200,y=480) #Se le asigna al boton a la variable
    botonSonido = Button(ventana,command = VentanaSonido,image = Sonido,bg = "RoyalBlue4",relief = FLAT).place(x=90,y=90) #Se le asigna al boton a la variable
    botonNotas = Button(ventana,command = VentanaNotasExtras,image = Notas,bg = "RoyalBlue4",relief = FLAT).place(x=140,y=90) #Se le asigna al boton a la variable
    botonImagenUsuario = Button(ventana,command = VentanaImagenes,image = ImagenUsuario,bg = "RoyalBlue4",relief = FLAT).place(x=190,y=90) #Se le asigna al boton a la variable
    EtiquetaContacto = Label(ventana,bg = "light sea green",width = 50,height = 4).place(x=0,y=1) #Se le asigna una etiqueta a la variable.
    TextoAñadir = Label(ventana,text = "Añadir",fg = "white",relief = FLAT,bg = "light sea green",font = ("ms sans Serif",12,"bold")).place(x=120,y=25) #Se le asigna una etiqueta a la variable.
    EtiquetaNombre = Label(ventana,text="Nombre",fg="white",bg="RoyalBlue4",width=50,height=4,relief=FLAT,font=("ms sans Serif",10,"bold")).place(x=-150,y=130) #Se le asigna una etiqueta a la variable.
    Name1 = StringVar() #Se le asigna el valor de string a la variable.
    EspacioNombre = Entry(ventana,textvariable = Name1,fg = "black",bg = "white",width = 15,font = ("arial",10,"bold")).place(x=120,y=155) #Se le asigna a la variable un campo de texto.
    EtiquetaNumero = Label(ventana,text = "Número",fg = "white",bg = "RoyalBlue4",width = 50,height = 4,relief = FLAT,font = ("ms sans Serif",10,"bold")).place(x=-150,y=180) #Se le asigna a la variable una etiqueta.
    Numer1 = StringVar() #Se le asigna el valor de string a la variable.
    EspacioNumero = Entry(ventana,textvariable=Numer1,fg="RoyalBlue4",bg="white",width=15,font=("arial",10,"bold")).place(x=120,y=205)
    Variable1 = StringVar() #Se le asigna el valor de string a la variable.
    Type1 = StringVar() #Se le asigna el valor de string a la variable.
    OptionNumero = ttk.Combobox(ventana,textvariable = Type1,values = ["Móvil","Casa","Trabajo","Fax","Otros"],width=3).place(x=255,y=205) #Se crea un boton de option y se lo asigna.
    EtiquetaCorreo = Label(ventana,text = "Correo",fg = "white",bg = "RoyalBlue4",width = 50,height = 5,relief = FLAT,font = ("ms sans Serif",10,"bold")).place(x=-150,y=230) #Se le asigna una etiqueta a la variable.
    Correo = StringVar() #Se le asigna el valor de string a la variable.
    EspacioCorreo = Entry(ventana,fg = "RoyalBlue4",textvariable = Correo,bg = "white",width = 15,font = ("arial",10,"bold")).place(x=120,y=255) #Se crea un campo de texto
    BotonNumeroYa = Button(ventana,command = NumerosAgregar,image = LlamadaYa,bg = "RoyalBlue4",relief = FLAT).place(x=5,y=200) #Se crea un boton.
    TypeCorreo = StringVar() #Se le asigna el valor de string a la variable.
    OptionCorreo = ttk.Combobox(ventana,textvariable = TypeCorreo,values = ["Personal","Trabajo","Otros"],width = 3).place(x=255,y=255) #Se crea un boton de option y se lo asigna.
    BotonCorreoYa = Button(ventana,command = CorreosAgregar,image = CorreoYa,bg = "RoyalBlue4",relief = FLAT).place(x=5,y=255) #Se crea un boton y se lo asigna.
    EtiquetaDireccionCasa = Label(ventana,text = "Domicilio",fg = "white",bg = "RoyalBlue4",width = 50,height = 4,relief = FLAT,font = ("ms sans Serif",10,"bold")).place(x=-150,y=280)#Se le asigna una etiqueta a la variable.
    DireccionC1 = StringVar() #Se le asigna el valor de string a la variable.
    EspacioDireccionCasa = Entry(ventana,textvariable = DireccionC1,fg = "RoyalBlue4",bg = "white",width = 15,font = ("arial",10,"bold")).place(x=120,y=305)#Se le asigna un campo de texto a la variable.
    EtiquetaDireccionEstudio = Label(ventana,text = "Estudio",fg = "white",bg = "RoyalBlue4",width = 50,height = 4,relief = FLAT,font = ("ms sans Serif",10,"bold")).place(x=-150,y=330)#Se le asigna una etiqueta a la variable.
    DireccionE1 = StringVar() #Se le asigna el valor de string a la variable.
    EspacioDireccionEstudio = Entry(ventana,textvariable = DireccionE1,fg = "RoyalBlue4",bg = "white",width = 15,font = ("arial",10,"bold")).place(x=120,y=355) #Se le asigna un campo de texto a la variable.
    EtiquetaDireccionTrabajo = Label(ventana,text = "Trabajo",fg = "white",bg = "RoyalBlue4",width = 50,height = 4,relief = FLAT,font = ("ms sans Serif",10,"bold")).place(x=-150,y=380)#Se le asigna una etiqueta a la variable.
    DireccionT1 = StringVar() #Se le asigna el valor de string a la variable.
    EspacioDireccionTrabajo = Entry(ventana,textvariable = DireccionT1,fg = "RoyalBlue4",bg = "white",width = 15,font = ("arial",10,"bold")).place(x=120,y=405) #Se le agrega a la pantalla un espacio para digitar la dirrecion del trabajo.
    ventana.mainloop() #La ventana espera hasta que el usuario digite algo.

#----------
#Funciones
#----------
#Descripción: La siguiente función agrega radiobutton a la pantalla dependiendo de los valores que le suministre a la entrada.
#Entradas: Tres strings y un entero.
#Salidas: Ninguna.
#Restricciones: Ninguna.
        
def InsertarRadioButton(numero,ventana,texto,IntString):
    num1 = 0
    num2 = numero 
    while num != numero:
        Radiobutton(ventana, text=texto, variable=IntString,value=num).pack()
        num1= num1+1
        num2=num2-1

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Ventana Sonido
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Descripción: El siguiente código crea la pantalla secundario del App Contactos, la ventana de sonido.
#Entradas: Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.


def VentanaSonido():
       
#----------
#Funciones
#----------
#Descripción: La siguiente funcion accede al sistema operativo y encontrar el archivo .wav y reproducirlo.
#Entradas: Ninguna.
#Salidas: Ninguna
#Restricciones: Ninguna.
       
    def ZeldaSong():
        os.system("start C:\zelda_theme.wav")#Accede o reproduce el sonido

#----------
#Funciones
#----------
#Descripción: La siguiente funcion accede al sistema operativo y encontrar el archivo .wav y reproducirlo.
#Entradas: Ninguna.
#Salidas: Ninguna
#Restricciones: Ninguna.

    def Beethoven():
        os.system("start C:\Beethoven-Fur_Elise.wav")#Accede o reproduce el sonido

#----------
#Funciones
#----------
#Descripción: La siguiente funcion accede al sistema operativo y encontrar el archivo .wav y reproducirlo.
#Entradas: Ninguna.
#Salidas: Ninguna
#Restricciones: Ninguna.

    def Beethoven2():
        os.system("start C:\Sinfonia9.wav")#Accede o reproduce el sonido

#----------
#Funciones
#----------
#Descripción: La siguiente funcion accede al sistema operativo y encontrar el archivo .wav y reproducirlo.
#Entradas: Ninguna.
#Salidas: Ninguna
#Restricciones: Ninguna.
        
    def Mario():
        os.system("start C:\mario_theme_song.wav")#Accede o reproduce el sonido

#----------
#Funciones
#----------
#Descripción: La siguiente funcion accede al sistema operativo y encontrar el archivo .wav y reproducirlo.
#Entradas: Ninguna.
#Salidas: Ninguna
#Restricciones: Ninguna.
        
    def BeethovenMoonlight():
        os.system("start C:\BeethovenMoonlight.wav")#Accede o reproduce el sonido 

#----------
#Funciones
#----------
#Descripción: La siguiente funcion muestra un mensaje de información diciendo que el sonido ha sido guardado en la ventana de sonido.
#Entradas: Ninguna.
#Salidas: Ninguna
#Restricciones: Ninguna.
        
    def InfoSonido():
        messagebox.showinfo("Info","El sonido ha sido guardado")#Aparece una ventana de informacion 

#----------
#Funciones
#----------
#Descripción: La siguiente funcion muestra un mensaje de error en la ventana de sonido.
#Entradas: Ninguna.
#Salidas: Ninguna
#Restricciones: Ninguna.
        
    def ErrorToqueUnSonido():
        messagebox.showerror("Error","Seleccione un sonido")#Mensaje de error para seleccionar un sonido.

#----------
#Funciones
#----------
#Descripción: La siguiente funcion cuando el usuario da aceptar puede retornar un mensaje de error, informacion o cerrar la ventana en la ventana de sonido.
#Entradas: Ninguna.
#Salidas: Ninguna
#Restricciones: Ninguna.
        
    def AceptarSonido():
        global sonido #Utiliza la variable global sonido
        Variable=var.get() #Recoge el valor de la Variable.
        if Variable == 1:
            sonido=["zelda_theme.wav"]
            InfoSonido() #Se abre la ventana de información.
            VentanaSonido.withdraw()
        if Variable == 2:
            sonido=["mario_theme_song.wav"]
            InfoSonido() #Se abre la ventana de información.
            VentanaSonido.withdraw()
        if Variable == 3:
            sonido=["Beethoven-Fur_Elise.wav"]
            InfoSonido() #Se abre la ventana de información.
            VentanaSonido.withdraw()
        if Variable == 4:
            sonido=["Sinfonia9.wav"]
            InfoSonido() #Se abre la ventana de información.
            VentanaSonido.withdraw()
        if Variable == 5:
            sonido=["BeethovenMoonlight.wav"]
            InfoSonido() #Se abre la ventana de información.
            VentanaSonido.withdraw()
        if Variable == 0:
            return ErrorToqueUnSonido()

#----------
#Funciones
#----------
#Descripción: La siguiente función cierra la ventana de sonido.
#Entradas: Ninguna.
#Salidas: Ninguna
#Restricciones: Ninguna.

    def CerrarVentanaSonido():
        global sonido
        sonido=["Silencio"]
        VentanaSonido.withdraw()

#----------------------------------------------------------------
#Ventana de Sonido
#----------------------------------------------------------------
#Descripción: Ventana de sonido.
#Entradas: Ninguna.
#Salidas: Ninguna
#Restricciones: Ninguna.
        
    VentanaSonido = Toplevel(celular) #Se crea una ventana.
    VentanaSonido.title("DContact") #Titulo de la ventana.
    icono = VentanaSonido.iconbitmap("guia-telefonica.ico") #Icono de la ventana.
    VentanaSonido.geometry("310x450") #Tamano de la ventana.
    VentanaSonido.maxsize(310,550) #El tamano máximo que se puede agrandar o minimizar la pantalla.
    VentanaSonido.config(bg = "RoyalBlue4") #Configura el color de la ventana.
    no = PhotoImage(file = "error.gif") #A la imagen de equis o no se le asigna a la variable no.
    si = PhotoImage(file = "exito.gif") #A la imagen de check se le asigna a la variable si.
    EtiquetaSonido = Label(VentanaSonido,bg="light sea green",width=50,height=4).place(x=0,y=1) #Se le asigna una etiqueta a la variable.
    TextoSonido = Label(VentanaSonido,text="Sonidos",fg="white",relief=FLAT,bg="light sea green",font=("ms sans Serif",12,"bold")).place(x=110,y=25) #Se le asigna una etiqueta a la variable.
    var=IntVar() #Se le asigna una variable de tipo entero.
    RadioB1 = Radiobutton(VentanaSonido,bg = "RoyalBlue4",fg="white",text="Zelda Theme",variable=var,value=1,anchor=W,font=("ms sans Serif",10,"bold"),command=ZeldaSong).place(x=85,y=100) #Se crea un radiobutton
    RadioB2 = Radiobutton(VentanaSonido,bg = "RoyalBlue4",fg="white",text="Mario Theme",variable=var,value=2,anchor=W,font=("ms sans Serif",10,"bold"),command=Mario).place(x=85,y=150) #Se crea un radiobutton
    RadioB3 = Radiobutton(VentanaSonido,bg = "RoyalBlue4",fg="white",text="Beethoven Fur Elise",variable=var,value=3,anchor=W,font=("ms sans Serif",10,"bold"),command=Beethoven).place(x=85,y=200) #Se crea un radiobutton
    RadioB4 = Radiobutton(VentanaSonido,bg = "RoyalBlue4",fg="white",text="Beethoven Sinfonía 9",variable=var,value=4,anchor=W,font=("ms sans Serif",10,"bold"),command=Beethoven2).place(x=85,y=250) #Se crea un radiobutton
    RadioB5 = Radiobutton(VentanaSonido,bg = "RoyalBlue4",fg="white",text="Beethoven Moonlight",variable=var,value=5,anchor=W,font=("ms sans Serif",10,"bold"),command=BeethovenMoonlight).place(x=85,y=300) #Se crea un radiobutton
    botonSi=Button(VentanaSonido,image=si,bg="RoyalBlue4",relief=FLAT,command=AceptarSonido).place(x=70,y=380) #Se crea el boton de aceptar.
    botonNo=Button(VentanaSonido,image=no,bg="RoyalBlue4",relief=FLAT,command=CerrarVentanaSonido).place(x=200,y=380) #Se crea el boton de no o cancelar.
    VentanaSonido.mainloop() #Espera hasta que el usuario interactue con la pantalla.

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Ventana de Consultar
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Descripción: Ventana de Consultar.
#Entradas: Ninguna.
#Salidas: Ninguna
#Restricciones: Ninguna.

def Consultar():
    global NameConsultar #Utiliza la variable global NameConsultar

#----------
#Funcion
#----------
#Descripción: La siguiente función retorna el string o nombre del sonido, buscando en la variable global.
#Entradas: Ninguna.
#Salidas: Un string.
#Restricciones: Ninguna.
    
    def Sonido():
        global ListasDeContactos,NameConsultar
        for i in ListasDeContactos:
            if i[0] == NameConsultar:
                   print(i[4][0])
                   return i[4][0]
#----------
#Funcion
#----------
#Descripción: La siguiente función retorna el string o nombre de la imagen, buscando en la variable global.
#Entradas: Ninguna.
#Salidas: Un string.
#Restricciones: Ninguna.
              
    def Imagen():
        global ListasDeContactos,NameConsultar
        for i in ListasDeContactos:
            if i[0] == NameConsultar:
                   print(i[1][0])
                   return i[1][0]

#----------
#Funcion
#----------
#Descripción: La siguiente función retorna el string o nombre del sonido, dependiendo del nombre del archivo que se le de en la entrada.
#Entradas: Un string.
#Salidas: Un string.
#Restricciones: Sólo strings.

    def CualSonido(nombre):
        
        if nombre == "zelda_theme.wav":
            return "Zelda Theme"
        if nombre == "mario_theme_song.wav":
            return "Mario Theme"
        if nombre == "Beethoven-Fur_Elise.wav":
            return "Beethoven F."
        if nombre == "Sinfonia9.wav":
            return "Beethoven S."
        if nombre == "BeethovenMoonlight.wav":
            return "Beethoven M."
        if nombre == "Silencio":
            return "Silencio"
               
#----------
#Funcion
#----------
#Descripción: La siguiente función inserta etiquetas en la pantalla de consultar de las datos extras.
#Entradas: Un string.
#Salidas: Ninguna.
#Restricciones: Sólo strings y nombres que existen en la variable global o registrados.
     
    def Intente(nombre):
        global ListasDeContactos
        for i in ListasDeContactos:
            if i[0] == nombre:
                if i[8] != []:
                    if i[8][0][1] != "" or i[8] != []:
                        Label(frameDeCanvas4,anchor=W,fg = "black",text = "Notas", font = ("ms sans Serif",10,"bold")).grid(row=1,column=1)
                        Label(frameDeCanvas4,anchor=NW,fg = "black",text = i[8][0][1],font = ("ms sans Serif",10,"bold")).grid(row=1,column=2)
                    if i[8][1][1] != "" or i[8] != []:
                        Label(frameDeCanvas4,anchor=W,fg="black",text="Acerca de la familia:",font=("ms sans Serif",10,"bold")).grid(row=2,column=1)
                        Label(frameDeCanvas4,anchor=W,fg="black",text= i[8][1][1],font=("ms sans Serif",10,"bold")).grid(row=2,column=2)
                    if i[8][2][1] != "" or i[8] != []:
                        Label(frameDeCanvas4,anchor=W,fg="black",text="Profesión" ,font=("ms sans Serif",10,"bold")).grid(row=3,column=1)
                        Label(frameDeCanvas4,anchor=NW,fg="black",text=i[8][2][1],font=("ms sans Serif",10,"bold")).grid(row=3,column=2)
                    if i[8][3][1] != "" or i[8] != []:
                        Label(frameDeCanvas4,anchor=W,fg="black",text="Cumpleaños" ,font=("ms sans Serif",10,"bold")).grid(row=4,column=1)
                        Label(frameDeCanvas4,anchor=NW,fg="black",text=i[8][3][1],font=("ms sans Serif",10,"bold")).grid(row=4,column=2)
                    if i[8][4][1] != "" or i[8] != []:
                        Label(frameDeCanvas4,anchor=W,fg="black",text="Aniversario",font=("ms sans Serif",10,"bold")).grid(row=5,column=1)
                        Label(frameDeCanvas4,anchor=NW,fg="black",text= i[8][4][1],font=("ms sans Serif",10,"bold")).grid(row=5,column=2)
                    if i[8][5][1] != "" or i[8] != []:
                        Label(frameDeCanvas4,anchor=W,fg="black",text="Inicio de Trabajo",font=("ms sans Serif",10,"bold")).grid(row=6,column=1)
                        Label(frameDeCanvas4,anchor=NW,fg="black",text=i[8][5][1],font=("ms sans Serif",10,"bold")).grid(row=6,column=2)
                    if i[8][6][1] != "" or i[8] != []:
                        Label(frameDeCanvas4,anchor=W,fg="black",text="Dirección de Trabajo" ,font=("ms sans Serif",10,"bold")).grid(row=7,column=1)
                        Label(frameDeCanvas4,anchor=NW,fg="black",text=i[8][6][1],font=("ms sans Serif",10,"bold")).grid(row=7,column=2)
                    if i[8][7][1] != "" or i[8] != []:
                        Label(frameDeCanvas4,anchor=W,fg="black",text="Entretenimiento" ,font=("ms sans Serif",10,"bold")).grid(row=8,column=1)
                        Label(frameDeCanvas4,anchor=NW,fg="black",text=i[8][7][1],font=("ms sans Serif",10,"bold")).grid(row=8,column=2)
                    if i[8][8][1] != "" or i[8] != []:
                        Label(frameDeCanvas4,anchor=W,fg="black",text="Deporte" ,font=("ms sans Serif",10,"bold")).grid(row=9,column=1)
                        Label(frameDeCanvas4,anchor=NW,fg="black",text=i[8][8][1],font=("ms sans Serif",10,"bold")).grid(row=9,column=2)

#----------
#Funcion
#----------
#Descripción: La siguiente función agrega los correos que existen asociados al nombre registrados en los contactos.
#Entradas: Un string.
#Salidas: Ninguna
#Restricciones: Sólo strings y nombres registrados.
                        
    def AgregarCorreos(nombre):
        global ListasDeContactos
        fila1=1
        for i in ListasDeContactos:
            if i[0] == nombre:
                fila2=1
                for j in i[2]:
                    Label(frameDeCanvas2,fg="black",text=j[0],font=("arial",10,"bold")).grid(row=fila2,column=1)
                    Label(frameDeCanvas2,fg="black",text=j[1],font=("arial",10,"bold")).grid(row=fila2,column=2)
                    fila2=fila2+1
                fila3=1
                for l in i[3]:
                    Label(frameDeCanvas1,fg="black",text=l[0],font=("arial",10,"bold")).grid(row=fila3,column=1)
                    Label(frameDeCanvas1,fg="black",text=l[1],font=("arial",10,"bold")).grid(row=fila3,column=2)
                    fila3=fila3+1
                #Llama a la función
                Intente(nombre)
                #Crea Labels
                Label(fram3,fg="black",text="Dirección Domicilio",font=("arial",10,"bold")).grid(row=1,column=1)
                Label(fram3,fg="black",text="Dirección Estudio",font=("arial",10,"bold")).grid(row=2,column=1)
                Label(fram3,fg="black",text="Dirección Trabajo",font=("arial",10,"bold")).grid(row=3,column=1)
                Label(fram3,fg="black",text=i[5],font=("arial",10,"bold")).grid(row=1,column=2)
                Label(fram3,fg="black",text=i[6],font=("arial",10,"bold")).grid(row=2,column=2)
                Label(fram3,fg="black",text=i[7],font=("arial",10,"bold")).grid(row=3,column=2)

#----------
#Funcion
#----------
#Descripción: La siguiente función dependiendo del evento que ejecuta el usuario sobre un scrollbar se va a mover.
#Entradas: Un evento o string.
#Salidas: Ninguna
#Restricciones: Ninguno.
                
    def EventosConsultar(eventos):
        canvasConsultar.configure(scrollregion=canvasConsultar.bbox("all"),width=250,height=280)

#----------
#Funcion
#----------
#Descripción: La siguiente función dependiendo del evento que ejecuta el usuario sobre un scrollbar se va a mover.
#Entradas: Un evento o string.
#Salidas: Ninguna
#Restricciones: Ninguno.
        
    def EventosConsultar2(eventos):
        canvasConsultar2.configure(scrollregion=canvasConsultar2.bbox("all"),width=250,height=280)

#----------
#Funcion
#----------
#Descripción: La siguiente función dependiendo del evento que ejecuta el usuario sobre un scrollbar se va a mover.
#Entradas: Un evento o string.
#Salidas: Ninguna
#Restricciones: Ninguno.

    def EventosConsultar4(eventos):
        canvasConsultar4.configure(scrollregion=canvasConsultar4.bbox("all"),width=250,height=280)

#----------
#Funcion
#----------
#Descripción: La siguiente función cierra la ventana de consulta.
#Entradas: Ninguno.
#Salidas: Ninguna
#Restricciones: Ninguno.
        
    def CerrarConsultar():
        ventanaConsulta.withdraw()
        
#-------------------------------
#Código de la pantalla consultar
#-------------------------------
#Descripción: La siguiente código abre la pantalla de consultar.
#Entradas: Ninguno.
#Salidas: Ninguna
#Restricciones: Ninguno.
    global NameConsultar
    
    ventanaConsulta = Toplevel(celular) #Se crea una ventana.
    ventanaConsulta.title("DContact") #Titulo de la ventana.
    icono = ventanaConsulta.iconbitmap("guia-telefonica.ico") #Icono de la ventana.
    ventanaConsulta.geometry("310x700") #Tamano de la ventana.
    ventanaConsulta.maxsize(310,550) #El tamano mÃ¡ximo que se puede agrandar o minimizar la pantalla.
    ventanaConsulta.config(bg = "RoyalBlue4") #Configura el color de la ventana.
    ImagenDeUsuario = PhotoImage(file = Imagen()) #Le asigna una imagen a la variable.
    EtiquetaConsulta = Label(ventanaConsulta,bg = "light sea green",width = 50,height = 4).place(x=0,y=1) #Se le asigna una etiqueta a la variable.
    EtiquetaImagen = Label(ventanaConsulta,bg = "light sea green",image = ImagenDeUsuario,relief = FLAT).place(x=250,y=20) #Se le asigna una etiqueta a la variable.
    TextoConsulta = Label(ventanaConsulta,text = NameConsultar,fg = "white",relief = FLAT,bg = "light sea green",font = ("ms sans Serif",11,"bold")).place(x=7,y=25) #Se le asigna una etiqueta a la variable.
    TextoSonido = Label(ventanaConsulta,text=CualSonido(Sonido()),fg = "white",relief = FLAT,bg="light sea green",font = ("ms sans Serif",11,"bold")).place(x=150,y=28) #Se le asigna una etiqueta a la variable.
    notebook = ttk.Notebook(ventanaConsulta,height = 306,width = 290) #Sea un nootebook dentro de la ventana.
    notebook.place(x=7,y=90) #Ubica el nootebook en esa posición x,y.
    Atras = PhotoImage(file="Atras.gif") #Se llama a la imagen.
    BotonAtras = Button(ventanaConsulta,command=CerrarConsultar,bg="RoyalBlue4",image=Atras,relief=FLAT).place(x=130,y=480) #Botón de atrás.
        
    fram1 = Frame(notebook,relief = GROOVE,bd = 1)#Se crea ventanillas para el nootebook o cuaderno
    fram1.pack(fill=BOTH, expand = True) #Se empaca 
    canvasConsultar = Canvas(fram1,width = 500,height = 200) #Se crea una ventana dentro del fram1
    frameDeCanvas1 = Frame(canvasConsultar) #Se crea una ventana dentro del canvas.
    Barra1=Scrollbar(fram1,orient = "vertical",command = canvasConsultar.yview) #Se crea un scrollbar.
    canvasConsultar.configure(yscrollcommand = Barra1.set) #Se configura el scrollbar.
    Barra1.pack(side = "right",fill = "y") #Se empaca el scrollbar.
    canvasConsultar.pack(side = "left") #Se empaca el canvas o ventana creado.
    canvasConsultar.create_window((0,0),window = frameDeCanvas1,anchor = 'nw') #Se crea una ventana en el canvas.
    frameDeCanvas1.bind("<Configure>",EventosConsultar) #En la ventana del canvas espera hasta que ocurra un evento y llama a la función EventosConsultar.

    fram2 = Frame(notebook,relief = GROOVE,bd = 1) #Se crea ventanillas para el nootebook o cuaderno
    fram2.place(x=10,y=10)#Lo ubica en el eje x a 10 pxeles y en el eje y a 10 pixeles.
    canvasConsultar2 = Canvas(fram2,width = 500,height = 200)#Se crea una ventana dentro del fram1
    frameDeCanvas2 = Frame(canvasConsultar2)#Se crea una ventana dentro del canvas.
    Barra2=Scrollbar(fram2,orient = "vertical",command = canvasConsultar2.yview)#Se crea un scrollbar.
    canvasConsultar2.configure(yscrollcommand = Barra2.set)#Se configura el scrollbar.
    Barra2.pack(side = "right",fill = "y") #Se empaca el scrollbar.
    canvasConsultar2.pack(side = "left") #Se empaca el canvas o ventana creado.
    canvasConsultar2.create_window((0,0),window = frameDeCanvas2,anchor = 'nw') #Se crea una ventana en el canvas.
    frameDeCanvas2.bind("<Configure>",EventosConsultar2)  #En la ventana del canvas espera hasta que ocurra un evento y llama a la función EventosConsultar.

    fram3 = Frame(notebook,relief = GROOVE,bd = 1) #Se crea ventanillas para el nootebook o cuaderno
    fram3.place(x=10,y=10)#Lo ubica en el eje x a 10 pxeles y en el eje y a 10 pixeles.

    fram4 = Frame(notebook,relief = GROOVE,bd = 1) #Se crea una etiqueta o Tab.
    fram4.pack(fill = BOTH, expand = True) #Se empaca la ventana creado.
    canvasConsultar4 = Canvas(fram4,width = 500,height = 200) #Se crea un canvas dentro de fram4.
    frameDeCanvas4 = Frame(canvasConsultar4) #Se crea una ventana dentro de un canvas.
    Barra4 = Scrollbar(fram4,orient = "vertical",command = canvasConsultar4.yview) #Se crea un scrollbar.
    canvasConsultar4.configure(yscrollcommand = Barra4.set) #Se configura el scrollbar.
    Barra4.pack(side = "right",fill = "y") #Se empaca el scrollbar.
    canvasConsultar4.pack(side = "left") #Se empaca el canvas o ventana creado.
    canvasConsultar4.create_window((0,0),window = frameDeCanvas4,anchor = 'nw') #Se crea una ventana en el canvas.
    frameDeCanvas4.bind("<Configure>",EventosConsultar4) #En la ventana del canvas espera hasta que ocurra un evento y llama a la función EventosConsultar.

    tab2 = notebook.add(fram2,text = "Números",padding = 10) #Se le agrega al cuaderno una etiqueta y se le asigna la imagen de consultar.
    tab1 = notebook.add(fram1,text = "Correos",padding = 10) #Se le agrega al cuaderno una etiqueta y se le asigna la imagen de Contactos.
    tab3 = notebook.add(fram3,text = "Direcciones",padding = 10) #Se le agrega al cuaderno una etiqueta y se le asigna la imagen de eliminar. 
    tab4 = notebook.add(fram4,text = "Notas Extras",padding = 10) #Se le agrega al cuaderno una etiqueta y se le asigna la imagen de modificar.

    AgregarCorreos(NameConsultar) #Llama a la función.
    ventanaConsulta.mainloop() #Espera hasta que el usuario haga un evento.  

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Pantalla o ventana modificar
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Descripción: La siguiente código abre la pantalla de modificar.
#Entradas: Ninguno.
#Salidas: Ninguna
#Restricciones: Ninguno.

#----------
#Función 
#----------
#Descripción: La siguiente función recoge los datos de la variable NombreAModificar
#Entradas: Ninguno.
#Salidas: Ninguna
#Restricciones: Ninguno.
    
def EsteNombreSeVaAModificar():
    global NombreAModificar
    NombreAModificar=NombreModificar.get()
    

def VentanaModificar2():

#Descripción: El siguiente código se utiliza para agregar números a la variable global, los números que desea.
#Entradas: Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.

    def NumerosAgregar():
       global listaNumero
       listaNum=[]
       numero = Numer1.get()
       TipoNumero = Type1.get()
       try:
              if int(numero)>0:
                   listaNumero = listaNumero +[[TipoNumero,int(numero)]]
       except:
              PongaNumero()

#Descripción: La siguiete función se utiliza para determinar si una cadena de string es un correo electronico.
#Entradas: Un string.
#Salidas: Un valor booleano.
#Restricciones: Sólo strings.
       
    def EsCorreo(correo):
       for i in correo:
              if i == "@":
                     return True
       return False

#Descripción: La siguinte función abre un mensaje de error indicandole que debe escribir un correo.
#Entradas: Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.

    def PongaCorreo():
       messagebox.showerror("Error","Error: Escriba un correo")

#Descripción: La siguiente función agregar correos a la variable global, la cantidad que desee.
#Entradas: Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.
       
    def CorreosAgregar():
       global listaCorreo
       Mail = Correo.get()
       TipoCorreo = TypeCorreo.get()
       if EsCorreo(Mail):
              listaCorreo = listaCorreo + [[TipoCorreo,Mail]]
       else:
              PongaCorreo()

#Descripción: La siguiente función agregar los números que se desea agregar a la variable global y el nombre asociado.
#Entradas: Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.
              
    def ModificarNumeros():
        global ListasDeContactos,listaNumero,NombreAModificar
        print(NombreAModificar)
        print(listaNumero)
        print(ListaDelContacto2())
        TuplaMode = TuplaModo(listaNumero) #Lo convierte en tuplas
        ListaDelContactoAModificarNumeros = ListaDelContacto2()[2] #Le asigna los números del contacto a modificar a la variable. 
        for i in TuplaMode:
            if i in ListaDelContactoAModificarNumeros:
                continue
            else:
                ListaDelContactoAModificarNumeros = ListaDelContactoAModificarNumeros + [i] #Se suma o se concatena a la varaible global.
        listaNumero = TuplaModo( ListaDelContactoAModificarNumeros) #Se lo asigna a la variable global
        
#Descripción: La siguiente función retorna el contacto que desea modificar.
#Entradas: Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.

    def ListaDelContacto2():
        global ListasDeContactos,NombreAModificar
        for i in ListasDeContactos:
            if i[0] == NombreAModificar[0]:
                return i

#Descripción: La siguiente función agregar los correos que se desea agregar a la variable global y el nombre asociado a tales correos.
#Entradas: Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.
              
    def ModificarCorreos():
        global ListasDeContactos, listaCorreo
        TuplaMode = TuplaModo(listaCorreo)
        ListaDeCorreosModificar = ListaDelContacto2()[3]
        for i in TuplaMode:
            if i in ListaDeCorreosModificar:
                continue
            else:
                ListaDeCorreosModificar = ListaDeCorreosModificar + [i]
        listaCorreo = ListaDeCorreosModificar

#Descripción: La siguiente función agregar los datos que no existen en los datos registrados.
#Entradas: Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.
        
    def Modifiquelo():
        global NombreAModificar,imagen,ListasDeContactos,sonido,ListaNotasExtras,listaCorreo #Utiliza la variable global
        
        ModificarNumeros() #Llama la función para agregar números
        ModificarCorreos() #Llama a la función para agregar correos extras.
        
        LaListaQueSeVaAModificar = ListaDelContacto2() #Llama a la función y le asigna lo que tiene 
        ListasDeContactos.remove(ListaDelContacto2())
        if imagen != LaListaQueSeVaAModificar[1] and imagen != []:
           LaListaQueSeVaAModificar[1]=imagen
        LaListaQueSeVaAModificar[2]=listaNumero
        LaListaQueSeVaAModificar[3] =listaCorreo
        if LaListaQueSeVaAModificar[4] != sonido and sonido != []:
            LaListaQueSeVaAModificar[4] = sonido
        LaListaQueSeVaAModificar[8]=ListaNotasExtras
        if LaListaQueSeVaAModificar[5] != DireccionC1.get() and DireccionC1.get() != "" and LaListaQueSeVaAModificar[5] !="":
            LaListaQueSeVaAModificar[5] =DireccionC1.get()
        if LaListaQueSeVaAModificar != DireccionE1.get() and DireccionE1.get() != "" and LaListaQueSeVaAModificar[6] !="":
            LaListaQueSeVaAModificar[6]=DireccionE1.get()
        if LaListaQueSeVaAModificar[7] != DireccionT1.get() and DireccionT1.get() != "" and LaListaQueSeVaAModificar[7] !="":
            LaListaQueSeVaAModificar[7] = DireccionT1.get()
        ListasDeContactos = [LaListaQueSeVaAModificar ]+ListasDeContactos #Utiliza la variable global
        print(ListasDeContactos)
        ventanaDeModificar.withdraw()
        Principal()

#Descripción: La siguiente función para cerrar ventanas.
#Entradas: Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.
        
    def Cancelar():
        ventanaDeModificar.withdraw()
        return Principal()

#--------------------------------------------------------------------------------------------------------------------------------------
#Ventana de Modificar
#--------------------------------------------------------------------------------------------------------------------------------------
        
    ventanaDeModificar = Toplevel(celular) #Se crea una ventana.
    ventanaDeModificar.title("DContact") #Titulo de la ventana.
    icono1 = ventanaDeModificar.iconbitmap("guia-telefonica.ico") #Icono de la ventana.
    global NumerosModificar #Utiliza la variable global 
    Notas = PhotoImage(file = "contrato.gif") #A la imagen se le asigna una variable.
    Sonido = PhotoImage(file = "anillo.gif") #A la imagen se le asigna una variable.
    ImagenUsuario = PhotoImage(file = "camara-de-fotos.gif") #A la imagen se le asigna una variable.
    LlamadaYa = PhotoImage(file = "llamada-telefonica.gif") #A la imagen se le asigna una variable.
    CorreoYa = PhotoImage(file = "correo.gif") #A la imagen se le asigna una variable.
    ventanaDeModificar.geometry("305x550") #Tamano de la ventana.
    ventanaDeModificar.maxsize(305, 550) #El tamano máximo que se puede agrandar o minimizar la pantalla.
    ventanaDeModificar.config(bg = "RoyalBlue4") #Configura el color de la ventana.
    no=PhotoImage(file = "error.gif") #A la imagen de equis o no se le asigna a la variable no.
    si=PhotoImage(file = "exito.gif") #A la imagen de check se le asigna a la variable si.
    botonSonido = Button(ventanaDeModificar,command = VentanaSonido,image = Sonido,bg = "RoyalBlue4",relief = FLAT).place(x=90,y=90) #Boton para poner sonido
    botonNotas = Button(ventanaDeModificar,command = VentanaNotasExtras,image = Notas,bg = "RoyalBlue4",relief = FLAT).place(x=140,y=90) #Boton para agregar notas extras.
    botonImagenUsuario = Button(ventanaDeModificar,command = VentanaImagenes,image = ImagenUsuario,bg = "RoyalBlue4",relief = FLAT).place(x=190,y=90) #Botobn para agregar una imagen.
    botonSi = Button(ventanaDeModificar,command = Modifiquelo,image = si,bg = "RoyalBlue4",relief = FLAT).place(x=70,y=480) #Boton de aceptar.
    botonNo = Button(ventanaDeModificar,command=Cancelar,image=no,bg="RoyalBlue4",relief=FLAT).place(x=200,y=480) #Boton de cancelar.
    Textomodificar = Label(ventanaDeModificar,text="Modificar",fg="white",relief=FLAT,bg="light sea green",font=("ms sans Serif",12,"bold")).place(x=110,y=25) #Se le asigna una etiqueta a la variable.

    EtiquetaContacto = Label(ventanaDeModificar,bg="light sea green",width=50,height=4).place(x=0,y=1) #Se le asigna una etiqueta a la variable.
    EtiquetaNumero = Label(ventanaDeModificar,text="Número",fg="white",bg="RoyalBlue4",width=50,height=4,relief=FLAT,font=("ms sans Serif",10,"bold")).place(x=-150,y=180) #Etiqueta de Número.
    Numer1 = StringVar() #Se le asigna a una variable el valor string.
    EspacioNumero = Entry(ventanaDeModificar,textvariable=Numer1,fg="RoyalBlue4",bg="white",width=15,font=("arial",10,"bold")).place(x=120,y=205) #Se le asigna el espacio a la variable.
    Variable1 = StringVar() #Se le asigna a una variable el valor string.
    Type1 = StringVar() #Se le asigna a una variable el valor string.
    OptionNumero = ttk.Combobox(ventanaDeModificar,textvariable=Type1,values=["Móvil","Casa","Trabajo","Fax","Otros"],width=3).place(x=255,y=205) #Se le asigna a la variable un Combobox
    EtiquetaCorreo = Label(ventanaDeModificar,text="Correo",fg="white",bg="RoyalBlue4",width=50,height=5,relief=FLAT,font=("ms sans Serif",10,"bold")).place(x=-150,y=230)#Se le asigna una etiqueta a la variable.
    Correo = StringVar() #Se le asigna a una variable el valor string.
    EspacioCorreo = Entry(ventanaDeModificar,fg="RoyalBlue4",textvariable=Correo,bg="white",width=15,font=("arial",10,"bold")).place(x=120,y=255) #Se le asigna el espacio a la variable.
    BotonNumeroYa = Button(ventanaDeModificar,command=NumerosAgregar,image=LlamadaYa,bg="RoyalBlue4",relief=FLAT).place(x=5,y=200)#Se le asigna un boton a la variable.
    TypeCorreo = StringVar() #Se le asigna a una variable el valor string.
    OptionCorreo = ttk.Combobox(ventanaDeModificar,textvariable=TypeCorreo,values=["Personal","Trabajo","Otros"],width=3).place(x=255,y=255) #Se le asigna a la variable un Combobox
    BotonCorreoYa = Button(ventanaDeModificar,command=CorreosAgregar,image=CorreoYa,bg="RoyalBlue4",relief=FLAT).place(x=5,y=255) #Se le asigna un boton a la variable.
    EtiquetaDireccionCasa = Label(ventanaDeModificar,text="Domicilio",fg="white",bg="RoyalBlue4",width=50,height=4,relief=FLAT,font=("ms sans Serif",10,"bold")).place(x=-150,y=280)#Se le asigna una etiqueta a la variable.
    DireccionC1 = StringVar() #Se le asigna a una variable el valor string.
    EspacioDireccionCasa = Entry(ventanaDeModificar,textvariable=DireccionC1,fg="RoyalBlue4",bg="white",width=15,font=("arial",10,"bold")).place(x=120,y=305)#Se le asigna el espacio a la variable.
    EtiquetaDireccionEstudio = Label(ventanaDeModificar,text="Estudio",fg="white",bg="RoyalBlue4",width=50,height=4,relief=FLAT,font=("ms sans Serif",10,"bold")).place(x=-150,y=330)#Se le asigna una etiqueta a la variable.
    DireccionE1 = StringVar() #Se le asigna a una variable el valor string.
    EspacioDireccionEstudio = Entry(ventanaDeModificar,textvariable=DireccionE1,fg="RoyalBlue4",bg="white",width=15,font=("arial",10,"bold")).place(x=120,y=355)#Se le asigna el espacio a la variable.
    EtiquetaDireccionTrabajo = Label(ventanaDeModificar,text="Trabajo",fg="white",bg="RoyalBlue4",width=50,height=4,relief=FLAT,font=("ms sans Serif",10,"bold")).place(x=-150,y=380)#Se le asigna una etiqueta a la variable.
    DireccionT1 = StringVar() #Se le asigna a una variable el valor string.
    EspacioDireccionTrabajo = Entry(ventanaDeModificar,textvariable=DireccionT1,fg="RoyalBlue4",bg="white",width=15,font=("arial",10,"bold")).place(x=120,y=405) #Se le agrega a la pantalla un espacio para digitar la dirrecion del trabajo.
    ventanaDeModificar.mainloop() 

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Pantalla principal de la aplicación contactos
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Descripción: La siguiente código abre la Pantalla principal de la aplicación contactos
#Entradas: Ninguno.
#Salidas: Ninguna
#Restricciones: Ninguno.

def Principal():

#Descripción: La siguiente funcion cierra la ventana principal.
#Entradas: Ninguno.
#Salidas: Ninguna
#Restricciones: Ninguno.
       def CerrarLaVentanaPrincipal():
              ventana1.withdraw()
    

#Descripción: La siguiente funcion retorna un mensaje de error en donde le pide que escriba el nombre.
#Entradas: Ninguno.
#Salidas: Ninguna
#Restricciones: Ninguno.
       
       def PongaNombre():
              messagebox.showerror("Error","Escriba un nombre")

#Descripción: La siguiente es una funcion en donde llama a otras funciones de mensajes de error o de informacion de la ventana de modificar.
#Entradas: Ninguno.
#Salidas: Ninguna
#Restricciones: Ninguno.

       def VentanaModificar():
              global NombreAModificar
              nombre = NombreModificar.get()
              if  nombre == "":
                     return PongaNombre()
              if Está(NombreModificar.get()):
                     NombreAModificar =[nombre]
                     return VentanaModificar2() 
              else:
                     return MensajeDeErrorNombres()
       NameConsultar=""

#Descripción: La siguiente es una funcion en donde llama a otras funciones de mensajes de error o de informacion de la ventana de consultar.
#Entradas: Ninguno.
#Salidas: Ninguna
#Restricciones: Ninguno.
       
       def VentanaConsultar():
              global NameConsultar
              nombre = NombreConsultar.get()
              if  nombre == "":
                     return PongaNombre()
              if Está(NombreConsultar.get()):
                     NameConsultar=nombre
                     return Consultar() 
              else:
                     return MensajeDeErrorNombres()

#Descripción: La siguiente es una funcion retorna un mensaje de error indicandole que escriba un numero.
#Entradas: Ninguno.
#Salidas: Ninguna
#Restricciones: Ninguno.
              
       def PongaNumero():
              messagebox.showerror("Error","Error: Escriba un número")
              
#Descripción: La siguiente es para eliminar un contacto de la variable global ListasDeContactos.
#Entradas: Ninguno.
#Salidas: Ninguna
#Restricciones: Ninguno.
              
       def Eliminar():
           global ListasDeContactos
           NewList=[]
           Name=NombreEliminar.get()
           for i in ListasDeContactos:
               if Name == i[0]:
                   continue
               else:
                   NewList=NewList+[i]
           ListasDeContactos=NewList
           print(ListasDeContactos)
           Clean()

#Descripción: La siguiente es una funcion en donde llama a otras funciones de mensajes de error o de informacion de la ventana de eliminar.
#Entradas: Ninguno.
#Salidas: Ninguna
#Restricciones: Ninguno.
              
       def VentanaDeEliminar():
              
              nombre = NombreEliminar.get()
              if  nombre == "":
                     return PongaNombre()
              if Está(NombreEliminar.get()):
                     return SeguroDeEliminar()
              else:
                     return MensajeDeErrorNombres()

#Descripción: La siguiente es una funcion abre una ventana de pregunta, preguntandole si esta seguro de eliminar o no el contacto.
#Entradas: Ninguno.
#Salidas: Ninguna
#Restricciones: Ninguno.
              
       def SeguroDeEliminar():
              variable = messagebox.askquestion("Estás seguro", "Estás seguro de eliminar a " + NombreEliminar.get())
              if variable == "yes":
                     return Eliminar()
              else:
                     return MensajeDeErrorNombres

#Descripción: La siguiente es una funcion es para agregarle los contactos al notebook.
#Entradas: Ninguno.
#Salidas: Ninguna
#Restricciones: Ninguno.
              
       def AgregarAlBookContacto():
           Alfabético()
           global ListasDeContactos #Utiliza la variable global
           cont=1
           l=0
           fila=1
           color=["light blue","cadet blue","khaki","beige"]
           cual=random.randint(0,3)
           for i in ListasDeContactos:
               Label(frameDeCanvas1,fg="black",text=i[0],bg=color[cual],font=("ms sans Serif",10,"bold")).grid(row=fila,column=1)
               imagen=PhotoImage(file=i[1][0])
               Image=Label(frameDeCanvas1,image=imagen,bg="light sea green")
               Image.image=imagen
               Image.grid(row=fila,column=0)
               cont=cont+1
               fila=fila+1
               l=l+1
               cual=random.randint(0,3)
               
#Descripción: La siguiente es una funcion es para limpiar la pantalla de contactos de la pantalla principal.
#Entradas: Ninguno.
#Salidas: Ninguna
#Restricciones: Ninguno.
               
       def Clean():
           fila=1
           for i in range(100):
               Label(frameDeCanvas1,bg="white",height=2,width=10).grid(row=fila,column=1)
               Label(frameDeCanvas1,bg="white",height=2,width=4).grid(row=fila,column=0)
               fila=fila+1
                  
#Descripción: La siguiente es para esperar hasta que usuario interactue con el scrollbar de la pantalla de canvas1.
#Entradas: Ninguno.
#Salidas: Ninguna
#Restricciones: Ninguno.
               
       def Eventos2(eventos):
           canvas2.configure(scrollregion=canvas2.bbox("all"),width=250,height=280)

#Descripción: La siguiente es para esperar hasta que usuario interactue con el scrollbar de la pantalla de canvas2.
#Entradas: Ninguno.
#Salidas: Ninguna
#Restricciones: Ninguno.

       def Eventos1(eventos):
           canvas1.configure(scrollregion=canvas1.bbox("all"),width=250,height=280)

       #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
       #Ventana Principal de la APP DContact
       #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
       #Descripción: El siguiente código crea la pantalla principal del App Contactos.
       #Entradas: Ninguna.
       #Salidas: Ninguna.
       #Restricciones: Ninguna.
              
       ventana1 = Toplevel(celular) #Se crea una ventana.
       ventana1.title("DContact") #Titulo de la ventana.
       icono = ventana1.iconbitmap("guia-telefonica.ico") #Icono de la ventana.
       ventana1.geometry("310x550") #Tamano de la ventana.
       ventana1.maxsize(310,550) #El tamano máximo que se puede agrandar o minimizar la pantalla.
       ventana1.config(bg = "RoyalBlue4") #Configura el color de la ventana.
       no = PhotoImage(file = "error.gif") #A la imagen de equis o no se le asigna a la variable no.
       si = PhotoImage(file = "exito.gif") #A la imagen de check se le asigna a la variable si.
       info = PhotoImage(file = "info.gif") #Se le asigna una imagen a la variable.
       Agregar = PhotoImage(file="Agregar.gif") #Se le asigna una imagen a la variable.
       ManualImagen = PhotoImage(file = "libro.gif") #Se le asigna una imagen a la variable.
       Cargar = PhotoImage(file = "repetir.gif") #Se le asigna una imagen a la variable.
       EtiquetaContacto = Label(ventana1,bg="light sea green",width=50,height=4).place(x=0,y=1) #Se le asigna una etiqueta a la variable.
       TextoContacto = Label(ventana1,text="Contactos",fg="white",relief=FLAT,bg="light sea green",font=("ms sans Serif",11,"bold")).place(x=7,y=25) #Se le asigna una etiqueta a la variable.
       botonAgregar = Button(ventana1,command=VentanaAgregar,image=Agregar,bg="light sea green",relief=FLAT).place(x=100,y=20) #Se le asigna un boton a una variable.
       botonManual = Button(ventana1,command=Manual,image=ManualImagen,bg="light sea green",relief=FLAT).place(x=200,y=20) #Se le asigna un boton a una variable.
       botonCargar = Button(ventana1,command=AgregarAlBookContacto,image=Cargar,bg="light sea green",relief=FLAT).place(x=250,y=20) #Se le asigna un boton a una variable.
       botonInfo = Button(ventana1,command=VentanaAcercaDe,image=info,bg="light sea green",relief=FLAT).place(x=150,y=20) #Se le asigna un boton a una variable.
       botonSi = Button(ventana1,image=si,bg="RoyalBlue4",relief=FLAT).place(x=70,y=480) #Se le asigna un boton a una variable.
       botonNo = Button(ventana1,image=no,command=CerrarLaVentanaPrincipal,bg="RoyalBlue4",relief=FLAT).place(x=200,y=480) #Se le asigna un boton a una variable.
       nbook = ttk.Notebook(ventana1,height=306,width=290) #Sea un nootebook dentro de la ventana.
       nbook.place(x=7,y=90) #Ubica el nootebook en esa posición x,y.
       frame1=Frame(nbook,relief=GROOVE,bd=1) #Se crea una ventana dentro del notebook
       frame1.pack(fill=BOTH, expand=True) #Se empaca la ventana.
       frame2=Frame(nbook,relief=GROOVE,bd=1) #Se crea una ventana dentro del notebook
       frame2.place(x=10,y=10) #Se empaca la ventana.
       frame3=Frame(nbook,relief=GROOVE,bd=1) #Se crea una ventana dentro del notebook
       frame3.place(x=10,y=10) #Se empaca la ventana.
       frame4 = Frame(nbook) #Se crea una etiqueta o Tab.
       frame4.pack(fill=BOTH, expand=True) #Se empaca la ventana.
       canvas = Canvas(frame1,bg="brown1", borderwidth=0) #Se crea una ventana dentro de la ventana contactos.
       ventanilla = ttk.Frame(canvas) #Se crea ua miniventana.
       canvas.pack(side = 'left', fill = 'both', expand=True) #Se empaca el Canvas.
       canvas1 = Canvas(frame2,width = 500,height = 200) #Se crea una ventana dentro de una ventana.
       frameDeCanvas1=Frame(canvas1) #Se crea una ventana dentro de una ventana dentro de una ventana.
       Barra1 = Scrollbar(frame2,orient = "vertical",command = canvas1.yview) #Se crea un scrollbar.
       canvas1.configure(yscrollcommand = Barra1.set) #Configura el scrollbar.
       Barra1.pack(side="right",fill="y") #El scrollbar se empaca y lo ubica en y.
       canvas1.pack(side="left") #El canvas se empaca.
       canvas1.create_window((0,0),window=frameDeCanvas1,anchor='nw') #Se crea una ventana dentro de la ventana.
       frameDeCanvas1.bind("<Configure>",Eventos1) #Espera a un evento del scrollbar.
       NombreConsultar = StringVar() #Se le asigna el valor string a la variable.
       EtiquetaConsultar  = Label(canvas,bg="brown1",text="Digite el nombre que desea consultar:",fg="white",font=("ms sans Serif",9,"bold")).place(x=30,y=60) #Se le asigna una etiqueta de texto a la variable.
       EspacioConsultar  = Entry(canvas,textvariable=NombreConsultar).place(x=70,y=120) #Se le asigna un campo de texto a la variable.
       BotonConsultar  = Button(canvas,text="Consultar",command=VentanaConsultar,relief=FLAT,fg="white",bg="deep sky blue").place(x=100,y=170)#Se le asigna un boton a la variable.
       canvas2 = Canvas(frame3, bg="brown1",borderwidth=0) #Se crea una ventana dentro de la ventana contactos.
       ventanilla2 = ttk.Frame(canvas2) #Se crea ua miniventana.
       canvas2.pack(side = 'left', fill = 'both', expand=True) #Se empaca el Canvas.
       canvas2.create_window((0, 0), window = ventanilla2, anchor = 'nw', tags = 'frame') #Se crea canvas un formato como una miniventana.
       NombreEliminar=StringVar() #Se le asigna el valor string a la variable.
       EtiquetaEliminar = Label(canvas2,bg="brown1",text="Digite el nombre que desea eliminar:",fg="white",font=("ms sans Serif",9,"bold")).place(x=30,y=60) #Se le asigna una etiqueta de texto a la variable.
       EspacioEliminar = Entry(canvas2,textvariable=NombreEliminar).place(x=70,y=120) #Se le asigna un campo de texto a la variable.
       BotonEliminar = Button(canvas2,command=VentanaDeEliminar,text="Eliminar",relief=FLAT,fg="white",bg="deep sky blue").place(x=100,y=170)#Se le asigna un boton a la variable.
       canvas3 = Canvas(frame4, borderwidth=0,bg="brown1") #Se crea una ventana dentro de la ventana contactos.
       ventanilla3 = ttk.Frame(canvas3) #Se crea ua miniventana.
       canvas3.pack(side = 'left', fill = 'both', expand=True) #Se empaca el Canvas.
       canvas3.create_window((0, 0), window = ventanilla3, anchor = 'nw', tags = 'frame') #Se crea canvas un formato como una miniventana.
       NombreModificar = StringVar() #Se le asigna el valor string a la variable.
       EtiquetaModificar = Label(canvas3,bg="brown1",text="Digite el nombre que desea modificar:",fg="white",font=("ms sans Serif",9,"bold")).place(x=30,y=60) #Se le asigna una etiqueta de texto a la variable.
       EspacioModificar = Entry(canvas3,textvariable = NombreModificar).place(x=70,y=120)#Se le asigna un campo de texto a la variable.
       BotonModificar = Button(canvas3,command=VentanaModificar,text="Modificar",relief=FLAT,fg="white",bg="deep sky blue").place(x=100,y=170)#Se le asigna un boton a la variable.
       eliminar  = PhotoImage(file = "goma-de-borrar_1_.gif") #Se crea una imagen y se lo asigna a la variable.
       buscar    = PhotoImage(file = "lupa.gif") #Se crea una imagen y se lo asigna a la variable.
       contactos = PhotoImage(file = "usuarios.gif") #Se crea una imagen y se lo asigna a la variable.
       modificar = PhotoImage(file = "modificar.gif") #Se crea una imagen y se lo asigna a la variable.
       tab2=nbook.add(frame2,image = contactos,padding = 10) #Se le agrega al cuaderno una etiqueta y se le asigna la imagen de consultar.
       tab1=nbook.add(frame1,image = buscar,padding = 10) #Se le agrega al cuaderno una etiqueta y se le asigna la imagen de Contactos.
       tab3=nbook.add(frame3,image = eliminar,padding = 10) #Se le agrega al cuaderno una etiqueta y se le asigna la imagen de eliminar. 
       tab4=nbook.add(frame4,image = modificar,padding = 10) #Se le agrega al cuaderno una etiqueta y se le asigna la imagen de modificar.
       ventana1.mainloop() #La ventana espera hasta que el usuario digite algo.


#-------------------
#Pantalla Principal
#-------------------

celular = Tk() #Se crea una ventana.


celular.title("Apps") #Titulo de la ventana.
iconoCelular = celular.iconbitmap("telefono-inteligente.ico") #Icono de la ventana.
celular.geometry("310x550") #Tamano de la ventana.
ImagenDContact=PhotoImage(file="DContactImagen.gif")
MasterMind = PhotoImage(file="tablero.gif")
dibujo=Canvas(celular) #Ventana de dibujos.
dibujo.pack(expand=True, fill=BOTH) #Empaca la ventana de dibujo.
botonMaster = Button(dibujo,image=MasterMind,relief=FLAT,bg="white smoke").place(x=100,y=30)
celular.maxsize(310,550) #El tamano máximo que se puede agrandar o minimizar la pantalla.
boton=Button(dibujo,image=ImagenDContact,command=Principal,relief=FLAT,bg="white smoke").place(x=30,y=30)
celular.mainloop() 
