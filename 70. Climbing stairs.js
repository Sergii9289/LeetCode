var climbStairs = function(n) {
    const dp = Array(n + 1).fill(0);
    dp[0] = 1;

    for (let i = 1; i <= n + 1; i++) {
      if (i - 1 >= 0) {
        dp[i] += dp[i - 1];
      };
      if (i - 2 >= 0) {
        dp[i] += dp[i - 2];
      };
     }
    return dp[n];
};

console.log(climbStairs(10))