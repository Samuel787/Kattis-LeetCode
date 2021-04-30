const gridTraveller = (row, col) => {
    if(row == 0 || col == 0){
        return 0;
    }
    if(row == 1 || col == 1){
        return 1;
    }
    return gridTraveller(row - 1, col) + gridTraveller(row, col - 1);
}

console.log(gridTraveller(2, 3));
console.log(gridTraveller(3, 3));