let promptInput = document.querySelector("#prompt");
let submitBtn = document.querySelector("#submit");
let chatContainer = document.querySelector(".chat-container");
let imageBtn = document.querySelector("#image");
let image = document.querySelector("#image img");
let imageInput = document.querySelector("#image input");

const API_URL = "https://www.low-taxes.com/"; 

let user = {
    message: null,
    file: {
        mime_type: null,
        data: null
    }
};

async function generateResponse(aiChatBox) {
    let textElement = aiChatBox.querySelector(".ai-chat-area");
    let requestBody = {
        question: user.message,
        file: user.file.data ? { mime_type: user.file.mime_type, data: user.file.data } : null
    };

    let requestOptions = {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(requestBody)
    };

    try {
        let response = await fetch(API_URL, requestOptions);
        let data = await response.json();
        let apiResponse = data.answer || "Sorry, I couldn't fetch an answer.";
        textElement.innerHTML = apiResponse;
    } catch (error) {
        console.error("Error fetching response:", error);
        textElement.innerHTML = "Something went wrong. Please try again.";
    } finally {
        chatContainer.scrollTo({ top: chatContainer.scrollHeight, behavior: "smooth" });
        image.src = `img.svg`;
        image.classList.remove("choose");
        user.file = { mime_type: null, data: null };
    }
}

function createChatBox(html, classes) {
    let div = document.createElement("div");
    div.innerHTML = html;
    div.classList.add(classes);
    return div;
}

function handleChatResponse(userMessage) {
    if (!userMessage.trim()) return;
    
    user.message = userMessage;
    let userHtml = `<img src="user.png" alt="User" width="8%">
        <div class="user-chat-area">
            ${user.message}
            ${user.file.data ? `<img src="data:${user.file.mime_type};base64,${user.file.data}" class="chooseimg" />` : ""}
        </div>`;
    
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
        generateResponse(aiChatBox);
    }, 600);
}

promptInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
        handleChatResponse(promptInput.value);
    }
});

submitBtn.addEventListener("click", () => {
    handleChatResponse(promptInput.value);
});

imageInput.addEventListener("change", () => {
    const file = imageInput.files[0];
    if (!file) return;
    
    let reader = new FileReader();
    reader.onload = (e) => {
        let base64string = e.target.result.split(",")[1];
        user.file = {
            mime_type: file.type,
            data: base64string
        };
        image.src = `data:${user.file.mime_type};base64,${user.file.data}`;
        image.classList.add("choose");
    };
    reader.readAsDataURL(file);
});

imageBtn.addEventListener("click", () => {
    imageInput.click();
});
