import { html } from '../../node_modules/lit-html/lit-html.js';
import * as petsService from '../api/pets.js'
import { createSubmitHandler } from '../utils.js';

//v editTemplate si slojihme na mqstoto na value="", .value=${el.property}
//slagame game kato parameter i FormHandlera za editbtn
const editTemplate = (pet, onSubmit) => html`
<section id="editPage">
    <form @submit=${onSubmit} class="editForm">
        <img src="./images/editpage-dog.jpg">
        <div>
            <h2>Edit PetPal</h2>
            <div class="name">
                <label for="name">Name:</label>
                <input name="name" id="name" type="text" .value=${pet.name}>
            </div>
            <div class="breed">
                <label for="breed">Breed:</label>
                <input name="breed" id="breed" type="text" .value=${pet.breed}>
            </div>
            <div class="Age">
                <label for="age">Age:</label>
                <input name="age" id="age" type="text" .value=${pet.age}>
            </div>
            <div class="weight">
                <label for="weight">Weight:</label>
                <input name="weight" id="weight" type="text" .value=${pet.weight}>
            </div>
            <div class="image">
                <label for="image">Image:</label>
                <input name="image" id="image" type="text" .value=${pet.image}>
            </div>
            <button class="btn" type="submit">Edit Pet</button>
        </div>
    </form>
</section>`;









//kakto v details tyk pravim sushtite operacii za da vzemem idto na elementa i tn
export async function editPage(ctx) {
    const petId = ctx.params.id;
    const pet = await petsService.getById(petId);

    ctx.render(editTemplate(pet, createSubmitHandler(ctx, onSubmit)));
}
//izpolzvame sushtata funkciq kato ot create.js no vikame .update na gameservice s parameter gameid i smenqme redirecta
async function onSubmit(ctx, data, event) {
    const petId = ctx.params.id;

    if (Object.values(data).some(f => f == '')) {
        return alert('All fields are required!')
    }
    //izprashtame dannite za create new element
    await petsService.update(petId, {
        name: data.name,
        breed: data.breed,
        age: data.age,
        weight: data.weight,
        image: data.image
    });

    event.target.reset();
    ctx.page.redirect('/details/' + petId);
}