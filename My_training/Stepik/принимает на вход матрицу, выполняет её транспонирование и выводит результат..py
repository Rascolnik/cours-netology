
def matrix (number_columns:int, number_lines:int ):
    count = 0
    for i in range(number_lines):
        for j in range(number_columns):
            count += 1
            print(count,end=" ")
        print()


if __name__ == "__main__":
    matrix(3, 2)
    matrix(4,1)