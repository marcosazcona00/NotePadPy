#@Author --> Azcona Marcos

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

def create_file(content):
    '''
        Crea el archivo en la carpeta que corresponda
    '''
    text = sg.popup_get_text('Ingrese el nombre del archivo')
    file_path = sg.popup_get_folder('folder',no_window=True) #Guardo en file_path la ruta del archivo
    filename=file_path+'/'+text #Concateno la ruta con el texto /home/directory/nombre_archivo.extension
    return filename

def main():

    #---------------VARIABLES-----------------------------------------#

    opened_file = '' #Guardo el archivo actualmente guardado

    menu = [
            ['Archivo',['Nuevo','Abrir','Guardar','Guardar Como','Salir']],
            ['Acerca de']
           ]

    column = [[sg.Multiline(size=(100,30),key='Multi')]]

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
        
        elif event is 'Abrir':
            filename = sg.popup_get_file('file to open', no_window=True)  #Devuelve la ruta completa del archivo
            if get_extension(filename) in extensions:   #Si es una extension valida
                text = get_content(filename)  
                opened_file = filename
                multiline_object.Update(value = text) #Actualizo la ventana con el texto del archivo
        
        elif event is 'Guardar' or 'Nuevo' or 'Guardar Como':
            text = multiline_object.Get() #El método Get() devuelve el contenido del Multiline
            if event is 'Guardar':
                filename = opened_file #Ahora el archivo donde guardar es el abierto
            elif event is 'Nuevo':
                filename = create_file(text) #Me devuelve el nombre del archivo nuevo creado
                opened_file = filename #El archivo actualmente abierto es el que creo anteriormente. Se usa opened_file en caso de que toque Guardar
                multiline_object.Update(value = '') #Actualizo la ventana para dejarala vacia   
            elif event is 'Guardar Como':
                #Cambio filename a la ruta donde quiere guardar el archivo
                filename = sg.popup_get_file('file to open', no_window=True)  #Devuelve la ruta completa del archivo  
            save_file(text,filename) #Guardo el texto en el archivo elegido


if __name__ == '__main__':
    main()