func containsDuplicate(nums []int) bool {
    hashMap := make(map[int]int)

    for _, num := range nums {
        if _, isFound := hashMap[num]; isFound {
            return true
        }
        hashMap[num] = 1
    }
    return false
}