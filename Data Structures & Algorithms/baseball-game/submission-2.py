class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        scores = []

        for operation in operations:
            try:
                score = int(operation)
            except:
                if operation == "+":
                    score = scores[-1] + scores[-2]
                if operation == "D":
                    score = scores[-1] * 2
                if operation == "C":
                    scores.pop(-1)
                    continue
            scores.append(score)
        
        return sum(scores)