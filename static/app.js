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
        
        if (data.error) {
            resultsDiv.innerHTML = `<p class="error">${data.error}</p>`;
            return;
        }

        // Display results
        resultsDiv.innerHTML = `
            <h2>Analysis Results</h2>
            <p><strong>Main Category:</strong> ${data.analysis['Main Category']}</p>
            <p><strong>Sub-Category:</strong> ${data.analysis['Sub-Category']}</p>
            <p><strong>Summary:</strong> ${data.analysis['Summary']}</p>
        `;
        resultsDiv.style.display = 'block';

        // Create and trigger CSV download
        const blob = new Blob([data.csv_data], { type: 'text/csv' });
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = data.filename;
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
        document.body.removeChild(a);

        // Show download notification
        showDownloadNotification(data.filename);
    } catch (error) {
        resultsDiv.innerHTML = `<p class="error">Error analyzing transcript: ${error}</p>`;
        resultsDiv.style.display = 'block';
    }
}

function showDownloadNotification(filename) {
    const notification = document.createElement('div');
    notification.className = 'download-notification';
    notification.innerHTML = `
        <p>📥 Downloading ${filename}</p>
    `;
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.remove();
    }, 3000);
}