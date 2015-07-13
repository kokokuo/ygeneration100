


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
$(window).load(function () {
// ====================
	// jQuery masonry
	$('.grid').masonry({
	  columnWidth: '.grid-sizer',
	  itemSelector: '.grid-item',
	  percentPosition: true
	});	
});

$(document).ready(function(){
	// Nested ===============
	var imgs = $('.grid img').attr('src');
	// var width_type = ['size52','size43']
	// var height_type = ['size35','size24']
	// var same_type = ['size33','size22','size44']
	// //先設定好size(隨機) 
	// $('#container img').each(
 //        function(){
 //        	var img_width = $(this).width();
 //        	var img_height = $(this).height();
 //        	if ( img_width > img_height){
 //            	var num = getRandomInt(0,2);
	// 			image.addClass(width_type[num]);
	// 		}
	// 		else if (img_width < img_height){
	// 			var num = getRandomInt(0,2);
	// 			image.addClass(height_type[num]);
	// 		}
	// 		else {
	// 			var num = getRandomInt(0,3);
	// 			image.addClass(same_type[num]);
	// 		}
			
 //    });

 //    $("#container").nested({
	// 	selector: '.box',
	// 	minWidth: 50,
	// 	resizeToFit: true,
		
	// });
});


function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min)) + min;
}