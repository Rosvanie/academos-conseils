

//EN GENERAL
// Sélectionner uniquement les éléments avec la classe "section"
const sections = document.querySelectorAll('.section');

// Options de l'observateur
const options = {
  threshold: 0.1, // Déclenchement quand 10% de la section est visible
};

// Fonction de l'observateur
const sectionObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('in-view');
    } else {
      entry.target.classList.remove('in-view');
    }
  });
}, options);

// Observer chaque section ayant la classe "section"
sections.forEach(section => {
  sectionObserver.observe(section);
});





//recherche
  // Lorsque l'utilisateur tape dans la barre de recherche
  document.getElementById('search-input').addEventListener('input', function() {
    let query = this.value; // Récupère la valeur de la recherche
    let resultsContainer = document.getElementById('search-results'); // Conteneur pour afficher les résultats
    
    if (query.length > 0) {
        // Envoi d'une requête AJAX pour rechercher des éléments correspondant à la requête
        fetch(`/recherche/?q=${query}`)
            .then(response => response.json())
            .then(data => {
                // Si des résultats sont trouvés
                if (data.results && data.results.length > 0) {
                    resultsContainer.innerHTML = ''; // Réinitialise les résultats précédents
                    data.results.forEach(item => {
                        const resultItem = document.createElement('div');
                        resultItem.classList.add('result-item');
                        resultItem.innerHTML = `
                            <a href="/programme/${item.id}/"> <!-- Utilisation de item.id -->
                                <h4>${item.title}</h4>
                            </a>
                        `;
                        resultsContainer.appendChild(resultItem);
                    });
                } else {
                    resultsContainer.innerHTML = '<p>Aucun résultat trouvé.</p>';
                }
            })
            .catch(error => {
                resultsContainer.innerHTML = '<p>Erreur lors de la recherche.</p>';
                console.error('Erreur de recherche:', error);
            });
    } else {
        resultsContainer.innerHTML = ''; // Si la recherche est vide, on efface les résultats
    }
  });
  


//CARD POUR ACCUEIL

// Vérification du support d'IntersectionObserver
if ('IntersectionObserver' in window) {
    const cards = document.querySelectorAll('.card');
  
    // Création de l'observateur
    const cardObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const index = Array.from(cards).indexOf(entry.target);
          entry.target.classList.add('in-view');
          entry.target.style.animationDelay = `${index * 0.2}s`;
        } else {
          entry.target.classList.remove('in-view');
          entry.target.style.animationDelay = '0s';
        }
      });
    }, { threshold: 0.1 }); // Seuil ici directement
  
    // Observer chaque carte
    cards.forEach(card => cardObserver.observe(card));
  } else {
    console.warn('IntersectionObserver n’est pas supporté par ce navigateur.');
  }
  


  //CARD POUR SERVICES
  document.addEventListener("DOMContentLoaded", function () {
    const serviceCards = document.querySelectorAll(".service-card");
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                serviceCards.forEach((card, index) => {
                    setTimeout(() => {
                        card.classList.add("in-view");
                    }, index * 200); // Délai de 200 ms entre chaque carte
                });
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    // Observer la section contenant les cartes
    const gridSection = document.querySelector(".services-grid");
    observer.observe(gridSection);
});




//POP UP 
document.addEventListener("DOMContentLoaded", function() {
  // Récupérer la div de confirmation
  var popup = document.getElementById('confirmation-popup');

  // Si un message de succès est présent
  if (popup && popup.dataset.message) {
      // Mettre le message dans le popup
      popup.querySelector('p').textContent = popup.dataset.message;

      // Afficher le pop-up
      popup.classList.add('show');

      // Cache le pop-up après 3 secondes
      setTimeout(function() {
          popup.classList.remove('show');
      }, 3000); // 3 secondes
  }
});






//CARD POUR APROPOS

document.addEventListener("DOMContentLoaded", function () {
  const contentBlocks = document.querySelectorAll(".content-block");

  // Fonction pour observer et déclencher l'animation
  const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
          if (entry.isIntersecting) {
              entry.target.classList.add("in-view");
          } else {
              // On retire la classe pour que l'animation se déclenche de nouveau à chaque scroll
              entry.target.classList.remove("in-view");
          }
      });
  }, { threshold: 0.1 });

  // On observe chaque bloc
  contentBlocks.forEach(block => observer.observe(block));
});



// POUR CONTACT

document.addEventListener("DOMContentLoaded", function () {
  const sections = document.querySelectorAll(".contact-info, .form-section");

  // Fonction pour observer et animer les éléments
  const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
          if (entry.isIntersecting) {
              entry.target.classList.add("in-view");
          } else {
              // Retire la classe pour réactiver l'animation au prochain scroll
              entry.target.classList.remove("in-view");
          }
      });
  }, { threshold: 0.1 });

  // Observer chaque section
  sections.forEach(section => observer.observe(section));
});






//POUR LES THEMATIC

document.addEventListener('DOMContentLoaded', function () {
  const onglets = document.querySelectorAll('.onglet_left a');
  const tables = document.querySelectorAll('.formations-table-container');

  // Fonction pour activer un tableau selon l'onglet cliqué
  function activateTable(tabId) {
      tables.forEach(table => {
          table.classList.remove('active'); // Cacher tous les tableaux
          if (table.id === tabId) {
              table.classList.add('active'); // Montrer seulement le tableau correspondant
          }
      });
  }

  // Gestion des clics sur les onglets
  onglets.forEach(onglet => {
      onglet.addEventListener('click', (e) => {
          e.preventDefault();

          // Supprimer la classe active de tous les onglets
          onglets.forEach(o => o.classList.remove('active'));

          // Activer l'onglet actuel
          onglet.classList.add('active');

          // Activer le tableau correspondant
          const tabId = onglet.getAttribute('data-tab');
          activateTable(tabId);
      });
  });

  // Activer le premier onglet et tableau au chargement
  onglets[0].classList.add('active');
  activateTable(onglets[0].getAttribute('data-tab'));
});





//LES ONGET DU PROGRAM
function ouvrirOnglet(evt, ongletId) {
  var i, contenuOnglet, boutonsOnglet;

  contenuOnglet = document.getElementsByClassName("onglet-contenu");
  for (i = 0; i < contenuOnglet.length; i++) {
      contenuOnglet[i].style.display = "none";
      contenuOnglet[i].classList.remove("actif");
  }

  boutonsOnglet = document.getElementsByClassName("onglet-bouton");
  for (i = 0; i < boutonsOnglet.length; i++) {
      boutonsOnglet[i].classList.remove("actif");
  }

  document.getElementById(ongletId).style.display = "block";
  document.getElementById(ongletId).classList.add("actif");
  evt.currentTarget.classList.add("actif");
}


//pour la page programme
// Attendre que le DOM soit complètement chargé
document.addEventListener('DOMContentLoaded', () => {
  const formationContainer = document.getElementById('formation-container');
  const formationDetails = document.querySelector('.formation-details');
  const formationSummary = document.querySelector('.formation-summary');

  // Débuter l'animation
  formationContainer.style.opacity = 1; // Afficher le container

  // Attendre un court instant avant de lancer les animations des enfants
  setTimeout(() => {
      formationDetails.classList.add('animation');
      formationSummary.classList.add('animation');
  }, 100); // Délai avant le démarrage des animations
});



// POUR LLA PARTIE DETAILS

document.addEventListener("DOMContentLoaded", function () {
  const sections = document.querySelectorAll(".formation-section");

  sections.forEach((section) => {
      const heading = section.querySelector("h3");
      const icon = heading.querySelector(".toggle-icon");
      const contents = section.querySelectorAll(".toggle-content");

      heading.addEventListener("click", function () {
          // Utiliser une condition pour afficher/masquer les éléments de contenu
          contents.forEach(content => {
              if (content.style.display === "none" || content.style.display === "") {
                  content.style.display = "block";  // Afficher les éléments
                  icon.textContent = "-";          // Changer icône en '-'
              } else {
                  content.style.display = "none";   // Masquer les éléments
                  icon.textContent = "+";          // Changer icône en '+'
              }
          });
      });
  });
});




