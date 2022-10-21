$(document).ready(function()
{
    $("#p1").prepend("<b>I love jQuery!!!</b>.");
    $('.div1').children().hide();
    
    const reqobj = new XMLHttpRequest();

    reqobj.onload = function(){
        if(this.readyState==4 && this.status==200)
        {
            var data= JSON.parse(this.responseText);
            var author=data.author_name;
        }
    }

    reqobj.open('GET', "path/to/bookstore_document.json");
    reqobj.send();
});
