const appName = 'WeirdCalcu'

const div = document.getElementById('div')
const btn = document.getElementById(appName + '_submit_btn')

const img = document.createElement('img')

btn.addEventListener('click', function(event) {
    event.preventDefault()

    const formData = new FormData(document.getElementById(appName + '_form'))

    try {
        const url = new URL('/calculated', window.location.href)
        url.search = new URLSearchParams(formData)

        fetch(url)
            .then(res => res.blob())
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
