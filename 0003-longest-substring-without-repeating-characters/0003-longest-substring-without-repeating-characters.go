func lengthOfLongestSubstring(s string) int {
    length := len(s)
    l := 0
    r := 0
    maxLength := 0
    idxMap := make(map[byte]int)
    for r < length {
        if idx, ok := idxMap[s[r]]; ok {
            l = max(l, idx + 1)
        }
        currLength := r - l + 1
        if currLength > maxLength {
            maxLength = currLength
        }
        idxMap[s[r]] = r
        r += 1
    }
    return maxLength
}