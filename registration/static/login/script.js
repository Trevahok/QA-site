async function validatepass() {
    var str = document.getElementById('password').value;
    if (str.length >= 8) {
        document.getElementById('pfalse').style.visibility = "hidden";
        document.getElementById('ptrue').style.visibility = "visible";

    } else {
        document.getElementById('ptrue').style.visibility = "hidden";
        document.getElementById('pfalse').style.visibility = "visible";

    }
}
async function validatecpass() {
    var str = document.getElementById('password').value;
    var str2 = document.getElementById('cpassword').value;
    if (str == str2 && str != '') {
        document.getElementById('cfalse').style.visibility = "hidden";
        document.getElementById('ctrue').style.visibility = "visible";

    } else {
        document.getElementById('ctrue').style.visibility = "hidden";
        document.getElementById('cfalse').style.visibility = "visible";

    }
}

setInterval(validatepass, 300);
setInterval(validatecpass, 300);