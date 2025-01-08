from student import Student
from data_structures import Stack, Queue, AVLTree
import os

DATA_FILE = "students.txt"

class StudentService:
    def __init__(self):
        self.tree = AVLTree()  # 高度平衡二元樹
        self.batch_queue = Queue()  # 佇列用於批次操作
        self.history = Stack()  # 記錄歷史操作

    # 讀取資料
    def load_data(self):
        if not os.path.exists(DATA_FILE):
            return
        with open(DATA_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                name, grade = line.split(",")
                grade = int(grade)
                student = Student(name, grade)
                self.tree.insert(student)
        print("資料已載入。")

    # 儲存資料
    def save_data(self):
        with open(DATA_FILE, "w") as file:
            for student in self.tree.in_order_traversal():
                file.write(f"{student.name},{student.grade}\n")
        print("資料已保存。")

    # 新增學生
    def add_student(self, name, grade):
        if self.tree.get_student(name) is not None:
            print("學生已存在！")
            return
        
        student = Student(name, grade)
        self.tree.insert(student)
        self.history.push(("add", student))
        print(f"已新增學生：{student}")

    # 更新學生成績
    def update_student(self, name, new_grade):
        old_grade = self.tree.get_student(name)
        if old_grade is None:
            print("學生不存在！")
            return

        self.tree.delete(name)
        updated_student = Student(name, new_grade)
        self.tree.insert(updated_student)
        self.history.push(("update", updated_student, old_grade))
        print(f"已更新學生 {name} 的成績為 {new_grade}")

    # 刪除學生
    def delete_student(self, name):
        old_grade = self.tree.get_student(name)
        if old_grade is None:
            print("學生不存在！")
            return

        student = Student(name, old_grade)
        self.tree.delete(name)
        self.history.push(("delete", student))
        print(f"已刪除學生：{student}")

    # 顯示指定學生成績
    def get_student(self, name):
        grade = self.tree.get_student(name)
        if grade is not None:
            print(f"{name}: {grade}")
        else:
            print("學生不存在！")

    # 顯示所有學生成績
    def display_students(self):
        print("所有學生（按成績排序）:")
        for student in self.tree.in_order_traversal():
            print(student)

    # 回復上一步操作
    def undo(self):
        if self.history.is_empty():
            print("無操作可復原！")
            return

        action = self.history.pop()

        if action[0] == "add":
            student = action[1]
            self.tree.delete(student.name)
            print(f"已復原新增操作：刪除學生 {student}")

        elif action[0] == "update":
            student, old_grade = action[1], action[2]
            self.tree.delete(student.name)
            student.grade = old_grade
            self.tree.insert(student)
            print(f"已復原更新操作：恢復學生 {student.name} 的成績為 {old_grade}")

        elif action[0] == "delete":
            student = action[1]
            self.tree.insert(student)
            print(f"已復原刪除操作：恢復學生 {student}")
    
    #批次新增學生資料
    def batch_add(self, batch_data):
        pairs = batch_data.split(";")
        for pair in pairs:
            try:
                name, grade = pair.split(",")
                name = name.strip()
                grade = int(grade)
                if 0 <= grade <= 100:
                    self.batch_queue.enqueue(Student(name, grade))
                else:
                    print(f"成績 {grade} 超出範圍，略過 {name}！")
            except ValueError:
                print(f"格式錯誤，略過資料：{pair}")
        while not self.batch_queue.is_empty():
            student = self.batch_queue.dequeue()
            self.add_student(student.name, student.grade)
