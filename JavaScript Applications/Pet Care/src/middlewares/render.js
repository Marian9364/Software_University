import { render, html } from '../../node_modules/lit-html/lit-html.js';

//direktno tuk si pravim navTemplate za navigaciqta  za da renderira sprqmo ima li user ili ne. nqma nujda ot nov fail samo za navtemplate

const navTemplate = (user) => html`
    <nav>
        <section class="logo">
            <img src="./images/logo.png" alt="logo">
        </section>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/catalog">Dashboard</a></li>
    ${user
    ? html`
            <li><a href="/create">Create Postcard</a></li>
            <li><a href="/logout">Logout</a></li>`
    : html`
            <li><a href="/login">Login</a></li>
            <li><a href="/register">Register</a></li>`}
        </ul>
    </nav>`;

//dobavihme class my-header na header v index.html za da go queryselectnem za root na navbar

const header = document.querySelector('.my-header');
const root = document.getElementById('content');

function ctxRender(content) {
    render(content, root);
}
//rendim navbara spramo ima li lognat user ili ne i dobavqme render kum ctx za vsihcki drugi renderi
export function addRender(ctx, next) {
    render(navTemplate(ctx.user), header)
    ctx.render = ctxRender;
    next();
}

