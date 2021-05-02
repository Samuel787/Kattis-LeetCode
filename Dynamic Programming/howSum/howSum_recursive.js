
function howSum(target, arr){
    if(target === 0){
        return [];
    }
    if(target < 0){
        return null;
    }
    var result = []
    for(var i = 0; i < arr.length; i++){
        var temp = howSum(target - arr[i], arr);
        if(temp != null){
            temp.push(arr[i]);
            return temp;
        }
    }
    return null;
}

console.log("This is the result, ", howSum(7, [5,4,3]))
console.log("This is the result, ", howSum(300, [7,14]))