var btn = document.createElement("BUTTON");
btn.style.margin = "10px";
btn.innerHTML = "Click me to change the background color";
document.body.appendChild(btn);

btn.onclick = changecolor;
btnOnCLick = 0;
function changecolor() {
    if (btnOnCLick == 0) {
        document.body.style.backgroundColor = "violet";
        btnOnCLick += 1;
        return false;
    }
    else if(btnOnCLick == 1) {
        document.body.style.backgroundColor = "purple";
        btnOnCLick -= 1;
        return false;
    }
}
