function addArticle(curPost) {
  var newDom = $('<article class="post"></article>');
  newDom.attr('id', 'post-' + curPost.pk);

  // article요소의 header.post-header를 생성
  newDom.append('<header class="post-header"></header>');
  var newDomHeader = newDom.find('header.post-header');
  newDomHeader.append('<span class="header-username"></span>');
  newDomHeader.append('<form action="" class="inline"></form>');
  newDomHeader.append('<span class="header-date"></span>');

  newDomHeader.find('span.header-username').text(curPost.author.username);
  // 문자열이아닌, momentjs를 사용해서 parse -> format한 형태를 대입
  var day = moment(curPost.created_date);
  var strDay = moment(day).format('YYYY년 M월 D일');
  var strDay2 = moment(day).format('lll');
  newDomHeader.find('span.header-date').text(strDay2);

  // aritcle요소의 post-image-container를 생성
  newDom.append('<div class="post-image-container"></div>');
  newDom.find('.post-image-container').append('<div class="swiper-container"></div>');
  newDom.find('.swiper-container').append('<div class="swiper-wrapper"></div>');
  var newDomSwiperWrapper = newDom.find('.swiper-wrapper');
  // curPost.postphoto_set을 loop하며
  //.swiper-wrapper의 내부에 postphoto.photo값을 사용해 .swiper-slide > img태그를 생성
  // img의 src속성과 같이 속성을 변화시킬 때는 .text()대신 .attr('속성명', '속성값')을 사용
  for(var j = 0; j < curPost.postphoto_set.length; j++) {
    var curPostPhoto = curPost.postphoto_set[j];
    // PostPhoto하나당 .swiper-slide > img만들고 src값을 PostPhoto의 photo속성으로 대입
    var newSwiperSlide = $('<div class="swiper-slide"></div>');
    newSwiperSlide.append('<img src="" alt="" />');
    newSwiperSlide.find('img').attr('src', curPostPhoto.photo);

    // 만들어진 swiper-slide를 swiper-wrapper내부에 append
    newDomSwiperWrapper.append(newSwiperSlide);
  }

  // aritlce요소의 post-bottom-container를 생성
  newDom.append('<div class="post-bottom-container"></div>');
  $('.post-list-container').append(newDom);

  // 새로만든 aritlce내부의 .swiper-container에 id값을 추가
  newDom.find('.swiper-container').attr('id', 'post-swiper-' + curPost.pk);
  // .swiper-container의 id로 Swiper초기화
  new Swiper('#post-swiper-' + curPost.pk);
}
