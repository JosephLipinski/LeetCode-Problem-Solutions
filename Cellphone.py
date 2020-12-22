class CellPhone:
    num_to_letter = {
        "1": [],
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }
    
    def letterCombinations(self, digits: str) -> list[str]:
        chars = []
        for d in digits:
            chars.append(self.num_to_letter[d])
        words = []
        first_instance = True
        for char_set in chars:
            result = []
            for letter in char_set:
                if first_instance:
                    words.append(letter)
                else:
                    for w in words:
                        result.append(w+letter)
            if not first_instance:
                words = result
            first_instance = False
        return words
