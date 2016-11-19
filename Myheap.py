__author__ = 'Sanket Agarwal'
class heap:
    __slots__=('hList','currSize')

    def __init__(self):
        self.hList = [0]
        self.currSize = 0

    def insert(self,k):
        self.hList.append(k)
        self.currSize += 1
        self.percUp(self.currSize)

    def percUp(self,i):
        while i//2 > 0:
            if self.hList[i] < self.hList[i//2]:
                self.hList[i],self.hList[i // 2] = self.hList[i // 2], self.hList[i]
            i=i//2


    def delmin(self):
        ret = self.hList[1]
        self.hList[1] = self.hList[self.currSize]
        self.currSize = self.currSize-1
        self.hList.pop()
        self.percDwn(1)
        return  ret

    def percDwn(self,i):
        while 2*i <= self.currSize:
            mc = self.minChild(i)
            if self.hList[mc] < self.hList[i]:
                self.hList[mc],self.hList[i] = self.hList[i],self.hList[mc]
            i = mc



    def minChild(self,i):
        if 2*i+1 > self.currSize:
            return 2*i
        else:
            if self.hList[2*i] <  self.hList[2*i+1]:
                return 2*i
            else:
                return 2*i+1

    def buildHeap(self,list):
        i = len(list)//2
        h = self.hList + list[0:]

        while i >0:
            self.percDwn(i)
            i = i-1

def main():

    h=heap()

    h.buildHeap([90,2,1,28,900])
    print(h.currSize)
    print(h.hList)
    for i in range(h.currSize):
        print(h.delmin())



if __name__ == '__main__':
    main()


