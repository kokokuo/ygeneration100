
// $(window).load(function () {
// // ====================
// 	 // jQuery masonry
// 	$('#grid').masonry({
// 		columnWidth: '.grid-sizer',
// 		// columnWidth: '.grid-sizer',
// 		itemSelector: '.grid-item',
// 		percentPosition: true,
// 	});	

// 	$('#grid-water').masonry({
// 		columnWidth: '.grid-sizer-water',
// 		itemSelector: '.grid-item-water',
// 		percentPosition: true,
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

(function() {

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


 var ias = $.ias({
	container : '#grid-water',      // 写入容器的元素 pic-flow 外面的div
	item: ".grid-item-water",        // 要加载数据的元素标识 下一页里面提取 
	pagination: '.pagination',    // 分页信息的容器元素标识  即：首页，上一页，下一页，尾页等 
	next: '.next',         // 下一页的元素标识，用来获取下一页的URL元素

	loader: '载入更多...',      // 数据进行提取加载的时候显示 可以自定义图片
	trigger: '查看更多',      // 加载次数完成后 出现的提示    
	history : false,        // 布尔值 在URL ture 会在 URL 补全 #/page/3
	onLoadItems: function(items) {
		console.log('run render');
        var newElems = $(items).show().css({ opacity: 0 });
        newElems.imagesLoaded(function(){
			newElems.animate({ opacity: 1 });
			$('#grid-water').masonry( 'appended', newElems, true );   // 把请求的结果给 masonry 执行瀑布流 
    	});
  	  	return true;
  	}
});
//  $('#grid-water').infinitescroll(
//  	{

// 		// selector for the paged navigation (it will be hidden)
// 		navSelector  : ".pagination",
// 		// selector for the NEXT link (to page 2)
// 		nextSelector : ".pagination a",
// 		// selector for all items you'll retrieve
// 		itemSelector : ".grid-item-water",

// 		// finished message
// 		loading: {
// 			finishedMsg: 'No more pages to load.'
// 		}
// 	},

// 	// Trigger Masonry as a callback
// 	function( newElements ) {
// 		console.log('run render');
// 		// hide new items while they are loading
// 		var $newElems = $( newElements ).css({ opacity: 0 });
// 		// ensure that images load before adding to masonry layout
// 		$newElems.imagesLoaded(function(){
// 			// show elems now they're ready
// 			$newElems.animate({ opacity: 1 });
// 			$('#grid-water').masonry( 'appended', $newElems, true );
// 		});
// 	}
// );

	ias.on('render', function(items) {
		console.log('run render');
		$(items).css({ opacity: 0 });
	});

	ias.on('rendered', function(items) {
		console.log('run rendered');
	 	$('#grid-water').appended(items);
	});

	ias.extension(new IASSpinnerExtension());
	ias.extension(new IASNoneLeftExtension({html: '<div class="ias-noneleft" style="text-align:center"><p><em>You reached the end!</em></p></div>'}));
})();

