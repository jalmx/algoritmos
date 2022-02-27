function resizeMarkmap(){

}


function setYear() {
    const txt = "Alejandro Leyva 2022 - " + new Date().getFullYear()
    const tagDate = document.createElement("div")
    // tagDate.setAttribute("style", "text-align: center")
    tagDate.innerHTML += txt
    const footer = document.getElementsByClassName("md-footer-copyright")[0]
    footer.appendChild(tagDate)
}

setYear()
// resizeMarkmap()