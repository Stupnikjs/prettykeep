
let divButton = document.querySelector('.button-div')



let updateButton = document.createElement('button')
updateButton.className = 'updateButton' 
updateButton.textContent = 'Update'

updateButton.addEventListener('click', (e) => {
    e.preventDefault()
    postUpdate()
})
divButton.appendChild(updateButton)


function postUpdate() {
    
    // Get the content of the textarea
    // Retrieve the data-fiche attribute value
    var dataFiche = document.querySelector('.data-card').getAttribute('data-fiche');
    console.log(dataFiche)
    // Parse the JSON string to get the JavaScript object
    
    var ficheObject = JSON.parse(dataFiche);
    
    let textarea = document.querySelector('textarea')
    ficheObject['text'] = textarea.value;
    ficheObject['id'] = textarea.id
    delete ficheObject['labels']
    console.log(ficheObject)
    // Prepare the data to be sent in the request body
    var data = {
        fiche: ficheObject
    };
    
    // Send a POST request to the server using the Fetch API
    fetch(`/updatefiche/${ficheObject['id']}`, {
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



