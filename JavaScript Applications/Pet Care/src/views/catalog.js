import { html } from '../../node_modules/lit-html/lit-html.js';
import * as petsService from '../api/pets.js';
//importvame gamesService demek vsichki funkcii ot games.js kato getRecent da vzeme vsichki segashni postove


const catalogTemplate = (pets) => html`
<section id="dashboard">
    <h2 class="dashboard-title">Services for every animal</h2>
    <div class="animals-dashboard">
    ${pets.length > 0
    ? pets.map(cardTemplate)
    : html`
        <div>
        <p class="no-pets">No pets in dashboard</p>
        </div>`}
    </div>
</section>`;

//suzdavame si template samo za edin element koito da izmapnem posle
const cardTemplate = (pet) => html`
<div class="animals-board">
    <article class="service-img">
        <img class="animal-image-cover" src=${pet.image}>
    </article>
    <h2 class="name">${pet.name}</h2>
    <h3 class="breed">${pet.breed}</h3>
    <div class="action">
        <a class="btn" href="/details/${pet._id}">Details</a>
    </div>
</div>`;


export async function catalogPage(ctx) {
    const pets = await petsService.getAll();
    ctx.render(catalogTemplate(pets));
}


