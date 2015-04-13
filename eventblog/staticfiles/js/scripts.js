
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

function view(){
	$("#view_body").show();
	$("#show_body").hide();
}

function show(){
	$("#view_body").hide();
	$("#show_body").show();
}

function feedback(){
	$("#feedback_body").show();
	$("#suggestion_body").hide();
}

function suggestion(){
	$("#feedback_body").hide();
	$("#suggestion_body").show();
}