
let fiches = document.querySelectorAll('.data-card')

let next = document.querySelector('data-card .next')





for ( let i = 0; i < fiches.length ; i++){
        
        fiches[i].addEventListener('click', () => {
      
            fiches[i].classList.add('inactive')
          if( i !== fiches.length - 1){ fiches[i+1].classList.remove('inactive')} else { fiches[0].classList.remove('inactive')}
        })
        
         
        
}


