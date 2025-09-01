// # 연습용

// document.addEventListener("DOMContentLoaded", function() {
//     console.log("app.js loaded!");

//     const btn = document.getElementById("ajax-btn");
//     if (btn) {
//         btn.addEventListener("click", function() {
//             fetch("/your-ajax-url/")  // 여기는 Django view URL로 바꿔야 함
//                 .then(response => response.json())
//                 .then(data => {
//                     alert("서버 응답: " + JSON.stringify(data));
//                 })
//                 .catch(error => console.error("Error:", error));
//         });
//     }
// });
