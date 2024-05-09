# explanations for member functions are provided in requirements.py
# each file that uses a Zip Tree should import it from this file

from __future__ import annotations
import math, random
from typing import TypeVar, Optional
from dataclasses import dataclass

KeyType = TypeVar('KeyType')
ValType = TypeVar('ValType')

@dataclass
class Rank:
    geometric_rank: int
    uniform_rank: int

class Node:
    def __init__(self, key: KeyType, val: ValType, rank: Rank):
        self.key = key
        self.val = val
        self.rank = rank
        self.left: Optional[ZipZipTree.Node] = None
        self.right: Optional[ZipZipTree.Node] = None

class ZipZipTree:
    def __init__(self, capacity: int):
        self.root: Optional[ZipZipTree.Node] = None
        self.capacity = capacity
        self.size = 0

    def get_random_rank(self) -> Rank:
        count = 0
        while random.randint(0,1) != 1:  
            count += 1
        uniform = random.randint(0,int(math.log2(self.capacity)**3-1))
        return Rank(count, uniform)

    def insert(self, key: KeyType, val: ValType, rank: Rank = None):
        if rank is None:
            rank = self.get_random_rank()

        new_node = Node(key, val, rank)
        cur = self.root
        prev = None

        # Navigate to the appropriate position to insert the new node based on rank and key
        while cur is not None and (rank.geometric_rank < cur.rank.geometric_rank or
                                (rank.geometric_rank == cur.rank.geometric_rank and rank.uniform_rank < cur.rank.uniform_rank) or
                                (rank.geometric_rank == cur.rank.geometric_rank and rank.uniform_rank == cur.rank.uniform_rank and key > cur.key)):
            prev = cur
            if key < cur.key:
                cur = cur.left
            else:
                cur = cur.right
        
        if cur == self.root:
            self.root = new_node
        elif new_node.key < prev.key:
            prev.left = new_node
        else:
            prev.right = new_node
        
        # Set the initial links for the newly inserted node
        if cur is None:
            new_node.left = new_node.right = None
            self.size += 1
            return
        if key < cur.key:
            new_node.right = cur
        else:
            new_node.left = cur
        
        prev = new_node
        while cur is not None:
            fix = prev
            if cur.key < key:
                while cur is not None and cur.key <= key:
                    prev = cur
                    cur = cur.right
            else:
                while cur is not None and cur.key >= key:
                    prev = cur
                    cur = cur.left

            if fix.key > key or (fix.key == new_node.key and prev.key > key):
                fix.left = cur
            else:
                fix.right = cur

        self.size += 1

    def remove(self, key: KeyType):
        if self.root is None:
            return

        cur = self.root
        prev = None

        # Find the node to delete
        while cur is not None and key != cur.key:
            prev = cur
            if key < cur.key:
                cur = cur.left
            else:
                cur = cur.right

        if cur is None:
            return  # Node to delete not found

        left = cur.left
        right = cur.right

        if left is None:
            cur = right
        elif right is None:
            cur = left
        elif self.compare_rank_gt(left, right):
            cur = left
        else:
            cur = right

        # Update root or parent's child reference
        if self.root.key == key:
            self.root = cur
        elif key < prev.key:
            prev.left = cur
        else:
            prev.right = cur

        # Fix the structure after deletion
        while left is not None and right is not None:
            if self.compare_rank_gt(left, right):
                while left is not None and self.compare_rank_gt(left, right):
                    prev = left
                    left = left.right
                prev.right = right
            else:
                while right is not None and self.compare_rank_lt(left, right):
                    prev = right
                    right = right.left
                prev.left = left

        self.size -= 1 
       
    def compare_rank_gt(self,left: Node, right: Node):
        return left.rank.geometric_rank > right.rank.geometric_rank \
            or (left.rank.geometric_rank == right.rank.geometric_rank and left.rank.uniform_rank > right.rank.uniform_rank) \
            or (left.rank.geometric_rank == right.rank.geometric_rank and left.rank.uniform_rank == right.rank.uniform_rank and left.key > right.key)
    
    def compare_rank_lt(self,left: Node, right: Node):
        return left.rank.geometric_rank < right.rank.geometric_rank \
            or (left.rank.geometric_rank == right.rank.geometric_rank and left.rank.uniform_rank < right.rank.uniform_rank) \
            or (left.rank.geometric_rank == right.rank.geometric_rank and left.rank.uniform_rank == right.rank.uniform_rank and left.key < right.key)


    def _min_value_node(self, node: Node) -> Node:
        current = node
        while current.left is not None:
            current = current.left
        return current

    def find(self, key: KeyType) -> Optional[ValType]:
        current = self.root
        while current is not None:
            if key == current.key:
                return current.val
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None

    def get_size(self) -> int:
        return self.size

    def get_height(self) -> int:
        return self._get_height(self.root)

    def _get_height(self, node: Optional[Node]) -> int:
        if node is None:
            return -1
        else:
            left_height = self._get_height(node.left)
            right_height = self._get_height(node.right)
            return max(left_height, right_height) + 1

    def get_depth(self, key: KeyType) -> int:
        return self._get_depth(self.root, key, 0)

    def _get_depth(self, node: Optional[Node], key: KeyType, depth: int) -> int:
        if node is None:
            return -1
        if key == node.key:
            return depth
        elif key < node.key:
            return self._get_depth(node.left, key, depth + 1)
        else:
            return self._get_depth(node.right, key, depth + 1)
        
    def print_tree(self):
        if self.root is None:
            print("Tree is empty")
        else:
           self._print_tree(self.root,0)
    
    def _print_tree(self, node: Optional[Node],depth: int):
        if node is not None:
            self._print_tree(node.right, depth + 1)
            print("    " * depth + f"({node.key},{node.val} rank: ({node.rank.geometric_rank}, {node.rank.uniform_rank}))")
            self._print_tree(node.left, depth + 1)