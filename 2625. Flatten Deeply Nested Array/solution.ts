type MultiDimensionalArray = (number | MultiDimensionalArray)[];

var flat = function (arr:  MultiDimensionalArray, n: number):  MultiDimensionalArray {
    // if n is 0, then just return
    // get result of n - 1
    // iterating that, if typeof is object, then it means, it's array,
    // try to flat the function, then append, to the array, then do rest of it, then return
    if (n === 0) return arr;
    const prev = flat(arr, n-1);
    // iterate
    const res = [] as MultiDimensionalArray
    for(const elem of prev) {
        if(typeof elem === 'object') {
            // do flattening
            res.push(...elem)
        } else {
            // then just include in res
            res.push(elem)
        }
    }
    return res
};
