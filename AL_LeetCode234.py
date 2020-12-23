import List
import List_Comprehension

import collections

def isPalindeom(head) -> bool:
  q: List = []
  if not head:
    return False
  
  node = head
  while len(node) is not 0:
    q.append(node.pop(0))
  while len(q) > 1:
    if q.pop(0) != q.pop():
      return False
  return True


def isPalindeom2(head) -> bool:
  q: Deque = collections.deque()
  if not head:
      return False

  node = head
  while node is not None:
      q.append(node.value)
      node =node.next

  while len(q) > 1:
      if q.popleft() != q.pop():
          return False
  return True


head = [1,2]

print(isPalindeom2(head))

head = [1,2,2,1]

print(isPalindeom2(head))