# (add 1 2)
# (mult 3 (add 2 3))
# (let x 2 (mult x 5)
# (let x 2 (mult x (let x 3 y 4 (add x y)))

# 计算表达式结果, 前两个返回3 和 15
# 第三个式子表示令x=2, 计算x * 5
# 第四个式子有两个赋值, x和y, 且在不同嵌套里有不同的赋值

# 给了三十分钟,要求编译通过. 我连parse表达式都没有写完... 另外let的情况如何处
# 理?

import re
class Solution:
    def evaluate(self, expr):
        tokens = re.split('[ ()]', expr)
        tokens = [token for token in tokens if token]
        var, stack, i = {}, [], 0
        keywords = set(['add', 'mult', 'let'])
        while i < len(tokens):
            if tokens[i] == 'add' or tokens[i] == 'mult':
                stack.append(tokens[i])
                i += 1
            elif tokens[i] == 'let':
                i += 1
                while i < len(tokens) and tokens[i] not in keywords:
                    var[tokens[i]] = int(tokens[i+1])
                    i += 2
            else:
                if tokens[i].isdigit():
                    stack.append(int(tokens[i]))
                else:
                    stack.append(var[tokens[i]])
                while len(stack) > 2 and isinstance(stack[-1], int) and isinstance(stack[-2], int):
                    num2, num1, op = stack.pop(), stack.pop(), stack.pop()
                    stack.append(self.compute(op, num1, num2))
        i += 1
        return stack[0]
        
    def compute(self, op, num1, num2):
        if op == 'add': return num1 + num2
        if op == 'mult': return num1 * num2

if __name__ == "__main__":

    sol = Solution()
    exprs = {
        '(add 1 2)': 3,
        '(mult 3 (add 2 3))': 15,
        '(let x 2 (mult x 5)': 10,
        '(let x 2 (mult x (let x 3 y 4 (add x y)))': 14,
        '(let a 2 (add a 2))': 4,
        '(let a 2 (add a let b 3 (mult b 3)))': 11
    }
    for expr, val in exprs.items():
        print(expr, val, sol.evaluate(expr))