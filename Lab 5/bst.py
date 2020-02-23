"""Module for BST
CPE202

Contains the data definition of BST,
and functions (not class member methods) on BST.

Functions defined here need to be recusrive functions,
and will be used by other classes such as TreeMap as
helper functions.


Author:
    Section:
    Your Name Here
"""


class BSTNode:
    def __init__(self, key, val, left=None, right=None):
        self.val = val
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        return 'Node(%s, %s, %s, %s)' % (repr(self.key), repr(self.val), repr(self.left), repr(self.right))

    def __eq__(self, other):
        return isinstance(other, BSTNode) \
               and self.val == other.val \
               and self.key == other.key \
               and self.left == other.left \
               and self.right == other.right


# ---- to do ----
# implement the following recursive funstions
# write a docstring for each function
#
def get(tree, key) -> any:
    if tree is None:
        return None
    if tree.key == key:
        return tree.val
    if tree.key > key:
        return get(tree.left, key)
    return get(tree.right, key)


def contains(tree, key) -> bool:
    if tree is None:
        return False
    if tree.key == key:
        return True
    if tree.key > key:
        return contains(tree.left, key)
    return contains(tree.right, key)


def insert(tree, key, val) -> BSTNode:
    if tree is None:
        return BSTNode(key, val)
    if tree.key > key:
        tree.left = insert(tree.left, key, val)
    elif tree.key < key:
        tree.right = insert(tree.right, key, val)
    return tree


def delete(tree, key) -> BSTNode:
    if tree is None:
        raise KeyError
    if tree.key == key:
        if tree.left and tree.right:
            rep = get_rep(tree.right)
            tree.right = delete(tree.right, rep.key)
            tree.key = rep.key
            tree.val = rep.val
        elif tree.left:
            return tree.left
        else:
            return tree.right
    elif tree.key > key:
        tree.left = delete(tree.left, key)
    else:
        tree.right = delete(tree.right, key)
    return tree


def get_rep(tree) -> BSTNode:
    if tree is None:
        raise ValueError
    if tree.left is None:
        return tree
    return get_rep(tree.left)


def find_min(tree) -> (any, any):
    if tree is None:
        raise ValueError
    if tree.left is not None:
        return find_min(tree.left)
    return tree.key, tree.val


def find_max(tree) -> (any, any):
    if tree is None:
        raise ValueError
    if tree.right is not None:
        return find_max(tree.right)
    return tree.key, tree.val


def inorder_list(tree, accum) -> list:
    if tree is not None:
        inorder_list(tree.left, accum)
        accum.append(tree.key)
        inorder_list(tree.right, accum)
    return accum


def preorder_list(tree, accum) -> list:
    if tree is not None:
        accum.append(tree.key)
        preorder_list(tree.left, accum)
        preorder_list(tree.right, accum)
    return accum


def tree_height(tree) -> int:
    if tree is None or (not tree.left and not tree.right):
        return 0
    return 1 + max(tree_height(tree.left), tree_height(tree.right))


def range_search(tree, lo, hi) -> list:
    return helper(tree, lo, hi, [])


def helper(tree, lo, hi, accum) -> list:
    if tree is None:
        return accum
    if tree.key < lo:
        return helper(tree.right, lo, hi, accum)
    elif tree.key >= hi:
        return helper(tree.left, lo, hi, accum)
    else:
        helper(tree.left, lo, hi, accum)
        accum.append(tree.val)
        helper(tree.right, lo, hi, accum)
    return accum
