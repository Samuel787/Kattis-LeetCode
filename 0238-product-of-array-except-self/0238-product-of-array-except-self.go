func productExceptSelf(nums []int) []int {
    result := make([]int, len(nums))
    prefix := make([]int, len(nums))
    postfix := make([]int, len(nums))

    prefix[0] = 1
    postfix[len(nums) - 1] = 1

    for i := 1; i < len(nums); i++ {
        prefix[i] = nums[i - 1] * prefix[i - 1]
    } 

    for i := len(nums) - 2; i >= 0; i-- {
        postfix[i] = nums[i + 1] * postfix[i + 1] 
    }

    for i := 0; i < len(nums); i++ {
        result[i] = prefix[i] * postfix[i]
    }

    return result
}