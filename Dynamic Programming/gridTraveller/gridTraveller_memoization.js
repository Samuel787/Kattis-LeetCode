const gridTraveller = (row, col, memo = {}) => {
    var key = row + "-" + col;
    if(row == 0 || col == 0){
        return 0;
    }
    if(row == 1 || col == 1){
        return 1;
    }
    if(key in memo){
        return memo[key];
    }
    var alt_key = col + "-" + row;
    if(alt_key in memo){
        return memo[alt_key];
    }
    memo[key] = gridTraveller(row - 1, col, memo) + gridTraveller(row, col - 1, memo);
    return memo[key]
}

console.log(gridTraveller(2, 3))
console.log(gridTraveller(3, 3))
console.log(gridTraveller(300, 300))