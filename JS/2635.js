/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    let out = [];
    for(let i=0;i<arr.length;i++){
        out.push(fn(arr[i],i))
    }  
    return out;
};
