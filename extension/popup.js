const DEFAULT_ENDPOINT = "http://127.0.0.1:8765/api/import";

const endpointInput = document.getElementById("endpoint");
const statusEl = document.getElementById("status");
const saveBtn = document.getElementById("save");

function setStatus(text, kind) {
  statusEl.textContent = text || "";
  statusEl.className = kind || "";
}

chrome.storage.sync.get({ endpoint: DEFAULT_ENDPOINT }, (data) => {
  endpointInput.value = data.endpoint || DEFAULT_ENDPOINT;
});

endpointInput.addEventListener("change", () => {
  chrome.storage.sync.set({ endpoint: endpointInput.value.trim() || DEFAULT_ENDPOINT });
});

function shareApiEndpoint(importEndpoint) {
  try {
    const u = new URL(importEndpoint || DEFAULT_ENDPOINT);
    u.pathname = "/api/share";
    return u.toString();
  } catch (_err) {
    return "http://127.0.0.1:8765/api/share";
  }
}

saveBtn.addEventListener("click", async () => {
  setStatus("Reading open chat…");
  saveBtn.disabled = true;
  try {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    if (!tab || !tab.id) {
      setStatus("No active tab.", "err");
      return;
    }
    const url = tab.url || "";
    if (!/https:\/\/(chatgpt\.com|chat\.openai\.com)\//.test(url)) {
      setStatus("Open a ChatGPT conversation or share tab first.", "err");
      return;
    }

    chrome.storage.sync.set({ endpoint: endpointInput.value.trim() || DEFAULT_ENDPOINT });

    // Public share tabs: let the local app fetch/parse the share URL (more reliable than DOM).
    if (/\/share\//.test(url)) {
      setStatus("Importing share link via local app…");
      const shareEndpoint = shareApiEndpoint(endpointInput.value.trim() || DEFAULT_ENDPOINT);
      const res = await fetch(shareEndpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url }),
      });
      const body = await res.json().catch(() => ({}));
      if (!res.ok) {
        setStatus(body.detail || "Share import failed", "err");
        return;
      }
      setStatus(`Saved ${body.filename || "note"} (${body.message_count || "?"} msgs)`, "ok");
      return;
    }

    let scrape;
    try {
      scrape = await chrome.tabs.sendMessage(tab.id, { type: "SCRAPE_CHAT" });
    } catch (_err) {
      await chrome.scripting.executeScript({
        target: { tabId: tab.id },
        files: ["content_script.js"],
      });
      scrape = await chrome.tabs.sendMessage(tab.id, { type: "SCRAPE_CHAT" });
    }

    if (!scrape || !scrape.ok) {
      setStatus((scrape && scrape.error) || "Could not read page.", "err");
      return;
    }

    const payload = scrape.payload || {};
    if (!(payload.messages || []).length && !payload.text) {
      setStatus("No messages found on this page.", "err");
      return;
    }

    const result = await chrome.runtime.sendMessage({
      type: "IMPORT_CHAT",
      payload,
    });

    if (!result || !result.ok) {
      setStatus(
        (result && (result.error || (result.body && result.body.detail))) ||
          "Local app not reachable. Run: chatgpt-obsidian-memory serve",
        "err"
      );
      return;
    }

    const body = result.body || {};
    if (body.saved === false) {
      setStatus("Preview only (auto-save off). Open the local UI to save.", "ok");
      return;
    }
    setStatus(`Saved ${body.filename || "note"}`, "ok");
  } catch (err) {
    setStatus(String(err), "err");
  } finally {
    saveBtn.disabled = false;
  }
});
