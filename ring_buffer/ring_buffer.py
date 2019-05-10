class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # if current index is less than the capacity 
    # change the value at the index to the item
    if self.current < self.capacity:
      self.storage[self.current] = item
      self.current += 1
    else:
      # if the index reaches the capacity
      # reset to 0 and replace the first
      # item in the list
      self.current = 0
      self.storage[self.current] = item
      self.current += 1

  def get(self):
    newList = []
    # create new list of items without
    # the possibility of any None values
    for i in range(len(self.storage)):
      if self.storage[i] is not None:
        newList.append(self.storage[i])
    return newList





newBuff = RingBuffer(5)

newBuff.append("a")
newBuff.append("b")
newBuff.append("c")
newBuff.append("d")
newBuff.get()
newBuff.append("e")
newBuff.get()
newBuff.append('f')
newBuff.get()
newBuff.append('g')
newBuff.append('h')
newBuff.append('i')
newBuff.get()

