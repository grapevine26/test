var activeIndex = -1;
$(document).ready( function() {
	
    $('.ai_virtual_product_item_summary').on('click', function() {
        
        var youtube_url_array = new Array();
        youtube_url_array.push('RtfD-3yT2CY');
        youtube_url_array.push('uCjyWClJ8LY');
        youtube_url_array.push('KODQ71WAcAU');
        youtube_url_array.push('4Ux54dE_t4Y');
        youtube_url_array.push('BStlpqxIJ54');

        var click_index = $( this ).index('.ai_virtual_product_item_summary');
        activeIndex = click_index;
    		
        allpauseYoutubeVideo();
        
        $('.ai_virtual_product_item_detail > td > div ').each( function(index) {
           $(this).css( {
               'display':'none',
               'width':'100%'
           });
        });
        

       $('.ai_virtual_product_item_detail > td > div .youtube_wrapper').each( function(index) {
        });        
        
        //////////////////////$('.ai_virtual_product_item_detail').eq( click_index ).children('td').children('div').children('.youtube_wrapper').html('<iframe width="690" height="400" src="https://www.youtube.com/embed/'+youtube_url_array[click_index]+'?rel=0&amp;autoplay=1&amp;mute=0" frameborder="0" allowfullscreen="">동영상을 불러오고 있습니다.</iframe>');
        //if( typeof player[click_index].getPlayerState == 'undefined' ) {
				onYouTubeIframeAPIReady( click_index, 'youtube_player_' + Number(click_index), youtube_url_array[click_index] );
				/*
			} else {
				//playYoutubeVideo(click_index);
			}
			*/
        
        
        $('.ai_virtual_product_item_detail').eq( click_index ).children('td').children('div').css( {
            'display':'inline-block'
        });
    });

    
    
    $('.view_result_button').on('click', function() {        
        $('.product_review').css('display', 'none');
        $('.product_score').css('display', 'inline-block');
    });

    $('.popup_close_button').on('click', function() {
    	
    		playYoutubeVideo( activeIndex );
    		
    		
        $('#my_popup').css('display', 'none');
        $('*').css({
            'opacity': '1',
            'filter': 'alpha(opacity=100)'
        });
    });

    $('.ai_virtual_product_detail_feed_button').on('click', function() {
        

        
        
        /*
        var wantHeight =  $(window).height();
        console.log('1: ' + wantHeight );
      */  
        	//if( )
        
        
        var index = $( this ).index( '.ai_virtual_product_detail_feed_button' );
        
			pauseYoutubeVideo(index);
			
        /* 제품 이미지를 설정한다. */
        $('.product_review_image').css('background-image', "url('" + $('.ai_virtual_product_item_summary').eq(index).find('.virtual_product').attr('src') + "')");
        $('.product_score_image').css('background-image', "url('" + $('.ai_virtual_product_item_summary').eq(index).find('.virtual_product').attr('src') + "')");

        /* 제품 명(한국어)을 설정한다. */
        $('.product_review_title').html( $('.ai_virtual_product_item_summary').eq(index).find('.virtual_product_name').html() );
        $('.product_score_title').html( $('.ai_virtual_product_item_summary').eq(index).find('.virtual_product_name').html() );

        /* 제품 명(영어)을 설정한다. */
        var product_name_english_array = new Array(5);
        product_name_english_array[0] = 'PERFECT LIPS Lip Cashmere';
        product_name_english_array[1] = '2X FIRST ESSENCE';
        product_name_english_array[2] = 'LUMINOUS GLOW CUSHION';
        product_name_english_array[3] = 'Backgel Eye liner long brush';
        product_name_english_array[4] = 'UNI DE HOMME Dynamic BB Cream';

        $('.product_review_title_sub').html( '(' + product_name_english_array[index] + ')' );
        $('.product_score_title_sub').html( '(' + product_name_english_array[index] + ')' );

        /* 제품 속성을 설정한다. */
        var product_attribute_item_array = new Array(5);
        var array_x = 0;
        product_attribute_item_array[array_x] = new Array(7);
        product_attribute_item_array[array_x][0] = '보습';
        product_attribute_item_array[array_x][1] = '스틱타입';
        product_attribute_item_array[array_x][2] = '영양공급';
        product_attribute_item_array[array_x][3] = '입술윤기';
        product_attribute_item_array[array_x][4] = '자외선차단';
        product_attribute_item_array[array_x][5] = '볼륨감';
        product_attribute_item_array[array_x][6] = '글로시';

        array_x = 1;
        product_attribute_item_array[array_x] = new Array(7);
        product_attribute_item_array[array_x][0] = '고보습';
        product_attribute_item_array[array_x][1] = '수분공급';
        product_attribute_item_array[array_x][2] = '영양공급';
        product_attribute_item_array[array_x][3] = '피부유연';
        product_attribute_item_array[array_x][4] = '유수분조절';
        product_attribute_item_array[array_x][5] = '보습';
        product_attribute_item_array[array_x][6] = '피부진정';

        array_x = 2;
        product_attribute_item_array[array_x] = new Array(7);
        product_attribute_item_array[array_x][0] = '결보정';
        product_attribute_item_array[array_x][1] = '보습';
        product_attribute_item_array[array_x][2] = '수분공급';
        product_attribute_item_array[array_x][3] = '윤기부여';
        product_attribute_item_array[array_x][4] = '자외선차단';
        product_attribute_item_array[array_x][5] = '쿠션타입';
        product_attribute_item_array[array_x][6] = '피부톤보정';

        array_x = 3;
        product_attribute_item_array[array_x] = new Array(7);
        product_attribute_item_array[array_x][0] = '고정력';
        product_attribute_item_array[array_x][1] = '워터프루프';
        product_attribute_item_array[array_x][2] = '젤타입';
        product_attribute_item_array[array_x][3] = '펄함유';
        product_attribute_item_array[array_x][4] = '펜슬타입';
        product_attribute_item_array[array_x][5] = '섀도우겸용';
        product_attribute_item_array[array_x][6] = '스머지팁내장';

        array_x = 4;
        product_attribute_item_array[array_x] = new Array(7);
        product_attribute_item_array[array_x][0] = '수분공급';
        product_attribute_item_array[array_x][1] = '유수분조절';
        product_attribute_item_array[array_x][2] = '피부결정톤';
        product_attribute_item_array[array_x][3] = '피부유연';
        product_attribute_item_array[array_x][4] = '피부진정';
        product_attribute_item_array[array_x][5] = '피지조절';
        product_attribute_item_array[array_x][6] = '모공관리';


        for( item in product_attribute_item_array[index] ) {
            $('.product_attribute_item_wrapper .product_attribute_item').eq(item).html( product_attribute_item_array[index][item] );
        }

        $('#my_popup').css('display', 'inline-block');
        $('.product_review').css('display', 'inline-block');
        $('.product_score').css('display', 'none');
        
        $('*').css({
            'opacity': '0.860529',
            'filter': 'alpha(opacity=86)'
        });

        $('#my_popup, #my_popup * ').css({
            'opacity': '1',
            'filter': 'alpha(opacity=100)'
        });
    });


    var isDragging = false;
    var isMouseDown = false;
    $(".product_review_title_wrapper .star-score")
    .mousedown(function() {
        isDragging = false;
        isMouseDown = true;
        console.log('mousedown');
    })
    .mousemove(function(event) {
        isDragging = true;
        if( isMouseDown ) {
            console.log('%o', event);
            console.log( 'width:' + $( this ).width() +'  :' + event.offsetX/$( this ).width() * 100 );
            console.log('mousemove:' + 'X=' + event.offsetX + ' y='+ event.offsetY);
            $( this ).children('.ico-sprite').css('width',  + String( event.offsetX/$( this ).width() * 100 ) + '%');
            event.offsetX/$( this ).width() * 100
        }
        
    })
    .mouseup(function(event) {
        isMouseDown = false;
        console.log('mouseup');
        $( this ).children('.ico-sprite').css('width',  + String( event.offsetX/$( this ).width() * 100 ) + '%');
        var wasDragging = isDragging;
        isDragging = false;
        if (!wasDragging) {
            console.log('wasDragging');
           // $("#throbble").toggle();
        }
    });

    /*
    					<div class="star_score_wrapper">
						<span class="ico-sprite star-score">
							<span class="ico-sprite" style="width: 90%;"></span>
						</span>
    */


       $(window).scroll(function(event){
       	
       	

/*
            var p = $( "#tonymoly_middle_banner" );
            var offset = p.offset();


            console.log( $(window).scrollTop() );

            if( $(window).scrollTop() + $(window).height() > offset.top ) {
				console.log('야호!');
            }			



            p = $( "#introduce_new_friends" );

            offset = p.offset();


            if( $(window).scrollTop() + $(window).height() > offset.top ) {



				if( didPlayed_zbot6 == false ) {

					if ($('#audio_zbot7')[0].paused == false) {

						$('#audio_zbot7')[0].pause();

					}

					if ($('#audio_zbot6')[0].paused == true) {

						$('#audio_zbot6')[0].play();

						didPlayed_zbot6 = true;

					}

				}

            }			



            p = $( "#propose_to_your_life_style" );



            offset = p.offset();



            if( $(window).scrollTop() + $(window).height() > offset.top ) {



				if( didPlayed_zbot7 == false ) {

					if ($('#audio_zbot6')[0].paused == false) {

						$('#audio_zbot6')[0].pause();

					}

					if ($('#audio_zbot7')[0].paused == true) {

						$('#audio_zbot7')[0].play();

						didPlayed_zbot7 = true;

					}

				}

            }			*/

        });
        
        
            var timerId = setInterval( function(){
            	auto_height_my_popup_contents();
            	//clearInterval(timerId); 
              }, 1000);

});


function auto_height_my_popup_contents() {
	/* 제품 평가 팝업의 높이를 동적으로 맞춰 준다. */
	var target = $('.my_popup_contents');
	var margin_top_my_popup_contents = target.offset().top - $(window).scrollTop();
	var padding_top_my_popup_contents = Number( String(target.css('padding-top')).replace(/px/gi, "") );
	var padding_bottom_my_popup_contents = Number( String( target.css('padding-bottom')).replace(/px/gi, "") );        
	var real_height_my_popup_contents = Number( target.height() + padding_top_my_popup_contents + padding_bottom_my_popup_contents  );
	 	
	if( margin_top_my_popup_contents + real_height_my_popup_contents > $(window).height() ) {       		
		var over_height_my_popup_contents = $(window).height() - margin_top_my_popup_contents * 2;
	 	target.css('height', over_height_my_popup_contents + 'px');	 	
	 	$('.my_popup_contents_title_sub').css('display', 'none');
	 	$('.product_attribute_item_wrapper').css('display','none');
	} else {
		//target.css('height', 'auto');
	 	//$('.my_popup_contents_title_sub').css('display', 'block');
	}
	
	/*
var margin_top_my_popup_contents = $('.my_popup_contents').eq(0).offset().top - $(window).scrollTop();
	var padding_top_my_popup_contents = Number( String($('.my_popup_contents').eq(0).css('padding-top')).replace(/px/gi, "") );
	var padding_bottom_my_popup_contents = Number( String($('.my_popup_contents').eq(0).css('padding-bottom')).replace(/px/gi, "") );        
	var real_height_my_popup_contents = Number( $('.my_popup_contents').eq(0).height() + padding_top_my_popup_contents + padding_bottom_my_popup_contents  );
	 	
	if( margin_top_my_popup_contents + real_height_my_popup_contents > $(window).height() ) {       		
		var over_height_my_popup_contents = $(window).height() - margin_top_my_popup_contents * 2;
	 	$('.my_popup_contents').css('height', over_height_my_popup_contents + 'px');
	}	
	*/
}


	//https://developers.google.com/youtube/iframe_api_reference?hl=ko#Playback_controls

      // 2. This code loads the IFrame Player API code asynchronously.
      var tag = document.createElement('script');

      tag.src = "https://www.youtube.com/iframe_api";
      var firstScriptTag = document.getElementsByTagName('script')[0];
      firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

      // 3. This function creates an <iframe> (and YouTube player)
      //    after the API code downloads.
      var player = new Array(5);
      function onYouTubeIframeAPIReady(array_index, youtube_player_id, youtube_vedeo_id ) {      	
      	done = false;
        player[array_index] = new YT.Player( youtube_player_id, {
          height: '400',
          width: '690',
          videoId: youtube_vedeo_id,
          events: {
            'onReady': onPlayerReady,
            'onStateChange': onPlayerStateChange
          }
        });
      }

      // 4. The API will call this function when the video player is ready.
      function onPlayerReady(event) {
        event.target.playVideo();
      }

      // 5. The API calls this function when the player's state changes.
      //    The function indicates that when playing a video (state=1),
      //    the player should play for six seconds and then stop.
      var done = false;
      function onPlayerStateChange(event) {
        if (event.data == YT.PlayerState.PLAYING && !done) {
          //setTimeout(stopVideo, 6000);
          console.log('재생 시작');
          done = true;
        }
      }
      
      function stopYoutubeVideo( array_index ) {
        player[array_index].stopVideo();
      }
      
      function pauseYoutubeVideo( array_index ) {
      	if( typeof player[array_index].getPlayerState != 'undefined' ) {        	
        	player[array_index].pauseVideo();
        }
      }      
      
     function playYoutubeVideo( array_index ) {
     	
        if( typeof player[array_index].getPlayerState != 'undefined' ) {        	
	        switch( player[array_index].getPlayerState() ) {
	  				case 2:
  						player[array_index].playVideo();
  					break;
  				}
        }
  			
      }
      
      
     function allpauseYoutubeVideo( ) {
     	
     		for( index in player ) {     			     			
     			if( typeof player[index] != 'undefined' && typeof player[index].getPlayerState != 'undefined' ) {
     				
     				switch( player[index].getPlayerState() ) {
     					case -1:
     						console.log('시작되지 않음');
     					break;
     					case 0:
     						console.log('종료');
     					break;
     					case 1:
     						console.log('재생 중');
     						player[index].pauseVideo();
     					break;
     					case 2:
     						console.log('일시중지');
     					break;
     					case 3:
     						console.log('버퍼링');
     					break;
     					case 5: //4번이 원래 없음
     						console.log('동영상 신호');
     					break;
     				}
     			}

     		}
     		
      }
      