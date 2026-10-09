type Pair struct {
    idx1, idx2 int
}

type Node struct {
    sum int
    p Pair
}

type MinHeap []Node

func (m MinHeap) Len() int {
    return len(m)
}

func (m MinHeap) Less(i, j int) bool {
    return m[i].sum < m[j].sum
}

func (m MinHeap) Swap(i, j int) {
    m[i], m[j] = m[j], m[i]
}

func (m MinHeap) Top() any {
    if len(m) > 0 {
        return m[0]
    }
    return Node{}
}

func (m *MinHeap) Push(n any) {
    *m = append(*m, n.(Node))
}

func (m *MinHeap) Pop() any {
    count := m.Len()
    minElem := (*m)[count - 1]
    *m = (*m)[0:count - 1]
    return minElem
}

func kSmallestPairs(nums1 []int, nums2 []int, k int) [][]int {
    result := [][]int{}
    visited := map[Pair]bool{}

    mHeap := &MinHeap{}
    heap.Init(mHeap)

    pair := Pair{0, 0}
    node := Node{nums1[0] + nums2[0], pair}
    heap.Push(mHeap, node)
    visited[pair] = true

    for k > 0 && mHeap.Len() > 0{
        top := heap.Pop(mHeap).(Node)
        pair := top.p

        result = append(result, []int{nums1[pair.idx1], nums2[pair.idx2]})
        if pair.idx1 + 1 < len(nums1) {
            nextPair := Pair{pair.idx1 + 1, pair.idx2}
            if _, ok := visited[nextPair]; ok == false {
                node = Node{nums1[nextPair.idx1] + nums2[nextPair.idx2], nextPair}
                visited[nextPair] = true
                heap.Push(mHeap, node)
            }
        }

        if pair.idx2 + 1 < len(nums2) {
            nextPair := Pair{pair.idx1, pair.idx2 + 1}
            if _, ok := visited[nextPair]; !ok {
                node = Node{nums1[nextPair.idx1] + nums2[nextPair.idx2], nextPair}
                visited[nextPair] = true
                heap.Push(mHeap, node)
            }
        }
        k--
    }
    return result
}