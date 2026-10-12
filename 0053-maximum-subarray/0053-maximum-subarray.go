func maxSubArray(nums []int) int {
    maxSum := nums[0]
    runSum := nums[0]
    for _, val := range nums[1:] {
        if val > runSum + val {
            runSum = val
        } else {
            runSum += val
        }
        maxSum = max(maxSum, runSum)
    }
    return maxSum
}