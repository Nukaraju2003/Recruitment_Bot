questions = [
    "Let's start with your name. What shall I call you?",
    "Please upload your resume"
]
responses = []

function greet() {
    botMessage("Hey! I'm HireeeeeeeBot, and I'm looking forward to know more about you!");
}

function botMessage(msg) {
    const chatWindow = document.getElementById('chatwindow');

    if (msg === "Please upload your resume") {
        const newDialogue = document.createElement("div");
        newDialogue.className = "row mt-2 bot_dialogue";
        newDialogue.innerHTML =
        `
        <div class="col-auto pt-4">
        <div class="row no-gutters">
        <div class="col-auto">
            <img src="/static/Assets/bot_bubble.svg" height="15px" width="15px">
        </div>
        <div class="col-auto">
            <div class="dialogue bot">
                <p>${msg}</p>
                <input type="file" id="resumeUpload" accept=".pdf" onchange="handleResumeUpload(this)">
            </div>
        </div>
        </div>
        </div>`;
        chatWindow.appendChild(newDialogue);
    } else {
        const dialogueTemplate = document.getElementsByClassName("row mt-2 bot_dialogue")[0];
        const newDialogue = dialogueTemplate.cloneNode(true);
        newDialogue.getElementsByClassName("dialogue bot")[0].innerText = msg.toString();
        chatWindow.appendChild(newDialogue);
    }
}

function userMessage (msg) {
    chatWindow = document.getElementById('chatwindow');
    dialogueTemplate = document.getElementsByClassName("row mt-2 justify-content-end user_dialogue")[0];
    newDialogue = dialogueTemplate.cloneNode(true);
    newDialogue.getElementsByClassName("dialogue user")[0].innerText = msg.toString();
    chatWindow.appendChild(newDialogue);
    newDialogue.scrollIntoView();
}

function sendMessage () {
    input = document.getElementById("msginput");
    msg = input.value
    if (msg != "") {
        input.value = "";
        userMessage(msg);
        responses.push(msg.toString());
        if (responses.length > questions.length) {
        } else {
            botMessage(questions[responses.length-1]);
        }
    }
}

