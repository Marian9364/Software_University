async function attachEvents() {
    let messagesArea = document.getElementById('messages');
    let nameInput = document.querySelector('#controls > input[name="author"]');
    let contentInput = document.querySelector('#controls > input[name="content"]');
    let sendBtn = document.getElementById('submit');
    let refreshBtn = document.getElementById('refresh');

    const url = `http://localhost:3030/jsonstore/messenger`

    sendBtn.addEventListener('click', onSend);
    refreshBtn.addEventListener('click', onRefresh);

    async function onRefresh(){
        messagesArea.textContent = "";
        try {
            const response = await fetch(url);
    
            if (!response.ok || response.status != 200) {
                throw new Error('Invalid request');
            }
            const data = await response.json();
            for (let el of Object.values(data)) {
                let chatLine = `${el.author}: ${el.content}`;
                messagesArea.textContent += chatLine + "\n";
            }
            messagesArea.textContent.trimEnd();
        }
        catch (error) {
            alert(error.message);
        }
    }

    async function onSend() {
        const currentMsgData  = {author: nameInput.value, content: contentInput.value};
        fetch(`http://localhost:3030/jsonstore/messenger`, {
            method: 'post',
            headers: {'Content-type': 'application/json'},
            body: JSON.stringify(currentMsgData),
        });
        nameInput.value = '';
        contentInput.value = '';

        // let newLine = `${nameInput.value}: ${contentInput.value}`       //that is the way of doing it without POST request
        // messagesArea.textContent += newLine + "\n";
    }


}

attachEvents();