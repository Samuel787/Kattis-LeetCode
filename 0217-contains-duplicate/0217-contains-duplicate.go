func containsDuplicate(nums []int) bool {
    
    mMap := make(map[int]bool)
    
    for _, num := range nums {
        if _, ok := mMap[num]; ok {
            return true
        }
        mMap[num] = true
    }
    return false
}