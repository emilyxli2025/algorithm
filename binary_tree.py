from enum import Enum

class VisitOrder(Enum):
    PreOrder = -1
    InOrder = 0
    PostOrder = 1
    
class TreeNode():
    
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


class BinaryTree():
    
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.value:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        return self._search_recursive(self.root, key)
        
    def _search_recursive(self, node, key):
        if node is None or node.value == key:
            return node
        
        if node.value > key:
            return self._search_recursive(node.right, key)
        
        return self._search_recursive(node.right, key)
    
    def print(self, order: VisitOrder):
        if order == VisitOrder.PreOrder:
            self._print_preorder_recursive(self.root)
        elif order == VisitOrder.InOrder:
            self._print_inorder_recursive(self.root)
        elif order == VisitOrder.PostOrder:
            self._print_postorder_recursive(self.root)

    def _print_preorder_recursive(self, node):
        if node is None:
            return
        
        print(node.value)
        self._print_preorder_recursive(node.left)
        self._print_preorder_recursive(node.right)

    def _print_inorder_recursive(self, node):
        if node is None:
            return
        
        self._print_inorder_recursive(node.left)
        print(node.value)
        self._print_inorder_recursive(node.right)

    def _print_postorder_recursive(self, node):
        if node is None:
            return
        
        self._print_postorder_recursive(node.left)
        self._print_postorder_recursive(node.right)
        print(node.value)


tree = BinaryTree()
for x in [96,7,4,2,5,8,9,24,85]:
    tree.insert(x)

tree.print(VisitOrder.InOrder)
        