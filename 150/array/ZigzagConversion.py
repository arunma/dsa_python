class ZigzagConversion:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        row_arr = [""] * (numRows + 1)
        # row_map = {row: "" for row in range(1, numRows + 1)}
        row = 1
        up = False
        for c in s:
            row_arr[row] += c
            if up:
                row -= 1
            else:
                row += 1

            if row == numRows:
                up = True
            elif row == 1:
                up = False

        result = ""
        for i in range(1, numRows + 1):
            result += row_arr[i]

        return result


if __name__ == '__main__':
    init = ZigzagConversion()
    print(init.convert("PAYPALISHIRING", 3))  # PAHNAPLSIIGYIR
