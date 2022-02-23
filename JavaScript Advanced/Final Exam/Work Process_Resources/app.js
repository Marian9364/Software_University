

function solve() {
    let firstNameEl = document.getElementById('fname');

    let lastNameEL = document.getElementById('lname');
    let emailEl = document.getElementById('email');
    let birthEL = document.getElementById('birth');
    let positionEl = document.getElementById('position');
    let salaryEl = document.getElementById('salary');
    let hireWorkerBtn = document.getElementById('add-worker');
    let tbodyEL = document.querySelector('tbody');
    let sumEl = document.getElementById('sum');
    let currentSum = 0


    hireWorkerBtn.addEventListener('click', (e)=>{
        e.preventDefault();

        if(firstNameEl.value == "" || lastNameEL.value == "" || emailEl.value == "" || birthEL.value == "" || positionEl.value == "" || salaryEl.value == ""){
            return
        }
        

        let trForTbody = document.createElement('tr');
        let tdFirstName = document.createElement('td');
        let tdLastName = document.createElement('td');
        let tdEmail = document.createElement('td');
        let tdDateOfBirth = document.createElement('td');
        let tdPosition = document.createElement('td');
        let tdSalary = document.createElement('td');
        let tdForButtonsFiredAndEdit = document.createElement('td');
        let editBtn = document.createElement('button');
        let firedBtn = document.createElement('button');
        

        editBtn.classList.add('edit');
        editBtn.textContent = "Edit";
        editBtn.addEventListener('click', (e)=>{


            let numberOfCurrentSalary = e.currentTarget.parentElement.parentElement.children[5];
            
            currentSum -= Number(numberOfCurrentSalary.textContent);
            
            sumEl.textContent = currentSum.toFixed(2);




            firstNameEl.value = e.currentTarget.parentElement.parentElement.children[0].textContent;
            lastNameEL.value = e.currentTarget.parentElement.parentElement.children[1].textContent;
            emailEl.value = e.currentTarget.parentElement.parentElement.children[2].textContent;
            birthEL.value = e.currentTarget.parentElement.parentElement.children[3].textContent;
            positionEl.value = e.currentTarget.parentElement.parentElement.children[4].textContent;
            salaryEl.value = e.currentTarget.parentElement.parentElement.children[5].textContent;
            
            let tdToRemove = e.currentTarget.parentElement.parentElement
            
            tdToRemove.remove();
           
        })


        firedBtn.classList.add('fired');
        firedBtn.textContent = "Fired";
        firedBtn.addEventListener('click', (e)=>{
            let numberOfCurrentSalary = e.currentTarget.parentElement.parentElement.children[5];
            
            currentSum -= Number(numberOfCurrentSalary.textContent);
            
            sumEl.textContent = currentSum.toFixed(2);
            let tdToRemove = e.currentTarget.parentElement.parentElement
           
            tdToRemove.remove();
        })
        

        tdFirstName.textContent = firstNameEl.value;
        tdLastName.textContent = lastNameEL.value;
        tdEmail.textContent = emailEl.value;
        tdDateOfBirth.textContent = birthEL.value;
        tdPosition.textContent = positionEl.value;
        tdSalary.textContent = salaryEl.value;
        tdForButtonsFiredAndEdit.appendChild(firedBtn);
        tdForButtonsFiredAndEdit.appendChild(editBtn);

        trForTbody.appendChild(tdFirstName);
        trForTbody.appendChild(tdLastName);
        trForTbody.appendChild(tdEmail);
        trForTbody.appendChild(tdDateOfBirth);
        trForTbody.appendChild(tdPosition);
        trForTbody.appendChild(tdSalary);
        trForTbody.appendChild(tdForButtonsFiredAndEdit);

        tbodyEL.appendChild(trForTbody);

        currentSum += Number(salaryEl.value)
        sumEl.textContent = currentSum.toFixed(2);


    

        firstNameEl.value = "";
        lastNameEL.value = "";
        emailEl.value = "";
        birthEL.value = "";
        positionEl.value = "";
        salaryEl.value = "";

    })
}
solve()