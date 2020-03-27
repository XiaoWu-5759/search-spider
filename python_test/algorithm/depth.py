def depth_tree(tree_node):
    if tree_node is not None:
        print(tree_node._data)
        if tree_node.left is not None:
            return depth_tree(tree_node._left)
        if tree_node.right is not None:
            return depth_tree(tree_node._right)