
function howSum(target, arr, memo={}){
    if(target in memo){
        return memo[target];
    }
    if(target === 0){
        return [];
    }
    if(target < 0){
        return null;
    }
    var result = []
    for(var i = 0; i < arr.length; i++){
        var temp = howSum(target - arr[i], arr, memo);
        memo[target - arr[i]] = temp;
        if(temp != null){
            temp.push(arr[i]);
            // memo[target] = temp;
            return temp;
        }
    }
    return null;
}

console.log("This is the result, ", howSum(7, [5,4,3]))
console.log("This is the result, ", howSum(300, [7,14]))
console.log("This is the target: 8", howSum(8, [2,3,5]));