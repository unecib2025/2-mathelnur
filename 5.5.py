event_code= input("Введите тип системы: ")
match event_code:
    case "ERR":
        print("Ошибка системы")
    case "WRN":
        print("Предупреждение")
    case "INF":
        print("Информационное сообщение")
    case _:
        print("Неизвестный код события")
