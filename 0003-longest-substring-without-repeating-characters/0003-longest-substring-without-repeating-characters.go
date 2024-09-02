func lengthOfLongestSubstring(s string) int {
    hashMap := make(map[byte]int)
    left := 0
    right := 0
    maxLength := 0

    for right < len(s) {
        hashMap[s[right]]++

        for left < right && hashMap[s[right]] > 1 {
            hashMap[s[left]]--
            left++
        }

        if (right - left + 1) > maxLength {
            maxLength = (right - left) + 1
        }
        right++
    }
    return maxLength
    // for idx, val := range s {
    //     if index, isPresent := hashMap[val]; isPresent {
    //         i = index + 1
    //     }
    //     hashMap[val] = idx
    //     if (idx - i) > maxLength {
    //         maxLength = (idx - 1)
    //     }
    // }
    // return maxLength
}