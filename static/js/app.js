Vue.component('home', {
    template: `
        <div>
            <h1>Welcome to My Portfolio</h1>
            <p>This is the home page.</p>
        </div>
    `
});

Vue.component('about', {
    template: `
        <div>
            <h1>About Me</h1>
            <p>This is the about page.</p>
        </div>
    `
});

Vue.component('contact', {
    template: `
        <div>
            <h1>Contact Me</h1>
            <p>This is the contact page.</p>
        </div>
    `
});

new Vue({
    el: '#app',
    data: {
        view: 'home'
    }
});
