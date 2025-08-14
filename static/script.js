function showPopup(prediction) {
    const popup = document.getElementById('popup');
    const popupText = document.getElementById('popup-text');
    popupText.textContent = prediction; // Use the dynamic result passed from the server
    popup.style.display = 'block';
}

function closePopup() {
    const popup = document.getElementById('popup');
    popup.style.display = 'none';
}