// 處理登入功能
const the_btn = document.getElementById("the_btn");
the_btn.addEventListener("click", function(event){
    const the_checkbox = document.getElementById("the_checkbox");
    // console.log(the_checkbox.checked);
    if (the_checkbox.checked == false){
        event.preventDefault(); //阻止提交表單
        window.alert("Please check the checkbox first");
    }
});

// 處理計算平方功能
const square_form = document.getElementById("square-form");
square_form.addEventListener("submit", function(event) {
    event.preventDefault();  // 阻止表單預設提交動作
    let num = document.getElementById("num").value;
    num = Number(num);

    if (num <= 0 || Number.isInteger(num) != true ) {
        alert("Please enter a positive integer");
        document.getElementById("num").value = "";
    } else {
        window.location.href = `/square/${num}`;
    }
});