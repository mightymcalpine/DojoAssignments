// Write a function that will find the max number, min number, and avg of all numbers of any given array.

function maxMinAvg(arr) {
    var arrX = [];
    var max = 0;
    var min = 0;
    var sum = 0;
    for(var i = 0; i < arr.length; i++) {
        // Check arr[i] for MAX
        if(arr[i] > max) {
           max = arr[i]; 
        }
        // Check arr[i] for MIN
        if(arr[i] < min) {
            min = arr[i];
        }
        // Check arr[i] for AVG
        sum = sum + arr[i];
    }
    arrX[0] = max;
    arrX[1] = min;
    arrX[2] = sum / arr.length;
    return arrX; 
}