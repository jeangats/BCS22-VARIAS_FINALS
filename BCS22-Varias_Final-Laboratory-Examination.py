# This algorithm uses a recursive function to traverse the tree and store nodes in a dictionary based on their horizontal distance. Then, it iterates through the dictionary and prints the nodes in their vertical order

# To represent a node in the binary tree (including its left and right child nodes)
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# This algorithm starts by traversing the tree in a level-order fashion. At each level, it assigns a horizontal distance (hd) to each node based on its position relative to the root

    # This function which takes the root node as input parameter visits each node once and inserts it into the map (O(1)) based on its horizontal distance. Thus, its time complexity is a linear time of O(n)

def vertical_order(root, hd, map):
    # Base Case
    if root is None:
        return

    # Store current node in map
        # To insert root.data at the beginning of the list if the data hd exists in the map
    try:
        map[hd].insert(0, root.data)
    except:
        map[hd] = [root.data]

    # Store nodes in left subtree
    vertical_order(root.left, hd - 1, map)

    # Store nodes in right subtree
    vertical_order(root.right, hd + 1, map)

def display_vertical_order(root):
    # Initialize an empty list to store the nodes in the order of their vertical levels
    nodes = []

    # Create a map and store the vertical order in it using the function vertical_order()
    # The hd helps determine the order of nodes at the same level. Nodes with the same horizontal distance belong to the same vertical level. The Nodes with a smaller horizontal distance appear earlier in the traversal than nodes with a larger horizontal distance. This allows us to arrange the nodes in a column-wise fashion, representing their true vertical levels.
    map = dict()
    hd = 0
    vertical_order(root, hd, map)

    # This allows the iteration from the rightmost level to the leftmost level. It iterates through the map in order of horizontal distance, retrieving and adding all nodes from each group to a final list.
    for index, value in enumerate(reversed(sorted(map))):
        for i in map[value]:
            nodes.append(i)

    # Returns and prints the array containing  the vertical order traversal of the tree from level F to A
    print(f"The vertical order traversal of the binary tree from rightmost to leftmost level is: {nodes}")
    # Print the vertical order traversal from level A to F
    print(f"The vertical order traversal of the binary tree from leftmost to rightmost level is: {nodes[::-1]}")


# Create the rest of the nodes and connect them to the appropriate parent nodes--- forming the binary tree.
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)
    root.right.right.right = Node(9)

    print("""\t\tBinary Tree
            1
          /   \\
         2     3
        / \   / \\
       4   5  6  7
               \\  \\
                8  9""")
    display_vertical_order(root)

# Overall Time Complexity: 0(n log n)
    # It is 0(n) for both the traversal of the map and to append nodes at every horizontal to the list
    # But iterating through the map and appending nodes to a list contributes to the overall time complexity. Since the dictionary is sorted based on horizontal distance, iterating through it requires logarithmic time (log n) for each level.

# Overall Space Complexity: O(n)
    # The map replicates the entire tree structure. As the number of key-value pairs (horizontal distances) is approximately equal to the number of nodes in the tree, the space complexity is O(n).