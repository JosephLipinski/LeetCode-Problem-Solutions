class Roman:
    roman_numerals = ["I", "V", "X", "L", "C", "D",  "M"]
    numerals       = [  1,   5,  10,  50, 100, 500, 1000]

    def digitToRoman(self, digit: int, index: int) -> str:
        print(digit, index)
        if digit == 9:
            return (self.roman_numerals[index] + self.roman_numerals[index+2])
        elif digit > 5:
            return (self.roman_numerals[index+1] + (self.roman_numerals[index] * (digit - 5)))
        elif digit == 5:
            return (self.roman_numerals[index+1])
        elif digit == 4:
            return self.roman_numerals[index] + self.roman_numerals[index+1]
        else:
            return (digit * self.roman_numerals[index])
        
    def intToRoman(self, num: int) -> str:
        roman = ""
        s = str(num)
        index = (len(s) * 2) - 2
        
        for i in range(0, len(s)):
            char = s[i]            
            roman += self.digitToRoman(int(s[i]), index)
            index -= 2
        return roman
    
    def romanToInt(self, s: str) -> int:
        number = 0
        previous_char = s[0]
        count = 1
        for i in range(1, len(s)):
            print("s[i] {} number {}".format(s[i], number))
            if previous_char == None:
                previous_char = s[i]
                
            if s[i] == previous_char:
                count+=1
            else:
                c_index = self.roman_numerals.index(s[i])
                p_index = self.roman_numerals.index(previous_char)
                #E.g. IV or IX
                if p_index < c_index:
                    number += (self.numerals[c_index] - self.numerals[p_index])
                    previous_char = None
                    count = 0
                else:
                    number += (self.numerals[p_index] * count)
                    previous_char = s[i]
                    count = 1
        try:
            if previous_char != None:
                number += (count * self.numerals[self.roman_numerals.index(s[i])])
        except UnboundLocalError:
            number += self.numerals[self.roman_numerals.index(previous_char)]
            pass
        return number
