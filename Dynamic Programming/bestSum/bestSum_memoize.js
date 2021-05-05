function bestSum(target, arr, isSorted=false, memo={}){
    if(target in memo){
        return memo[target]
    }
    if(target === 0){
        return [];
    }
    if(target < 0){
        return null;
    }
    if(!isSorted){
        arr.sort();
        isSorted = true
    }
    var result = []
    for(var i = arr.length - 1; i >= 0; i--){
        var temp = bestSum(target - arr[i], arr, isSorted);
        memo[target - arr[i]] = temp;
        if(temp != null){
            temp.push(arr[i])
            return temp;
        }
    }
    return null;
}

console.log("This is the result: ", bestSum(300, [7, 14]));