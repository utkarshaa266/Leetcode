class Solution:
    def largestOverlap(self, img1, img2):
        n = len(img1)
        count = {}
        ans = 0

        # Positions of 1s in img2
        ones2 = []
        for i in range(n):
            for j in range(n):
                if img2[i][j] == 1:
                    ones2.append((i, j))

        # Compare every 1 in img1 with every 1 in img2
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:

                    for x, y in ones2:
                        dx = x - i
                        dy = y - j

                        key = (dx, dy)

                        count[key] = count.get(key, 0) + 1
                        ans = max(ans, count[key])

        return ans