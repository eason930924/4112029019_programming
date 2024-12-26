class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0) if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0


class BinaryTreeNode:
    def __init__(self, student):
        self.student = student
        self.left = None
        self.right = None

class BinaryTree:
    class Node:
        def __init__(self, student):
            self.student = student
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, student):
        #不需要輸入node就可操作，簡化程式
        def _insert(node, student):
            if node is None:
                return self.Node(student)
            if student.grade < node.student.grade:
                node.left = _insert(node.left, student)
            elif student.grade > node.student.grade:
                node.right = _insert(node.right, student)
            return node

        self.root = _insert(self.root, student)

    def in_order_traversal(self):
        #不需要輸入node就可操作，簡化程式
        def _in_order(node):
            if not node:
                return []
            return _in_order(node.left) + [node.student] + _in_order(node.right)

        return _in_order(self.root)

    def delete(self, grade):
        #不需要輸入node就可操作，簡化程式
        def _delete(node, grade):
            if not node:
                return node

            if grade < node.student.grade:
                node.left = _delete(node.left, grade)
            elif grade > node.student.grade:
                node.right = _delete(node.right, grade)
            else:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left

                temp = self.find_min(node.right)
                node.student = temp.student
                node.right = _delete(node.right, temp.student.grade)

            return node

        self.root = _delete(self.root, grade)

    def find_min(self, node):
        while node.left:
            node = node.left
        return node
