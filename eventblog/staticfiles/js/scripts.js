
$(document).ready(function(){/* jQuery toggle layout */
$('#btnToggle').click(function(){
  if ($(this).hasClass('on')) {
    $('#main .col-md-6').addClass('col-md-4').removeClass('col-md-6');
    $(this).removeClass('on');
  }
  else {
    $('#main .col-md-4').addClass('col-md-6').removeClass('col-md-4');
    $(this).addClass('on');
  }
});
});

function topevents(){
    $("#topblogs").removeClass("active")
    $("#topevents").addClass("active")
    $("#myblog").removeClass("active")
    $(this).addClass("active")
	$("#topevents_body").show();
	$("#topblogs_body").hide();
	$("#myblog_body").hide();
}

function topblogs(){
    $("#topblogs").addClass("active")
    $("#topevents").removeClass("active")
    $("#myblog").removeClass("active")
	$("#topevents_body").hide();
	$("#topblogs_body").show();
	$("#myblog_body").hide();
}

function myblog(){
    $("#topblogs").removeClass("active")
    $("#topevents").removeClass("active")
    $("#myblog").addClass("active")
	$("#topevents_body").hide();
	$("#topblogs_body").hide();
	$("#myblog_body").show();
}

function feedback(id){
    $("#suggestion_body_"+id).hide()
    $("#rating_body_"+id).hide()
    $("#feedback_body_"+id).toggle()
    $("#feedback_body_"+id).find("#id_event").val(id)
}

function suggestion(id){
    $("#feedback_body_"+id).hide()
    $("#rating_body_"+id).hide()
    $("#suggestion_body_"+id).toggle()
    $("#suggestion_body_"+id).find("#id_event").val(id)
}

function rating(id){
    $("#feedback_body_"+id).hide()
    $("#suggestion_body_"+id).hide()
    $("#rating_body_"+id).toggle()
    $("#rating_body_"+id).find("#id_event").val(id)
}



function comment(id){
    $("#comment_body_"+id).toggle()
    $("#comment_body_"+id).find("#id_blog").val(id)
}

function comments(id){
    $("#comment_body"+id).toggle()
    $("#comment_body"+id).find("#id_blog").val(id)
}

function adminlogin(){
    $("#employeelogin_body").hide();
	$("#adminlogin_body").toggle();
}

function employeelogin(){
	$("#adminlogin_body").hide();
	$("#employeelogin_body").show();
}