$(function () {
    name_error=false;
    pwd_error=false;
    if({{ error_name }} == 1){
        $('.user_error').html("用户名错误").show();
    }
    if({{ error_pwd }} == 1)
    {
        $('.pwd_error').html("用户名错误").show();
    }
    $('.name_input').blur(function () {
        if($('.name_input').val().length==0){
            $('.user_error').html("请填写用户名").show();
            name_error=false;
        }else {
            $('.user_error').html().hide();
            name_error=true;
        }
    });
    $('.pass_input').blur(function () {
        if($(this).val().length==0){
            $('.pwd_error').html("请填写密码").show();
            pwd_error=false;
        }else {
            $('.pwd_error').html().hide();
            pwd_error=true;
        }
    });
    $('.form_input').submit(function () {
       if(name_error==false&&pwd_error==false){
           return true;
       } else{
           return false;
       }
    });
})