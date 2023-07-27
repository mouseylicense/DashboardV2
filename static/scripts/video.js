
  //get video
  var vid = document.getElementById("video")
  var source = document.getElementById("src")
  function fetchvideo(){
  
  $.ajax({
   url: '/get_video',
   type: 'get',
   success: function(response){
    console.log(response);
    if (response == "empty"){
      console.log("No Video to play")}
    else{
      document.getElementById('video_cont').style.display = 'block'
      source.src = `static/videos/${response}`
      vid.load()
      vid.play()    
    }


    }})
    }
 
 
 $(document).ready(function(){
    fetchvideo()
    setInterval(fetchvideo,5000);
  
 });