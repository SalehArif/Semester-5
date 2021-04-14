
document.addEventListener('DOMContentLoaded', () => {
    
    document.querySelectorAll('button').forEach(button => {
        button.onclick= () => {
            document.querySelector('h1').style.color = button.dataset.color;
        }
    })
})

// document.addEventListener('DOMContentLoaded', function(){
            
//     document.querySelector('#red').onclick = function(){
//         document.querySelector('h1').style.color= 'red';
//     }
//     document.querySelector('#green').onclick = function(){
//         document.querySelector('h1').style.color= 'green';
//     }
//     document.querySelector('#blue').onclick = function(){
//         document.querySelector('h1').style.color= 'blue';
//     }
// })