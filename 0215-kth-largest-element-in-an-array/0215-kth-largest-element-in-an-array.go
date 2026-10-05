type MinHeap []int

func (m MinHeap) Len() int {
    return len(m)
}

func (m MinHeap) Less(i, j int) bool {
    return m[i] < m[j]
}

func (m MinHeap) Swap(i, j int) {
    m[i], m[j] = m[j], m[i]
}

func (m MinHeap) Top() any {
    if m.Len() > 0 {
        return m[0]
    }
    return -100000
}

func (m *MinHeap) Push(num any) {
    *m = append(*m, num.(int))
}

func (m *MinHeap) Pop() any {
    count := len(*m)
    if count < 1 {
        return nil
    }
    retVal := (*m)[count - 1]
    *m = (*m)[:count - 1]
    return retVal
}

func findKthLargest(nums []int, k int) int {
    h := &MinHeap{}
    heap.Init(h)

    for i := 0; i < len(nums); i++ {
        if h.Len() < k {
            heap.Push(h, nums[i])
        } else {
            if nums[i] > h.Top().(int) {
                heap.Pop(h)
                heap.Push(h, nums[i])
            }
        }
    }
    return heap.Pop(h).(int)
}