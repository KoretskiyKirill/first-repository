try:
    if input('лето?') == 'да':
        if input('идёт дождь?') == 'да':
            print('надень дождевик')
        elif input('идёт дождь?') == 'нет':
            print('надень футболку и шорты')
    elif input('осень или весна') == 'да':
        if input('идёт дождь?') == 'да':
            print('возьми зонт')
        elif input('идёт дождь?') == 'нет':
            print('надень ветровку')
    elif input('зима') == 'да':
        print('надень пуховик')
except():
    print('да либо нет')