function greatestCommonDivisor(num1, num2) {
    let divisorsForNum1 = [];
    let divisorsForNum2 = [];
    let commonDivisors = [];
    for (let i = 0; i <= num1; i++) {
        if (num1 % i == 0) {
            divisorsForNum1.push(i);
        }
    }
    for (let i = 0; i <= num2; i++) {
        if (num2 % i == 0) {
            divisorsForNum2.push(i);
        }
    }
    
    for(let num of divisorsForNum1) {
        if (divisorsForNum2.includes(num)) {
            commonDivisors.push(num)
        }
    }
    let maxGCD = commonDivisors.reduce(function(a, b) {
        return Math.max(a, b);
    }, 0);
    console.log(maxGCD)
}
