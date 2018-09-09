with open("data/some_data.txt", "rt", newline='') as f:
    line = f.read()
    print(line)

with open("data/some_data_1.txt", "wt") as f:
    line = "Hello to you!"
    f.write(line)

with open("data/some_data_1.txt", "at") as f:
    print("Add me to!", file=f)

