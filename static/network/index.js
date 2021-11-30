document.addEventListener('DOMContentLoaded', function () {

    let element = document.querySelectorAll(".edit-icon")
    element.forEach(function (el) {
        el.addEventListener('click', () => create_edit(el));
    });
});

function create_edit(el) {
    let card = el.parentElement.parentElement.parentElement
    let body = card.getElementsByClassName('card-body')[0]
    let id = card.getElementsByClassName('post-id')[0].value

    var input = document.createElement("textarea");
    let button = document.createElement("button")
    button.innerHTML = "Save"
    button.className = "btn btn-primary btn-sm"
    input.value = body.innerHTML
    body.innerHTML = ""
    input.className = 'form-control'
    input.id = "textarea"
    input.style.boxSizing = 'border-box'
    input.style.width = '100%'

    input.name = "post";
    body.append(input);
    body.appendChild(button);

    button.onclick = function() {
        edit_post(id, input.value, body)
    }

}

function edit_post(id, content, body) {
    fetch(`/edit_post/${id}/`, {
      method: "POST",
      body: JSON.stringify({
      body:content
      })
    })
    .then((res) => {
        document.querySelector('#textarea').style.display = "none"
        body.innerHTML = content
        body.style.display = "block"
        })
    .catch(error => {
        console.log(error)
    });
  }