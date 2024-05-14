document.addEventListener("DOMContentLoaded", function () {
  var commentContainers = document.querySelectorAll(".comment");

  commentContainers.forEach(function (container) {
      var replyBtn = container.querySelector(".reply-btn");
      var replyForm = container.querySelector(".reply-form");
      
      replyBtn.addEventListener("click", function () {
          // Toggle hiển thị của form trả lời
          replyForm.style.display = (replyForm.style.display === "block") ? "none" : "block";
      });
  });
});

  document.addEventListener("DOMContentLoaded", function () {
    // var commentsContainer = document.getElementById("comments-container");
    var loadMoreBtn = document.getElementById("load-more-btn");
    var allComments = document.querySelectorAll(".comment");
    var visibleComments = 3; // Số lượng comment hiện tại đang hiển thị

    // Ẩn các comment còn lại
    for (var i = 3; i < allComments.length; i++) {
      allComments[i].style.display = "none";
    }

    // Xử lý sự kiện khi nhấp vào nút "Xem thêm"
    loadMoreBtn.addEventListener("click", function () {
      // Hiển thị thêm 3 comment
      for (var i = visibleComments; i < visibleComments + 3 && i < allComments.length; i++) {
        allComments[i].style.display = "block";
      }
      visibleComments += 3; // Cập nhật số lượng comment đang hiển thị

      // Ẩn nút "Xem thêm" nếu đã hiển thị tất cả comment
      if (visibleComments >= allComments.length) {
        loadMoreBtn.style.display = "none";
      }
    });
  });