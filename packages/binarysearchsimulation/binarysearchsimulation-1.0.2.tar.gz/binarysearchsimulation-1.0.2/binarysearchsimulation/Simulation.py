class Simulation:
    def __init__(self):
        self.middleColor = "\033[48;5;196m\033[38;5;15m"  # red
        self.leftPointerColor = "\033[48;5;27m\033[38;5;15m"  # blue
        self.rightPointerColor = "\033[48;5;13m\033[38;5;15m"  # pink
        self.endColoring = "\033[0m"

    def printList(self, arr, pos, color):
        mylist = arr.copy()
        mylist[pos] = color + str(mylist[pos]) + self.endColoring
        for i in range(len(mylist)):
            print(str(mylist[i]) + " \n"[1 if i + 1 == len(mylist) else 0], end="")


    def printListWithSpaces(self, arr, pos, color):
        mylist = arr.copy()
        for i in range(len(mylist)):
            mylist[i] = " " * len(str(mylist[i]))
        self.printList(mylist, pos, color)


    def clearRange(self, arr, left, right):
        mylist = arr.copy()
        for i in range(left):
            mylist[i] = " " * len(str(mylist[i]))
        for i in range(len(arr) - 1, right, -1):
            mylist[i] = " " * len(str(mylist[i]))
        return mylist
    
    def run(self):
        print("Insert list of numbers, each of them separated by a space:")
        arr = ["  "]
        arr += list(map(int, input().split()))
        arr += ["  "]
        print("Insert the number you want to find:")
        target = int(input())
        print("Insert 0 to simulate lower_bound or 1 to simulate upper_bound:")
        isUpperBound = bool(int(input()))
        print("\n\nTarget =", target)
        print()

        print("=" * 25, "0", "=" * 25)

        left = 0
        right = len(arr) - 1
        cnt = 1
        mid = -1

        while (right - left > 1):
            mid = left + (right - left) // 2
            print()
            self.printListWithSpaces(arr, left, self.leftPointerColor)
            self.printList(self.clearRange(arr, left, right), mid, self.middleColor)
            self.printListWithSpaces(arr, right, self.rightPointerColor)
            print()
            print("=" * 25, cnt, "=" * 25)
            if (arr[mid] < target):
                left = mid
            elif (arr[mid] > target):
                right = mid
            else:
                if isUpperBound:
                    left = mid
                else:
                    right = mid
            cnt += 1

        mid = left + (right - left) // 2
        print()
        self.printListWithSpaces(arr, left, self.leftPointerColor)
        self.printList(arr, mid, self.middleColor)
        self.printListWithSpaces(arr, right, self.rightPointerColor)
        print()
        print("=" * 25, "END", "=" * 25)
        print()
        print(self.leftPointerColor + "  " + self.endColoring + " Left:", left)
        print()
        print(self.rightPointerColor + "  " + self.endColoring + " Right:", right)
        print()
        print()

