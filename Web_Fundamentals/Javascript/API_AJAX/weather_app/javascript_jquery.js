var temperature = 0
function convertTemperature(x){
	temperature = Math.round(x * 9/5 - 459.67)
}
$(document).ready(function() {
	$('form').submit(function() {	    			
   var userInput = $('#city').val()
   var apiKey = '&appid=dd85f8c765cba3d95db858295a41adc7'
   	console.log(userInput)
  	
  $.get("http://api.openweathermap.org/data/2.5/weather?q=" + userInput + apiKey, function(res) {	            
			console.log(res)
      var cityTemperature = res.main.temp;
      convertTemperature(cityTemperature);
      	console.log(temperature);
      $('#resultCity').text(res.name);
      $('#resultTemp').text(temperature + '°');
      $('#city').val('');
      
     }, 'json');
     return false;
	});
});