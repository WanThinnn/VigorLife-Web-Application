document.getElementById("Form").addEventListener("submit", function (event) {
    event.preventDefault();

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

    var bmi;
    height /= 100;
    bmi=weight/(height*height);
    
    var dec1, dec2, dec3, inc1, inc2, inc3;

    dec1 = 0.85 * tdee;
    dec2 = 0.71 * tdee;
    dec3 = 0.42 * tdee;
    inc1 = 1.15 * tdee;
    inc2 = 1.29 * tdee;
    inc3 = 1.58 * tdee;

    document.getElementById("BMR").innerText = bmr.toFixed(0);
    document.getElementById("TDEE").innerText = tdee.toFixed(0);
    document.getElementById("BMI").innerText = bmi.toFixed(2);
    document.getElementById("keepWeight").innerText = tdee.toFixed(0); 
    document.getElementById("decrease85").innerText = dec1.toFixed(0); 
    document.getElementById("decrease71").innerText = dec2.toFixed(0); 
    document.getElementById("decrease42").innerText = dec3.toFixed(0); 
    document.getElementById("increase115").innerText = inc1.toFixed(0); 
    document.getElementById("increase129").innerText = inc2.toFixed(0); 
    document.getElementById("increase158").innerText = inc3.toFixed(0); 
});