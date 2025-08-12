function TreeNode(val, left, right) {
   this.val = (val===undefined ? 0 : val)
   this.left = (left===undefined ? null : left)
   this.right = (right===undefined ? null : right)
}

/**
 * @param {TreeNode} root
 * @return {boolean}
 */

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

var isSymmetric = function(root) {
    function isMirror (t1, t2) {
      if (!t1 && !t2) {
        return true;
      }
      if (!t1 || !t2) {
        return false;
      }
      return (t1.val === t2.val && isMirror(t1.left, t2.right) && isMirror(t1.right, t2.left));
    }
    if (root != null) {
      return isMirror(root.left, root.right);
    }
    return true;
};

const tree = build_Tree_FromList([1, 2, 2, 3, 4, 4, 3]);
console.log(isSymmetric(tree));