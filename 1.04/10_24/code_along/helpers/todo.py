
def get_todo():
    #context manager 
    with open("10_24/code_along/data/todo.txt") as f:
        lines = f.readlines()

        for row in lines:
            print(row)

#keep for testing but don't rin when importing
if __name__ == "__main__":
    print("youve ran todo.py")
