"""
Youtube downloader version 0.01

This project is getting moved to it's own respository as I its going to get larger
and I would like to keep things organized .

"""

from pytube import YouTube
import PySimpleGUI as sg
from pytube.streams import Stream

layout = [[sg.Text('URL', size=(15,1)),sg.InputText()],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Download'), sg.Button('Quit')]
        ]

# Create the window
window = sg.Window('Youtube Downloader', layout)

#Event Loop
while True:
    event, values = window.read()
   
    # Waiting for quit press
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    
    url = values[0]
    yt = YouTube(url)
    window['-OUTPUT-'].update(yt.title + ' is finished downloading') 
    yt.streams.all()
    stream = yt.streams.first()
    stream.download()

    window.refresh

# Finish up by removing from the screen
window.close()
