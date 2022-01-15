function radarCheck(speed, area) {
    const motorwayLimit = 130;
    const interstateLimit = 90;
    const cityLimit = 50;
    const residentialAreaLimit = 20;
    let result = '';

    switch (area) {
        case 'city': if (speed <= cityLimit) {
            result = `Driving ${speed} km/h in a ${cityLimit} zone`
        } else if (speed <= cityLimit + 20) {
            absoluteDifference = Math.abs(speed - cityLimit);
            result = `The speed is ${absoluteDifference} km/h faster than the allowed speed of ${cityLimit} - speeding`

        } else if (speed <= cityLimit + 40) {
            absoluteDifference = Math.abs(speed - cityLimit);
            result = `The speed is ${absoluteDifference} km/h faster than the allowed speed of ${cityLimit} - excessive speeding`

        } else {
            absoluteDifference = Math.abs(speed - cityLimit);
            result = `The speed is ${absoluteDifference} km/h faster than the allowed speed of ${cityLimit} - reckless driving`

        } break;

        case 'motorway': if (speed <= motorwayLimit) {
            result = `Driving ${speed} km/h in a ${motorwayLimit} zone`
        } else if (speed <= motorwayLimit + 20) {
            absoluteDifference = Math.abs(speed - motorwayLimit);
            result = `The speed is ${absoluteDifference} km/h faster than the allowed speed of ${motorwayLimit} - speeding`

        } else if (speed <= motorwayLimit + 40) {
            absoluteDifference = Math.abs(speed - motorwayLimit);
            result = `The speed is ${absoluteDifference} km/h faster than the allowed speed of ${motorwayLimit} - excessive speeding`

        } else {
            absoluteDifference = Math.abs(speed - motorwayLimit);
            result = `The speed is ${absoluteDifference} km/h faster than the allowed speed of ${motorwayLimit} - reckless driving`

        } break;

        case 'interstate': if (speed <= interstateLimit) {
            result = `Driving ${speed} km/h in a ${interstateLimit} zone`
        } else if (speed <= interstateLimit + 20) {
            absoluteDifference = Math.abs(speed - interstateLimit);
            result = `The speed is ${absoluteDifference} km/h faster than the allowed speed of ${interstateLimit} - speeding`

        } else if (speed <= interstateLimit + 40) {
            absoluteDifference = Math.abs(speed - interstateLimit);
            result = `The speed is ${absoluteDifference} km/h faster than the allowed speed of ${interstateLimit} - excessive speeding`

        } else {
            absoluteDifference = Math.abs(speed - interstateLimit);
            result = `The speed is ${absoluteDifference} km/h faster than the allowed speed of ${interstateLimit} - reckless driving`

        } break;

        case 'residential': if (speed <= residentialAreaLimit) {
            result = `Driving ${speed} km/h in a ${residentialAreaLimit} zone`
        } else if (speed <= residentialAreaLimit + 20) {
            absoluteDifference = Math.abs(speed - residentialAreaLimit);
            result = `The speed is ${absoluteDifference} km/h faster than the allowed speed of ${residentialAreaLimit} - speeding`

        } else if (speed <= residentialAreaLimit + 40) {
            absoluteDifference = Math.abs(speed - residentialAreaLimit);
            result = `The speed is ${absoluteDifference} km/h faster than the allowed speed of ${residentialAreaLimit} - excessive speeding`

        } else {
            absoluteDifference = Math.abs(speed - residentialAreaLimit);
            result = `The speed is ${absoluteDifference} km/h faster than the allowed speed of ${residentialAreaLimit} - reckless driving`

        } break;

        
    }


    console.log(result)
}

