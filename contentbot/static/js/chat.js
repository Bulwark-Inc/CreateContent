document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('chat-form');
    const messageInput = document.getElementById('user-message');
    const outputDiv = document.getElementById('chat-output');

    form.addEventListener('submit', async (event) => {
        event.preventDefault(); // Prevent form from reloading the page
        const userMessage = messageInput.value;

        // Clear the input
        messageInput.value = '';

        // Display user message
        outputDiv.innerHTML += `<p><strong>You:</strong> ${userMessage}</p>`;

        try {
            const response = await fetch('http://127.0.0.1:8000/api/chat/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Token 568304114229b67c12a081b3810fd2677a2e2784`,
                },
                body: JSON.stringify({ message: userMessage }),
            });

            if (!response.ok) {
                throw new Error('Failed to fetch response from the bot.');
            }

            const data = await response.json();
            outputDiv.innerHTML += `<p><strong>Bot:</strong> ${data.response}</p>`;
        } catch (error) {
            outputDiv.innerHTML += `<p><strong>Error:</strong> ${error.message}</p>`;
        }

        // Scroll to the bottom
        outputDiv.scrollTop = outputDiv.scrollHeight;
    });
});
