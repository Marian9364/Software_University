function calorieObject(array){
    let calObj = {};
    for (let i = 0; i < array.length; i++){
        if (i % 2 == 0){
            let element = array[i];
            calObj[element] = Number(array[i + 1]);
        }
    }
    console.log(calObj)
}
