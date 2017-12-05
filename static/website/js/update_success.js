$(document).ready(function () {
        var success = SUCCESS.toLowerCase() === 'true';
        if (success) {
            showToastMessage("Monografía actualizada");
        }
    });

function showToastMessage(message) {
    document.getElementById('toast').MaterialSnackbar.showSnackbar({
        message: message
    });
}