//vsichki tezi operacii mogat da budat i v api.js vmesto v nov fail
//tova e service file

import * as api from './api.js';

const endpoints = {
    //recent: '/data/games?sortBy=_createdOn%20desc&distinct=category',
    pets: '/data/pets?sortBy=_createdOn%20desc&distinct=name',
    create: '/data/pets',
    byId: '/data/pets/',
    deleteById: '/data/pets/',
    update: '/data/pets/'
};
//vzimame segashi igri s funtion getRecent koqto pravi get zaqvka na daden adres ot endpoints
// export async function getRecent() {
//     return api.get(endpoints.recent);
// }

//vzimame vsichki igri s funtion getAll koqto pravi get zaqvka na daden adres ot endpoints
export async function getAll() {
    return api.get(endpoints.pets);
}

//za details ni trqbva getById za da pokajem tochniq detail za izbraniq el         
export async function getById(id) {
    return api.get(endpoints.byId + id)
}

//funkciq za suzdavane na edinichen element demek da dobavim nova igra
export async function create(data) {
    return api.post(endpoints.create, data);
}

//funkciq za update na element demek edit
export async function update(id, data) {
    return api.put(endpoints.update + id, data)
}


//funkciq delete na edinichen element
export async function deleteById(id) {
    return api.del(endpoints.deleteById + id);
}