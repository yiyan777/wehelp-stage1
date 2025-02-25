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