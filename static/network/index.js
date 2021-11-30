document.addEventListener('DOMContentLoaded', function () {


    let element = document.querySelectorAll(".edit-icon")
    element.forEach(function (el) {
        el.addEventListener('click', () => create_like(el));
    });

    let like_element = document.querySelectorAll(".like-icon")
    like_element.forEach(function (el) {
        el.addEventListener('click', () => create_like(el));
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
    //   body: JSON.stringify({
    //   body:content
    //   })
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


  function create_like(el) {
    let card = el.parentElement.parentElement.parentElement.parentElement
    let id = card.getElementsByClassName('post-id')[0].value
    console.log('el ', el.innerHTML)
    console.log(id)
    like_post(id, el)
  }

  function like_post(id, el) {
    fetch(`/like_post/${id}/`, {
      method: "POST",
      body: JSON.stringify({
      body:id
      })
    })
    .then((response) => response.json())
    .then((res) => {
        console.log(res.total_likes)
        let total_likes = res.total_likes
        let like = el
        animate(like, el)
        el.innerText = total_likes
        })
    .catch(error => {
        console.log(error)
    });
  }

  function animate(icon, el){
    if(icon.className=="far fa-heart like-icon"){
      icon.className = "fa-solid fa-heart like-icon";
    }else{
      icon.className = "far fa-heart like-icon";
    }
  }