class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class GameSession:
    def __init__(self, seed):
        self.seed = seed
        self.head = None
        self.values = set()
        self.score = 0

    def guess(self, value):
        if value in self.values:
            return False
        self.values.add(value)
        self.head = Node(value, self.head)
        self.score += 1
        return True

    def history(self):
        result, current = [], self.head
        while current:
            result.append(current.value)
            current = current.next
        return result[::-1]
