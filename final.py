def draw(list_of_cells):
    print("---------")
    k = 0
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            if list_of_cells[k] == "_":
                print(" ", end=" ")
            else:
                print(list_of_cells[k], end=" ")
            k = k + 1
        print("|")

    print("---------")


def move(list_of_cells, val):

    while True:
        is_problem = False
        coordinates = input("Enter the coordinates: ").split()

        for x in coordinates:
            if not x.isnumeric():
                print("You should enter numbers!")
                is_problem = True

            elif int(x) > 3 or int(x) < 1:
                print("Coordinates should be from 1 to 3!")
                is_problem = True

        if is_problem:
            continue
        coordinates = [int(x) for x in coordinates]

        position = (coordinates[0] - 1) * 3 + coordinates[1] - 1

        if list_of_cells[position] == "_":
            list_of_cells[position] = val
            draw(list_of_cells)
            break
        else:
            print("This cell is occupied! Choose another one!")


def win(list_cells):
    has_empty_cell = "_" in list_cells
    is_X_won = False
    is_O_won = False

    # Row
    for i in range(0,8,3):
        temp = list()
        for j in range(3):
            temp.append(list_cells[i + j])
        if temp.count("X") == 3:
            is_X_won = True
        if temp.count("O") == 3:
            is_O_won = True


    # Column
    for i in range(3):
        temp = list()
        for j in range(0,8,3):
            temp.append(list_cells[i+j])
        if temp.count("X") == 3:
            is_X_won = True
        if temp.count("O") == 3:
            is_O_won = True



    # Diagonal check to right
    temp = list()
    for x in range(0,9,4):
        temp.append(list_cells[x])
    if temp.count("X") == 3:
        is_X_won = True
    if temp.count("O") == 3:
        is_O_won = True

    # Diagonal check to left
    temp = list()
    for x in range(2,8,2):
        temp.append(list_cells[x])
    if temp.count("X") == 3:
        is_X_won = True
    if temp.count("O") == 3:
        is_O_won = True

    # Win condition
    if is_X_won and not is_O_won:
        print("X wins")
        exit()
    elif is_O_won and not is_X_won:
        print("O wins")
        exit()


    # Draw condition
    if not is_X_won and not is_O_won and not has_empty_cell:
        print("Draw")
        exit()




def game():

    list_of_cells = [x for x in "_________"]
    draw(list_of_cells)

    win(list_of_cells)
    move(list_of_cells,"X")
    win(list_of_cells)
    move(list_of_cells, "O")

    win(list_of_cells)
    move(list_of_cells,"X")
    win(list_of_cells)
    move(list_of_cells, "O")

    win(list_of_cells)
    move(list_of_cells,"X")
    win(list_of_cells)
    move(list_of_cells, "O")

    win(list_of_cells)
    move(list_of_cells,"X")
    win(list_of_cells)
    move(list_of_cells, "O")
    win(list_of_cells)

    win(list_of_cells)
    move(list_of_cells,"X")
    win(list_of_cells)


game()