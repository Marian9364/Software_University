import { setUserData, clearUserData } from '../utils.js';
import * as api from './api.js';

//fail v koito da izvurshvame osnovnite operacii svurzani s potrebitelq kato login register i logout
//nujni sa ni funciite suvrzani s localStorage kato token i tn. koito sa v util.js

const endpoints = {
    login: '/users/login',
    register: '/users/register',
    logout: '/users/logout'
}

export async function login(email, password) {
    const result = await api.post(endpoints.login, { email, password });
    setUserData(result);
}

export async function register(email, password) {
    const result = await api.post(endpoints.register, { email, password });
    setUserData(result);  
}

export async function logout() {
    api.get(endpoints.logout);
    clearUserData();
}