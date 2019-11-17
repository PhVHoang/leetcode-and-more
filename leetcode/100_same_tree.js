/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */

// Using In-order traversal

var isSameTree = function(p, q) {
    if (!p && !q) return true;
    if ((!p && q) || (p && !q)) return false;

    if (p.val != q.val) return false;
    return isSameTree(p.right, q.right) && isSameTree(p.left, q.left);
};