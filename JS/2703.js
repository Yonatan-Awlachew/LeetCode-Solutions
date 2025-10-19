/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    let count=0;
    args.forEach((x)=>{
        count+=1;
    });
    return count;
};
