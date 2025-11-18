# تعريف عقدة الشجرة
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# الحل
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # إذا كانت الشجرة فارغة
        if root is None:
            return 0
        
        # إذا لم يكن للشجرة أبناء على اليسار
        if root.left is None:
            return self.minDepth(root.right) + 1
        
        # إذا لم يكن للشجرة أبناء على اليمين
        if root.right is None:
            return self.minDepth(root.left) + 1
        
        # إذا كانت للشجرة أبناء على الجهتين
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
