#!/usr/bin/env Python3     
import os 
import PySimpleGUI as sg 

def get_extension(filename):
    '''
        Retorna la extension del archivo
    ''' 
    index_id = 0
    for index in range(len(filename)):
        if filename[index] is '.': #Si en esa posición está el punto, todo lo que resta es extension
            index_id = index #Guardo el indice de donde arranca el punto.
            break
    return filename[index_id:] #Devuelve el string desde el punto hasta el final

def save_file(text,filename):
    '''
        Guarda el contenido de lo escrito en el archivo
    '''            
    with open(filename,'w') as file:
        file.write(text)

def get_content(filename):
    '''
        Devuelve el cotenido del archivo
    '''
    with open(filename,'r') as file:
        return file.read()

def create_file():
    '''
        Crea el archivo en la carpeta que corresponda y devuelve la ruta completa del nuevo archivo creado
    '''
    text = sg.popup_get_text('Ingrese el nombre del archivo')
    file_path = sg.popup_get_folder('folder',no_window=True) #Guardo en file_path la ruta del archivo
    filename=file_path+'/'+text #Concateno la ruta con el texto /home/directory/nombre_archivo.extension
    return filename

def change_title_window(window,opened_file):
    '''
        Cambia el nombre del titulo al del archivo abierto actualmente
    '''
    opened_file_name = opened_file.split('/') #Lo separo y creo una lista
    opened_file_name = opened_file_name[len(opened_file_name)-1] #Me quedo con la ultima posicion que es el nombre del archivo
    window.TKroot.title(opened_file_name) #Cambio el titulo de la ventana
    return opened_file_name

def is_python_extension(opened_file_name):
    '''
        Retorna un booleano indicando si la extension del archivo es .py
    '''
    return get_extension(opened_file_name) == '.py'

def create_python_structure():
    '''
        Devuelve un texto con la estructura de un .py basico
    '''
    text = '''
#!/usr/bin/env Python3     
import PySimpleGUI as sg

def main():
    pass

if __name__ == '__main__':
    main()
    '''
    return text


def main():

    #---------------VARIABLES-----------------------------------------#
    opened_file = '' #Guardo el archivo actualmente abierto, el path completo
    opened_file_name = '' #Guardo el nombre del archivo

    menu = [
            ['Archivo',['Nuevo','Abrir','Guardar','Guardar Como','Salir']],
            ['Acerca de'],
            ['Python', ['Ejecutar']]
           ]

    column = [[sg.Multiline(size=(140,35),font='Courier 11',key='Multi')]]

    layout = [[sg.Menu(menu),sg.Column(column)]]

    window = sg.Window('Ventana',layout)

    multiline_object = window['Multi'] #Devuelve un objeto de tipo Multiline

    extensions = ['.txt','.py','.doc','.docx','.c','.cs'] #Defino las extensiones que puedo abrir


    #-----------------------------------------------------------------#
    while True:
        event,values = window.Read()
        if event is None:
            window.Close()
            break
        else:
            if event is 'Abrir':
                filename = sg.popup_get_file('file to open', no_window=True)  #Devuelve la ruta completa del archivo
                if get_extension(filename) in extensions:   #Si es una extension valida
                    text = get_content(filename) #Devuelve el contenido del archivo
                    opened_file = filename
                    multiline_object.Update(value = text) #Actualizo la ventana con el texto del archivo
                    opened_file_name = change_title_window(window,opened_file)
           
            elif event is 'Guardar' or 'Nuevo' or 'Guardar Como':
                text = multiline_object.Get() #El método Get() devuelve el contenido del Multiline
                if event is 'Guardar':
                    filename = opened_file #Ahora el archivo donde guardar es el abierto
                elif event is 'Nuevo':
                    filename = create_file() #Me devuelve el nombre del archivo nuevo creado
                    opened_file = filename #El archivo actualmente abierto es el que creo anteriormente. Se usa opened_file en caso de que r
                    opened_file_name = change_title_window(window,opened_file) #Me devuelve el nombre del archivo 'notepad.py' por ejemplo
                    if get_extension(opened_file_name) == '.py': #Si la extension del archivo es .py
                    	text= create_python_structure() #Retorna el texto con la estructura de un .py
                    multiline_object.Update(value = text) #Actualizo la ventana para dejarala vacia   

                elif event is 'Guardar Como':
                    #Cambio filename a la ruta donde quiere guardar el archivo
                    filename = sg.popup_get_file('file to open', no_window=True)  #Devuelve la ruta completa del archivo  
                try:
                    save_file(text,filename) #Guardo el texto en el archivo elegido
                except UnboundLocalError: #Esta excepcion es por si crea un archivo vacio y manda a ejecutar
                    continue
            if event is 'Ejecutar' and is_python_extension(opened_file_name):
                #Permite ejecutar un .PY
                os.system('/usr/bin/python3 {}'.format(filename))


if __name__ == '__main__':
    main()


