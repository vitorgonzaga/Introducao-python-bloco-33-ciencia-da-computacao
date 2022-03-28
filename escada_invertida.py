from os import remove


def vertical_inverted_ladder(word):
    for removed_letters in range(len(word)):
        for index in range(len(word) - removed_letters):
            print(word[index], end="")
        print() # add a new line or a vertical space

if __name__ == "__main__":
    name = input("Digite um nome: ")
    vertical_inverted_ladder(name)
