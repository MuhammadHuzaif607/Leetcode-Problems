from collections import deque
class TreeNode:
    def __init__(self,val = 0,right = None,left = None):
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
    
    
    def isSame(self,p,q):
        if p == None and q == None:
            return True
        
        elif p == None or q == None:
            return False
        
        return p.val == q.val and (self.isSame(p.left,q.left)) and (self.isSame(p.right,q.right))


    def Invert_Binary_Tree(self,root):
        if root.left == None and root.right == None:
            return root
        
        root.left,root.right = root.right,root.left
        
        self.Invert_Binary_Tree(root.left)
        self.Invert_Binary_Tree(root.right)
        return root


    def flatten(self,root):
        stack = [root]
        head = TreeNode()
        gv = head
        while stack:
            node = stack.pop()
            head.right = node
            head = head.right
            if node.right : stack.append(node.right)
            if node.left : stack.append(node.left)
            
        return gv.right


    def isSymmetric(self, root):
        def dfs(left,right):
            if left == None and right == None:
                return None
            if left == None or right == None:
                return False

            return left.val == right.val and (dfs(left.left,right.right)) and (dfs(left.right,right.left))
        
        
    def Path_Sum(self,root,targetSum):
        def pathsum(root,sum,targetSum):
            
            sum += root.val
            if sum == targetSum:
                return True
            
            
            if root.left == None and root.right == None:
                return 
            
           
            
            return pathsum(root.left,sum,targetSum)
            return pathsum(root.right,sum,targetSum)
            
            return False
            
        
        return pathsum(root,0,targetSum)
        

    
tree = TreeNode()
q_arr = [5,1,4]
root = tree.array_to_btree(q_arr)
# tree.dfs(root)
print(tree.Path_Sum(root,9))

