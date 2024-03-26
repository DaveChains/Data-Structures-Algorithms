class MaxNumberOfBalloons:
    def maxNumberOfBalloons(self, text: str) -> int:
        blue_print = [0] * 26
        count = [0] * 26
        times_b = 0
        for each_c in "balloon":
            blue_print[ord(each_c) - ord("a")] += 1

        for c in text:
            i = ord(c) - ord("a")
            if c in "balloon" and count[i] < blue_print[i]:
                count[i] += 1
            if count == blue_print:
                times_b += 1
                count = [0] * 26

        # l, r = 0, len(text)-1
        # while l < r:
        #     cl = text[l]
        #     cr = text[r]
        #     cl_i = ord(cl) - ord("a")
        #     cr_i = ord(cr) - ord("a")
        #
        #     if cl in "balloon" and count[cl_i] < blue_print[cl_i]:
        #         count[cl_i] += 1
        #         l += 1
        #
        #     if cr in "balloon" and count[cr_i] < blue_print[cr_i]:
        #         count[cr_i] += 1
        #         r -= 1
        #
        #     if count == blue_print:
        #         times_b += 1
        #         count = [0] * 26
        #
        # return times_b

    def neetMaxNumberOfBalloons(self, text: str) -> int:
        countText = {}  # or Counter() to hashmap
        balloon = {}  # or Counter() to hashmap
        res = len(text)
        for n in text:
            countText[n] = countText.get(n, 0) + 1

        for v in "balloon":
            balloon[v] = balloon.get(v, 0) + 1

        for c in balloon:
            countTextL = countText.get(c, 0)
            balloonR = balloon.get(c, 0)
            res = min(res, countTextL // balloonR)

        return res


driver = MaxNumberOfBalloons()
print(driver.neetMaxNumberOfBalloons("nlaebolko"))
print(driver.neetMaxNumberOfBalloons("loonbalxballpoon"))
print(driver.maxNumberOfBalloons("balllllllllllloooooooooon"))
print(driver.maxNumberOfBalloons("leetcode"))
