#  File: Josephus.py

#  Description: Make a circular linked list to solve Josephus problem.

#  Date Created: 10/12/2021

#  Date Last Modified: 10/18/2021
import sys

class Link(object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next
  
  def __str__(self):
    return (f"{self.data}")


class CircularList(object):
  # Constructor
  def __init__ ( self ):
    self.length = 0
    self.head = None
    self.tail = None

  # Insert an element (value) in the list
  def insert ( self, data ):
    self.length += 1
    new_link = Link(data)
    current = self.head
    if current == None:
      self.head = new_link
      self.tail = new_link
    else:
      new_link.next = self.head
      self.tail.next = new_link
      self.tail = new_link

  # Find the Link with the given data (value)
  # or return None if the data is not there
  def find ( self, data ):
    current = self.head
    if (self.head == None):
      return None
    else:
      while (current.data != data):
        if (current == self.tail):
          return None
        current = current.next
    return current


  # Delete a Link with a given data (value) and return the Link
  # or return None if the data is not there
  def delete ( self, data ):
    if self.head == None:
      return None
    self.length -= 1
    previous = self.head
    current = self.head
    
    while previous.next != self.head:
      previous = previous.next
    if current.data == data:
      previous.next = current.next
    current = current.next
    previous = previous.next
    
    while current.data != data and current != self.head:
      current = current.next
      previous = previous.next
    if current.data == data:
      previous.next = current.next
    return current

  # Delete the nth Link starting from the Link start
  # Return the data of the deleted Link AND return the
  # next Link after the deleted Link in that order
  def delete_after ( self, start, n ):
    self.length -= 1
    previous = self.head 
    current = start
    if self.head == None:
      return None
    while (n - 1 > 0):
      previous = current
      current = current.next
      n -= 1
    previous.next = current.next
    
    if current == self.head:
      self.head = previous.next
    elif current == self.tail:
      self.tail = previous
    
    print(current)
    return current.next

  # Return a string representation of a Circular List
  # The format of the string will be the same as the __str__
  # format for normal Python lists
  def __str__ ( self ):
    current = self.head
    previous = self.head
    str_list = []
    
    while (previous != self.tail):
      str_list.append(str(current.data))
      previous = current
      current = current.next
    return ('[' + ', '.join(str_list) + ']')

    

def main():
  # read number of soldiers
  line = sys.stdin.readline()
  line = line.strip()
  num_soldiers = int (line)

  # read the starting number
  line = sys.stdin.readline()
  line = line.strip()
  start_count = int (line)

  # read the elimination number
  line = sys.stdin.readline()
  line = line.strip()
  elim_num = int (line)

  # your code
  # creates circular list of soldiers by using for loop to insert each integer
  soldiers = CircularList()
  for i in range (0, num_soldiers):
    [soldiers.insert(i+1)]
  # start count for the delete after function
  order_of_elim = soldiers.find(start_count)
  # uses start count for start and elim_num variable as the n value
  # prints order of elimination using delete after function
  while soldiers.length > 0:
    order_of_elim = soldiers.delete_after(soldiers.find(order_of_elim.data), elim_num)
if __name__ == "__main__":
  main()

