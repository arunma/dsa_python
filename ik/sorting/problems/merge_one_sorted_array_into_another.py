def merge_one_into_another(first, second):
    fi = len(first) - 1
    si = 0

    while second[si] != 0:
        si += 1
    si -= 1

    place = len(second) - 1

    while fi >= 0 and si >= 0:
        if first[fi] > second[si]:
            second[place] = first[fi]
            fi -= 1
            place -= 1
        else:
            second[place] = second[si]
            si -= 1
            place -= 1

    if fi >= 0:
        second[:fi + 1] = first[:fi + 1]
    return second


if __name__ == '__main__':
    print(merge_one_into_another(first=[1, 3, 5], second=[2, 4, 6, 0, 0, 0]))
