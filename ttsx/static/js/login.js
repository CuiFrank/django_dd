/**
 * Created by python on 17-7-5.
 */
$(function(){

    name_error = true
    pwd_error = false


    $('.name_input').blur(function(){
        name = $('.name_input').val()
        $.get('/user/register_name/?name='+name,function(dat){
            if (dat['res']== '1'){
                $('.user_error').html('用户名不存在').show()
                name_error = false
            }
            else{
                $('.user_error').hide()
                name_error = true
            }
        })
    })


    $('#login_form').submit(function(){
        pwd = $('.pass_input').val()
        name = $('.name_input').val()
        if(pwd != ''){
            pwd_error = true
        }
        else{
            $('.pwd_error').show()
        }
        if(name == ''){
            name_error = false
        }
        if (name_error && pwd_error){
            return true
        }
        else{
            return false
        }
    })


})