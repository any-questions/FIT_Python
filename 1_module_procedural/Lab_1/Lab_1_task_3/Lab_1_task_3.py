list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
number_of_players = len(set(list_players))
print(list_players[0:number_of_players//2])
print(list_players[number_of_players//2:number_of_players])
