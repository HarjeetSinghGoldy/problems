import time

from Complexity.all_examples import range1


class Complexity(object):

    def logarithmic(self, n):
        print("BIG O(log(n)) / Logarithmic Time Complexity(Base 2)")
        # Time Taken:=> 2.3365020751953125e-05 sec
        fooSum = 0
        for i in range1(n, 2):  # own range function doubling the range 2 ,4 , 8 , 16, 32, 64....
            fooSum = fooSum + 1  # your statement
        return fooSum


def main():
    n = 100000
    start = time.time()
    print("Output=>", Complexity().logarithmic(n))
    end = time.time()
    print("Time Taken:=>", end - start, "sec")


if __name__ == "__main__":
    main()
