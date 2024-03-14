$(document).ready(function(){
    $('.btn-check').click(function()
    {
        $(this).addClass('active-btn');
        $(this).prop('disabled', true);

    });
});


