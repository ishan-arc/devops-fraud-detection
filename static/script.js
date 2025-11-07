document.getElementById('prediction-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const amount = document.getElementById('amount').value;
    const resultDiv = document.getElementById('result');

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ amount: parseFloat(amount) })
    })
    .then(response => response.json())
    .then(data => {
        if (data.fraud) {
            resultDiv.innerHTML = '<p class="fraud">Fraudulent Transaction Detected!</p>';
        } else {
            resultDiv.innerHTML = '<p class="not-fraud">Transaction is likely not fraudulent.</p>';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        resultDiv.innerHTML = '<p class="error">An error occurred. Please try again.</p>';
    });
});
