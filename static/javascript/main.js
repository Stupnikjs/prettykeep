
function postUpdate() {
    // Get the content of the textarea
    // recuperer tout le contenu de la fiche 
    // title created updated complete_start complete_end 

    let textarea = document.querySelector('textarea')
    var textareaContent = textarea.value;
    let id = textarea.id
    print(textarea)
    // Prepare the data to be sent in the request body
    var data = {
        text: textareaContent
    };
    print(data)
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
