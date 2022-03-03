function getInfo() {
    let stopIDEl = document.getElementById('stopId').value;
    let stopNameField = document.getElementById('stopName');
    let busesList = document.getElementById('buses');

    let validBuses = ['1287', '1308', '2334', '1327'];

    let url = `http://localhost:3030/jsonstore/bus/businfo/${stopIDEl}`;

    fetch(url)
        .then(response => {
            if(!validBuses.includes(stopIDEl)) {
                throw new Error('Error');
            }

            return response.json();
        })
        .then(data => {
            busesList.replaceChildren();
            stopNameField.textContent = data.name;
            Object.entries(data.buses)
                .map(([bus, time]) => {
                    let liEl = document.createElement('li');
                    liEl.textContent = `Bus ${bus} arrives in ${time}`;

                    busesList.appendChild(liEl);
                });
        })
        .catch(error => {
            busesList.replaceChildren();
            stopNameField.textContent = error.message;
        })

}