function mouseOverImg(id) {
    document.getElementById(id).src = "LeorreSea3Circle.png";
}

function mouseOutImg(id) {
    document.getElementById(id).src = "LeorreSeaCircle.png";
}

function changeElementSize(id,size){
    document.getElementById(id).style.width=size;
    document.getElementById(id).style.height=size;
}

function focusingContact(x,color){
    x.style.background=color;
}

function submitPop(){
    var popup = document.getElementById("myPopup");
    popup.classList.toggle("show");
}

