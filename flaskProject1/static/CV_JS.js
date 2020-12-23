function mouseOverImg(id,newSrc) {
    document.getElementById(id).src = newSrc;
}

function mouseOutImg(id,newSrc) {
    document.getElementById(id).src = newSrc;
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

