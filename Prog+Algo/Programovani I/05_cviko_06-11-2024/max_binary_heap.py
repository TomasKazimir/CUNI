class MaxBinaryHeap:
    def __init__(self):
        self.h = []
    
    def max(self):
        """Returns maximal value"""
        return self.h[0]
    
    def del_max(self):
        """Deletes and returns max value"""
        if len(self.h) == 0:
            return 0
        m = self.h[0]
        self.h[0] = self.h.pop()
        
        i = 0
        while 2*i + 1 < len(self.h):
            child_index = 2*i + 1
            if child_index < len(self.h) - 1:
                if self.h[child_index+1] > self.h[child_index]:
                    child_index += 1
            if self.h[i] < self.h[child_index]:
                self.h[i], self.h[child_index] = self.h[child_index], self.h[i]
                i = child_index
            else:
                break

        return m
    
    def add(self, value):
        """Adds new value into heap"""
        self.h.append(value)
        
        j = len(self.h) - 1
        while j > 0 and self.h[j] > self.h[(j-1)//2]:
            self.h[j], self.h[(j-1)//2] = self.h[(j-1)//2], self.h[j]
            j = (j-1)//2

heap = MaxBinaryHeap()
heap.add(1)
heap.add(2)
heap.add(3)
heap.add(4)
heap.add(2)
heap.add(1)
heap.add(10)
heap.add(7)
print(heap.h)
print(heap.del_max())
print(heap.del_max())
print(heap.del_max())
print(heap.del_max())
print(heap.del_max())
print(heap.del_max())
print(heap.del_max())
print(heap.del_max())

# """napis funkci, ktera setridi sestupne pole. Vime, ze kazdy prvek ve vstupnim poli je od sve cilove pozice vzdalen max k pozic"""
# k = 3
# #    8 7 6 5 4 3 2 1 0
# p = [8,6,5,7,3,4,0,1,2]

# heap = MaxBinaryHeap()
# for i in range(min(k, len(p))):
#     heap.add(p[i])

# if k < len(p):
#     for i in range(k, len(p)):
#         p[i - k] = heap.max()
#         heap.del_max()
#         heap.add(p[i])
# m = len(heap.h)
# for i in range(m):
#     p[-(m-i)] = heap.max()
#     heap.del_max()

# print(p)
