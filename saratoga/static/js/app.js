function same_height(id1, id2){
    var elemet1 = '#'+id1;
    var elemet2 = '#'+id2;
    var height_text = $(elemet1).height();
    var max_height = Math.max($(elemet1).height(), $(elemet2).height());
    $(elemet1).height(max_height);
    $(elemet2).height(max_height);
}