function rangeOfNumbers(startNum, endNum) {
  if (startNum > endNum)
    return [];
  else
    // if (arr === undefined){
    //   var arr = [];
    // }
    var arr = rangeOfNumbers(startNum, endNum-1);
    arr.push(endNum);
    return arr;
};
console.log(rangeOfNumbers(1, 5));