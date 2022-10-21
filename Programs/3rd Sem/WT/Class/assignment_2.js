function on_head_click(event){
    alert("The discount sale will end very soon");
}

function on_para_click(event){
    paragraph[0].style.color = "red";

    paragraph[0].style.fontSize = "26px";
}

const header = document.getElementsByClassName("h");
const paragraph = document.getElementsByClassName("price");

header[0].addEventListener('click',on_head_click,true);
paragraph[0].addEventListener('click',on_para_click,true);