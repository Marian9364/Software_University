function arrWithDelimiter(arr, delimiter) {
    let filteredArr = [];

    for (let i = 0; i < arr.length; i++) {
        if (i == arr.length - 1) {
            filteredArr.push(arr[i]);
        } else {
            filteredArr.push(arr[i], delimiter);
        }
    }
    console.log(filteredArr.join(""));
}
