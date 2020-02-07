
#!/usr/bin/env Python3     
import PySimpleGUI as sg

def main():
    layout = [
              [sg.T('Hola') 
	     ]
    window = sg.Window('v',layout)
    window.Read()

if __name__ == '__main__':
    main()
    
