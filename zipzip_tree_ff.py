from dataclasses import dataclass

from zipzip_tree import ZipZipTree, Node

@dataclass
class FFVal:
    remain_capacity: float
    best_remaining_capacity: float

class ZipZipTreeFF(ZipZipTree):
    def update_node(self, node: Node):
        best_on_left_side = node.left.val.best_remaining_capacity if node.left else 0
        myself = node.val.remaining_capacity

        return max(...)