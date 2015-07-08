


// $(window).load(function () {
//     $('.Collage').collagePlus({
// 	        // change this to adjust the height of the rows
// 	        'targetHeight' : 100,
// 	        // change this to try different effects
// 	        // valid effets = effect-1 to effect-6
// 	        'effect' : "effect-6",
// 	     	'fadeSpeed' : "fast",
// 	    });
// });

$(document).ready(function(){
	
	var type = ['size32','size43','size53','size42']
	//先設定好size(隨機) 
	$('#container img').each(
        function(){
            var num = getRandomInt(0,4);
			
			$(this).addClass(type[num]);
			
    });

    $("#container").nested({
		selector: '.box',
		minWidth: 50,
		resizeToFit: true,
		
	});
});


function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min)) + min;
}