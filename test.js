//naver 뉴스 

//! 사용할 cheerio 함수들
// cheerio 는 jQuery 를 이용해서 웹 페이지를 parsing 하고, 데이터 구조의 결과물을 탐색 및 조작할 수 있도록 도와주는 Node.js 의 라이브러리이다. 
// 일반적으로 jQuery Selector $ 에 load 된 HTML 값을 넣어 사용한다.
// load : html 문자열을 받아 cheerio 객체를 반환
// children : html selector를 문자열로 받아 cheerio 객체에서 선택된 html 문자열에서 해당하는 모든 태그들의 배열을 반환
// each : 콜백 함수를 받아 태그들의 배열을 순회 하면서 콜백함수를 실행
// find : html selector 를 문자열로 받아 해당하는 태그를 반환

//! Puppeteer
// puppeteer 은 Chrome 또는 Chronium 을 제어할 수 있는 high-level 의 API 를 제공하는 Node.js 의 라이브러리이다.
// 기본적으로 headless browser 에서 동작하지만 full (non-headless) Chrome 에서도 동작할 수 있다.

//Crawler 모듈
var Crawler = require("crawler");

var c = new Crawler({
  maxConnections: 10,
  // This will be called for each crawled page
  callback: function (error, res, done) {
    if (error) {
      console.log(error);
    } else {
      var $ = res.$;
      // $ is Cheerio by default
      //a lean implementation of core jQuery designed specifically for the server
      console.log($("title").text());

      const $bodyList = $("div.thumb_area").children("div.thumb_box");

      let newsList = [];
      $bodyList.each(function (i, elem) {
        newsList[i] = $(this).find('a.thumb img').attr('alt');
      });

      console.log(newsList);
    }
    done();
  }
});

// Queue just one URL, with default callback
c.queue('http://www.naver.com');




