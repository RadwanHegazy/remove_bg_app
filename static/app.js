


// variabels

var form = document.querySelector('form');
var file = document.querySelector('form input');
var loadLayer = document.querySelector('.load')


form.addEventListener('click',function(){
    file.click()
})



file.addEventListener('change',f=>{
    loadLayer.classList.toggle('view')

    var data = new FormData();
    data.append("image", $("#file")[0].files[0])
    $.ajax({
        method: "POST",
        url: "/process/",
        processData: false,
        contentType: false,
        mimeType: "multipart/form-data",
        data: data,
        success: function(data) {

            var download_url = data ;
            var a = document.createElement('a');
            
            a.href = download_url;
            a.download = true
            a.id = 'download'
            a.target = '_blank'
            
            a.click()
            
            loadLayer.classList.remove('view')
        }
    })



})
