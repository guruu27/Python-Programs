class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        combinations =['']

        for digit in digits:
            new_comb = []
            for combn in combinations:
                for letter in phone_map[digit]:
                    new_comb.append(combn+letter)
            combinations=new_comb
        
        return combinations
