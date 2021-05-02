const getArrMin = (arr) => {
    if(arr.length == 0){
        return null;
    }
    var min = Number.POSITIVE_INFINITY;
    arr.forEach(element => {
        if(element < min){
            min = element
        }
    });
    return min;
}

const calcSum = (target, arr, min_in_arr=null) => {
    if(target == 0){
        return true;
    }
    if(min_in_arr == null){
        min_in_arr = getArrMin(arr);
    }
    if(target < min_in_arr){
        return false;
    }
    for(var i = 0; i < arr.length; i++){
        if(calcSum(target - arr[i], arr, min_in_arr)){
            return true;
        }
    }
    return false;
}

arr = [5,3,4,7];
console.log(calcSum(7, arr));
console.log(calcSum(300, [7, 14])); // this will take too long -> goal: optimise with memoization