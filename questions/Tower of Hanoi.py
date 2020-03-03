inte = int(input("Enter the number of Disks: "))


def tower(num, a, c, b):
    if num == 1:
        print("Move Disk 1 from {} to {}".format("A", "C"))
        return
    tower(num-1, a, b, c)
    print("Move Disk {} from {} to {}".format(num, "A", "C"))
    tower(num-1, b, c, a)


tower(inte, "A", "B", "C")
