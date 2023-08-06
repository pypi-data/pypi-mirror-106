class SnapshootableStack(object):
    def __init__(self):
        self.stack = []
        
    def pop(self):
        return self.stack.pop()
    
    def push(self, item):
        self.stack.append(item)
    
    def snapshot(self):
        return self.stack.copy()
