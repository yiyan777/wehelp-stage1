const findBtn = document.querySelector(".find-name-btn");
const usernameInput = document.getElementById("username-input");
const updateSection = document.querySelector(".update-name");

const resultDiv = document.createElement("div"); //新增一個div來顯示結果
resultDiv.style.textAlign = "center";
resultDiv.style.fontSize= "24px";
updateSection.parentNode.insertBefore(resultDiv, updateSection); //插入到更新區塊上方
        
        
function getData(){         
    fetch("http://127.0.0.1:8000/api/member?username="+usernameInput.value).then(function(response){
        return response.json();  
    }).then(function(data){
        if (data["data"]){
            let memberName = data["data"]["name"];
            let username = data["data"]["username"];
            resultDiv.textContent = `${memberName} (${username})`; // 更新畫面
        } else {
            resultDiv.textContent = "No Data";
        }
        
    });
}
findBtn.addEventListener("click", getData);

// 按下Enter也可以觸發查詢
usernameInput.addEventListener("keydown", function(event){
    if (event.key === "Enter"){
        getData();
    }
})

const updateBtn = document.querySelector(".update-name-btn");
const newNameInput = document.getElementById("new-name");
const updateResultDiv = document.createElement("div"); //用來顯示結果
updateResultDiv.style.textAlign = "center";
updateResultDiv.style.fontSize = "24px";
document.body.appendChild(updateResultDiv);

function updateName(){
    const newName = newNameInput.value;
    fetch("http://127.0.0.1:8000/api/member",{
        method: "PATCH",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ name: newName })
    })
    .then(response => response.json())
    .then(data => {
        if (data.ok){
            updateResultDiv.textContent = "更新成功";
            const nameOnScreen = document.querySelector(".text");
            nameOnScreen.textContent = `${newName}您好，歡迎登入系統`;
            newNameInput.value="";
        } else {
            updateResultDiv.textContent = "更新失敗";
        }
    })
    .catch(error => {
        updateResultDiv.textContent = "發生錯誤";
        console.error("Error:", error);
    });
}
updateBtn.addEventListener("click", updateName);
        
// 按下Enter也可以觸發更新
newNameInput.addEventListener("keydown", function(event){ 
    if (event.key === "Enter"){
        updateName();
    }
})