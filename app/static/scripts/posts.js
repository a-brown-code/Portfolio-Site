const form = document.getElementById('message-form');
form.addEventListener('submit', function(e) { 
    e.preventDefault();
    const formData = new FormData(form);
    const payload = new URLSearchParams(formData);
    fetch('http://http://aerinbrownportfolio.duckdns.org:5000/api/timeline_post', {method: 'POST', body: payload})
    .then(res => res.json())
    .then(data => console.log(data))
    location.reload();
})

fetch('http://http://aerinbrownportfolio.duckdns.org:5000/api/timeline_post')
    .then((response) => {return response.json();})
    .then((data) => {
        let posts = data.timeline_posts;
        const messageList = document.querySelector('#message-list') 
        posts.map(function(post) {
            let name = document.createElement('p');
            let email = document.createElement('p');
            let content = document.createElement('p');
            name.innerHTML = post.name;
            email.innerHTML = post.email;
            content.innerHTML = post.content;
            
            let message = document.createDocumentFragment();
            message.appendChild(name);
            message.appendChild(email);
            message.appendChild(content);
            messageList.appendChild(message);
        });
    })
    .catch(function(error) {
        console.log(error);
    })