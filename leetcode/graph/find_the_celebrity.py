def knows(a: int, b: int) -> bool:
    # return False
    # dt = {
    #     0: {0: True, 1: True, 2: False},
    #     1: {0: False, 1: True, 2: False},
    #     2: {0: True, 1: True, 2: True}
    # }
    dt = {
        0: {1: True},
        1: {0: True},
    }
    return b in dt[a]


class FindTheCelebrity:
    def findCelebrity(self, n: int) -> int:
        celeb = 0
        for cand in range(1, n):
            if knows(celeb, cand):
                celeb = cand

        # if any(knows(celeb, cand) for cand in range(n) if cand != celeb):
        if any(knows(celeb, cand) for cand in range(celeb)):
            return -1
        if any(not knows(cand, celeb) for cand in range(n)):
            return -1

        return celeb


if __name__ == '__main__':
    init = FindTheCelebrity()
    print(init.findCelebrity(2))  # 1'
    print(init.findCelebrity(2))  # 1'
