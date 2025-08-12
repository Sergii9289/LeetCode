function TreeNode(val, left, right) {
  this.val = (val===undefined ? 0 : val)
  this.left = (left===undefined ? null : left)
  this.right = (right===undefined ? null : right)
}

var inorderTraversal = function(root) {
    const result = [];

    function traverse(node) {
      if (!node) {
        return;
      }
      traverse(node.left);
      result.push(node.val);
      traverse(node.right);
    }
    traverse(root);
    return result;
};

const tree = new TreeNode(1, null, new TreeNode(2, new TreeNode(3), null));
console.log(inorderTraversal(tree)); // Виведе: [1, 3, 2]