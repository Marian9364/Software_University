window.addEventListener('load', solve);

function solve() {
    let genreEl = document.getElementById("genre");
    let nameEl = document.getElementById("name");
    let authorEl = document.getElementById("author");
    let dateEL = document.getElementById("date");
    let addBtn = document.getElementById("add-btn");
    let allHitsContainerEl = document.querySelector("#all-hits > .all-hits-container");
    let totalLikespEl = document.querySelector('#total-likes > div > p');
    let savedSongsEl = document.querySelector(".saved-container");

    addBtn.addEventListener('click', (e)=>{
        e.preventDefault();

        if(genreEl.value && nameEl.value && authorEl.value && dateEL.value){
            let divHitsInfo = document.createElement('div');
            divHitsInfo.classList.add("hits-info");
            let img = document.createElement('img');
            img.src = './static/img/img.png';
            let genreH2El = document.createElement('h2');
            genreH2El.textContent = "Genre: " + genreEl.value;

            let nameH2El = document.createElement('h2');
            nameH2El.textContent = "Name: " + nameEl.value;

            let authorH2El = document.createElement('h2');
            authorH2El.textContent = "Author: " + authorEl.value;

            let dateH3El = document.createElement('h3');
            dateH3El.textContent = "Date: " + dateEL.value;

            let saveBtn = document.createElement('button');
            saveBtn.classList.add('save-btn')
            saveBtn.textContent = "Save song";
            saveBtn.addEventListener('click', (e)=>{
                
                savedSongsEl.appendChild(e.currentTarget.parentNode);
                e.currentTarget.parentElement.children[6].remove();
                e.currentTarget.parentElement.children[5].remove();
                
                
            })

            let likeBtn = document.createElement('button');
            likeBtn.classList.add('like-btn');
            likeBtn.textContent = "Like song";
            likeBtn.addEventListener('click', (e)=>{
                let splittedData = totalLikespEl.textContent.split(" ");
                let totalLikes = Number(splittedData[2]);
                totalLikes++;
                totalLikespEl.textContent = "Total Likes: " + totalLikes;
                e.currentTarget.setAttribute("disabled", true);
            })

            let deleteBtn = document.createElement('button');
            deleteBtn.classList.add('delete-btn');
            deleteBtn.textContent = "Delete";
            deleteBtn.addEventListener('click', (e)=>{
                e.currentTarget.parentNode.remove();
            })

            divHitsInfo.appendChild(img);
            divHitsInfo.appendChild(genreH2El);
            divHitsInfo.appendChild(nameH2El);
            divHitsInfo.appendChild(authorH2El);
            divHitsInfo.appendChild(dateH3El);
            divHitsInfo.appendChild(saveBtn);
            divHitsInfo.appendChild(likeBtn);
            divHitsInfo.appendChild(deleteBtn);

            allHitsContainerEl.appendChild(divHitsInfo);

            genreEl.value = "";
            nameEl.value = "";
            authorEl.value = "";
            dateEL.value = "";

        }
    })
}