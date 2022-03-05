;
document.addEventListener("DOMContentLoaded",function(){
    markmaps = document.querySelectorAll(".mkdocs-markmap");

    for (let i = 0; i < markmaps.length ; i++){
        markmaps[i].style.heigth = parseFloat(markmaps[i].offsetHeight) * 3
        
    }
});

