def get_cheapest_cost(rootNode):
  # 0 nodes
  if not rootNode:
    return None
  
  # leaf nodes
  if not rootNode.children:
    return rootNode.cost
  
  min_cost = float('inf')
  for child in rootNode.children:
    temp_cost = get_cheapest_cost(child)
    if temp_cost < min_cost:
      min_cost = temp_cost
  
  return min_cost + rootNode.cost

########################################## 
# Use the helper code below to implement #
# and test your function above           #
##########################################

# A node 
class Node:

  # Constructor to create a new node
  def __init__(self, cost):
    self.cost = cost
    self.children = []
    self.parent = None

#         0
#       / \  \
#      5   3   6
#     /   / \
#    4   2   7

a = Node(0)
b = Node(5)
c = Node(3)
d = Node(6)
a.children = [b, c, d]
e = Node(4)
b.children = [e]
f = Node(2)
g = Node(7)
c.children = [f, g]
print(get_cheapest_cost(a))
