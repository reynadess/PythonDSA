import math


class SieveOfEratosthenes:
    def __init__(self, num):
        self.num = num
        self.primes_list = list()
        self._bool_primes = [True for _ in range(num + 1)]
        self.populated = False

    def get_prime_nos(self) -> list:
        if len(self.primes_list) == 0:
            self.do_sieve_of_eratosthenes()
        return self.populate_primes()

    def populate_primes(self):
        if self.populated:
            return self.primes_list
        self.populated = True
        for i in range(len(self._bool_primes)):
            if self._bool_primes[i]:
                self.primes_list.append(i)
        return self.primes_list

    def do_sieve_of_eratosthenes(self):
        self._bool_primes[0] = False
        self._bool_primes[1] = False
        for i in range(2, int(math.sqrt(self.num)) + 1):
            for j in range(i * 2, self.num + 1, i):
                self._bool_primes[j] = False


if __name__ == '__main__':
    sol = SieveOfEratosthenes(45000)
    print(sol.get_prime_nos())
