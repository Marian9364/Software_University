function attachEvents() {
    let postsBtn = document.getElementById('btnLoadPosts');
    let viewPostBtn = document.getElementById('btnViewPost');
    let dropDownMenu = document.getElementById('posts');

    postsBtn.addEventListener('click', createPosts);
    viewPostBtn.addEventListener('click', generateInformation);

    async function createPosts() {
        try {
            const response = await fetch('http://localhost:3030/jsonstore/blog/posts');
    
            if (!response.ok || response.status != 200) {
                throw new Error('Invalid request');
            }
            const data = await response.json();

            Object.values(data).forEach(info => {    
                let optionEl = createElement('option', info.id, info.title, dropDownMenu);
            });
    
        } catch (error) {
            alert(error.message);
        }
    }
    
    async function generateInformation() {
        let titleHeader = document.querySelector('#post-title');
        let contentList = document.querySelector('#post-body');
        let commentSection = document.querySelector('#post-comments');
        let targetId = dropDownMenu.value;

        try {
            const response = await fetch(`http://localhost:3030/jsonstore/blog/posts/${targetId}`);
    
            if (!response.ok || response.status != 200) {
                throw new Error('Invalid request');
            }
            const data = await response.json();

            titleHeader.textContent = data.title;
            contentList.textContent = data.body;
    
        } catch (error) {
            alert(error.message);
        }

        try {
            const response = await fetch(`http://localhost:3030/jsonstore/blog/comments`);

            if (!response.ok || response.status != 200) {
                throw new Error('Invalid request');
            }
            const data = await response.json();

            commentSection.replaceChildren();
            Object.values(data).forEach(info => {
                if (info.postId == targetId) {
                    let listEl = createElement('li', undefined, info.text, commentSection);
                    listEl.id = info.id;
                }
            })

        } catch (error) {
            alert(error.message);
        }
    }
}

function createElement(element, value, textCon, parent) {
    const el = document.createElement(element);

    if (value) {
        el.value = value;
    }
    if (textCon) {
        el.textContent = textCon;
    }
    if (parent) {
        parent.appendChild(el);
    }

    return el;
}

attachEvents();