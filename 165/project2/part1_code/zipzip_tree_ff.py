from dataclasses import dataclass
from typing import Optional, List
from zipzip_tree import ZipZipTree, Node, Rank, KeyType
from decimal import Decimal, getcontext


@dataclass
class FFVal:
    remaining_capacity: Decimal
    best_remaining_capacity: Decimal

class ZipZipTreeFF(ZipZipTree):
    def __init__(self, capacity: int):
        super().__init__(capacity)
        getcontext().prec = 6

    def update_node(self, node: Node):
        best_on_left_side = node.left.val.best_remaining_capacity if node.left else Decimal(0)
        best_on_right_side = node.right.val.best_remaining_capacity if node.right else Decimal(0)
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
        
    
    def find_first_fit(self, item_size: float) -> Optional[Node]:
        current = self.root
        best_fit = None

        while current is not None:
            left_best = current.left.val.best_remaining_capacity if current.left else Decimal(0)
            right_best = current.right.val.best_remaining_capacity if current.right else Decimal(0)

            # If the left subtree has a bin that can fit the item, go left
            if left_best >= item_size:
                current = current.left
            elif current.val.remaining_capacity >= item_size:
                # Check the current node's bin
                best_fit = current
                break
            elif right_best >= item_size:
                # If the right subtree has a bin that can fit the item, go right
                current = current.right
            else:
                break

        return best_fit        

