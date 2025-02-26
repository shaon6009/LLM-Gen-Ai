let promptInput = document.querySelector("#prompt");
let submitBtn = document.querySelector("#submit");
let chatContainer = document.querySelector(".chat-container");

const DATA_FILE = "custom_data.txt";
let qaData = {}; 

async function loadQAData() {
    try {
        let response = await fetch(DATA_FILE);
        if (!response.ok) throw new Error("Failed to load the data file.");
        
        let text = await response.text();
        parseQAData(text);
    } catch (error) {
        console.error("Error loading Q&A data:", error);
    }
}

// Function to parse the text file into a dictionary
function parseQAData(text) {
    qaData = {};
    let lines = text.split("\n");
    
    for (let line of lines) {
        let [question, answer] = line.split("=");
        if (question && answer) {
            qaData[question.trim().toLowerCase()] = answer.trim();
        }
    }
}

// Function to generate a response based on custom Q&A data
function generateResponse(userMessage, aiChatBox) {
    let textElement = aiChatBox.querySelector(".ai-chat-area");

    let response = qaData[userMessage.toLowerCase()] || "Sorry, I don't have an answer for that.";
    textElement.innerHTML = response;
}

// Function to create chat bubbles
function createChatBox(html, classes) {
    let div = document.createElement("div");
    div.innerHTML = html;
    div.classList.add(classes);
    return div;
}

// Function to handle user input and generate a response
function handleChatResponse(userMessage) {
    if (!userMessage.trim()) return;
    
    let userHtml = `<img src="user.png" alt="User" width="8%">
        <div class="user-chat-area">${userMessage}</div>`;
    
    promptInput.value = "";
    let userChatBox = createChatBox(userHtml, "user-chat-box");
    chatContainer.appendChild(userChatBox);
    chatContainer.scrollTo({ top: chatContainer.scrollHeight, behavior: "smooth" });

    setTimeout(() => {
        let aiHtml = `<img src="ai.png" alt="AI" width="10%">
            <div class="ai-chat-area">
                <img src="loading.webp" alt="Loading" class="load" width="50px">
            </div>`;
        let aiChatBox = createChatBox(aiHtml, "ai-chat-box");
        chatContainer.appendChild(aiChatBox);
        generateResponse(userMessage, aiChatBox);
    }, 600);
}

// Event listeners
promptInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter") handleChatResponse(promptInput.value);
});

submitBtn.addEventListener("click", () => {
    handleChatResponse(promptInput.value);
});


loadQAData();
