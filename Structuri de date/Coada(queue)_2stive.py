#Implementarea unei cozi(queue) cu 2 stive
class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, item):
        self.s1.append(item)

    def pop(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

coada = MyQueue()
coada.push(1)
print("Elementele ramase in stiva(s1):",coada.s1)
coada.push(2)
print("Elementele ramase in stiva(s1):",coada.s1)
coada.push(3)
print("Elementele ramase in stiva(s1):",coada.s1)
coada.push(4)
print("Elementele ramase in stiva(s1):",coada.s1)
coada.pop()
print("Elementele ramase in stiva(s1):",coada.s1)
print("Elementele din stiva(s2)",coada.s2)