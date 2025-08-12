function TreeNode(val, left, right) {
  this.val = (val===undefined ? 0 : val)
  this.left = (left===undefined ? null : left)
  this.right = (right===undefined ? null : right)
}

var isSameTree = function(p, q) {
    if (!p && !q) {
      return true;
    }
    if (!p || !q) {
      return false;
    }
    if (p.val != q.val) {
      return false;
    }
    return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
};

const tree1 = new TreeNode(1, null, new TreeNode(2, new TreeNode(3), null));
const tree2 = new TreeNode(1, new TreeNode(2, null, null), new TreeNode(3, null, null));
console.log(isSameTree(tree1, tree2));