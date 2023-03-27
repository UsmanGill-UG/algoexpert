function twoNumberSum(array, targetSum) {
  // Write your code here.
  const num = {};
  for (const i of array)
  {
    if (targetSum - i in num)
    {
      return [targetSum - i, i];
    } else
    {
      num[i] = i;
    }
  }
  return [];
}

// Do not edit the line below.
exports.twoNumberSum = twoNumberSum;
