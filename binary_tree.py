class Node:
    """
    Node in a Binary Tree
    """

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    """
    Binary Tree Data Structure
    """

    def __init__(self):
        self.root = None

    def insert(self, val: int) -> None:
        """
        Inserts a new node with the given value into the binary tree.
        """
        if not self.root:
            self.root = Node(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val: int, node: Node) -> None:
        """
        Recursively inserts a new node with the given value into the binary tree.
        """
        if val < node.val:
            if node.left:
                self._insert(val, node.left)
            else:
                node.left = Node(val)
        else:
            if node.right:
                self._insert(val, node.right)
            else:
                node.right = Node(val)

    def inorder_traversal(self) -> list:
        """
        Makes an in-order traversal of the binary tree and returns the nodes in a list.
        """
        traversal = []
        self._inorder_traversal(self.root, traversal)
        return traversal

    def _inorder_traversal(self, node: Node, traversal: list) -> None:
        """
        Recursively makes an in-order traversal of the binary tree and appends the nodes to the given result list.
        """
        if not node:
            return
        self._inorder_traversal(node.left, traversal)
        traversal.append(node.val)
        self._inorder_traversal(node.right, traversal)

    def preorder_traversal(self) -> list:
        """
        Makes a pre-order traversal of the binary tree and returns the nodes in a list.
        """
        traversal = []
        self._preorder_traversal(self.root, traversal)
        return traversal

    def _preorder_traversal(self, node: Node, traversal: list) -> None:
        """
        Recursively makes a pre-order traversal of the binary tree and appends the nodes to the given result list.
        """
        if not node:
            return
        traversal.append(node.val)
        self._preorder_traversal(node.left, traversal)
        self._preorder_traversal(node.right, traversal)

    def postorder_traversal(self) -> list:
        """
        Makes a post-order traversal of the binary tree and returns the nodes in a list.
        :return:
        """
        traversal = []
        self._postorder_traversal(self.root, traversal)
        return traversal

    def _postorder_traversal(self, node: Node, traversal: list) -> None:
        """
        Recursively makes a post-order traversal of the binary tree and appends the nodes to the given result list.
        """
        if not node:
            return
        self._preorder_traversal(node.left, traversal)
        self._preorder_traversal(node.right, traversal)
        traversal.append(node.val)


b_tree = BinaryTree()

count_of_nodes = int(input("Input number of nodes: "))

for i in range(count_of_nodes):
    node_value = int(input(f"Input {i}th node's value: "))
    b_tree.insert(node_value)

result = b_tree.postorder_traversal()
print("Binary tree with post_order traversal", b_tree.postorder_traversal())
print("Binary tree with pre_order traversal", b_tree.preorder_traversal())
print("Binary tree with in_order traversal", b_tree.inorder_traversal())
