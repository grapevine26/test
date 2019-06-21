var sns_list = ['fb_h2', 'ig_h2', 'gg_h2', 'li_h2', 'tt_h2'];

create_terminal_line('facebook', 'collect', 'user_facebook_information');
create_terminal_line('instagram', 'collect', 'user_instagram_information');
create_terminal_line('google', 'collect', 'user_google_information');
create_terminal_line('linkedin', 'collect', 'user_linkedin_information');
create_terminal_line('twitter', 'collect', 'user_twitter_information');


setTimeout(function(){
    create_terminal_line('etc', 'collect', 'collecting', 0);
    twinkle_process(75);

    setTimeout(function(){
        create_terminal_line('etc', '', '', 10);
        twinkle_word_change('Collecting');

        setTimeout(function(){
            create_terminal_line('etc', '', '', 0);
            create_terminal_line('etc', '', '', 0);

            setTimeout(function(){
                create_terminal_line('etc', '', 'sorting', 0);

                setTimeout(function(){
                    create_terminal_line('etc', '', '', 10);
                    twinkle_word_change('Sorting');

                    setTimeout(function(){
                        create_terminal_line('etc', '', '', 0);
                        create_terminal_line('etc', '', '', 0);

                        setTimeout(function(){
                            create_terminal_line('etc', '', 'complete!', 0); //완료시점


                            for(var i = 0; i < document.getElementsByClassName('plat_info').length; i++){
                               document.getElementsByClassName('plat_info')[i].style.padding = '15px 10px';
                            }
                            $('.plat_con > .plat_info > div').fadeIn();
                        }, 1000);
                    }, 1900);
                }, 1000);
            }, 1000);
        }, 1900);
    }, 1000);
}, 500);


function twinkle_words(id, times, speed){ // id, 횟수, 속도
    var count = 0;
    var start_twinkle = setInterval(function(){
        count++;
        var inf = $('#'+id).fadeIn();
        var outf = $('#'+id).fadeOut();

        if(count % 2 == 0) outf;
        else  inf;

        if(count == times) clearInterval(start_twinkle);
    }, speed)
};

function twinkle_process(speed){ // 반짝임 프로세스
    for(var i = 0; i < sns_list.length; i++){
        twinkle_words(sns_list[i], 10, speed);
    }
}

function twinkle_word_change(word){ // 단어 한번에 바꾸기
    for(var i = 0; i < sns_list.length; i++){
        document.getElementById(sns_list[i]).innerHTML = word;
    }
}
