$(document).ready(function(){

	//Slick
	$('.fast_ques_slide_right').slick({
		infinite: true,
		slidesToShow: 5,

		//slide animation direction and amount (if set -1 means slder animated from left to right) , the dot will disappear
		// and you should set rtl = true ,too
		slidesToScroll: -5,
		
		// Enable Next/Prev arrows
		arrows: false,

		// prev arrow
		prevArrow: '<button type="button" data-role="none" class="slick-prev">Previous</button>',

		// next arrow
		nextArrow: '<button type="button" data-role="none" class="slick-next">Next</button>',

		// Enables auto play of slides
		autoplay: true,

		// Auto play change interval
		autoplaySpeed: 3000,

		// Enables centered view with partial prev/next slides. 
		// Use with odd numbered slidesToShow counts.
		centerMode: false,

		// Side padding when in center mode. (px or %)
		centerPadding: '50px',

		// CSS3 easing
		cssEase: 'ease',

		// Current slide indicator dots
		dots: true,

		//滑鼠懸停,自動播放
		pauseOnHover: false,

		//slider : right to left direction(image index),if set true ,then you will add a custom attribute tag called 'dir' 
		//and set value is rtl
		rtl: true,
	});

	
	$('.fast_ques_slide_left').slick({
		infinite: true,
		slidesToShow: 5,

		//slide animation direction and amount (if set -1 means slder animated from left to right) , the dot will disappear
		// and you should set rtl = true ,too
		slidesToScroll: 5,
		
		// Enable Next/Prev arrows
		arrows: false,

		// prev arrow
		prevArrow: '<button type="button" data-role="none" class="slick-prev">Previous</button>',

		// next arrow
		nextArrow: '<button type="button" data-role="none" class="slick-next">Next</button>',

		// Enables auto play of slides
		autoplay: true,

		// Auto play change interval
		autoplaySpeed: 3000,

		// Enables centered view with partial prev/next slides. 
		// Use with odd numbered slidesToShow counts.
		centerMode: false,

		// Side padding when in center mode. (px or %)
		centerPadding: '50px',

		// CSS3 easing
		cssEase: 'ease',

		// Current slide indicator dots
		dots: false,

		//滑鼠懸停,自動播放
		pauseOnHover: false,

		//slider : right to left direction(image index),if set true ,then you will add a custom attribute tag called 'dir' 
		//and set value is rtl
		rtl: true,
	});

	//=============
	//Free Wall
	
});
