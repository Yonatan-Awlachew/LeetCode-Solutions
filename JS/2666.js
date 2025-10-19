/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
        let is_Called=false;
        let result;
    return function(...args){
        if(!is_Called){
            is_Called = true;
            result = fn(...args);
            return result
        }
        return undefined;
    }
};

