function same_height_news(){
    var h1 = $("#sub-news-area-left")[0].scrollHeight
    var h2 = $("#sub-news-area-right")[0].scrollHeight
    var h3 = Math.max(h1,h2);
    $("#news-area-left").height(h3);
    $("#news-area-right").height(h3);
}