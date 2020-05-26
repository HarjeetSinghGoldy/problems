import time


def range1(stop, start):
    while start < stop:
        yield start
        start <<= 1


class Complexity(object):
    def constant(self, arr):
        print("BIG O(1) / Constant Time Complexity")
        return arr[1]  # Your Statement

    def logarithmic(self, n):
        print("BIG O(log(n)) / Logarithmic Time Complexity base 2")
        fooSum = 0
        for i in range1(n, 2):  # custom doubling function
            fooSum = fooSum + 1
        return fooSum

    def logOflogarithmic(self, n):
        print("BIG O(log(log(n))) / Logarithmic of Log Time Complexity base 2")
        fooSum = 0
        p = 0
        for i in range1(n, 2):  # custom doubling function
            p = p + 1
        for i in range1(p, 2):
            fooSum = fooSum + 1
        return fooSum

    def fractionalPower(self, n):
        print("BIG O(n^c) 0<c<1 / Fractional Power Time Complexity")
        fooSum = 0
        p = 0
        i = 1
        while p <= n:
            fooSum = fooSum + 1
            i = i + 1
            p = p + i
        return fooSum

    def linear(self, n):
        print("BIG O(n) / Linear Time Complexity")
        fooSum = 0
        for i in range(n):
            fooSum = fooSum + 1  # Your Statement
        return fooSum

    def loglinear(self, n):
        print("BIG O(log(log(n))) / Log Linear Time Complexity")
        fooSum = 0
        for i in range(n):
            for k in range1(n, 2):
                # print(fooSum)
                fooSum = fooSum + 1  # Your Statement
        return fooSum

    def quadratic(self, n):
        print("BIG O(n^2) / Quadratic Time Complexity")
        fooSum = 0
        for i in range(n):
            for j in range(n):
                fooSum = fooSum + 1
        return fooSum

    def cubic(self, n):
        print("BIG O(n^3) / Cubic Time Complexity")
        fooSum = 0
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    # print(fooSum)
                    fooSum = fooSum + 1
        return fooSum

    fooSum = 0

    def factorial(self, n):
        print("BIG O(n!) / Factorial Time Complexity")

        def helper(n):
            for i in range(n):
                for j in range(helper(n - 1)):
                    print(self.fooSum)
                    self.fooSum = self.fooSum + 1
            return n

        helper(n)

        return self.fooSum


def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = 1000000
    start = time.time()
    # print("Output=>", Complexity().constant(arr))
    # print("Output=>", Complexity().linear(n))
    # print("Output=>", Complexity().quadratic(n))
    # print("Output=>", Complexity().logarithmic(n))
    # print("Output=>", Complexity().logOflogarithmic(n))
    # print("Output=>", Complexity().loglinear(n))
    # print("Output=>", Complexity().fractionalPower(n))
    # print("Output=>", Complexity().cubic(n))
    print("Output=>", Complexity().factorial(n))
    end = time.time()
    print("Time Taken:=>", end - start, "sec")


if __name__ == "__main__":
    main()
