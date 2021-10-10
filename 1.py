def ans(hours, minutes):
    return (hours % 24) *60 + minutes
while True:
    try:
        hours = int(input("Введите часы:"))
        minutes = int(input("Введите минуты:"))
    except ValueError:
        print('error')
    else:
        break
if hours < 0 or minutes < 0 or minutes > 59:
    print("error")
else:
    print("Ответ:", ans(hours, minutes))
