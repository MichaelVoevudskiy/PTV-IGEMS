import flet as ft
import pars 

def main(page: ft.Page):
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width=800
    page.scroll='auto'

    # Создаем текстовое поле для отображения пути к файлу
    file_path_text = ft.TextField(label="Путь к файлу", width=500, read_only=True, border_color='#ffffff')

    # Функция, которая обрабатывает файл после выбора
    def on_file_picked(e: ft.FilePickerResultEvent):
        if e.files:
            file_path = e.files[0].path  # получаем путь к выбранному файлу
            file_path_text.value = file_path  # устанавливаем путь в текстовое поле
            page.update()
            print(file_path_text.value)
            
    def creator(e):
        nfn = pars.process_dig_file(file_path_text.value, txt_number.value)

        
        page.add(ft.Row([ft.Text("file created: ", color="#74d5ff"), 
                         ft.Text(nfn, color="#ADFF2F")], 
               alignment=ft.MainAxisAlignment.CENTER))
        
        for el in pars.baza:
            page.add(ft.Row([ft.Text(el, color="#74d5ff"), ft.Text(' - ' + pars.baza[el] + 'шт', color="#ADFF2F")],alignment=ft.MainAxisAlignment.CENTER))
            
        page.update()
  


    def minus_click(e):
        if (txt_number.value != "1"):
            txt_number.value = str(int(txt_number.value) - 1)
            page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()
        

    # Создаем объект FilePicker и кнопку для открытия диалога выбора файла
    file_picker = ft.FilePicker(on_result=on_file_picked)
    page.overlay.append(file_picker)

    # Кнопка для открытия выбора файла
    open_file_button = ft.ElevatedButton("Выбрать файл", on_click=lambda _: file_picker.pick_files())

    txt_number = ft.TextField(value="1", text_align=ft.TextAlign.RIGHT, width=100)
    buton_create = ft.ElevatedButton("create file", on_click=creator)
    btrem = ft.IconButton(ft.icons.REMOVE, on_click=minus_click)
    btadd = ft.IconButton(ft.icons.ADD_CIRCLE, on_click=plus_click)
    
    # Добавляем виджеты на страницу
    page.add(
        ft.Row([ft.Text('https://github.com/MichaelVoevudskiy', size=12, color="#d974ff")]),
        ft.Row([open_file_button, file_path_text], 
               alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.Text("Количество комплектов: "), btrem,txt_number, btadd, buton_create], 
               alignment=ft.MainAxisAlignment.CENTER)
        
        )
    


ft.app(target=main)
