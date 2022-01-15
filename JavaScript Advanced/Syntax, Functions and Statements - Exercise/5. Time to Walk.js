function timeToWalk(steps,footprintLength,speed){
    const restDuration = 60;
    let metersTotal = steps * footprintLength;
    let restsCount = Math.floor(metersTotal / 500);
    let kilometersTotal = metersTotal / 1000;
    let timeInSeconds = (kilometersTotal / speed * 3600) + (restsCount * restDuration);
    let timeInHours = Math.floor(timeInSeconds / 3600);
    timeInSeconds %= 3600;
    let timeInMinutes = Math.floor(timeInSeconds / 60);
    timeInSeconds = Math.round(timeInSeconds % 60);
    let result = '';
    result += timeInHours < 10 ? '0' + timeInHours : timeInHours;
    result += ':';
    result += timeInMinutes < 10 ? '0' + timeInMinutes : timeInMinutes;
    result += ':';
    result += timeInSeconds < 10 ? '0' + timeInSeconds : timeInSeconds;
    return result;
}
