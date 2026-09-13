const form = document.getElementById("askForm");
const questionInput = document.getElementById("question");
const askButton = document.getElementById("askButton");
const answer = document.getElementById("answer");
const result = document.getElementById("result");
const welcome = document.getElementById("welcome");
const loading = document.getElementById("loading");
const error = document.getElementById("error");
const concepts = document.getElementById("concepts");
const conceptCount = document.getElementById("conceptCount");
const apiKey = document.getElementById("apiKey");
const connectionStatus = document.getElementById("connectionStatus");
const apiUrl = window.location.hostname === "127.0.0.1" || window.location.hostname === "localhost"
    ? "http://127.0.0.1:8000"
    : window.location.origin;

form.addEventListener("submit", (event) => {
    event.preventDefault();
    askQuestion();
});

document.querySelectorAll(".suggestion").forEach((button) => {
    button.addEventListener("click", () => {
        questionInput.value = button.dataset.question;
        askQuestion();
    });
});

async function askQuestion() {
    const question = questionInput.value.trim();
    if (!question) {
        showError("Write a question before sending it to the agent.");
        questionInput.focus();
        return;
    }

    setLoading(true);
    hideError();
    const headers = { "Content-Type": "application/json" };
    if (apiKey.value.trim()) headers["X-Groq-API-Key"] = apiKey.value.trim();

    try {
        const response = await fetch(`${apiUrl}/api/ask`, {
            method: "POST",
            headers,
            body: JSON.stringify({ question }),
        });
        const data = await response.json();
        if (!response.ok || !data.success) {
            throw new Error(data.detail || data.error || "The agent could not answer that question.");
        }
        displayResult(data);
        connectionStatus.classList.add("connected");
        connectionStatus.innerHTML = "<span></span> Connected";
    } catch (requestError) {
        showError(requestError.message || "Could not connect to the backend.");
    } finally {
        setLoading(false);
    }
}

function displayResult(data) {
    welcome.hidden = true;
    result.hidden = false;
    answer.innerHTML = renderMarkdown(data.answer || "No answer returned.");
    const items = data.knowledge?.concepts || [];
    conceptCount.textContent = items.length;
    concepts.innerHTML = items.length
        ? items.map((item) => `<div class="concept-item"><span>${escapeHtml(item.title || item.id)}</span></div>`).join("")
        : '<p class="empty-state">No matching concepts found.</p>';
}

function setLoading(isLoading) {
    loading.hidden = !isLoading;
    askButton.disabled = isLoading;
    askButton.querySelector("span:first-child").textContent = isLoading ? "Thinking" : "Ask agent";
    if (isLoading) result.hidden = true;
}

function showError(message) {
    error.textContent = message;
    error.hidden = false;
}

function hideError() {
    error.hidden = true;
}

function escapeHtml(value) {
    return String(value).replace(/[&<>'"]/g, (character) => ({
        "&": "&amp;", "<": "&lt;", ">": "&gt;", "'": "&#39;", '"': "&quot;",
    }[character]));
}

function renderMarkdown(markdown) {
    const lines = String(markdown).replace(/\r/g, "").split("\n");
    let html = "";
    let inList = false;
    let listType = "ul";
    const closeList = () => {
        if (inList) { html += `</${listType}>`; inList = false; }
    };

    lines.forEach((line) => {
        const trimmed = line.trim();
        const heading = trimmed.match(/^(#{1,3})\s+(.+)$/);
        const bullet = trimmed.match(/^[-*+]\s+(.+)$/);
        const ordered = trimmed.match(/^\d+[.)]\s+(.+)$/);
        if (!trimmed) { closeList(); return; }
        if (heading) { closeList(); html += `<h${heading[1].length}>${inlineMarkdown(heading[2])}</h${heading[1].length}>`; return; }
        if (bullet || ordered) {
            const nextType = bullet ? "ul" : "ol";
            if (!inList || listType !== nextType) { closeList(); listType = nextType; html += `<${listType}>`; inList = true; }
            html += `<li>${inlineMarkdown((bullet || ordered)[1])}</li>`;
            return;
        }
        closeList();
        html += `<p>${inlineMarkdown(trimmed)}</p>`;
    });
    closeList();
    return html;
}

function inlineMarkdown(value) {
    let safe = escapeHtml(value);
    safe = safe.replace(/`([^`]+)`/g, "<code>$1</code>");
    safe = safe.replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>");
    safe = safe.replace(/__([^_]+)__/g, "<strong>$1</strong>");
    safe = safe.replace(/\*([^*]+)\*/g, "<em>$1</em>");
    return safe;
}
