function create_terminal_line(platform_name, fn, fv, dot_max_count){
    // 터미널 형식 디스플레이 만들기  @@platform_name : 'facebook', 'google', 'linkedin', 'instagram', 'twitter', 'etc' .. 중 택 1, 필드명, 필드값
    // platform_name이 etc 이면 플랫폼 외의 다른 문구 추가 액션, dot_max_count가 0보다 크면 ...을 추가함
    var union_result_line = document.createElement('div');
    union_result_line.className = 'union_result_line';

    var p = document.createElement('p');

    var union_path = document.createElement('span');
    union_path.className = 'union_path';
    union_path.innerHTML = 'dev_com:result_folder ';

    var dev_team = document.createElement('span');
    dev_team.className = 'dev_team';
    dev_team.innerHTML = 'dev_team$ ';

    var plat_n = document.createElement('span');
    if(platform_name == 'facebook') plat_n.className = 'plat_n_fb';
    else if(platform_name == 'google') plat_n.className = 'plat_n_go';
    else if(platform_name == 'linkedin') plat_n.className = 'plat_n_li';
    else if(platform_name == 'instagram') plat_n.className = 'plat_n_is';
    else plat_n.className = 'plat_n_tw';
    if(platform_name != 'etc') plat_n.innerHTML = platform_name + ' ';

    var field_name = document.createElement('span');
    field_name.className = 'field_name';
    if(platform_name != 'etc') field_name.innerHTML = fn + '=';

    var field_value = document.createElement('span');
    field_value.className = 'field_value';
    //field_value.innerHTML = fv;

    p.appendChild(union_path);
    p.appendChild(dev_team);
    p.appendChild(plat_n);
    p.appendChild(field_name);
    p.appendChild(field_value);

    union_result_line.appendChild(p);

    document.getElementById('union_result_div').appendChild(union_result_line);

    if(platform_name != 'etc'){
        //field_value 한글자씩 추가 액션
        var fv_timer = 0;

        //글자수별 속도조절
        if(fv.length < 25) fv_timer = 30;
        else if(fv.length < 50) fv_timer = 20;
        else if(fv.length < 100) fv_timer = 15;
        else if(fv.length < 150) fv_timer = 10;
        else fv_timer = 5;

        add_word(field_value, fv, fv.length, fv_timer)
    }else{ // terminal line 에 다른 문구를 추가
        if(dot_max_count > 0){
            var dot_count = 0;
            var create_dot = setInterval(function(){
                dot_count++;

                if(dot_count == dot_max_count) {
                    dot_count = 0;
                    clearInterval(create_dot);
                }else field_name.innerHTML = field_name.innerHTML + '.';
            }, 150);
        }else add_word(field_value, fv, fv.length, 50); //...추가가 아니면 fv 의 값으로 문구를 추가
    }
};

function add_word(ele, word, max_length, timer){ // 한글자씩 추가하는 함수 [적용할 엘리머튼, 적용할 단어, 단어의 길이, 추가되는 속도]
    var length_count = 0;
    var add_word = setInterval(function(){
        ele.innerHTML = ele.innerHTML + word.charAt(length_count);
        length_count++;

        if(length_count == max_length) clearInterval(add_word);
    }, timer);
};