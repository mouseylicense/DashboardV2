  //get message
  var message = document.getElementById("message")
  function fetchmessage(){
  $.ajax({
   url: '/message',
   type: 'post',
   success: function(response){
    console.log(response)
    if (response["message"] == undefined){
      document.getElementById("message").innerHTML = ""}
    else{
      message.innerHTML = response["message"]
      message.style.backgroundColor = response["color"]
    }
    }
    
    
    });
 }
 
 $(document).ready(function(){
  fetchmessage()
  setInterval(fetchmessage,(60*1000));
  
 });