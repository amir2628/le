class RingBuffer:
    # not-yet-full
    def __init__(self,size_max):
        self.max = size_max
        self.data = []

    class __Full:
        #full
        def append(self, x):
            #overwriting the oldest element
            self.data[self.cur] = x
            self.cur = (self.cur+1) % self.max
        def get(self):
            #list of elements in correct order
            return self.data[self.cur:]+self.data[:self.cur]

    def append(self,x):
        #append element at the end of the buffer
        self.data.append(x)
        if len(self.data) == self.max:
            self.cur = 0
            # Permanently change self's class from non-full to full
            self.__class__ = self.__Full

    def get(self):
        #list of elements from the oldest to the newest
        return self.data

if __name__=='__main__':
    x=RingBuffer(5)
    x.append(1); x.append(2); x.append(3); x.append(4)
    print x.__class__, x.get(  )
    x.append(5)
    print x.__class__, x.get(  )
    x.append(6)
    print x.data, x.get(  )
    x.append(7); x.append(8); x.append(9); x.append(10)
    print x.data, x.get(  )