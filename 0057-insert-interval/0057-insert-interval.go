func insert(intervals [][]int, newInterval []int) [][]int {
    result := make([][]int, 0)

    if len(intervals) == 0 {
        result = append(result, newInterval)
        return result
    }

    hasInserted := false
    // insert at start
    if newInterval[1] < intervals[0][0] {
        result = append(result, newInterval)
        hasInserted = true
    }
    
    // try in middle
    for i := 0; i < len(intervals); i++ {
        if hasInserted {
            result = append(result, intervals[i])
            continue
        }

        // edge case: it should be inserted before ith element: 
        if newInterval[0] < intervals[i][0] && newInterval[1] < intervals[i][0] {
            result = append(result, newInterval)
            hasInserted = true
            i--
            continue
        }

        shouldMerge := false
        for i < len(intervals) && !(newInterval[1] < intervals[i][0] || newInterval[0] > intervals[i][1]) {
            shouldMerge = true
            newInterval[0] = findMin(newInterval[0], intervals[i][0])
            newInterval[1] = findMax(newInterval[1], intervals[i][1])
            i++
        }
        
        if shouldMerge {
            hasInserted = true
            i-- // the above loop incremented i but iTH index failed the criteria
            result = append(result, newInterval)
        } else {
            result = append(result, intervals[i])
        }
    }

    // insert at the end
    if !hasInserted {
        result = append(result, newInterval)
    }

    return result
}

func findMin(a int, b int) int {
    if a < b {
        return a
    } else {
        return b
    }
}

func findMax(a int, b int) int {
    if a > b {
        return a
    }
    return b
}