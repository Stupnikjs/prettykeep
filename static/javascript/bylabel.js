
let fiches = document.querySelectorAll('.data-card')

let nexts = document.querySelectorAll('.data-card .next')
let previous = document.querySelectorAll('.data-card .previous')




for ( let i = 0; i < fiches.length ; i++){
        
        nexts[i].addEventListener('click', () => {
      
           fiches[i].classList.add('inactive')
          if( i !== fiches.length - 1){ fiches[i+1].classList.remove('inactive')} else { fiches[0].classList.remove('inactive')}
        })

        previous[i].addEventListener('click', () => {
      
            fiches[i].classList.add('inactive')
           if( i !== 0 ){ fiches[i-1].classList.remove('inactive')} else { fiches[fiches.length - 1].classList.remove('inactive')}
         })
        
         
        
}


