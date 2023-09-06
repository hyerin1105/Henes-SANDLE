function login() {
    var pw = document.querySelector('#password');

    if(pw.value == "") {
        alert("로그인을 할 수 없습니다.")
    }
    else {
        location.href = 'main.html';
    }
}

function back() {
    history.go(-1);
}

function create_id() {
    var add = document.querySelector('#address');
    var pw = document.querySelector('#password');
    var r_pw = document.querySelector('#r_pw');

    if(add.value == "" || pw.value == "" || r_pw.value == "") {
        alert("회원가입을 할 수 없습니다.")
    }
    else {
        if(pw.value !== r_pw.value) {
            alert("비밀번호를 확인해주세요.")
        }
        else {
            location.href = 'login.html';
        }
    }
}