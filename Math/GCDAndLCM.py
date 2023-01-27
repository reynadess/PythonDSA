class GCDAndLCM:
    def gcd(self, a, b):
        if b == 0:
            return a
        elif a == 0:
            return b
        return self.gcd(b, a % b)

    def lcm(self, a, b):
        return (a * b) / self.gcd(a, b)


if __name__ == '__main__':
    sol = GCDAndLCM()
    print(sol.gcd(10, 0))
    print(sol.lcm(10, 12))