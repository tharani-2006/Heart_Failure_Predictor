function showPopup(event) {
    event.preventDefault();
    const popup = document.getElementById('popup');
    const popupText = document.getElementById('popup-text');
    popupText.textContent = "The patient is not at risk of heart failure."; // Replace with dynamic result
    popup.style.display = 'block';
}

function closePopup() {
    const popup = document.getElementById('popup');
    popup.style.display = 'none';
}