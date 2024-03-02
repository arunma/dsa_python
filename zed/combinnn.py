import itertools

if __name__ == '__main__':
    # input = ["hello", "world", "three", "four", "three", "four"]
    input = ["hello", "world", "three", "four", "three"]
    for comi in itertools.combinations(input, 3):
        print(comi)

    print("-----")
    for permi in itertools.permutations(input, 3):
        print(permi)

    # N = len(input)
    # out = []
    # for i in range(N):
    #     for j in range(i + 1, N):
    #         for k in range(j + 1, N):
    #             out.append((input[i], input[j], input[k]))

    # print(out)
    # print(len(out))
