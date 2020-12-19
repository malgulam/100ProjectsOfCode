// assigning the hamburger elem to a var
const hamburger = document.querySelector(".hamburger");

// assigning the navlinks elem to a var
const navlinks = document.querySelector('.nav-links');

// assigning the links elem to a var
const links = document.querySelector('.nav-links li')

//js arrow function in use here
hamburger.addEventListener("click", () => {
    navlinks.classList.toogle("open");
    links.forEach(link => {
        link.classList.toogle("fade");
    });
});