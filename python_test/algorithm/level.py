"""利用队列实现树的广度优先遍历"""
def level_queue(root):
    if root is None:
        return
    my_queue = []
    node = root
    my_queue.append(node)
    # 循环队列
    while my_queue:
        node = my_queue.pop(0)
        print(node.elem)
        if node.lchid is not None:
            my_queue.append(node.lchild)
        if node.rchild is not None:
            my_queue.append(node.rchild)