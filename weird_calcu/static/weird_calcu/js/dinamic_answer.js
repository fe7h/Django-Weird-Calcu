const appName = 'WeirdCalcu'

const div = document.getElementById(appName + '_answer')
const btn = document.getElementById(appName + '_submit_btn')

const img = document.createElement('img')

btn.addEventListener('click', function(event) {
    event.preventDefault()

    const form = document.getElementById(appName + '_form')
    const formData = new FormData(form)

    try {
        const url = new URL(form.action, window.location.origin)
        url.search = new URLSearchParams(formData)

        fetch(url)
            .then(res => {
                if (!res.ok){
                    throw new Error(`${res.status}:${res.statusText}`)
                }
                return res.blob()
            })
            .then(function(blob) {
                const img_url = URL.createObjectURL(blob)
                console.log(img_url)
                img.setAttribute('src', img_url)
                div.prepend(img)
            })
    } catch(error) {
        console.log(error.message)
    }
})
