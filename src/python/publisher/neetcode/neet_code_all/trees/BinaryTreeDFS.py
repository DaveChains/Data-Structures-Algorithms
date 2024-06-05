from typing import List, Optional


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTreeDFS():

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]: #94
        res = []
        def inOrder(root):
            if not root:
                return

            inOrder(root.left)
            res.append(root.val)
            inOrder(root.right)

        inOrder(root)

        return res

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]: #144

        res = []

        def preOrder(root):
            if not root:
                return
            res.append(root.val)
            preOrder(root.left)
            preOrder(root.right)

        preOrder(root)
        return res

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]: # 145
        res = []

        def postOrder(root):
            if not root:
                return

            postOrder(root.left)
            postOrder(root.right)
            res.append(root.val)

        postOrder(root)
        return res

[1,null,2,3]

tree1 = TreeNode()
tree1.val = 1
tree1.left = None
tree1.right = 2