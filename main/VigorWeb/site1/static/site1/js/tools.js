document.getElementById("Form").addEventListener("submit", function (event) {
    event.preventDefault(); // Ngăn chặn hành vi mặc định của liên kết

    var height = parseFloat(document.getElementById("height").value);
    var weight = parseFloat(document.getElementById("weight").value);
    var age = parseFloat(document.getElementById("age").value);
    var gender = parseInt(document.querySelector('input[name="phai"]:checked').value);
    var activity = parseInt(document.querySelector('input[name="cuong-do"]:checked').value);

    var bmr;
    if (gender === 1) {
        bmr = 66 + (13.7 * weight) + (5 * height) - (6.8 * age);
    } else {
        bmr = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age);
    }

    var tdee;
    switch(activity) {
        case 1:
            tdee = bmr * 1.2;
            break;
        case 2:
            tdee = bmr * 1.375;
            break;
        case 3:
            tdee = bmr * 1.55;
            break;
        case 4:
            tdee = bmr * 1.725;
            break;
        case 5:
            tdee = bmr * 1.9;
            break;
    }
    document.getElementById("BMR").innerText = bmr.toFixed(0);
    document.getElementById("TDEE").innerText = tdee.toFixed(0);
    document.getElementById("keepWeight").innerText = tdee.toFixed(0); 
});