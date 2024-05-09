from dataclasses import dataclass
from typing import Optional, List
from zipzip_tree import ZipZipTree, Node, Rank, KeyType

@dataclass
class FFVal:
    remaining_capacity: float
    best_remaining_capacity: float

class ZipZipTreeFF(ZipZipTree):
    def __init__(self, capacity: int):
        super().__init__(capacity)

    def update_node(self, node: Node):
        best_on_left_side = node.left.val.best_remaining_capacity if node.left else 0
        best_on_right_side = node.right.val.best_remaining_capacity if node.right else 0
        myself = node.val.remaining_capacity

        node.val.best_remaining_capacity = max(myself,best_on_left_side,best_on_right_side)
    
    def insert(self, key: KeyType, val: FFVal, rank: Rank = None):
        super().insert(key, val,rank)
        self.update_tree(key) 

    def update_tree(self, key: KeyType):
        current = self.root
        stack = []

        while current is not None:
            stack.append(current)
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                break
        
        while stack:
            node = stack.pop()
            self.update_node(node)
        
    
    def find_best_fit(self, item_size: float) -> Optional[Node]:
        current = self.root
        best_fit = None

        while current is not None:
            if current.val.remaining_capacity >= item_size - 1e-9 or self.is_equal(current.val.remaining_capacity,item_size):
                best_fit = current
                current = current.left
            else:
                current = current.right
        
        return best_fit
    
    def is_equal(self,l: float, r: float) -> bool:
        if abs(l - r) > 1e-9:
            return False
        return True


        
        


