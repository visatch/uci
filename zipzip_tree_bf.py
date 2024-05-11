from dataclasses import dataclass
from typing import Optional
from zipzip_tree import ZipZipTree, Node, Rank, KeyType
from decimal import Decimal, getcontext


@dataclass
class BFVal:
    remaining_capacity: Decimal
    best_remaining_capacity: Decimal


class ZipZipTreeBF(ZipZipTree):
    def __init__(self, capacity: int):
        super().__init__(capacity)
        getcontext().prec = 6

    def update_node(self, node: Node):
        best_on_left_side = node.left.val.best_remaining_capacity if node.left else Decimal(0)
        best_on_right_side = node.right.val.best_remaining_capacity if node.right else Decimal(0)
        myself = node.val.remaining_capacity

        node.val.best_remaining_capacity = max(myself, best_on_left_side, best_on_right_side)
    
    def insert(self, key: KeyType, val: BFVal, rank: Rank = None):
        super().insert(key, val, rank)
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
    
    def find_best_fit(self, item_size: Decimal) -> Optional[Node]:
        # current = self.root
        # best_fit = None

        # while current is not None:
        #     left_best = current.left.val.best_remaining_capacity if current.left else Decimal(0)
        #     if current.val.remaining_capacity >= item_size:
        #         if best_fit is None or current.val.remaining_capacity < best_fit.val.remaining_capacity:
        #             best_fit = current
        #     if left_best >= item_size:
        #         current = current.left
        #     else:
        #         current = current.right

        # return best_fit
        best_fit = None
        current = self.root

        while current is not None:
            if current.val.remaining_capacity >= item_size:
                # If current node can fit the item, check if it is a better fit than the current best fit
                if best_fit is None or current.val.remaining_capacity < best_fit.val.remaining_capacity:
                    best_fit = current

            # Explore both left and right subtrees if they have a best remaining capacity that can fit the item
            if current.left and current.left.val.best_remaining_capacity >= item_size:
                current = current.left
            elif current.right and current.right.val.best_remaining_capacity >= item_size:
                current = current.right
            else:
                break

        return best_fit