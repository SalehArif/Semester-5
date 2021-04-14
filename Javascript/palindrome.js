function palindrome(str) {
  var isPal=true;
  str=str.toLowerCase();

  for(var i=0; i<str.length;i++){
    // console.log(str[i]+str[str.length-1-i]);
    if(str[i]!==str[str.length-i-1]){
      isPal = false;
      break;
    }
  }
  return isPal;
}

function spec(str){
  var form = " _/\\|-,.:";
  for(var i=0; i<str.length;i++){
    for(var j=0;j<form.length;j++){
    if(str[i]===form[j])
      str[i]="";
      break;
    }
  }
  return str;
}

console.log(spec("0_0 (: /-\ :) 0-0"));
console.log(palindrome("0_0 (: /-\ :) 0-0"));