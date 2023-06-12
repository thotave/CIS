def first_last_name(first_name, last_name):

    full_name = []
    for i, j in zip(first_name, last_name):
        full_name.append((i, j))
    return full_name

first_name = ["Madhav", "Suresh", "Satish", "Manoj", "Sravani"]
last_name = ["Thota", "Kasarla", "Pasupuleti", "Kola", "Chittabatteni"]

print(first_last_name(first_name, last_name))






