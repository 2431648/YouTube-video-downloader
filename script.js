// static/script.js
const form = document.getElementById('downloadForm');
const btn = document.getElementById('btn');
const statusText = document.getElementById('status');
const loader = document.getElementById('loader');

form.addEventListener('submit', async (e) => {
    e.preventDefault(); // Stop page reload

    const url = document.getElementById('url').value;
    
    // 1. UI Changes: Show Loading
    btn.innerText = "Processing...";
    btn.style.opacity = "0.7";
    btn.disabled = true;
    loader.style.display = "block";
    statusText.innerText = "Fetching video details...";
    statusText.style.color = "#fff";

    try {
        // 2. Send Data to Python Backend
        const response = await fetch('/download', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ url: url })
        });

        const data = await response.json();

        // 3. Handle Success
        if (data.status === 'success') {
            statusText.innerText = "Download Started! ✅";
            statusText.style.color = "#00ff88"; // Neon Green
            
            // Trigger the browser download
            window.location.href = data.download_link; 
        } else {
            throw new Error(data.message);
        }

    } catch (error) {
        statusText.innerText = "Error: " + error.message;
        statusText.style.color = "#ff4444";
    } finally {
        // 4. Reset Button
        btn.innerText = "Download Now";
        btn.style.opacity = "1";
        btn.disabled = false;
        loader.style.display = "none";
    }
});