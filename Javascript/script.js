function func(){
    let ans = document.querySelector('h1');
    if(ans.innerHTML === 'Head')
        ans.innerHTML = 'Changed';
    else
        ans.innerHTML = 'Head';
}
