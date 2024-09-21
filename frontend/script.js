// Attach event listener to the analyze button
document.querySelector('.analyze-btn').addEventListener('click', predictDisease);

// Show the preview of the uploaded image
document.getElementById('imageUpload').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const imagePreview = document.getElementById('imagePreview');
            imagePreview.src = e.target.result;
            imagePreview.style.display = 'block'; // Show the image preview
        };
        reader.readAsDataURL(file);
    }
});

// Function to handle prediction of plant disease
async function predictDisease() {
    const fileInput = document.getElementById('imageUpload');
    const loadingElement = document.getElementById('loading');
    const resultSection = document.getElementById('resultSection');
    const resultText = document.getElementById('resultText');
    const treatmentText = document.getElementById('treatmentText');

    // Check if file is selected
    if (fileInput.files.length === 0) {
        alert("Please upload an image of the plant.");
        return;
    }

    const file = fileInput.files[0];

    // Create a FormData object to send the image
    const formData = new FormData();
    formData.append('file', file);

    // Display loading spinner
    loadingElement.style.display = 'block';

    try {
        // Send the image to the Flask server
        const response = await fetch('/predict', {
            method: 'POST',
            body: formData
        });

        // Check if the response is OK
        if (!response.ok) {
            throw new Error('Error in the prediction request');
        }

        const data = await response.json();

        // Display the prediction result
        loadingElement.style.display = 'none';
        resultSection.style.display = 'block';
        resultText.textContent = `Prediction: ${data.prediction}`;

        // Display additional information about the disease or healthy status
        if (data.prediction === 'Healthy') {
            treatmentText.textContent = "The plant is healthy and doesn't need treatment.";
        } else {
            treatmentText.textContent = `The plant is affected by ${data.prediction}. Please consult an expert for treatment advice.`;
        }
    } catch (error) {
        loadingElement.style.display = 'none';
        alert('There was an error in processing the image. Please try again.');
    }
}
