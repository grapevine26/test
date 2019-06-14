window.onload = function(){
	showCheck();  
};
 
function showCheck(){
	var show_index = 0;
	var listOne_index = 0;
	
	var show_intervar = setInterval(function(){
		//세로로 체크표시 하기
		/*show_index = show_index + 1;
		if(listOne_index == 5) clearInterval(show_intervar);
		else{
			if(show_index > 1 && show_index < 6) $('.listDiv > .listOne:nth-child('+(listOne_index + 2)+') > .listColumn:nth-child('+show_index+') > .listRow > .listCheck > .checkImg').fadeIn();
			else if(show_index == 8){
				$('.listDiv > .listOne:nth-child('+(listOne_index + 2)+') > .listColumn:nth-child('+show_index+') > .listRow > .listCheck > .checkImg').fadeIn();
				listOne_index = listOne_index + 1;
				show_index = 0;
			}
		}*/
		
		//가로로 체크표시 하기
		listOne_index = listOne_index + 1;
		
		if(show_index == 6) {
			$('.listDiv > .listOne:nth-child('+(listOne_index + 1)+') > .listColumn:nth-child(8) > .listRow > .listCheck > .checkImg').fadeIn();
			if(listOne_index == 5) clearInterval(show_intervar);
		}else{
			if(listOne_index == 5){
				$('.listDiv > .listOne:nth-child('+(listOne_index + 1)+') > .listColumn:nth-child('+(show_index + 1)+') > .listRow > .listCheck > .checkImg').fadeIn();
				show_index = show_index + 1;
				listOne_index = 0;
			}else $('.listDiv > .listOne:nth-child('+(listOne_index + 1)+') > .listColumn:nth-child('+(show_index + 1)+') > .listRow > .listCheck > .checkImg').fadeIn();
		}
	}, 50);
}; 