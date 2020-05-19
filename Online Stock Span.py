class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        
        count = 1
        if len(self.stack) == 0:
            self.stack.append((price, count))
            return count
        else:
            #print(self.stack,self.stack[-1][0])
 
            while len(self.stack) > 0 and price >= self.stack[-1][0]:
                count += self.stack[-1][1]
                self.stack.pop(-1)
            self.stack.append((price, count))
            return count
