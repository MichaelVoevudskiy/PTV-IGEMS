import os
import xml.etree.ElementTree as ET
os.system('cls')

# Функция для обработки каждого .dig файла

asd = ''
baza = {}

def process_dig_file(file_path, num):
    # Парсинг XML из файла
    global asd
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Поиск всех элементов с тегом Quantity

    for a in root.iter('PartID'):
        for c in a.iter('Quantity'):
            QuantityP = c.text
        for b in a.iter('Name'):
            NameP = b.text
            baza.update({NameP: QuantityP})    
        
    for quantity in root.iter('Quantity'):
        try:
            # Умножаем значение Quantity на 2
            current_value = int(quantity.text)
            quantity.text = str(current_value * int(num))

        except ValueError:
            print(f"Invalid value for Quantity parameter in file {file_path}: {quantity.text}")
    nfn= file_path+"___"+num+"-SETS.dig"
    print(nfn)

    
    # Сохранение изменений обратно в файл
    tree.write(file_path+"___"+num+"-SETS.dig", encoding='utf-8', xml_declaration=True)
    
    
    return nfn
