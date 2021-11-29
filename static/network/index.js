document.addEventListener('DOMContentLoaded', function () {

    console.log('hi')
    let element = document.querySelectorAll(".edit-icon")
    element.forEach(function(el){
        el.addEventListener('click', function () {
            let card = el.parentElement.parentElement.parentElement
            let body = card.getElementsByClassName('card-body')[0]
            
            // console.log(card.childNodes[0])
          console.log('click', body.innerHTML);

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

        });
      });
});

