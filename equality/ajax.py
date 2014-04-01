##from django.utils import json
##from dajaxice.decorators import dajaxice_register
##
##@dajaxice_register
##def sayhello(request):
##    return simplejson.dumps({'message':'Hello World'})

$(function(){

    $('#searchtest').click(function() {

        $.ajax({
            type: "POST",
            url: "/searchtrips/",
            data: {
                'city' : $('#city').val(),
                'location' : $('#location').val(),
                'duration' : $('#duration').val(),
                'search_text' : $('#searchtest').val(),
                'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccess,
            dataType: 'html'
        });

    });

});

function searchSuccess(data, textStatus, jqXHR)
{
    $('#search-results').html(data);
}
