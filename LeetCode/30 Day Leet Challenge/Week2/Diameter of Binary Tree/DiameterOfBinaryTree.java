public class DiameterOfBinaryTree {
    public static void main(String[] args) {
        TreeNode treeNode=new TreeNode(0);
        Solution solution = new Solution();
        solution.diameterOfBinaryTree(treeNode);
    }
}
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}
class Solution {
    int maxDiameter = 0;
    public int diameterOfBinaryTree(TreeNode root) {
        depth(root);
        return maxDiameter;
    }
    public int depth(TreeNode node) {
        if (node == null) return 0;
        int L = depth(node.left );
        int R = depth(node.right);
        maxDiameter = Math.max(maxDiameter, L+R+1);
        return Math.max(L, R) + 1;
    }
}