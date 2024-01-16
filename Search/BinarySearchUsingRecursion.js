/* Using Recursion */
const totalArrayValues = [1,2,3,4,5,6,8,9,1,2,4,6,78,9,0];
sortedValues = totalArrayValues.sort((a,b) => a - b);
let start = 0, end = sortedValues.length - 1;
const binaryResursive = (sortedValues, searchValue, startPosition, endPosition) => {
    if(startPosition > endPosition) return "Search Not found";
    const midPosition = Math.floor((startPosition + endPosition)/2);
    if(sortedValues[midPosition] === searchValue) return "Search Found";
    (sortedValues[midPosition] < searchValue) ? start = midPosition + 1 : end = midPosition -1 ;
    return binaryResursive(sortedValues, searchValue, start, end);
}
console.log(binaryResursive(sortedValues, 16, start, end));