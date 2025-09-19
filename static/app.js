async function analyzeTranscript() {
    const transcript = document.getElementById('transcript').value;
    const resultsDiv = document.getElementById('results');
    
    try {
        const response = await fetch('/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: transcript })
        });
        
        const data = await response.json();
        
        resultsDiv.innerHTML = `
            <h2>Analysis Results</h2>
            <p><strong>Main Category:</strong> ${data['Main Category']}</p>
            <p><strong>Sub-Category:</strong> ${data['Sub-Category']}</p>
            <p><strong>Summary:</strong> ${data['Summary']}</p>
        `;
        resultsDiv.style.display = 'block';
    } catch (error) {
        resultsDiv.innerHTML = `<p class="error">Error analyzing transcript: ${error}</p>`;
        resultsDiv.style.display = 'block';
    }
}