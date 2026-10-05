const DEFAULT_ENDPOINT = "http://127.0.0.1:8765/api/import";

chrome.runtime.onInstalled.addListener(() => {
  chrome.storage.sync.get({ endpoint: DEFAULT_ENDPOINT }, (data) => {
    if (!data.endpoint) {
      chrome.storage.sync.set({ endpoint: DEFAULT_ENDPOINT });
    }
  });
});

chrome.runtime.onMessage.addListener((message, _sender, sendResponse) => {
  if (message && message.type === "IMPORT_CHAT") {
    chrome.storage.sync.get({ endpoint: DEFAULT_ENDPOINT }, async (data) => {
      try {
        const res = await fetch(data.endpoint, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(message.payload),
        });
        const body = await res.json().catch(() => ({}));
        sendResponse({
          ok: res.ok,
          status: res.status,
          body,
        });
      } catch (err) {
        sendResponse({ ok: false, error: String(err) });
      }
    });
    return true;
  }
  return false;
});
