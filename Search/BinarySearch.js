/*---------------------------
Simple Concept: Binary Search
    - First Sort it in Ascending order
    - check the conditions inside the loop
        mid index value === search value
        mid index value < search value
        mid index value > search value
*/
const totalArrayValues = [1,2,3,4,5,6,8,9,1,2,4,6,78,9,0];
sortedValues = totalArrayValues.sort((a,b) => a - b);
console.log(sortedValues);
const binarySearch = (sortedValues, searchValue) => {
    let startPosition = 0;
    let endPosition = (totalArrayValues.length - 1);
    while(startPosition <= endPosition){
        let midPosition = Math.floor((startPosition + endPosition)/2);
        if(totalArrayValues[midPosition] === searchValue) return true;
        else if(totalArrayValues[midPosition] < searchValue) {
            startPosition = midPosition + 1;
            midPosition = startPosition;
        }
        else{
            endPosition = midPosition - 1;
            midPosition = endPosition;
        }
    }
    return false
}
console.log(binarySearch(sortedValues, 0));
console.log(binarySearch(sortedValues, 56));