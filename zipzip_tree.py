# explanations for member functions are provided in requirements.py
# each file that uses a Zip Tree should import it from this file

from __future__ import annotations

# from typing import TypeVar
# from dataclasses import dataclass

# KeyType = TypeVar('KeyType')
# ValType = TypeVar('ValType')

# @dataclass
# class Rank:
# 	geometric_rank: int
# 	uniform_rank: int

# @dataclass
# class Node:
#     key: KeyType
#     val: ValType
#     rank: Rank
#     left: Node = None
#     right: Node = None
# 	#parent: Node = None

# class ZipZipTree:
# 	def __init__(self, capacity: int):
# 		pass

# 	def get_random_rank(self) -> Rank:
# 		pass

# 	def insert(self, key: KeyType, val: ValType, rank: Rank = None):
# 		if not rank:
# 			rank = self.get_random_rank()
# 			node_to_add = Node(key, val, rank)
# 		pass

# 	def insert_recursive(...):
# 		x.left = y
# 		self.update_node(x)


# 	def remove(self, key: KeyType):
# 		pass

# 	def find(self, key: KeyType) -> ValType:
# 		pass

# 	def get_size(self) -> int:
# 		pass

# 	def get_height(self) -> int:
# 		pass

# 	def get_depth(self, key: KeyType):
# 		pass

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
        while (r := random.randint(0,1)) != 1:  
            count += 1
        uniform = random.randint(0,int(math.log2(self.capacity**3-1)))
        return Rank(count, uniform)

    def insert(self, key: KeyType, val: ValType, rank: Rank = None):
        # if rank is None:
        #     rank = self.get_random_rank()

        # new_node = Node(key, val, rank)
        if rank is None:
            rank = self.get_random_rank()

        new_node = Node(key, val, rank)
        cur = self.root
        prev = None

        # Navigate to the appropriate position to insert the new node based on rank and key
        while cur is not None and (rank.geometric_rank < cur.rank.geometric_rank or
                                (rank.geometric_rank == cur.rank.geometric_rank and rank.uniform_rank < cur.rank.uniform_rank) or
                                (rank.geometric_rank == cur.rank.geometric_rank and rank.uniform_rank == cur.rank.uniform_rank and key < cur.key)):
            prev = cur
            if key < cur.key:
                cur = cur.left
            else:
                cur = cur.right

        # Attach new node to the tree
        if prev is None:
            self.root = new_node
        elif key < prev.key:
            prev.left = new_node
        else:
            prev.right = new_node

        # Set the initial links for the newly inserted node
        new_node.left = None
        new_node.right = None
        if cur is not None:
            if key < cur.key:
                new_node.right = cur
            else:
                new_node.left = cur

        # Fix the position of the new node in the tree, adjusting links as necessary
        fix = prev
        while cur is not None:
            fix = prev
            if cur.key < key:
                while cur is not None and cur.key < key:
                    prev = cur
                    cur = cur.right
            else:
                while cur is not None and cur.key > key:
                    prev = cur
                    cur = cur.left

            if fix.key > key or (fix == new_node and prev.key > key):
                fix.left = cur
            else:
                fix.right = cur

        self.size += 1

    def remove(self, key: KeyType):
        self.root = self._remove(self.root, key)

    def _remove(self, node: Optional[Node], key: KeyType) -> Optional[Node]:
        if node is None:
            return None
        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                # Get the minimum node in the right subtree
                min_larger_node = self._min_value_node(node.right)
                node.key = min_larger_node.key
                node.val = min_larger_node.val
                node.rank = min_larger_node.rank
                node.right = self._remove(node.right, min_larger_node.key)
        return node

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
            return 0
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