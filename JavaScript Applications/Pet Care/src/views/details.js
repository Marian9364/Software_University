import { html, nothing } from '../../node_modules/lit-html/lit-html.js';
import * as petsService from '../api/pets.js'

const detailsTemplate = (pet, onDelete) => html`
<section id="detailsPage">
<div class="details">
    <div class="animalPic">
        <img src=${pet.image}>
    </div>
    <div>
        <div class="animalInfo">
            <h1>Name: ${pet.name}</h1>
            <h3>Breed: ${pet.breed}</h3>
            <h4>Age: ${pet.age}</h4>
            <h4>Weight: ${pet.weight}</h4>
            <h4 class="donation">Donation: 0$</h4>
        </div>
        <!-- if there is no registered user, do not display div-->
        <div class="actionBtn"></div>

        <!-- Edit/Delete buttons ( Only for creator of this game )  -->
        ${pet.isOwner
        ? html`
            <!-- Only for registered user and creator of the pets-->
            <a href="/edit/${pet._id}" class="edit">Edit</a>
            <a @click=${onDelete} href="javascript:void(0)" class="remove">Delete</a>`
        : nothing}
        </div>
    </div>
</div>
</section>`;




            // <!--(Bonus Part) Only for no creator and user-->
            // <a href="#" class="donate">Donate</a>


 
export async function detailsPage(ctx) {
    //suzdavame potrebitelsko id
    const petId = ctx.params.id;
    //vzimame opredelen element po ID
    const pet = await petsService.getById(petId);
    //ako ima lognat user zakachame .isOwner na samiq element(igra) koito da go ima samo ako user-ID = element.id(gameID)
    if (ctx.user) {
        pet.isOwner = ctx.user._id == pet._ownerId;
    }
    //renderirame
    ctx.render(detailsTemplate(pet, onDelete));

    //eventhandler za deletebtn
    async function onDelete() {
        const choice = confirm('Are you sure that you want to delete this element?');
        if (choice) {
            await petsService.deleteById(petId);
            ctx.page.redirect('/');
        }
    }
}






