# n different recipes string. 2d string array ingredients
# recipes[i] can create when ingredients[i][] if all are present
# sometimes you have to create a recipe to create another recipe (ingredients[i][j] = recipes[j])
# supplies are initial ingredients
# return name of all the recipes you can create
# cyclic dependency
from typing import List


# loop through each recipe, check for ingredients present in supplies then in recipes to check all the ingredients we
# maintain visited to make sure there is not cyclic depth first searach, if cyclic is present we return false if no
# is present and all the ingredients are present return true

class Solution:
    def binaryGap(self, n: int) -> int:
        binaryString = format(n, "b")
        print(binaryString)
        longestDistance = 0
        last1Idx = -1

        for idx in range(len(binaryString)):
            if binaryString[idx] == "1":
                if last1Idx == -1:
                    last1Idx = idx
                else:
                    if longestDistance < (idx - last1Idx):
                        longestDistance = idx - last1Idx
                last1Idx = idx

        return longestDistance


if __name__ == "__main__":
    s1 = Solution()
    s1.binaryGap(15)
