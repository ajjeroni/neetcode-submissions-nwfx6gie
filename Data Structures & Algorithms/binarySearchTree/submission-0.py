class TreeNode:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

class TreeMap:
    
    def __init__(self):
        self.map = {}
        self.root = None

    def insert(self, key: int, val: int) -> None:
        if not self.root:
            self.root = TreeNode(key)
            self.map[key] = val
            return 

        if key in self.map:
            self.map[key] = val
            return
        
        def _insertBST(node, key):
            if not node: return TreeNode(key)

            if node.key < key:
                node.right = _insertBST(node.right, key)
            else:
                node.left = _insertBST(node.left, key)
            
            return node
            
        self.map[key] = val
        _insertBST(self.root, key)
        

    def get(self, key: int) -> int:
        if key in self.map: return self.map[key]

        return -1

    def getMin(self) -> int:
        if not self.root: return -1

        curr = self.root

        while curr and curr.left:
            curr = curr.left
        
        return self.map[curr.key]
        

    def getMax(self) -> int:
        if not self.root: return -1

        curr = self.root

        while curr and curr.right:
            curr = curr.right

        return self.map[curr.key]

    def remove(self, key: int) -> None:
        if key not in self.map or not self.root: return

        def _getMin(node):
            while node and node.left:
                node = node.left

            return node

        def _removeNode(node, key):
            if not node: return None

            if node.key < key:
                node.right = _removeNode(node.right, key)
            elif node.key > key:
                node.left = _removeNode(node.left, key)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:
                    minNode = _getMin(node.right)
                    node.key = minNode.key
                    node.right = _removeNode(node.right, minNode.key)
            return node
        
        self.root = _removeNode(self.root, key)
        del self.map[key]

    def getInorderKeys(self) -> List[int]:
        keys = []

        def _dfs(node):
            if not node: return

            _dfs(node.left)
            keys.append(node.key)
            _dfs(node.right)

        _dfs(self.root)
        return keys
        






