import PySimpleGUI as sg
import create_table
from user_login import user_input

data_array = []
headers = ['User', 'Shift', 'QL(UID)', 'DateTimeStart', 'DateTimeEnd', 'RecordCreation']


layout = [[sg.Text('User:', sg.Text(user_input, background_color='EFF2F6')],
          [sg.]