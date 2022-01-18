function sortByTwoCriteria(arr){

    let resultArr= [];
    resultArr = arr.sort((a,b) =>a.length - b.length|| a.localeCompare(b));

    console.log(resultArr.join('\n'))
}
