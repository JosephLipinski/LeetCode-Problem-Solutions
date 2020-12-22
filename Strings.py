class Strings:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
        
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        if len(strs) > 1:
            sorted_list = sorted(strs)
            for i in range(0, len(sorted_list[0])):
                try:
                    chars = [s[:i+1] for s in sorted_list]
                except IndexError:
                    chars = [s[:i] for s in sorted_list]
                if len(set(chars)) == 1:
                    prefix += sorted_list[0][i]
            pass
        elif len(strs):
            prefix = strs[0]
        else:
            pass
        
        return prefix
