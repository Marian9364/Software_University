function sameNumbers(number) {
    let same = true;
    let sum = 0;
    let str = number.toString();

    for(let i = 0; i < str.length - 1; i++){
        if(str.charAt(i) != str.charAt(i+1))
        {
            same = false;
            break;
        }
    }
    for (num of str) {
        sum += Number(num);
    } 
    
    console.log(same);
    console.log(sum);
}
