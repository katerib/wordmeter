document.addEventListener("DOMContentLoaded", function() {
    function updateProgress() {
        fetch('/progress')
            .then(response => response.json())
            .then(data => {
                const progressBar = document.getElementById('fileUploadProgress');
                progressBar.value = data.progress;
                progressBar.innerText = `${data.progress}%`;

                if(data.progress < 100) {
                    setTimeout(updateProgress, 1000);
                } else {
                    window.location.href = '/results'; // Redirect to results page
                }
            });
    }
    updateProgress();
});
