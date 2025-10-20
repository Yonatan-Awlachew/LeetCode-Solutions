/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    let cache = {};
    return function(...args) {
        let x = JSON.stringify(args);
        if (x in cache){
            return cache[x];
        }
        else{
            let result = fn(...args);
            cache[x] = result;
            return result;
        }
    }
}

