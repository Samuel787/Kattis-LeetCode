func lengthOfLongestSubstring(s string) int {
    length := len(s)
    l := 0
    r := 0
    maxLength := 0
    idxMap := make(map[byte]int)
    for r < length {
        if idx, ok := idxMap[s[r]]; ok {
            l = max(l, idx + 1)
            // fmt.Printf("Increment l to %d and r to %d and skip this iteration\n", l, r)
        } //else {
            currLength := r - l + 1
            if currLength > maxLength {
                maxLength = currLength
                // fmt.Printf("l is %d, r is %d, max string: %s\n", l, r, s[l:r + 1])
            }
        //}
        idxMap[s[r]] = r
        r += 1
    }
    return maxLength
}