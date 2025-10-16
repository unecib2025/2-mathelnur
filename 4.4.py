checksum_original= int(input("Введите число: "))
checksum_current= int(input("Введите число: "))
status="Файл не изменён" if checksum_original==checksum_current else "Файл повреждён"
print(status)