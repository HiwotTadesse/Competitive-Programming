from tkinter import N


def domino_pining(m, n):
    max_number_of_rectangle = m * n
    max_domino = max_number_of_rectangle // 2

    return max_domino

print(domino_pining(3, 2))