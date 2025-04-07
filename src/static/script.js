document.addEventListener('DOMContentLoaded', function() {
    // Fetch live data when the page loads
    fetchLiveData();

    // Event listener for the 'Send' button
    const sendBtn = document.getElementById("send_btn");
    sendBtn.addEventListener("click", async function() {
        const userInput = document.getElementById("user_input").value;
        if (userInput.trim()) {
            // Display user's input in the chat
            addToChat("You: " + userInput);
            // Send the user's input to the Flask backend
            const response = await fetch('/predict', {
                method: 'POST',
                body: JSON.stringify({ input: userInput }),
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            const data = await response.json();
            addToChat("AI: " + data.response);
            document.getElementById("user_input").value = ""; // Clear input field
        }
    });

    // Function to add a new message to the chat
    function addToChat(message) {
        const chatBox = document.getElementById("chat");
        const messageDiv = document.createElement("div");
        messageDiv.textContent = message;
        chatBox.appendChild(messageDiv);
        chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the latest message
    }

    // Function to fetch live news and crypto prices
    async function fetchLiveData() {
        try {
            // Fetch latest news from the backend
            const newsResponse = await fetch('/live-news');
            const newsData = await newsResponse.json();
            const newsContainer = document.getElementById("news");
            newsContainer.innerHTML = "<strong>Latest News:</strong><br>" + newsData.news.join("<br>");

            // Fetch latest crypto prices from the backend
            const cryptoResponse = await fetch('/crypto-prices');
            const cryptoData = await cryptoResponse.json();
            const cryptoContainer = document.getElementById("crypto");
            cryptoContainer.innerHTML = "<strong>Crypto Prices:</strong><br>" +
                `Bitcoin: ${cryptoData.prices.bitcoin} USD<br>` +
                `Ethereum: ${cryptoData.prices.ethereum} USD`;
        } catch (error) {
            console.error("Error fetching live data: ", error);
        }
    }
});
