function printNEl(arr, n) {
    let filteredArr = [];
    for (let i = 0; i < arr.length; i+= n) {
        filteredArr.push(arr[i]);
    }
    return filteredArr;
}
