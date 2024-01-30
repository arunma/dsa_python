def get_words_from_phone_number(phone_number):
    mapp = {"1": " ", "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz", "0": " "}
    result = []
    get_words_from_phone_number_inner(phone_number, mapp, "", 0, result)
    return result


def get_words_from_phone_number_inner(phone_number, mapp, curr, index, result):
    if len(curr) == len(phone_number):
        result.append(curr.replace(" ", ""))
        return

    for i in range(index, len(phone_number)):
        for c in mapp[phone_number[i]]:
            get_words_from_phone_number_inner(phone_number, mapp, curr + c, i + 1, result)


if __name__ == '__main__':
    print(get_words_from_phone_number("1234567"))
    print(get_words_from_phone_number("1237890"))
    print(get_words_from_phone_number("1010101"))
