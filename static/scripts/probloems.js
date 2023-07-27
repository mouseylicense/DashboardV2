//get problems
console.log("started")
  function fetchdata(){
  $.ajax({
   url: '/data',
   type: 'post',
   success: function(response){
    document.getElementById("container").innerHTML = "<h1 id='loading'>No Data</h1>"
    if (response != undefined){
      document.getElementById("container").innerHTML = ""

    }
    // Perform operation on the return value
    for(const property in response){

    room = property
    var problemsList = ""
    if (response[room]["problems"][0]){
      
      var img = `<img src="./static/Xmark.png" alt="problem" width="150" height="100">`
      for(let i=0;i<response[room]["problems"].length;i++){
        problemsList += `<div class="problem"><p>${response[room]["problems"][i]}</p></div>`

      }
    } else {
      var img = `<img src="./static/checkmark.png" alt="aok" width="150" height="100">`
      problemsList = `<div class="ok"><p>אין בעיות</p></div>`
    }
    document.getElementById("container").innerHTML +=
    `<div class="gallery">
      <div class="img-container">${img}</div>
      <div class="desc">
        <h2>${room}</h2>
        
        <div class="problems">${problemsList}</div>
        <p>${response[room]["isFree"]}</p>

      </div>
    </div>`
  }
   }
  });
 }
 
 $(document).ready(function(){
  fetchdata()
  setInterval(fetchdata,5000);
  
 });