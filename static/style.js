document.addEventListener("DOMContentLoaded", () => {
  const targets = [
    document.querySelector("#about.scroll-pop > .container"),
    ...document.querySelectorAll(".product-item.scroll-pop")
  ].filter(Boolean);

  if (!targets.length) return;

  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduceMotion) return;

  let frameRequested = false;

  function updateTargets() {
    const viewportCenter = window.innerHeight * 0.5;

    targets.forEach((element) => {
      const rect = element.getBoundingClientRect();
      const sectionCenter = rect.top + rect.height * 0.5;
      const travel = Math.max(viewportCenter + rect.height * 0.5, 1);
      const visibility = Math.max(0, 1 - Math.abs(viewportCenter - sectionCenter) / (travel * 1.6));
      const easedVisibility = visibility * visibility * (3 - 2 * visibility);
      const y = 24 * (1 - easedVisibility);
      const scale = 0.975 + easedVisibility * 0.025;

      element.style.transform = `translate3d(0, ${y.toFixed(2)}px, 0) scale(${scale.toFixed(4)})`;
    });

    frameRequested = false;
  }

  function requestUpdate() {
    if (frameRequested) return;
    frameRequested = true;
    window.requestAnimationFrame(updateTargets);
  }

  window.addEventListener("scroll", requestUpdate, { passive: true });
  window.addEventListener("resize", requestUpdate, { passive: true });
  requestUpdate();
});
