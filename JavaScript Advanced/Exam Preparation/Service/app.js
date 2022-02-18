

window.addEventListener('load', solve);

function solve() {
    let typeProductEl = document.getElementById("type-product");
    let descriptionEl = document.getElementById("description");
    let clientNameEL = document.getElementById("client-name");
    let clientPhoneEL = document.getElementById("client-phone");
    let buttonSubmitEl = document.querySelector('#right button');
    let recievedOrdersEl = document.querySelector('#received-orders');
    let completedOrdersEl = document.getElementById('completed-orders');
    let clearBtn = document.querySelector('.clear-btn');


    
    clearBtn.addEventListener('click',(e)=>{
        const containers = document.querySelectorAll("#completed-orders .container");
        for(let cont of containers){
            cont.remove();
        }
    });

    buttonSubmitEl.addEventListener('click', (e)=>{
        e.preventDefault();
        if(typeProductEl.value == "" || descriptionEl.value == "" || clientNameEL.value == "" || clientPhoneEL.value == ""){
            return;
        }

        let containerDiv = document.createElement('div');
        let productTypeH2 = document.createElement('h2');
        let clientInfoH3 = document.createElement('h3');
        let descriptionH4 = document.createElement('h4');
        let btnStart = document.createElement('button');
        let btnFinish = document.createElement('button');

        containerDiv.classList.add("container");
        productTypeH2.textContent = `Product type for repair: ${typeProductEl.value}`;
        clientInfoH3.textContent = `Client information: ${clientNameEL.value}, ${clientPhoneEL.value}`;
        descriptionH4.textContent = `Description of the problem: ${descriptionEl.value}`;
        
        btnStart.classList.add("start-btn");
        btnStart.textContent = "Start repair";
        btnStart.addEventListener('click', (e)=>{
            btnStart.disabled = true;
            btnFinish.disabled = false;
        })

        btnFinish.classList.add("finish-btn");
        btnFinish.textContent = "Finish repair";
        btnFinish.setAttribute("disabled", true);
        btnFinish.addEventListener('click', (e)=>{
            completedOrdersEl.appendChild(containerDiv);
            btnFinish.remove();
            btnStart.remove();
        })

        
        containerDiv.appendChild(productTypeH2);
        containerDiv.appendChild(clientInfoH3);
        containerDiv.appendChild(descriptionH4);
        containerDiv.appendChild(btnStart);
        containerDiv.appendChild(btnFinish);

        recievedOrdersEl.appendChild(containerDiv);

        typeProductEl.value = "";
        descriptionEl.value = "";
        clientNameEL.value = "";
        clientPhoneEL.value = "";
        


    })

}