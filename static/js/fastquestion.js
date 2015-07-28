
// $(window).load(function () {
// // ====================
// 	 // jQuery masonry
// 	$('#grid').masonry({
// 		columnWidth: '.grid-sizer',
// 	  // columnWidth: '.grid-sizer',
// 	  itemSelector: '.grid-item',
// 	  percentPosition: true,
// 	});	

// 	$('#grid-water').masonry({
// 			columnWidth: '.grid-sizer-water',
// 			itemSelector: '.grid-item-water',
// 			percentPosition: true,
// 			singleMode:true,
// 			animate:true
// 	});

// 	// Modal ： Show Face
// 	// need loaded images then can work
// 	$('a[id^=face_video_]').click(function(event) {
// 	    	event.preventDefault();
// 	        var faceVideoModal = $('#face_modal');
// 	        modalBody = faceVideoModal.find('.modal-body');

// 			video_serial =''
// 	        // Get id 
// 	        var id = $(this).attr('id').split("face_video_")[1]
// 	        console.log('face id =' + id)
// 	        //ajax
// 	        $.get(
// 	        	"/fastquestion/video/",
// 	        	{
// 	        		face_id:id
// 	        	},
// 	        	function(data){
// 			        // video serial
// 			        video_serial = data.youtube_serial;
// 			        console.log(id,video_serial)
// 			        //name
// 			        modalTitle = faceVideoModal.find('.modal-title')
// 			        modalTitle.text(data.title)
// 			        // load content into modal
// 			        // ?enablejsapi=1 for enable Js Youtube api ,then can close  or pause
// 			        content = '<div class="videowrapper">' +
// 			                    	'<iframe width="100%" height="390px" src="https://www.youtube.com/embed/' + video_serial + '?enablejsapi=1" frameborder="0" allowfullscreen></iframe>'
// 			                    	+
// 			                	'</div>';
// 			        if(modalBody.find('.videowrapper')){
// 			        	$('.videowrapper').remove();	
// 			        }
// 			        // if(modalBody.find('p')){
// 			        // 	$('p').remove();	
// 			        // }
// 			        modalBody.append(content);
//         		}
//     		);
// 	        // display modal
// 	        // attribute data set ,so dont need
// 	        // faceVideoModal.modal('show');
// 	});
	
// 	// detect when modal close (hidden)
// 	$('#face_modal').on('hidden.bs.modal', function () {
//   		// do something…
// 		 var faceVideoModal = $('#face_modal');
// 	    modalBody = faceVideoModal.find('.modal-body');

// 	    if(modalBody.find('.videowrapper')){
// 	    	$('.videowrapper > iframe').get(0).contentWindow.postMessage('{"event":"command","func":"' + 'stopVideo' + '","args":""}', '*');  
	    	
// 		}
// 	});

// });

$('#grid').imagesLoaded( function() {
	 // jQuery masonry
	$('#grid').masonry({
		columnWidth: '.grid-sizer',
	  // columnWidth: '.grid-sizer',
	  itemSelector: '.grid-item',
	  percentPosition: true,
	});	
});	

$('#grid-water').imagesLoaded( function() {
	console.log('all images are loaded');
	$('#grid-water').masonry({
		columnWidth: '.grid-sizer-water',
		itemSelector: '.grid-item-water',
		percentPosition: true,
		singleMode:true,
		animate:true
	});


	$('a[id^=face_video_]').click(function(event) {
	    	event.preventDefault();
	        var faceVideoModal = $('#face_modal');
	        modalBody = faceVideoModal.find('.modal-body');

			video_serial =''
	        // Get id 
	        var id = $(this).attr('id').split("face_video_")[1]
	        console.log('face id =' + id)
	        //ajax
	        $.get(
	        	"/fastquestion/video/",
	        	{
	        		face_id:id
	        	},
	        	function(data){
			        // video serial
			        video_serial = data.youtube_serial;
			        console.log(id,video_serial)
			        //name
			        modalTitle = faceVideoModal.find('.modal-title')
			        modalTitle.text(data.title)
			        // load content into modal
			        // ?enablejsapi=1 for enable Js Youtube api ,then can close  or pause
			        content = '<div class="videowrapper">' +
			                    	'<iframe width="100%" height="390px" src="https://www.youtube.com/embed/' + video_serial + '?enablejsapi=1" frameborder="0" allowfullscreen></iframe>'
			                    	+
			                	'</div>';
			        if(modalBody.find('.videowrapper')){
			        	$('.videowrapper').remove();	
			        }
			        // if(modalBody.find('p')){
			        // 	$('p').remove();	
			        // }
			        modalBody.append(content);
        		}
    		);
	        // display modal
	        // attribute data set ,so dont need
	        // faceVideoModal.modal('show');
	});
	
	// detect when modal close (hidden)
	$('#face_modal').on('hidden.bs.modal', function () {
  		// do something…
		 var faceVideoModal = $('#face_modal');
	    modalBody = faceVideoModal.find('.modal-body');

	    if(modalBody.find('.videowrapper')){
	    	$('.videowrapper > iframe').get(0).contentWindow.postMessage('{"event":"command","func":"' + 'stopVideo' + '","args":""}', '*');  
	    	
		}
	});
});

$('#grid-water').infinitescroll({

	nextSelector: '.pagination a.next',
	navSelector: '.pagination',
	itemSelector: '.grid-item-water',
	loading: {
			finishedMsg: 'No more pages to load.'
			}
		},

		// Trigger Masonry as a callback
		function( newElements ) {
			// hide new items while they are loading
			var $newElems = $( newElements ).css({ opacity: 0 });
			// ensure that images load before adding to masonry layout
			$newElems.imagesLoaded(function(){
				// show elems now they're ready
				$newElems.animate({ opacity: 1 });
				$container.masonry( 'appended', $newElems, true );
			});

});


