/* Progressive enhancement: wallet handles amount, invoice checks and payment approval.
 * No wallet calls on load, third-party scripts, secret storage, or invoice proxies.
 */
(() => {
  "use strict";
  const section = document.getElementById("support");
  const status = document.getElementById("donation-status");
  if (!section || !status) return;
  const address = section.dataset.lightningAddress;
  let pending = false;

  section.querySelectorAll("[data-donation-link]").forEach((link) => {
    link.addEventListener("click", async (event) => {
      if (event.button !== 0 || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
      const provider = window.webln;
      // Optional API: leave the real lightning: link intact for other wallets.
      if (!provider || typeof provider.enable !== "function" || typeof provider.lnurl !== "function") return;
      event.preventDefault();
      event.stopPropagation();
      if (pending) return;
      pending = true;
      section.setAttribute("aria-busy", "true");
      status.textContent = "Choose an amount and confirm in your wallet.";
      try {
        await provider.enable();
        const result = await provider.lnurl(address);
        if (result && result.status === "OK" && result.data && result.data.preimage && result.data.paymentHash) {
          status.textContent = "Your wallet reports a completed payment. Thank you for supporting my work!";
        } else {
          status.textContent = "Payment was not confirmed here. Check your wallet before retrying, or use Open another wallet.";
        }
      } catch (_) {
        // Never retry a possibly completed payment or expose a provider's raw errors.
        status.textContent = "Payment was not completed here. Check your wallet before retrying, or use Open another wallet.";
      } finally {
        pending = false;
        section.removeAttribute("aria-busy");
      }
    });
  });

  const copy = document.getElementById("copy-lightning-address");
  if (copy) {
    copy.hidden = false;
    copy.addEventListener("click", async () => {
      try {
        await navigator.clipboard.writeText(address);
        status.textContent = "Lightning address copied. Paste it into your wallet to donate.";
      } catch (_) {
        status.textContent = "Copy is unavailable in this browser. Select and copy the Lightning address above.";
      }
    });
  }
})();
