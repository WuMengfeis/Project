
var oParent =  document.getElementById('container');

window.addEventListener('load', function(){
    imgLocation('box');
}, false);
function imgLocation(child){
    var oContent = getChilds(child);
    var imgWidth = oContent[0].offsetWidth;
    var num = ~~(document.documentElement.clientWidth / imgWidth);
    //console.log(oContent);
    oParent.style.cssText = 'width: ' + (imgWidth * num) + 'px; margin: 0 auto;'; 
    
    var heightArr = [];
    oContent.forEach(function(current, index){
        if(index < num){
            heightArr.push(current.offsetWidth);
        }
        else{
            var minHeight = Math.min.apply(Math, heightArr);
            current.style.position = 'absolute';
            //current.style.top = ;
            //current.style.left = ;
            console.log(minHeight);
        }
        
    });
}
imgLocation('box');

function getChilds(child){
    var childArr = [];
    var tagsAll = oParent.getElementsByTagName('*');
    for (var i = 0; i < tagsAll.length; i++) {
        if(tagsAll[i].className == child){
            childArr.push(tagsAll[i]);
        }
    }
    return childArr;
    //console.log(tagsAll);
}
getChilds('box');


    // $(document).ready(function () {   
    //     $('.select ul li').on("click", function (e) {   
    //         var _this = $(this);   
    //         $('.select >p').text(_this.attr('data-value'));   
    //         $(_this).addClass('selected').siblings().removeClass('selected');   
    //         $('.select').toggleClass('open');   
    //         cancelBubble(e);   
    //     });   
  
    //     $('.select>p').on("click", function (e) {   
    //         $('.select').toggleClass('open');   
    //         cancelBubble(e);   
    //     });   
  
    //     $(document).on('click', function () {   
    //         $('.select').removeClass('open');   
    //     })   
    // })   


    //  $(document).ready(function () {   
    //     $('.select1 ul li').on("click", function (e) {   
    //         var _this = $(this);   
    //         $('.select1 >p').text(_this.attr('data-value'));   
    //         $(_this).addClass('selected').siblings().removeClass('selected');   
    //         $('.select1').toggleClass('open');   
    //         cancelBubble(e);   
    //     });   
  
    //     $('.select1>p').on("click", function (e) {   
    //         $('.select1').toggleClass('open');   
    //         cancelBubble(e);   
    //     });   
  
    //     $(document).on('click', function () {   
    //         $('.select1').removeClass('open');   
    //     })   
    // })
    // $(document).ready(function () {   
    //     $('.select2 ul li').on("click", function (e) {   
    //         var _this = $(this);   
    //         $('.select2 >p').text(_this.attr('data-value'));   
    //         $(_this).addClass('selected').siblings().removeClass('selected');   
    //         $('.select2').toggleClass('open');   
    //         cancelBubble(e);   
    //     });   
  
    //     $('.select2>p').on("click", function (e) {   
    //         $('.select2').toggleClass('open');   
    //         cancelBubble(e);   
    //     });   
  
    //     $(document).on('click', function () {   
    //         $('.select2').removeClass('open');   
    //     })   
    // })
  
    // function cancelBubble(event) {   
    //     if (event.stopPropagation) {   
    //         event.preventDefault();   
    //         event.stopPropagation();   
    //     } else {   
    //         event.returnValue = false;   
    //         event.cancelBubble();   
    //     }   
    // }   
