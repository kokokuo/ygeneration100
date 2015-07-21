
$(window).load(function () {
// ====================
	 // jQuery masonry
	$('#grid').masonry({
		columnWidth: '.grid-sizer',
	  // columnWidth: '.grid-sizer',
	  itemSelector: '.grid-item',
	  percentPosition: true,
	});	

	$('#grid-water').masonry({
			columnWidth: '.grid-sizer-water',
			itemSelector: '.grid-item-water',
			percentPosition: true,
			singleMode:true,
			animate:true
	});

	// Modal ： Show Face
	// need loaded images then can work
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
			        content = '<div class="videowrapper">' +
			                    	'<iframe width="100%" height="390px" src="https://www.youtube.com/embed/' + video_serial + '" frameborder="0" allowfullscreen></iframe>'
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
	
});

$(document).ready(function(){

});



