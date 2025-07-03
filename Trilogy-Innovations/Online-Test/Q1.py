import itertools
class CryptarithmicSolver:
  
    def solution(self, crypt):

        words = [word[::-1] for word in crypt]
        self.cols = list(itertools.zip_longest(*words))
        self.leading_letters = {a[0] for a in crypt if len(a) > 1}
        self.mapping = {}  
        self.used_digits = [False] * 10  
        return self.backtrack(0, 0)

    def backtrack(self, column, carry):

        if column == len(self.cols):
            return 1 if carry == 0 else 0

        total_solutions = 0
        current_col = self.cols[column]

        letter_to_allot = []
        for char in set(current_col):
            if char is not None and char not in self.mapping:
                letter_to_allot.append(char)

        available_digits = [d for d, is_used in enumerate(self.used_digits) if not is_used]

        for p in itertools.permutations(available_digits, len(letter_to_allot)):
            
            is_a_valid_permutation = True
            for letter, digit in zip(letters_to_assign, p):
                if digit == 0 and letter in self.leading_letters:
                    is_valid_perm = False
                    break
            if not is_a_valid_permutation:
                continue

            for letter, digit in zip(letter_to_allot, p):
                self.mapping[letter] = digit
                self.used_digits[digit] = True
            
            value_1 = self.mapping.get(current_col[0], 0)
            value_2 = self.mapping.get(current_col[1], 0)
            value_3 = self.mapping.get(current_col[2], 0)

            if (value_1 + value_2 + carry) % 10 == value_3:
                new_carry = (value_1 + value_2 + carry) // 10
                total_solutions += self.backtrack(column + 1, new_carry)
              
            for letter in letter_to_allot:
                digit = self.mapping[letter]
                del self.mapping[letter]
                self.used_digits[digit] = False
                
        return total_solutions
      
def solution(crypt):
  
    if len(crypt[2]) < max(len(crypt[0]), len(crypt[1])):
        return 0
        
    solver = CryptarithmicSolver()
    return solver.solution(crypt)
