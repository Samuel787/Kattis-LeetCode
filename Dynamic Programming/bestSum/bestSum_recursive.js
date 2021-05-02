function bestSum(target, arr, isSorted=false){
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
        if(temp != null){
            temp.push(arr[i])
            return temp;
        }
    }
    return null;
}

console.log("This is the result: ", bestSum(8, [2,3,5]));