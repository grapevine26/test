function activeTab(tabIdx){
	$('.tabDiv > .tabOne > .tabImg').removeClass('activeTab');
	$('.tabContentsDiv').css('display', 'none');
	 
	var thisTab = document.querySelector('.tabDiv > .tabOne:nth-child('+tabIdx+') > .tabImg');
	thisTab.classList.add('activeTab');    
	
	if(tabIdx == 1) document.getElementById('firstTab').style.display = 'block';
	else if(tabIdx == 2) document.getElementById('secondTab').style.display = 'block';
	else if(tabIdx == 3) document.getElementById('thirdTab').style.display = 'block';
	else if(tabIdx == 4) document.getElementById('fourthTab').style.display = 'block';
	else  document.getElementById('fifthTab').style.display = 'block';
};     