function dropdown(el) {
    if(el.parentElement.classList.contains("open")){
        el.parentElement.classList.remove("open");
    } else {
        el.parentElement.classList.add("open");
    }
}

function closeDropdown(el){
    el.parentElement.parentElement.classList.remove("open");
}