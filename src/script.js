function newpage(x) {
    decreaseOpacity(() => {
        window.location.href = x;
    });
}

function decreaseOpacity(callback) {
    let opacity = parseFloat(window.getComputedStyle(document.body).opacity);
    
    const interval = setInterval(() => {
        opacity -= 0.01;
        document.body.style.opacity = opacity;

        if (opacity <= 0) {
            clearInterval(interval);
            if (callback) callback();
        }
    }, 3);  
}