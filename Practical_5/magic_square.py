import numpy as np

def check_magic_square(test):
    srow=[]
    scol=[0]*len(test[0])
    d1 = 0
    d2 = 0

    for row in range(0, len(test)):
        for elem in range(0, len(test[row])):
            scol[elem] += test[row][elem]
            if row == elem:
                d1 += test[row][elem]

            if row == len(test)-elem-1:
                d2 += test[row][elem]
        srow.append(test[row].sum())

    rowmin = min(srow)
    rowmax = max(srow)
    colmin = min(scol)
    colmax = max(scol)

    print("Minimum of sum of rows -", rowmin)
    print("Maximum of sum of rows -", rowmax)

    print("Minimum of sum of columns -", colmin)
    print("Maximum of sum of columns -", colmax)

    print("Sum of primary diagonal -", rowmin)
    print("Sum of secondary diagonal -", rowmax)


    if d1==d2==rowmax==rowmin==colmin==colmax:
        print("The given matrix is a magic square")
        return True
    else:
        print("The given matrix is not a magic square")
        return False

def main():
    test=np.array([[17, 24, 1, 8, 15], [23, 5, 7, 14, 16], [ 4, 6, 13, 20, 22], [10, 12, 19, 21, 3], [11, 18, 25, 2, 9]])

    check_magic_square(test)

if __name__ == "__main__":
    main()