/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let count = init;

    function increment(){
        return ++count;
    }
    function decrement(){
        return --count;
    }
    function reset(){
        count = init;
        return count;
    }
    return {
        increment:increment,
        decrement:decrement,
        reset:reset
    }
};
