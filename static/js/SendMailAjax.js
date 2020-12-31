$(document).ready(function () {
    console.log('test');
    $('#AjaxSend').on('click', function (e) {
        e.preventDefault();
        var SubEemail = $('#id_SubEemail').val();
        var data = {
            SubEemail: SubEemail,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        };
        console.log(data, SubEemail);
        $.ajax({
            type: "post",
            url: "http://127.0.0.1:8000/subs/",
            data: "data",
            success: function (response) {
                console.log(response);
                alert('yo')
            },
            error: function (error) {
                console.log(JSON.stringify(error));
            }
        });
    })
});
// const csrftoken = Cookies.get('csrftoken');