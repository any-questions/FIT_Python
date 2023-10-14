users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
visitors={
    "Общее количество":0,
    "Уникальные посещения":0,
}
visitors["Общее количество"]=len(users)
visitors["Уникальные посещения"]=len(set(list(users)))
print(visitors)