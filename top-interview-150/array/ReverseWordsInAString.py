class ReverseWordsInAString:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        result = []
        for each in reversed(s.split()):
            result.append(each)
        return " ".join(result)

    def reverseWords(self, s: str) -> str:
        result = []
        temp = ""

        for c in s:
            if c != " ":
                temp += c
            elif temp != "":
                result.append(temp)
                temp = ""
        if temp != "":
            result.append(temp)

        return " ".join(result[::-1])


if __name__ == '__main__':
    init = ReverseWordsInAString()
    print(init.reverseWords("the sky is blue"))
    print(init.reverseWords(" hello world "))
