/**
 * DOM scrape helpers for the open ChatGPT conversation page.
 * Selectors are intentionally tolerant — ChatGPT UI changes often.
 * Falls back to large text blocks when structured turns are missing.
 */

function cleanText(value) {
  return (value || "").replace(/\u00a0/g, " ").replace(/[ \t]+\n/g, "\n").trim();
}

function detectRole(article) {
  const testId = (article.getAttribute("data-testid") || "").toLowerCase();
  if (testId.includes("user")) return "user";
  if (testId.includes("assistant") || testId.includes("bot")) return "assistant";

  const labeled = article.querySelector("[data-message-author-role]");
  if (labeled) {
    const role = (labeled.getAttribute("data-message-author-role") || "").toLowerCase();
    if (role === "user") return "user";
    if (role === "assistant" || role === "system") return role === "system" ? "system" : "assistant";
  }

  const heading = cleanText(
    (article.querySelector("h5, h6, [class*='font-semibold']") || {}).textContent || ""
  ).toLowerCase();
  if (heading.includes("you")) return "user";
  if (heading.includes("chatgpt") || heading.includes("assistant")) return "assistant";
  return "other";
}

function extractMessageText(article) {
  const markdown = article.querySelector(".markdown, .prose, [class*='markdown']");
  if (markdown) return cleanText(markdown.innerText || markdown.textContent);
  const content = article.querySelector("[data-message-author-role]");
  if (content) return cleanText(content.innerText || content.textContent);
  return cleanText(article.innerText || article.textContent);
}

function scrapeConversation() {
  const messages = [];
  const articles = Array.from(document.querySelectorAll("article, [data-testid^='conversation-turn']"));

  for (const article of articles) {
    const role = detectRole(article);
    if (role === "system") continue;
    const content = extractMessageText(article);
    if (!content) continue;
    // Avoid tiny chrome labels
    if (content.length < 2) continue;
    messages.push({ role: role === "other" ? "assistant" : role, content });
  }

  // Fallback: role-tagged nodes scattered in the tree
  if (!messages.length) {
    const nodes = document.querySelectorAll("[data-message-author-role]");
    nodes.forEach((node) => {
      const role = (node.getAttribute("data-message-author-role") || "").toLowerCase();
      if (role === "system") return;
      const content = cleanText(node.innerText || node.textContent);
      if (!content) return;
      messages.push({
        role: role === "user" ? "user" : "assistant",
        content,
      });
    });
  }

  let title =
    cleanText(document.title).replace(/\s*[-|•]\s*ChatGPT\s*$/i, "").trim() ||
    "Untitled Chat";

  const heading = document.querySelector("nav [aria-current='page'], main h1");
  if (heading) {
    const h = cleanText(heading.textContent);
    if (h) title = h;
  }

  return {
    title,
    url: location.href,
    messages,
    text: messages.map((m) => `${m.role}: ${m.content}`).join("\n\n"),
  };
}

chrome.runtime.onMessage.addListener((message, _sender, sendResponse) => {
  if (message && message.type === "SCRAPE_CHAT") {
    try {
      sendResponse({ ok: true, payload: scrapeConversation() });
    } catch (err) {
      sendResponse({ ok: false, error: String(err) });
    }
  }
  return true;
});
