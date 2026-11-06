class ProductOfNumbers(object):

    def __init__(self):
        self.prefix=[1]
        self.len=1
        
        

    def add(self, num):
        if num == 0:
          self.prefix = [1]
          self.len = 1
        else:

          self.prefix.append(self.prefix[-1]*num)
          self.len=self.len+1
        
        

    def getProduct(self, k):
        if k >= len(self.prefix):
            return 0
        return self.prefix[self.len-1]//self.prefix[self.len-1-k]
