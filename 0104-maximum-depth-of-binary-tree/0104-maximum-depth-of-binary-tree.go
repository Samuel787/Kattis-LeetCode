/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxDepth(root *TreeNode) int {
    return findMaxDepth(root, 0)
}

func findMaxDepth(root *TreeNode, currDepth int) int {
    if root == nil {
        return currDepth
    }
    leftDepth := findMaxDepth(root.Left, currDepth + 1)
    rightDepth := findMaxDepth(root.Right, currDepth + 1)
    if leftDepth > rightDepth {
        return leftDepth
    } else {
        return rightDepth
    }
}