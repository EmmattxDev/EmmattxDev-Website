let checkbox = document.querySelector("input[name=theme_switch]");

//system or browser preferred theme initialization
if (window.matchMedia('(prefers-color-scheme: dark)').matches){
    document.documentElement.setAttribute('data-theme', 'dark');
    checkbox.checked = true;
} else {
    document.documentElement.setAttribute('data-theme', 'light');
    checkbox.checked = false;
}

//dynamic theme toggle functionality with checkbox
checkbox.addEventListener('change', (cb) =>{
    document.documentElement.setAttribute(
        'data-theme',
        cb.target.checked ? 'dark' : 'light'
    );
})