
$(window).load(function () {
// ====================
	 // jQuery masonry
	$('#grid').masonry({
		columnWidth: '.grid-sizer',
	  // columnWidth: '.grid-sizer',
	  itemSelector: '.grid-item',
	  percentPosition: true,
	});	

	// // 屬性選擇出 div face_content_block_開頭
	//  $('div[id^=face_content_block_]').each(function(index){
	//  		// 找出此selector下的元素img
	//  		var face_image_w = $( this ).find('img').width();
	//  		var face_image_h = $( this ).find('img').height();
	//  		console.log(index,face_image_w,face_image_h)
	//  		// 加入到css中
	//  		$(this).css('width',face_image_w).css('height',face_image_h);
	//  });
	
	 // jQuery masonry
	 // 不同的區塊要使用完全不同的css

	$('#grid-water').masonry({
			columnWidth: '.grid-sizer-water',
			itemSelector: '.grid-item-water',
			percentPosition: true,
			singleMode:true,
			animate:true
	});

	// Modal ： 點擊人臉或文字時會彈出影片，透過編號過濾出
	// 需要當圖片載入完才可以做的動作，imagesLoaded套件要待測試
	$('a[id^=face_video_]').click(function(event) {
	    	event.preventDefault();
	        var faceVideoModal = $('#face_modal');
	        modalBody = faceVideoModal.find('.modal-body');

			video_serial =''
	        // 取 id 
	        var id = $(this).attr('id').split("face_video_")[1]
	        console.log('face id =' + id)
	        //ajax
	        $.get(
	        	"/fastquestion/video/",
	        	{
	        		face_id:id
	        	},
	        	function(data){
			        // 影片的編號
			        video_serial = data.youtube_serial;
			        console.log(id,video_serial)
			        //名稱
			        modalTitle = faceVideoModal.find('.modal-title')
			        modalTitle.text(data.title)
			        // load content into modal
			        content = '<div class="videowrapper">' +
			                    	'<iframe width="100%" height="390px" src="https://www.youtube.com/embed/' + video_serial + '" frameborder="0" allowfullscreen></iframe>'
			                    	+
			                	'</div>' +
			                	'<p>' + data.content + '</p>';
			        if(modalBody.find('.videowrapper')){
			        	$('.videowrapper').remove();	
			        }
			        if(modalBody.find('p')){
			        	$('p').remove();	
			        }
			        modalBody.append(content);
        		}
    		);


	        
	        // display modal
	        // 因為已經用attribute data設定了，所以不用再次顯示
	        // faceVideoModal.modal('show');
	});
	
});

$(document).ready(function(){


	
	// Nested ===============
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



// Collage
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
