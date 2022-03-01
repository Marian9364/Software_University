async function lockedProfile() {
    const url = 'http://localhost:3030/jsonstore/advanced/profiles';

    let response = await fetch(url);
    let data = await response.json();
    let mainElement = document.getElementById('main');
    mainElement.innerHTML = '';
    
    let numOfCurrentProfile = 0;
    for (const currentProfile in data) {
        numOfCurrentProfile++;

        const profileHTML = `<div class="profile">
            <img src="./iconProfile2.png" class="userIcon" />
            <label>Lock</label>
            <input type="radio" name="user${numOfCurrentProfile}Locked" value="lock" checked>
            <label>Unlock</label>
            <input type="radio" name="user${numOfCurrentProfile}Locked" value="unlock"><br>
            <hr>
            <label>Username</label>
            <input type="text" name="user${numOfCurrentProfile}Username" value="${data[currentProfile].username}" disabled readonly />
            <div class="hiddenInfo" disabled readonly>
                <hr>
                <label>Email:</label>
                <input type="email" name="user${numOfCurrentProfile}Email" value="${data[currentProfile].email}"/>
                <label>Age:</label>
                <input type="email" name="user${numOfCurrentProfile}Age" value="${data[currentProfile].age}"/>
            </div>
    
            <button>Show more</button>
        </div>`;

        mainElement.innerHTML += profileHTML + '\n';

    }

    mainElement.innerHTML.trimEnd();

    const buttons = Array.from(document.getElementsByTagName('button'));
    buttons.forEach(b => b.addEventListener('click', showHideFields));

    function showHideFields(event) {
        if(event.target.parentNode.children[2].checked) {

            return;
        }
        
        if(event.target.textContent === 'Show more') {
            event.target.parentNode.children[9].style.display = 'block';
            event.target.parentNode.children[9].classList.remove('hiddenInfo');
            event.target.parentNode.children[9].children[2].style.display = 'block';
            event.target.parentNode.children[9].children[3].style.display = 'block';
            event.target.textContent = 'Hide it';
        } else {
            event.target.parentNode.children[9].style.display = 'none';
            event.target.parentNode.children[9].classList.add('hiddenInfo');
            event.target.textContent = 'Show more';
        }
    }
}