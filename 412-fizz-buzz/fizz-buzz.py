class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n + 1):
            if i % 3 == 0:
                if i % 5 == 0:
                    answer.append("FizzBuzz")
                    continue
                answer.append("Fizz")
                continue
            elif i % 5 == 0:
                answer.append("Buzz")
                continue
            answer.append(str(i))
        return answer
