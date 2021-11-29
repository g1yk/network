document.addEventListener('DOMContentLoaded', function () {

    console.log('hi')
    let element = document.querySelectorAll(".edit-icon")
    element.forEach(function (el) {
        el.addEventListener('click', () => create_edit(el));
    });
});

function create_edit(el) {
    let card = el.parentElement.parentElement.parentElement
    let body = card.getElementsByClassName('card-body')[0]
    let id = card.getElementsByClassName('post-id')[0].value

    // console.log(card.childNodes[0])
    console.log('click', body.innerHTML, id.innerHTML);

    var input = document.createElement("textarea");
    let button = document.createElement("button")
    button.innerHTML = "Save"
    button.className = "btn btn-primary btn-sm"
    input.value = body.innerHTML
    body.innerHTML = ""
    input.className = 'form-control'
    input.style.boxSizing = 'border-box'
    input.style.width = '100%'

    input.name = "post";
    body.append(input); //appendChild
    body.appendChild(button);

    button.onclick = function() {
        edit_post(id, input.value)

    }

}

function edit_post(id, content) {
console.log('sending ', content)
    fetch(`/edit_post/${id}/`, {
      method: "POST",
      body: JSON.stringify({
      body:content
      })
    }).catch(error => {
        console.log(error)
    });
    // }).then((res) => {
    //   document.querySelector(`#post-content-${id}`).textContent = post;
    //   document.querySelector(`#post-content-${id}`).style.display = "block";
    //   document.querySelector(`#post-edit-${id}`).style.display = "none";
    //   document.querySelector(`#post-edit-${id}`).value = post.trim();
    // });
  }