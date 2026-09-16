document.addEventListener("DOMContentLoaded", function () {
  const scrollTargets = [
    document.querySelector("#about.scroll-pop > .container"),
    ...document.querySelectorAll(".product-item.scroll-pop")
  ].filter(Boolean);

  function animateSectionsOnScroll() {
    scrollTargets.forEach(function (content) {
      const rect = content.getBoundingClientRect();
      const viewportCenter = window.innerHeight / 2;
      const sectionCenter = rect.top + rect.height / 2;

      const distance = Math.abs(viewportCenter - sectionCenter);
      const maximumDistance = (viewportCenter + rect.height / 2) * 1.6;

      const rawVisibility = Math.max(0, 1 - distance / maximumDistance);
      const movement = 35 * (1 - rawVisibility);
      const scale = 0.94 + rawVisibility * 0.06;

      content.style.transform =
        `translateY(${movement}px) scale(${scale})`;
    });
  }

  window.addEventListener("scroll", animateSectionsOnScroll, { passive: true });
  window.addEventListener("resize", animateSectionsOnScroll);

  animateSectionsOnScroll();
});