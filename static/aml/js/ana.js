var ana_count = 0;
var ana_display = setInterval(function () {
    if (ana_count < 4) {
        document.getElementById('main_title').innerHTML = document.getElementById('main_title').innerHTML + '.';
        ana_count++;
    } else {
        document.getElementById('main_title').innerHTML = 'Analyzing';
        ana_count = 0;
    }
}, 500);

display_org_name(0); // 카드형식 분석 애니메이션 실행 + SNS 분석 실행


function display_org_name(index) {
    var search_list = [ // 기관명 리스트
        'United Nations Named Terrorists', 'European Union Designated Terrorist Groups & Individuals', 'World Bank Ineligible Firms', 'Interpol Most Wanted', 'Financial Crimes Enforcement Network Special Alert List',
        'FBI Top Ten Most Wanted', 'FBI wanted', 'State Department Foreign Terrorist Organizations & State Department Terrorist Exclusions', 'OFAC Specially Designated Nationals List', 'OFAC Foreign Sanctions Evaders List',
        'OFAC Sectoral Sanctions Identifications List', 'OFAC Palestine Legislative Council List', 'OFAC Sanctioned Countries List', 'Office if the Comptroller of the Currency Alert', 'Offshore Financial Centers',
        'Canada Entities & OSFI Canada Individuals', 'Her Majesty Treasury Consolidated List', 'US Bureau of Industry and Security - Denied Entity List & Denied Person List & Unverified Entity List', 'Defense Trade Controls Debarred Parties', 'Chiefs of State and Foreign Cabinet Members',
        'FATF Financial Action Task Force, Deficient Jurisdictions - Countries', 'Australia Department Of Foreign Affairs and Trade', 'Hong Kong Monetary Authority', 'Monetary Authority of Singapore', 'Primary Money Laundering Concern',
        'Commodity Futures Trading Commission, Regulatory and Self-Regulatory Authorities', 'Foreign Agents Registration Act'
    ]
    var info = document.getElementById('info');

    var org_name_span = info.querySelectorAll('p > .organization_name'); // info > p > span 기관명 출력
    for (var i = 0; i < org_name_span.length; i++) {
        org_name_span[i].innerHTML = '';
        org_name_span[i].innerHTML = search_list[index];
    }

    var org_name_p = info.querySelectorAll('p');
    for (var i = 0; i < org_name_p.length; i++) {
        info_p_setTimeout(i, index);
    }
    ;
};

function add_dot(index, time) { // info 속 p 태그 ... 액션주기
    var org_name_p = info.querySelectorAll('p');
    var connect_count = 0;
    var connect_display = setInterval(function () {
        connect_count++;
        org_name_p[index].innerHTML = org_name_p[index].innerHTML + '.';
        if (connect_count == 4) { // ... 액션 멈추기
            clearInterval(connect_display);
            org_name_p[index].innerHTML = org_name_p[index].innerHTML.split('.')[0];
        }
    }, time);
};

function info_p_setTimeout(i, index) { // info 속 p 태그 fade in out 함수
    var real_index = i + 1;
    var time; // info 속 p 태그가 나타나는 속도.

    if (i == 0) time = 100;
    else if (i == 1) time = 250;
    else if (i == 2) time = 1000;
    else if (i == 3) time = 1400;
    else time = 1800;

    var action_timeout = setTimeout(function () {
        if (i == 4) {
            $('#info > p').fadeOut();
            var action_timeout_2 = setTimeout(function () { // Done 출력
                $('#info > p:nth-child(' + real_index + ')').fadeIn();
                $('#info > p:nth-child(' + real_index + ')').fadeOut();
                var action_timeout_3 = setTimeout(function () { // 다음으로 넘기기
                    if (index < 26) {
                        index++;
                        display_org_name(index); // 다시 반복
                        $('#coverflow').coverflow('next'); // 다음 기관으로 이동
                    } else { // 모든 기관이 끝났을 때 SNS 분석 시작
                        $('#coverflow_stop_btn_div').fadeOut();
                        $('.ui-coverflow-wrapper').fadeOut();
                        setTimeout(function () { // 끝나는 지점
                            $('#circle_div').fadeIn();
                            circle_action(0); //  SNS 분석 실행
                        }, 2000);
                    }
                }, 1000);
                document.getElementById('coverflow_stop_btn').setAttribute('onclick', 'stop(' + index + ', ' + action_timeout_3 + ');');
                document.getElementById('coverflow_skip_btn').setAttribute('onclick', 'skip(' + action_timeout_3 + ');');
            }, 500);
            document.getElementById('coverflow_stop_btn').setAttribute('onclick', 'stop(' + index + ', ' + action_timeout_2 + ');');
            document.getElementById('coverflow_skip_btn').setAttribute('onclick', 'skip(' + action_timeout_2 + ');');

        } else {
            $('#info > p:nth-child(' + real_index + ')').fadeIn();
            add_dot(i, time / 10);
        }
    }, time);
    document.getElementById('coverflow_stop_btn').setAttribute('onclick', 'stop(' + index + ', ' + action_timeout + ');');
    document.getElementById('coverflow_skip_btn').setAttribute('onclick', 'skip(' + action_timeout + ');');
};

function skip(timeout) { // SKIP 버튼 클릭 이벤트
    $('#coverflow_stop_btn_div').fadeOut();
    $('.ui-coverflow-wrapper').fadeOut();
    $('#info').fadeOut();
    stop(0, timeout);

    setTimeout(function () {
        $('#circle_div').fadeIn();
        circle_action(0); //  SNS 분석 실행
    }, 1000);
};

function stop(index, timeout) { // STOP 버튼 클릭 이벤트
    clearTimeout(timeout);
    document.getElementById('coverflow_stop_btn').setAttribute('onclick', 'play(' + index + ');');
    document.getElementById('coverflow_stop_btn').innerHTML = 'PLAY';
};

function play(index) { // PLAY 버튼 클릭 이벤트
    $('#info > p').fadeOut();
    document.getElementById('coverflow_stop_btn').innerHTML = 'STOP';
    display_org_name(index);
};

function circle_action(index) { //  SNS 분석 실행 함수 (퍼센트 + 문구)
    var this_c_ele = document.getElementsByClassName('circle_contents')[index];
    var this_c_ele_h1 = this_c_ele.querySelector('.circle_percentage > h1');
    //var this_c_ele_info_cr_js = this_c_ele.querySelector('.circle_contents_info > h2:first-child');

    var ele_index = index + 1;
    var this_c_ele_info_p = $('.circle_contents:nth-child(' + ele_index + ') > .circle_contents_info > p');
    var this_c_ele_info_cr = $('.circle_contents:nth-child(' + ele_index + ') > .circle_contents_info > h2:first-child');
    var this_c_ele_info_co = $('.circle_contents:nth-child(' + ele_index + ') > .circle_contents_info > h2:last-child');

    var c_per = 0;
    var c_per_action = setInterval(function () {
        c_per++;

        if (c_per < 100) { // 100%  미만일 때
            /*// Crawling 깜박임 이벤트
            if(c_per < 10)  this_c_ele_info_cr.fadeIn(); // 10 이하 일 때
            else if(c_per % 20 < 10){ // 짝수번대의 10의 자리 수 ex) 20, 40, 60, 80 ...
                this_c_ele_info_cr.fadeOut();
            }else this_c_ele_info_cr.fadeIn(); // 홀수번대의 10의 자리 수 ex) 10, 30, 50, 70, 90 ...*/


            this_c_ele_h1.innerHTML = c_per + '%';
            if (c_per == 50) { // 50% 이상일 때 다음 엘리먼트 액션
                if (ele_index < 5) { // 마지막 SNS 가 아닐 때 다음 SNS fadeIn()
                    $('.circle_contents:nth-child(' + (ele_index + 1) + ')').fadeIn();
                    circle_action(index + 1);
                }
            }

            if (ele_index == 1) { // 페이스북 p 태그 컨트롤
                if (c_per == 1) getting_p_action(index, 1, 250);
                else if (c_per == 20) getting_p_action(index, 2, 180);
                else if (c_per == 30) getting_p_action(index, 3, 180);
                else if (c_per == 40) getting_p_action(index, 4, 180);
                else if (c_per == 50) getting_p_action(index, 5, 180);
                else if (c_per == 60) getting_p_action(index, 6, 180);
                else if (c_per == 70) getting_p_action(index, 7, 180);
                else if (c_per == 80) getting_p_action(index, 8, 180);
                else if (c_per == 85) getting_p_action(index, 9, 200);
            } else if (ele_index == 2) { // 인스타 p 태그 컨트롤
                if (c_per == 1) getting_p_action(index, 1, 300);
                else if (c_per == 20) getting_p_action(index, 2, 250);
                else if (c_per == 40) getting_p_action(index, 3, 200);
                else if (c_per == 50) getting_p_action(index, 4, 500);
                else if (c_per == 90) getting_p_action(index, 5, 100);
            } else if (ele_index == 3) { // 구글 p 태그 컨트롤
                if (c_per == 1) getting_p_action(index, 1, 450);
                else if (c_per == 30) getting_p_action(index, 2, 350);
                else if (c_per == 60) getting_p_action(index, 3, 350);
                else if (c_per == 90) getting_p_action(index, 4, 100);
            } else if (ele_index == 4) { // 링크드인 p 태그 컨트롤
                if (c_per == 1) getting_p_action(index, 1, 100);
                else if (c_per == 10) getting_p_action(index, 2, 500);
                else if (c_per == 50) getting_p_action(index, 3, 400);
                else if (c_per == 85) getting_p_action(index, 4, 150);
            } else { // 트위터 p 태그 컨트롤
                if (c_per == 1) getting_p_action(index, 1, 300);
                else if (c_per == 20) getting_p_action(index, 2, 100);
                else if (c_per == 30) getting_p_action(index, 3, 300);
                else if (c_per == 50) getting_p_action(index, 4, 200);
                else if (c_per == 70) getting_p_action(index, 5, 200);
                else if (c_per == 90) getting_p_action(index, 6, 50);
            }
        } else { // 100% 이상일 때
            clearInterval(c_per_action);
            this_c_ele_h1.innerHTML = '100%';
            this_c_ele_info_p.fadeOut();
            //this_c_ele_info_cr.fadeOut(500);

            setTimeout(function () {
                this_c_ele.querySelector('.circle_contents_info').style.height = '40%';
                this_c_ele.querySelector('.circle_contents_info').style.padding = 'unset';
                this_c_ele_info_co.fadeIn(500);
                if (ele_index == 5) {
                    $('#info_2').fadeIn(1000);
                    //$('#main_title').fadeOut();
                    clearInterval(ana_display);
                    document.getElementById('main_title').innerHTML = 'Finished Analyzing';

                    setTimeout(function () { // 끝나는 지점
                        $('#info_2').fadeOut();
                        $('#circle_div').fadeOut();
                        $('#main_title_div').fadeOut();

                        setTimeout(function () {
                            martix();
                            google_title_action();
                        }, 1000);

                    }, 1000);
                }
            }, 1000);
        }
    }, 60);
};

function getting_p_action(circle_contents_index, p_index, timer) { // percentage 별로 Getting 메세지 ... 액션주기.. 플랫폼 별 인덱스 / 적용 p태그 인덱스 / setInterval 시간
    $('.circle_contents:nth-child(' + (circle_contents_index + 1) + ') > .circle_contents_info > p:nth-child(' + p_index + ')').fadeIn();

    var this_c_ele = document.getElementsByClassName('circle_contents')[circle_contents_index];
    var this_c_ele_p = this_c_ele.querySelector('.circle_contents_info > p:nth-child(' + p_index + ')');
    var action_count = 0;

    var action_circle_p = setInterval(function () {
        action_count++;

        if (action_count < 5) this_c_ele_p.innerHTML = this_c_ele_p.innerHTML + '.';
        else {
            action_count = 0;
            clearInterval(action_circle_p);
            this_c_ele_p.innerHTML = this_c_ele_p.innerHTML.split('.')[0].replace('Getting', 'Collected')
        }
    }, timer);
};

// 매트릭스 시작
var font_size = 10;
var drops = [];

function martix() {
    setTimeout(function () {
        $('#matrix').append("<br /><canvas id='c' style='position:fixed; z-index:3; width: 100vw; height: 100vh; top: 0px; left: 0px;'></canvas>");
        c = document.getElementById("c");
        ctx = c.getContext("2d");

        chinese = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQURSTUVWXYZ.";

        //making the canvas full screen
        c.height = window.innerHeight;
        c.width = window.innerWidth;

        columns = c.width / font_size; //number of columns for the rain

        //chinese characters - taken from the unicode charset
        //converting the string into an array of single characters
        chinese = chinese.split("");

        //an array of drops - one per column
        //x below is the x coordinate
        //1 = y co-ordinate of the drop(same for every drop initially)
        for (var x = 0; x < columns; x++)
            drops[x] = 1;

        refreshIntervalId = setInterval(draw, 33);
        /*
        if( typeof $('#ox1step1203aslowsrv2') == 'undefined' ) {
            refreshIntervalId =	setInterval(draw, 33);
        } else {
            $('#c').css('display','none');
        }
        */
    }, 1);
}

function draw() {
    //Black BG for the canvas
    //translucent BG to show trail
    ctx.fillStyle = "rgba(255, 255, 255, 0.05)";
    ctx.fillRect(0, 0, c.width, c.height);

    ctx.fillStyle = "#333"; //green text
    ctx.font = font_size + "px arial";
    //looping over drops
    for (var i = 0; i < drops.length; i++) {
        //a random chinese character to print
        var text = chinese[Math.floor(Math.random() * chinese.length)];
        //x = i*font_size, y = value of drops[i]*font_size
        ctx.fillText(text, i * font_size, drops[i] * font_size);

        //sending the drop back to the top randomly after it has crossed the screen
        //adding a randomness to the reset to make the drops scattered on the Y axis
        if (drops[i] * font_size > c.height && Math.random() > 0.975)
            drops[i] = 0;

        //incrementing Y coordinate
        drops[i]++;
    }
}

function google_title_action() { // matrix 액션 이벤트
    var h1_text = document.getElementById('google_title');

    $('#matrix').fadeIn();
    $('#matrix_info').fadeIn();

    h1_text.innerHTML = 'News Data';

    var gt_action_count = 0;
    var gt_action = setInterval(function () {
        gt_action_count++;

        if (gt_action_count % 2 == 1) {
            $('#google_title').fadeOut();
            if (gt_action_count == 9) { // 끝나는 지점
                //$('#matrix').fadeOut();
                $('#matrix_info > #matrix_title').fadeOut();
                clearInterval(gt_action);

                setTimeout(function () {
                    //$('#union_result_div').fadeIn();
                    //document.getElementById('main_title').innerHTML = 'Raw Datas';
                    //$('#main_title_div').fadeIn();

                    $('#matrix').fadeOut();
                    setTimeout(function () {
                        random_check();
                        setTimeout(function () {
                            $('#union_result_div').fadeIn();
                            setTimeout(function () { // 끝나는 지점
                                location.href = 'AML/';
                            }, 2000);

                        }, 500);


                        //JSON 또는 배열을 for를 이용해서 한번에 출력.. 밑에는 그냥 예시로 여러번 함수 호출.
                        /*create_terminal_line('facebook', 'user_gender', 'male32462346362346234632462346234623472347');
                        create_terminal_line('facebook', 'user_gender', 'femlae242642');
                        create_terminal_line('facebook', 'user_gender', 'femlae242642');
                        create_terminal_line('facebook', 'user_gender', 'femlae242642');
                        create_terminal_line('facebook', 'user_gender', 'femlae242642');
                        create_terminal_line('instagram', 'user_gnw3naender', 'maawetbmaawetbawetbawetblemaawetbawetbawetblemaawetbawetbawetblemaawetbawetbawetbleawetbawetble');
                        create_terminal_line('instagram', 'user_gnw3naender', 'maawetbmaawetbawetbawetblemaawetbawetbawetblemaawetbawetbawetblemaawetbawetbawetbleawetbawetble');
                        create_terminal_line('instagram', 'user_gnw3naender', 'maawetbmaawetbawetbawetblemaawetbawetbawetblemaawetbawetbawetblemaawetbawetbawetbleawetbawetble');
                        create_terminal_line('instagram', 'user_gnw3naender', 'maawetbmaawetbawetbawetblemaawetbawetbawetblemaawetbawetbawetblemaawetbawetbawetbleawetbawetble');
                        create_terminal_line('instagram', 'user_gnw3naender', 'maawetbmaawetbawetbawetblemaawetbawetbawetblemaawetbawetbawetblemaawetbawetbawetbleawetbawetble');
                        create_terminal_line('instagram', 'user_gnw3naender', 'maawetbmaawetbawetbawetblemaawetbawetbawetblemaawetbawetbawetblemaawetbawetbawetbleawetbawetble');
                        create_terminal_line('instagram', 'user_gnw3naender', 'maawetbmaawetbawetbawetblemaawetbawetbawetblemaawetbawetbawetblemaawetbawetbawetbleawetbawetble');
                        create_terminal_line('instagram', 'user_gnw3naender', 'maawetbmaawetbawetbawetblemaawetbawetbawetblemaawetbawetbawetblemaawetbawetbawetbleawetbawetble');
                        create_terminal_line('twitter', 'userw3n_gender', 'maawetbwetle');
                        create_terminal_line('twitter', 'userw3n_gender', 'maawetbwetle');
                        create_terminal_line('twitter', 'userw3n_gender', 'maawetbwetle');
                        create_terminal_line('twitter', 'userw3n_gender', 'maawetbwetle');
                        create_terminal_line('twitter', 'userw3n_gender', 'maawetbwetle');
                        create_terminal_line('twitter', 'userw3n_gender', 'maawetbwetle');
                        create_terminal_line('twitter', 'userw3n_gender', 'maawetbwetle');
                        create_terminal_line('twitter', 'userw3n_gender', 'maawetbwetle');
                        create_terminal_line('twitter', 'userw3n_gender', 'maawetbwetle');
                        create_terminal_line('linkedin', 'user_gaw3ynaw3ender', 'mawetbawmawetbaw3naw3nlemawetbaw3naw3nlemawetbaw3naw3nlemawetbaw3naw3nlemawetbaw3naw3nlemawetbaw3naw3nlemawetbaw3naw3nlemawetbaw3naw3nlemawetbaw3naw3nlemawetbaw3naw3nlemawetbaw3naw3nlemawetbaw3naw3nle3naw3nle');
                        create_terminal_line('linkedin', 'user_gaw3ynaw3ender', 'mawetbawmawetbaw3naw3nlemawetbaw3naw3nlemawetbaw3naw3nlemawetbaw3naw3nlemawetbaw3naw3nlemawetbaw3naw3nlemawetbaw3naw3nlemawetbaw3naw3nlemawetbaw3naw3nlemawetbaw3naw3nlemawetbaw3naw3nlemawetbaw3naw3nle3naw3nle');
                        create_terminal_line('linkedin', 'user_gaw3ynaw3ender', 'mawetbawmawetbaw3naw3nlemawetbaw3naw3nlemawetbaw3naw3nlemawetbaw3naw3nlemawetbaw3naw3nlemawetbaw3naw3nlemawetbaw3naw3nlemawetbaw3naw3nlemawetbaw3naw3nlemawetbaw3naw3nlemawetbaw3naw3nlemawetbaw3naw3nle3naw3nle');
                        create_terminal_line('google', 'user_gender', 'maawetbawetale');
                        create_terminal_line('google', 'useraw36naw3n6_gender', 'maaw3ybaw3bw3lmawetbaw3naw3nlee');
                        create_terminal_line('google', 'useraw36naw3n6_gender', 'maaw3ybaw3bw3lmawetbaw3naw3nlee');
                        create_terminal_line('google', 'useraw36naw3n6_gender', 'maaw3ybaw3bw3lmawetbaw3naw3nlee');
                        create_terminal_line('google', 'useraw36naw3n6_gender', 'maaw3ybaw3bw3lmawetbaw3naw3nlee');
                        create_terminal_line('google', 'useraw36naw3n6_gender', 'maaw3ybaw3bw3lmawetbaw3naw3nlee');
                        create_terminal_line('google', 'useraw36naw3n6_gender', 'maaw3ybaw3bw3lmawetbaw3naw3nlee');*/
                    }, 1000);

                }, 1000);
            }
        } else if (gt_action_count % 2 == 0) {
            if (gt_action_count == 2) h1_text.innerHTML = 'Browser Data';
            else if (gt_action_count == 4) h1_text.innerHTML = 'Community Data';
            else if (gt_action_count == 6) h1_text.innerHTML = 'Shopping Data';
            else if (gt_action_count == 8) h1_text.innerHTML = 'Transaction Data';
            $('#google_title').fadeIn();
        }
    }, 1500);
};

function random_check() {
    var union_result_div = document.getElementById('union_result_div');
    var contents = union_result_div.querySelectorAll('.union_contents_div');

    var class_list = ['check', 'uncheck'];
    for (var i = 0; i < contents.length; i++) {
        var ran_num = random_return(0, 1);
        var this_class_name = class_list[ran_num];

        if (i == 0 || i == 1 || i == 2 || i == 4 || i == 5 || i == 7) contents[i].classList.add('check');
        else contents[i].classList.add(this_class_name);
    }
}

function random_return(min, max) { //min 포함 ~ max 포함 랜덤 반환
    return Math.floor(Math.random() * (max - min + 1)) + min;
};