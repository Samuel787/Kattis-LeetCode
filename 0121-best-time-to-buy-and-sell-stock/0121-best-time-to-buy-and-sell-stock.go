func maxProfit(prices []int) int {
    maxProfit := 0
    minPrice := prices[0]
    for idx, price := range prices {
        if idx == 0 {
            continue
        }
        currProfit := price - minPrice
        if currProfit > maxProfit {
            maxProfit = currProfit
        }
        if price < minPrice {
            minPrice = price
        }
    }
    return maxProfit
}