class ZigZagText:
    """
    Input: s = "PAYPALISHIRING", numRows = 4
    Output: "PINALSIGYAHRPI"
    Explanation:
    P     I    N
    A   L S  I G
    Y A   H R
    P     I
    """
    
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 0:
            return ""
        elif numRows == 1:
            return s
        else:
            increment = True
            current_row = 0
            rows = [[] for i in range(0, numRows)]
            for i in range(0, len(s)):
                if increment:
                    rows[current_row].append(s[i])
                    current_row += 1
                    if current_row % numRows == 0 and i != 0:
                        increment = False
                        current_row -= 1
                else:
                    current_row -= 1
                    rows[current_row].append(s[i])
                    if current_row % numRows == 0:
                        increment = True
                        current_row += 1
  
            text = ""
            for row in rows:
                text += "".join(row)
            return text

