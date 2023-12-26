



let allCards = document.querySelectorAll('.data-card')
let divButtons = document.querySelectorAll('.button-div')
console.log(divButtons)
for( let j = 0; j < allCards.length; j++ ){

    let updateButton = document.createElement('button')
    updateButton.className = 'updateButton' 
    updateButton.textContent = 'Update'
    updateButton.addEventListener('click', (e) => {
        e.preventDefault()
        postUpdate(allCards[j], allCards[j].querySelector('textarea').getAttribute('id'))
    })
    divButtons[j].appendChild(updateButton)
    
}


function postUpdate(card, id) {
        
    // Get the content of the textarea
    // Retrieve the data-fiche attribute value
    var dataFiche = card.getAttribute('data-fiche');
    console.log(dataFiche)
    // Parse the JSON string to get the JavaScript object
    
    var ficheObject = JSON.parse(dataFiche);
    
    let textarea = card.querySelector('textarea')
    ficheObject['text'] = textarea.value;
    ficheObject['id'] = textarea.getAttribute('id')
    delete ficheObject['labels']
    // Prepare the data to be sent in the request body
    var data = {
        fiche: ficheObject
    };
    
    // Send a POST request to the server using the Fetch API
    fetch(`/updatefiche/${id}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        // Traitez la réponse ici
        console.log('Success:', data);
    })
    .catch(error => {
        // Gérez les erreurs ici
        console.error('Error:', error);
    });
  
}





