
function find_min_in_arr(arr){
    if(arr.constructor !== Array || arr.length == 0){
        return null;
    }
    var running_min = arr[0]
    for(var i = 1; i < arr.length; i++){
        if(arr[i] < running_min){
            running_min = arr[i]
        }
    }
    return running_min;
}
function calcSum(target, arr, min=null, memo={}){
    if(target in memo){
        return memo[target];
    }
    if(target === 0){
        return true;
    }
    if(min == null){
        min = find_min_in_arr(arr);
    }
    if(target < min){
        return false;
    }
    for(var i = 0; i < arr.length; i++){
        memo[target - arr[i]] = calcSum(target - arr[i], arr, min, memo);
        if(memo[target - arr[i]]){
            return true;
        }
    }
    return false;
}

console.log(calcSum(300, [7,14]));

