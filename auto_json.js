// ==UserScript==
// @name         New Userscript
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://www.example.com
// @icon         https://www.example.com
// @grant        none
// ==/UserScript==

(function() {
'use strict';

// Your code here...
let array =[];
for(var i = 1 ; i < 100 ; i += 1){
    let box ={};
    
   // 欲しい情報に合わせて書き換えてください。
   // box.x = (document.querySelectorAll(`#example_selector > li:nth-child\(${i}\) > dl >dt > a > img`)[0].getAttribute("alt"))
   // box.y = (document.querySelectorAll(`#example_selector > li:nth-child\(${i}\) > dl >dt > a`)[0].getAttribute("href"))
   // box.z = (document.querySelectorAll(`#example_selector > li:nth-child(${i}) > something_elements`)[0].innerText)
    array.push(JSON.stringify(box));


}

    const obj = {...array};
    location.href = URL.createObjectURL(new Blob([JSON.stringify(obj)], {
    type: "application/octet-stream"
    }))

})();


