class Solution:

    # A helper function to make the algorithm of dynamicProgrammingApproach more understandible.
    def print_dp(self, dp):
        for row in dp:
            print(row)

    # The Most Efficient Solution According to the Solution Section
    def dynamicProgrammingApproach(self, s, p):
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        # Assume that a solution can be found
        dp[-1][-1] = True
        # Populate the decisions of the matrix to reflect our decision history
        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                # i < len(s)          Check that we are not in padding column
                # p[j] in {s[i], '.'} Check if we are matching the character 
                first_match = i < len(s) and p[j] in {s[i], '.'}
                # j+1 < len(p) Check that we are not in the padding column
                # p[j+1]       Check if the previous character was "*" 
                if j+1 < len(p) and p[j+1] == '*':
                    result = dp[i][j+2] or first_match and dp[i+1][j]
                    dp[i][j] = result 
                    if result:
                        print(i, j)
                        self.print_dp(dp)
                else:
                    # First match explained at assignment
                    # dp[i+1][j+1] Check down right of current position i.e. the previous character matched
                    result = first_match and dp[i+1][j+1]
                    dp[i][j] = result
                    if result:
                        print(i, j)
                        self.print_dp(dp)
                

        return dp[0][0]
    
    # If the language has in built regex why not use it
    def regexMatch(self, s, p):
        
        import re

        x = re.search(p, s)
        try:
            group_0 = (x.group(0))
            print(group_0)
            if group_0 == s:
                return True
            else: 
                return False
        except AttributeError:
            return False
    
    def make_pattern_stack(self, pattern_string: str) -> list:
        p_stack = []
        asterisk_at = list(filter(lambda x: x != None, list(set([i if pattern_string[i] == "*" else None for i in range(0, len(pattern_string))]))))
        
        p_stack = [pattern_string[i] if i+1 not in asterisk_at and i not in asterisk_at 
                                     else (pattern_string[i], "*") if  i not in asterisk_at else None for i in range(0, len(pattern_string))]
        p_stack = list(filter(lambda a: a != None, p_stack))
        
        return p_stack
    
    # My solution a bit cumbersome and slow but working
    def isMatch(self, s, p):
        s_stack = [s_0 for s_0 in s]
        p_stack = self.make_pattern_stack(p)
        p_stack_tupleless = list(filter(lambda x: not isinstance(x, tuple), p_stack))

        # Case 1 p has extraneous characters
        tupleless_difference = list(set(p_stack_tupleless).difference(set(s_stack)))
        
        for diff in tupleless_difference:
            if diff not in s_stack and diff != ".":
                print("BROKEN IN CASE 1")
                return False
        
        # Case 2 p is not large enough to fully cover s
        if len(s_stack) > len(tupleless_difference):
            extra_characters = list(set(tupleless_difference).difference(set(s_stack)))
            for char in extra_characters:
                if (char, "*") not in p_stack and char != ".":
                    print(char)
                    print("BROKEN IN CASE 2")
                    return False
                
            
        # Case 3 We have to recurse
        if s_stack != [] and p_stack != []:
            s_head = s_stack[0]
            p_head = p_stack[0]

            if isinstance(p_head, tuple):
                p_character = p_head[0]
                if p_character == "." or p_character == s_head:
                    return self.isMatch(s[1:], p[2:]) or self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
                else:
                    return self.isMatch(s, p[2:]) 

            else:
                if s_head == p_head or p_head == ".":
                    return self.isMatch(s[1:], p[1:])
                else:
                    return False    
                
        elif s_stack == [] and p_stack == []:
            return True
        elif p_stack != []:
            return False if False in [isinstance(p_0, tuple) for p_0 in p_stack] else True
        else:
            return False


if __name__ == "__main__":
    solution = Solution()
    string = "mississippi" 
    pattern = "mis*is*ip*i"
    solution.dynamicProgrammingApproach(string, pattern)
