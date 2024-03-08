// translation.js
function switchLanguage(lang) {
    console.log("Switching language to:", lang);
    document.querySelectorAll("[data-key]").forEach(elem => {
      const key = elem.getAttribute("data-key");
      console.log("Translating element:", key);
      if (translations[lang] && translations[lang][key]) {
        elem.textContent = translations[lang][key];
        console.log("Translated:", key, "to", translations[lang][key]);
      } else {
        console.log("Translation missing for key:", key);
      }
    });
    document.documentElement.setAttribute('lang', lang); 
  }
  