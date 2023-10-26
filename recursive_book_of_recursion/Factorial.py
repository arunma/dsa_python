from typing import *


class Factorial:
    def factorial(self, n):
        if n<=1:
            return 1

        result=1
        for i in range(1,n+1):
            result*=i
        return result

    def factorial_recursive(self, n):
        if n<=1:
            return 1
        return n*self.factorial_recursive(n-1)

    def sum_series(self, n):
        result=0
        for i in range(1,n+1):
            result+=i
        return result

    def sum_series_recursive(self, n):
        if n<=1:
            return n
        return n+self.sum_series_recursive(n-1)

    def sum_powers_of_2(self, n):
        if n<=1:
            return n

        result=0
        for i in range(1,n+1):
            result+=i**2
        return result

    def sum_powers_of_2_recursive(self, n):
        if n<=1:
            return n
        return n**2 + self.sum_powers_of_2_recursive(n-1)



if __name__ == '__main__':
    init = Factorial()
    print(init.factorial(10)) #3628800
    print(init.factorial_recursive(10)) #3628800
    print(init.sum_series(10)) #55
    print(init.sum_series_recursive(10)) #55
    print(init.sum_powers_of_2(10)) #385
    print(init.sum_powers_of_2_recursive(10)) #385
    print(init.sum_powers_of_2_recursive(3)) #14
