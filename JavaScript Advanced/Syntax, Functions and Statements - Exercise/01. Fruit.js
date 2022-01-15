function calcSum(fruit, weightInGrams, pricePerKg) {
    let weightInKg = weightInGrams / 1000
    let sum = weightInKg * pricePerKg
    console.log(`I need $${sum.toFixed(2)} to buy ${weightInKg.toFixed(2)} kilograms ${fruit}.`);

}
