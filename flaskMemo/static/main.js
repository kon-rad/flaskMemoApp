'use strict';

(function(){


  console.log($);
  $('#memo_submit').click( function(e) {
    e.preventDefault();

    var data = {};
    data.title = $('#memo_title').val();
    data.message = $('#memo_content').val();
    $.ajax('http://localhost:5000/memo', {
      method: 'POST',
      data: JSON.stringify(data),
      headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
      },
      contentType: 'application/json',
      success: function(data) {
          console.log('success');
          console.log(JSON.stringify(data));
          $('#result').html( JSON.stringify(data) );
      },
      error  : function() { console.log('error');}
    });
    
    // $.ajax({
    //   type: 'POST',
    //   data: JSON.stringify(data),
    //       contentType: 'application/json',
    //               url: 'http://localhost:5000/memo',						
    //               success: function(data) {
    //                   console.log('success');
    //                   console.log(JSON.stringify(data));
    //                   $('#result').html( data );
    //               },
    //               error  : function() { console.log('error');}
    //           });
  })


}())