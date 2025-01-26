const elem_show = document.querySelector(".mobile-menu");
elem_show.addEventListener("click", () =>{
    var show = document.querySelector(".mobile-item-list");
    show.style.display = "block";
});
const elem_disappear = document.querySelector(".cross");
elem_disappear.addEventListener("click", () =>{
    var disappear = document.querySelector(".mobile-item-list");
    disappear.style.display = "none";
});
function getData(){
    fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1").then(
        function(response){
            return response.json();
        }).then(function(data_hw){
            // console.log(data_hw);  // JSON 格式資料
            const spotsArray = data_hw.data.results;  //第0筆是新北投溫泉區, 第1筆是大稻埕 ...
            // console.log(spotsArray);
            var frame = document.getElementById("frame");

            spotsArray.slice(0, 3).forEach((spot, index) => {
                createSpotCardSmall(frame, spot, index);
            });
            spotsArray.slice(3, 13).forEach((spot, index) => {
                createSpotCardBig(frame, spot, index);
            });

        });
}
function createSpotCardSmall(container, spot, index){
    const cardDiv = document.createElement("div");
    cardDiv.className = `small-box s${index + 1}`; //賦予class
    
    const image = document.createElement("img");
    image.style.width = "80px";
    image.style.height = "50px";
    image.src = parseImageUrl(spot.filelist); //處理small圖片URL
    cardDiv.appendChild(image);

    const textDiv = document.createElement("div");
    textDiv.className = "text";
    textDiv.textContent = spot.stitle; //景點名稱
    cardDiv.appendChild(textDiv);

    container.appendChild(cardDiv);
}

function createSpotCardBig(container, spot, index){
    const cardDiv = document.createElement("div");
    cardDiv.className = `big-box b${index + 1}`; //賦予class
    cardDiv.style.backgroundImage = parseBigImageUrl(spot.filelist);
    
    const starDiv = document.createElement("div"); //裝星星的div
    starDiv.className = "star";
    cardDiv.appendChild(starDiv);

    const imageStar = document.createElement("img");  //星星的img
    imageStar.style.width = "30px";
    imageStar.src = "imgs/star.png";
    starDiv.appendChild(imageStar);

    const textDiv = document.createElement("div");
    textDiv.className = "title";

    // const maxLength = 7;
    // textDiv.textContent = spot.title.length > maxLength?`${spot.stitle.substring(0, max.Length)}...`: spot.stitle; 

    textDiv.textContent = spot.stitle; //景點名稱
    cardDiv.appendChild(textDiv);

    container.appendChild(cardDiv);
}
function parseImageUrl(filestring){
    const urls = filestring.split("https://");
    return `https://${urls[1]}`; 
}
function parseBigImageUrl(filestring){
    const urls = filestring.split("https://");
    return `url(https://${urls[1]})`; 
}


getData();