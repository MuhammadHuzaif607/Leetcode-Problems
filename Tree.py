from collections import deque
class TreeNode:
    def __init__(self,val = None,right = None,left = None):
        self.val = val
        self.right = right
        self.left = left
    
    
    # Iterative Depth First Search 
    def dfs(self,root):
        stack = [root]
        while stack:
            node = stack.pop()
            print(node.val)
            if node.right : stack.append(node.right)
            if node.left : stack.append(node.left)
            
    # Iterative Breadth First Search 
    def bfs(self,root):
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.pop()
            print(node.val)
            if node.left : queue.append(node.left)
            if node.right : queue.append(node.right)
            
            
    # Recursive Depth First Search
    def pre_order(self,node):
        if not node:
            return 
        
        print(node)
        self.pre_order(node.left)
        self.pre_order(node.right)
        
    
    # Recursive In order traversal
    def in_order(self,node):
        if not node:
            return 
        
        self.in_order(node.left)
        print(node)
        self.in_order(node.right)
        
        
    # Recursive In order traversal
    def post_order(self,node):
        if not node:
            return 
        
        self.post_order(node.left)
        self.post_order(node.right)
        print(node)
        
    def array_to_btree(self, arr):
        if not arr:
            return None

        root = TreeNode(arr[0])
        queue = deque([root])
        i = 1

        while i < len(arr):
            current = queue.popleft()
            if arr[i] is not None:
                current.left = TreeNode(arr[i])
                queue.append(current.left)
            i += 1

            if i < len(arr) and arr[i] is not None:
                current.right = TreeNode(arr[i])
                queue.append(current.right)
            i += 1

        return root
           
    def max_depth(self,node):
        if not node:
            return 0
        
        return 1 + max(self.max_depth(node.right),self.max_depth(node.left))
    
tree = TreeNode()
q = [1,2,3]
p = tree.array_to_btree(q)
tree.bfs(p)