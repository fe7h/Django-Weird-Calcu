
const btn = document.getElementById('btn')
const img = document.createElement('img')

btn.addEventListener('click', function(event){
    event.preventDefault()

    const form = document.getElementById('form')

    try{
    const queryParams = {
        first: +form.elements.first.value,
        second: +form.elements.second.value
    }

    const url = new URL('/calculated', window.location.href)
    url.search = new URLSearchParams(queryParams)

    fetch(url)
        .then(res => res.json())
        .then(function(data){
            console.log(data)
            img.setAttribute('src',data.img)
            btn.after(img)
        })
    } catch(error){
        console.log(error.message)
    }
})
