function addAndRemoveEls(arr) {
    let resultArr = [];
    for (let i = 0; i <= arr.length; i++){
        currentCommand = arr[i];
        if (currentCommand == 'add'){
            resultArr.push(i + 1);
        } else if (currentCommand == 'remove'){
            resultArr.pop();
        }
    }
    if (resultArr.length == 0){
        console.log("Empty");
    } else {
        resultArr.forEach(element => {
            console.log(element);
        });
    }
}
