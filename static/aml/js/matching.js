window.onload = function(){
	 
};

function init_matching( arm_user_code_number ) {

	var arrMatchingColors;  // 매칭 선 채우기 색 목록
	var map_crawling_data_data = new Map(); //Crawling DATA Input Datas Map
	var map_customer_data_data = new Map(); //Customer DATA Input Datas Map
	var crawling_data_card_images_content;	//Crawling DATA 카드 이미지
	var customer_data_card_images_content;	//Customer DATA 카드 이미지

	if( arm_user_code_number.indexOf('2') > -1 ) {
		arrMatchingColors =['green','green','green','green','green','green','green','green'];
		map_crawling_data_data.set('name', 'Mark');
		map_crawling_data_data.set('age', '29');
		map_crawling_data_data.set('gender', 'MAN');
		map_crawling_data_data.set('mobile', '76-24-842');
		map_crawling_data_data.set('city', 'Los Angeles');
		map_crawling_data_data.set('email', 'Mark_love7@gmail.com');
		map_crawling_data_data.set('job', 'Programmer');

		map_customer_data_data.set('name', 'Mark');
		map_customer_data_data.set('age', '29');
		map_customer_data_data.set('gender', 'MAN');
		map_customer_data_data.set('mobile', '76-24-842');
		map_customer_data_data.set('city', 'Los Angeles');
		map_customer_data_data.set('email', 'Mark_love7@gmail.com');
		map_customer_data_data.set('job', 'Programmer');
		crawling_data_card_images_content = 
		'	<div class="cardImg"> ' +
		'		<div class="card" style="background-repeat : no-repeat; background-position : center;	background-image : url(img/card/citi.png);"></div> ' +
		'	</div> ' +
		'	<div class="cardImg"> ' +
		'		<div class="card" style="background-repeat : no-repeat; background-position : center;	background-image : url(img/card/chase.png);"></div> ' +
		'	</div> ' +
		'	<div class="cardImg">    ' +		
		'	</div>';
		customer_data_card_images_content = 
		'	<div class="cardImg"> ' +
		'		<div class="card" style="background-repeat : no-repeat; background-position : center;	background-image : url(img/card/citi.png);"></div> ' +
		'	</div> ' +
		'	<div class="cardImg"> ' +
		'		<div class="card" style="background-repeat : no-repeat; background-position : center;	background-image : url(img/card/chase.png);"></div> ' +
		'	</div> ' +
		'	<div class="cardImg">    ' +		
		'	</div>';
	} else if( arm_user_code_number.indexOf('3') > -1 ) {
		arrMatchingColors = ['green','red','green','red','red','red','green','red'];
		map_crawling_data_data.set('name', 'Noah');
		map_crawling_data_data.set('age', '31');
		map_crawling_data_data.set('gender', 'MAN');
		map_crawling_data_data.set('mobile', '76-33-357');
		map_crawling_data_data.set('city', 'Seattle');
		map_crawling_data_data.set('email', 'nnoo77@gmail.com');
		map_crawling_data_data.set('job', 'Civil Engineering');

		map_customer_data_data.set('name', 'Noah');
		map_customer_data_data.set('age', '33');
		map_customer_data_data.set('gender', 'MAN');
		map_customer_data_data.set('mobile', '76-82-387');
		map_customer_data_data.set('city', 'Atlanta');
		map_customer_data_data.set('email', 'kifjds@gmail.com');
		map_customer_data_data.set('job', 'Civil Engineering');
		crawling_data_card_images_content =
		'	<div class="cardImg"> ' +
		'		<div class="card" style="background-repeat : no-repeat; background-position : center;	background-image : url(img/card/citi.png);"></div> ' +
		'	</div> ' +
		'	<div class="cardImg"> ' +
		'		<div class="card" style="background-repeat : no-repeat; background-position : center;	background-image : url(img/card/chase.png);"></div> ' +
		'	</div> ' +
		'	<div class="cardImg">    ' +
		'		<div class="card" style="background-repeat : no-repeat; background-position : center;	background-image : url(img/card/american_express_logo_wordmark_detail.png);"></div> ' +
		'	</div>';
		customer_data_card_images_content = 
		'	<div class="cardImg"> ' +
		'		<div class="card" style="background-repeat : no-repeat; background-position : center;	background-image : url(img/card/citi.png);"></div> ' +
		'	</div> ' +
		'	<div class="cardImg"> ' +
		'		<div class="card" style="background-repeat : no-repeat; background-position : center;	background-image : url(img/card/chase.png);"></div> ' +
		'	</div> ' +
		'	<div class="cardImg">    ' +		
		'	</div>';
	} else {
		arrMatchingColors = ['green','green','green','red','green','green','red','green'];
		map_crawling_data_data.set('name', 'James');
		map_crawling_data_data.set('age', '35');
		map_crawling_data_data.set('gender', 'MAN');
		map_crawling_data_data.set('mobile', '75-84-287');
		map_crawling_data_data.set('city', 'Chicago');
		map_crawling_data_data.set('email', 'hypo@gmail.com');
		map_crawling_data_data.set('job', 'developer');

		map_customer_data_data.set('name', 'James');
		map_customer_data_data.set('age', '35');
		map_customer_data_data.set('gender', 'MAN');
		map_customer_data_data.set('mobile', '75-84-286');
		map_customer_data_data.set('city', 'Chicago');
		map_customer_data_data.set('email', 'hypo@gmail.com');
		map_customer_data_data.set('job', 'soccer');
		crawling_data_card_images_content =
		'	<div class="cardImg"> ' +
		'		<div class="card" style="background-repeat : no-repeat; background-position : center;	background-image : url(img/card/citi.png);"></div> ' +
		'	</div> ' +
		'	<div class="cardImg"> ' +
		'		<div class="card" style="background-repeat : no-repeat; background-position : center;	background-image : url(img/card/chase.png);"></div> ' +
		'	</div> ' +
		'	<div class="cardImg">    ' +
		'		<div class="card" style="background-repeat : no-repeat; background-position : center;	background-image : url(img/card/american_express_logo_wordmark_detail.png);"></div> ' +
		'	</div>';
		customer_data_card_images_content = 
		'	<div class="cardImg"> ' +
		'		<div class="card" style="background-repeat : no-repeat; background-position : center;	background-image : url(img/card/citi.png);"></div> ' +
		'	</div> ' +
		'	<div class="cardImg"> ' +
		'		<div class="card" style="background-repeat : no-repeat; background-position : center;	background-image : url(img/card/chase.png);"></div> ' +
		'	</div> ' +
		'	<div class="cardImg">    ' +
		'		<div class="card" style="background-repeat : no-repeat; background-position : center;	background-image : url(img/card/american_express_logo_wordmark_detail.png);"></div> ' +
		'	</div>';
	}

	for (var idx of map_crawling_data_data.keys()) {
		$('#crawling_data #' +idx ).val( map_crawling_data_data.get(idx) );
	}

	for (var idx of map_customer_data_data.keys()) {
		$('#customer_data #' +idx ).val( map_customer_data_data.get(idx) );
	}

	$('#crawling_data #card_images').html(crawling_data_card_images_content);
	$('#customer_data #card_images').html(customer_data_card_images_content);

	setTimeout(function(){
		document.querySelector('.compareDiv:first-child').style.display = 'none';
		document.querySelector('.compareDiv:first-child').style.visibility = 'visible';
		$('.compareDiv:first-child').fadeIn();
	}, 1000);
	
	setTimeout(function(){
		$('.compareDiv:last-child').fadeIn();
	}, 500);
	
	setTimeout(function(){
		
		drawLine( arrMatchingColors );
	}, 1500);
}


function drawLine( arrMatchingColors ){
	var width_percentage = 0;
	var line_index = 0;
	
	var draw_interval = setInterval(function(){
		var setWidth = width_percentage++;
		
		var left_line = document.querySelector('.actionEle:nth-child('+(line_index + 1)+') > div:first-child > div');
		var right_line = document.querySelector('.actionEle:nth-child('+(line_index + 1)+') > div:last-child > div');
		var light_box = document.querySelector('.actionEle:nth-child('+(line_index + 1)+') > div:nth-child(2) > div');
		
		left_line.style.width = setWidth + "%";
		right_line.style.width = setWidth + "%";

		light_box.style.backgroundColor = arrMatchingColors[line_index];
		/*
		if((line_index + 1) == num1) light_box.style.backgroundColor = 'red';
		else if((line_index + 1) == num2) light_box.style.backgroundColor = 'red';
		else light_box.style.backgroundColor = 'green';
		*/
		if(line_index == 7) {
			if(setWidth == 100) {
				$('.actionEle:nth-child('+(line_index + 1)+') > div:nth-child(2) > div').fadeIn();
				
				setTimeout(function(){
					$('.explainDiv').fadeIn();
				}, 500);
				
				clearInterval(draw_interval);
			}
		}else{
			if(setWidth == 100) {     
				$('.actionEle:nth-child('+(line_index + 1)+') > div:nth-child(2) > div').fadeIn();
				line_index = line_index + 1; 
				width_percentage = 0;
			}
		}
	}, 1);
};           