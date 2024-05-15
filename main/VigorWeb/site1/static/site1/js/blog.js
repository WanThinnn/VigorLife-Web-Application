document.addEventListener('DOMContentLoaded', function() {
    // Lấy phần tử .about-project-section
    var aboutProjectSection = document.querySelector('.about-project-section');

    // Lấy chiều cao của các phần tử con
    var childElements = aboutProjectSection.children;
    var totalHeight = 0;
    for (var i = 0; i < childElements.length; i++) {
        totalHeight += childElements[i].offsetHeight;
    }

    // Cập nhật chiều cao của .about-project-section
    aboutProjectSection.style.height = totalHeight + 'px';
});

document.addEventListener('DOMContentLoaded', function() {
    // Lấy phần tử .about-project-section
    var aboutProjectSection = document.querySelector('.about-ús-section');

    // Lấy chiều cao của các phần tử con
    var childElements = aboutProjectSection.children;
    var totalHeight = 0;
    for (var i = 0; i < childElements.length; i++) {
        totalHeight += childElements[i].offsetHeight;
    }

    // Cập nhật chiều cao của .about-project-section
    aboutProjectSection.style.height = totalHeight + 'px';
});