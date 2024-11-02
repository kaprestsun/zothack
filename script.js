console.log("hello");

function clicked(){
    window.location.href = 'http://127.0.0.1:5501/index.html';
}

fetch('http://169.234.5.101:8000/').then(res=> res.json()).then(respose => {
    console.log(response);
})
