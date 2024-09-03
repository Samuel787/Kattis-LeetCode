func rob(nums []int) int {
    if len(nums) == 1 {
        return nums[0]
    }
    if len(nums) == 2 {

    }
    
    dp := make([]int, len(nums))
    dp[0] = nums[0]
    if (nums[0] > nums[1]) {
        dp[1] = nums[0]
    } else {
        dp[1] = nums[1]
    }

    for i := 2; i < len(nums); i++ {
        robHouse := nums[i] + dp[i - 2]
        dontRobHouse := dp[i - 1]
        if robHouse > dontRobHouse {
            dp[i] = robHouse
        } else {
            dp[i] = dontRobHouse
        }
    }
    return dp[len(nums) - 1]
}