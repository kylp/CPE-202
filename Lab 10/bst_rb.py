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
    def __init__(self, key, val, left=None, right=None, color='red'):
        self.val = val
        self.key = key
        self.left = left
        self.right = right
        self.color = color

    def __repr__(self):
        return 'Node(%s, %s, %s, %s, %s)' % (repr(self.key), repr(self.val), repr(self.left), repr(self.right),
                                             repr(self.color))

    def __eq__(self, other):
        return isinstance(other, BSTNode) \
               and self.val == other.val \
               and self.key == other.key \
               and self.left == other.left \
               and self.right == other.right \
               and self.color == other.color


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
    # if tree is None:
    #     return BSTNode(key, val)
    # if tree.key > key:
    #     tree.left = insert(tree.left, key, val)
    # elif tree.key < key:
    #     tree.right = insert(tree.right, key, val)
    tree = insert_helper(tree, key, val)
    tree.color = 'black'
    return tree


def rebalance(tree):
    #rrb pattern
    if tree.color == 'black' and tree.left and tree.left.color == 'red' \
            and tree.left.left and tree.left.left.color == 'red':
        #convert to brb
        return BSTNode(tree.left.key, tree.left.val, color='red',
                       left=BSTNode(tree.left.left.key, tree.left.left.val,
                                    left=tree.left.left.left, right=tree.left.left.right, color='black'),
                       right=BSTNode(tree.key, tree.val, tree.left.right, tree.right, 'black'))
    #rbr pattern
    elif tree.color =='black' and tree.left and tree.left.color =='red' \
            and tree.left.right and tree.left.right.color =='red':
        #convert to brb
        return BSTNode(tree.left.right.key, tree.left.right.val, color='red',
                       left=BSTNode(tree.left.key, tree.left.val, tree.left.left, tree.left.right.left, color='black'),
                       right=BSTNode(tree.key,tree.val, tree.left.right.right, tree.right, color='black'))

    #brr pattern
    elif tree.color =='black' and tree.right and tree.right.color =='red' \
            and tree.right.left and tree.right.left.color =='red':
        #convert to brb
        return BSTNode(tree.right.left.key, tree.right.left.val, color='red',
                       right=BSTNode(tree.right.key, tree.right.val, tree.right.left.right, tree.right.right, color='black'),
                       left=BSTNode(tree.key,tree.val, tree.left, tree.right.left.left, color='black'))
    #brr pattern
    elif tree.color =='black' and tree.right and tree.right.color =='red' \
            and tree.right.right and tree.right.right.color == 'red':
        #convert to brb
        return BSTNode(tree.right.key, tree.right.val, color='red',
                       left=BSTNode(tree.key, tree.val, tree.left, tree.right.left, 'black'),
                       right=BSTNode(tree.right.right.key, tree.right.right.val,
                                    left=tree.right.right.left, right=tree.right.right.right, color='black'))
    return tree


def insert_helper(tree, key, val) -> BSTNode:
    if tree is None:
        return BSTNode(key, val)
    if key < tree.key:
        tree.left = insert_helper(tree.left, key, val)
    else:
        tree.right = insert_helper(tree.right, key, val)
    return rebalance(tree)


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

