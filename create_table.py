# Import
import  PySimpleGUI as sg


def create(data_array, headers):
    layout = [
        [sg.Table(values=data_array, headings=headers, max_col_width=35,
                  auto_size_columns=True,
                  display_row_numbers=True,
                  justification='right',
                  num_rows=20,
                  key='-TABLE-',
                  row_height=35,
                  tooltip='VAS Table')]
    ]

    scans_window = sg.Window("Scanned VAS Entries - Current Session",
                                           layout, modal=True)

    while True:
        event, values = scans_window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    scans_window.close()