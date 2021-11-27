
document.addEventListener('DOMContentLoaded', function() {
    // Use buttons to toggle between views
    // document.querySelector('#inbox').addEventListener('click', () => display_emails('inbox'));
    document.getElementById('compose-form').addEventListener('submit', send_email)

  });


  function send_email(event) {
    const body = document.querySelector('#compose-body').value
    console.log(`body ${body}`);
    fetch('/posts', {
            method: 'POST',
            body: JSON.stringify({
                body: body
            })
        })
        .then(response => response.json())
        .then(result => {
            // Print result
            console.log(result);
            display_emails('sent');
        })
        .catch(error => {
            console.log(`Error ${error}`);
        });
    event.preventDefault();
  }