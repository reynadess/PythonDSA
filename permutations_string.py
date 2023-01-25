# generate permutations of string
def permutations_of_string(s: str, l: int, r: int):
    if l == len(s) - 1:
        print(s)
        return
    for i in range(l, r + 1):
        s = list(s)
        s[l], s[i] = s[i], s[l]
        s = "".join(s)
        permutations_of_string(s, l + 1, r)
        s = list(s)
        s[l], s[i] = s[i], s[l]
        s = "".join(s)


if __name__ == "__main__":
    permutations_of_string("abc", 0, 2)
