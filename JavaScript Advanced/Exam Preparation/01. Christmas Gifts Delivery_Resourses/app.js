function solution() {

    let btnAddGift = document.querySelector('.card div button');
    let ulElOfListOfGifts = document.querySelectorAll('ul')[0];
    let ulElOfSentGifts = document.querySelectorAll('ul')[1];
    let ulElOfDiscardedGifts = document.querySelectorAll('ul')[2];

    btnAddGift.addEventListener('click', () => {
        let inputOfAddGifts = document.querySelector('.card input[placeholder="Gift name"]');
        let liEl = document.createElement('li');
        let sendButton = document.createElement('button');
        let discardButton = document.createElement('button');

        sendButton.setAttribute('id', 'SendButton');
        sendButton.textContent = 'Send';
        sendButton.addEventListener('click', (e) => {
            let newLi = document.createElement('li');
            let text = e.currentTarget.parentElement.innerText;
            let indexOfSendDiscard = text.indexOf('SendDiscard');
            let substringText = text.substring(0, indexOfSendDiscard);
            newLi.textContent = substringText;
            e.currentTarget.style.display = "none";
            discardButton.style.display = "none";
            ulElOfSentGifts.appendChild(newLi);
            ulElOfListOfGifts.removeChild(e.currentTarget.parentElement);
            
        })

        discardButton.setAttribute('id', 'DiscardButton');
        discardButton.textContent = 'Discard';

        discardButton.addEventListener('click', (e) => {
            let newLi = document.createElement('li');
            let text = e.currentTarget.parentElement.innerText;
            let indexOfSendDiscard = text.indexOf('SendDiscard');
            let substringText = text.substring(0, indexOfSendDiscard);
            newLi.textContent = substringText;
            e.currentTarget.style.display = "none";
            sendButton.style.display = "none";
            ulElOfDiscardedGifts.appendChild(newLi);
            ulElOfListOfGifts.removeChild(e.currentTarget.parentElement);

            
        })

        liEl.textContent = inputOfAddGifts.value;
        liEl.classList.add("gift");
        liEl.appendChild(sendButton);
        liEl.appendChild(discardButton);

        ulElOfListOfGifts.appendChild(liEl);

  
        inputOfAddGifts.value = "";
        let arrOfGifts = Array.from(ulElOfListOfGifts.children);
        if (arrOfGifts.length > 1){
            let sortedArrOfGifts = arrOfGifts.sort((a, b) => a.textContent.localeCompare(b.textContent));
        
            for(let gift of sortedArrOfGifts){
                ulElOfListOfGifts.appendChild(gift);
            }
        }

    });


    

}