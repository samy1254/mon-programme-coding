// Texte dynamique qui change dans le hero
const titres = [
  "Développeur Web 🌐",
  "Étudiant en Python 🐍",
  "Futur dev Android 📱",
  "Passionné de réseaux 🔒"
];

let indexTitre = 0;
let indexLettre = 0;
let effacement = false;
const element = document.getElementById("titre-dynamique");

function ecrire() {
  const titre = titres[indexTitre];
  if (!effacement) {
    element.textContent = titre.substring(0, indexLettre + 1);
    indexLettre++;
    if (indexLettre === titre.length) {
      effacement = true;
      setTimeout(ecrire, 2000);
      return;
    }
  } else {
    element.textContent = titre.substring(0, indexLettre - 1);
    indexLettre--;
    if (indexLettre === 0) {
      effacement = false;
      indexTitre = (indexTitre + 1) % titres.length;
    }
  }
  setTimeout(ecrire, effacement ? 50 : 100);
}
ecrire();

// Animation au scroll
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add("visible");
      const fill = entry.target.querySelector(".progress-fill");
      if (fill) {
        fill.style.width = fill.dataset.width + "%";
      }
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll(".skill-card, .timeline-item").forEach(el => {
  observer.observe(el);
});
