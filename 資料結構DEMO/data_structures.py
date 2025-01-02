class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop() 
        else :
            return None

    def is_empty(self):
        return len(self.items) == 0


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)  
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0


class AVLNode:
    def __init__(self, student):
        self.student = student
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.root = None

    # 計算節點的高度
    def height(self, node):
        return node.height if node else 0

    # 計算節點的平衡因子
    def balance_factor(self, node):

        return self.height(node.left) - self.height(node.right) if node else 0

    # 左旋
    def rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        # 更新高度
        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y

    # 右旋
    def rotate_right(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        # 更新高度
        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y

    # 插入節點
    def _insert(self, node, student):
        if not node:
            return AVLNode(student)

        # 修改插入邏輯：先比成績，成績相同再比名稱
        if (student.grade < node.student.grade) or \
           (student.grade == node.student.grade and student.name < node.student.name):
            node.left = self._insert(node.left, student)
        else:
            node.right = self._insert(node.right, student)

        # 更新高度
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        # 計算平衡因子
        balance = self.balance_factor(node)

        #LL，右旋使樹重新平衡
        if balance > 1 and (student.grade < node.left.student.grade or \
                            (student.grade == node.left.student.grade and student.name < node.left.student.name)):
            return self.rotate_right(node)

        #RR，左旋使樹重新平衡
        if balance < -1 and (student.grade > node.right.student.grade or \
                             (student.grade == node.right.student.grade and student.name > node.right.student.name)):
            return self.rotate_left(node)

        #LR，對左子節點進行左旋，再對當前節點進行右旋
        if balance > 1 and (student.grade > node.left.student.grade or \
                            (student.grade == node.left.student.grade and student.name > node.left.student.name)):
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        #RL，對右子節點進行右旋，再對當前節點進行左旋
        if balance < -1 and (student.grade < node.right.student.grade or \
                             (student.grade == node.right.student.grade and student.name < node.right.student.name)):
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    # 封裝_insert()方便使用
    def insert(self, student):
        self.root = self._insert(self.root, student)

    # 反向中序遍歷，返回按排序順序的節點
    def in_order(self, node):
        if not node:
            return []
        return self.in_order(node.right) + [node.student] + self.in_order(node.left)

    # 封裝in_order()方便使用
    def in_order_traversal(self):
        return self.in_order(self.root)

    # 尋找子樹中的最小值節點
    def find_min(self, node):
        while node.left:
            node = node.left
        return node

    # 刪除節點
    def _delete(self, node, student):
        if not node:
            return node

        # 使用 (成績, 名稱) 進行匹配
        if (student.grade, student.name) < (node.student.grade, node.student.name):
            node.left = self._delete(node.left, student)
        elif (student.grade, student.name) > (node.student.grade, node.student.name):
            node.right = self._delete(node.right, student)
        else:
            # 找到節點，開始刪除邏輯1
            if not node.left:
                return node.right
            if not node.right:
                return node.left

            # 用右子樹的最小值替換節點
            temp = self.find_min(node.right)
            node.student = temp.student
            node.right = self._delete(node.right, temp.student.grade)

        # 更新節點高度
        node.height = 1 + max(self.height(node.left), self.height(node.right))

        # 計算平衡因子並調整
        balance = self.balance_factor(node)
        
         #LL，右旋平衡
        if balance > 1 and self.balance_factor(node.left) >= 0:
            return self.rotate_right(node)
        
        # RR，左旋平衡
        if balance < -1 and self.balance_factor(node.right) <= 0:
            return self.rotate_left(node)
        
        # LR，先左旋再右旋平衡
        if balance > 1 and self.balance_factor(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        
        # RL，先右旋再左旋平衡
        if balance < -1 and self.balance_factor(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    # 封裝_delete()方便使用

    def delete(self, student):
        self.root = self._delete(self.root, student)

    # 尋找指定學生
    def get_student(self, name):
        return self._get_student(self.root, name)

    # 封裝_get_student()方便使用
    def _get_student(self, node, name):
        if not node:
            return None  # 未找到目標學生

        if name == node.student.name:
            return node.student
        elif name < node.student.name:
            return self._get_student(node.left, name)
        else:
            return self._get_student(node.right, name)    
