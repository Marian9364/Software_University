function solve() {

    let infoField = document.querySelector('.info');
    let departBtn = document.getElementById('depart');
    let arriveBtn = document.getElementById('arrive');
    let stopID = 'depot'

    function depart() {
        let url = `http://localhost:3030/jsonstore/bus/schedule/${stopID}`;

        
        fetch(url)
            .then(response => {
                if (response.status != 200) {
                    throw new Error("Error");
                }
                return response.json()
            })
            .then(data => {
                infoField.textContent = `Next stop ${data.name}`;
                departBtn.disabled = true;
                arriveBtn.disabled = false;
            })
            .catch(error => {
                departBtn.disabled = true;
                arriveBtn.disabled = true;
                infoField.textContent = error.message;
            })


    }

    function arrive() {
        let url = `http://localhost:3030/jsonstore/bus/schedule/${stopID}`;

        
        fetch(url)
            .then(response => {
                if (response.status != 200) {
                    throw new Error("Error");
                }
                return response.json()
            })
            .then(data => {
                stopID = data.next;
                infoField.textContent = `Arriving at ${data.name}`;
                departBtn.disabled = false;
                arriveBtn.disabled = true;
            })
            .catch(error => {
                departBtn.disabled = true;
                arriveBtn.disabled = true;
                infoField.textContent = error.message;
            })
        }

    return {
        depart,
        arrive
    };
}

let result = solve();