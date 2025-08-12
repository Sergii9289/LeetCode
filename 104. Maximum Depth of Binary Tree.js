function TreeNode(val, left, right) {
   this.val = (val===undefined ? 0 : val)
   this.left = (left===undefined ? null : left)
   this.right = (right===undefined ? null : right)
}

function build_Tree_FromList(array) {
  if (!array || array.length === 0) return null;

  const root = new TreeNode(array[0]);
  const queue = [root];
  let i = 1;

  while (queue.length > 0 && i < array.length) {
    const current = queue.shift();

    if (i < array.length) {
      if (array[i] != null) {
        current.left = new TreeNode(array[i]);
        queue.push(current.left);
      }
      i++;
    }

    if (i < array.length) {
      if (array[i] != null) {
        current.right = new TreeNode(array[i]);
        queue.push(current.right);
      }
      i++;
    }
  }

  return root;
}

/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxDepth = function(root) {
  if (!root) {
    return 0;
  }

  let result = [];
  let queue = [root];

  while (queue.length != 0) {
    let levelSize = queue.length;
    let currentLevel = [];

    for (let i = 0; i < levelSize; i++) {
      let node = queue.shift();
      currentLevel.push(node.val);

      if (node.left != null) {
        queue.push(node.left);
      }
      if (node.right != null) {
        queue.push(node.right);
      }
    }
    result.push(currentLevel);
  }
  return result.length
};

const tree = build_Tree_FromList([3,9,20,null,null,15,7]);
console.log(tree)
console.log(maxDepth(tree))