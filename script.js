// Smooth scrolling for navigation links including those with full URLs containing hash
document.querySelectorAll('a[href*="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    // Only handle this for same-page links or links to objectives.html
    const href = this.getAttribute('href');
    if (href.startsWith('#') || href.includes('objectives.html#')) {
      e.preventDefault();
      
      let targetId;
      if (href.startsWith('#')) {
        targetId = href; // Same page link like #objective1
      } else {
        // If we're already on the objectives page, extract just the hash part
        if (window.location.pathname.endsWith('objectives.html')) {
          targetId = href.substring(href.indexOf('#'));
        } else {
          // It's a link to objectives.html from another page, let the normal navigation happen
          return;
        }
      }
      
      const target = document.querySelector(targetId);
      if (target) {
        window.scrollTo({
          top: target.offsetTop - 70, // Adjust for sticky nav
          behavior: 'smooth'
        });
      }
    }
  });
});

// Contact form submission handler
document.getElementById("contactForm")?.addEventListener("submit", function (e) {
  e.preventDefault();
  const name = document.getElementById("name").value;
  const confirmationElement = document.getElementById("confirmation");
  
  confirmationElement.textContent = `Thanks, ${name}! Your message has been sent.`;
  confirmationElement.classList.add('show');
  
  // Reset the form
  this.reset();
  
  // Remove the confirmation message after 5 seconds
  setTimeout(() => {
    confirmationElement.classList.remove('show');
  }, 5000);
});

// Add fade-in effect when scrolling to sections
document.addEventListener('DOMContentLoaded', function() {
  const sections = document.querySelectorAll('section');
  
  function checkSections() {
    sections.forEach(section => {
      const sectionTop = section.getBoundingClientRect().top;
      const windowHeight = window.innerHeight;
      
      if (sectionTop < windowHeight * 0.75) {
        section.style.opacity = '1';
        section.style.transform = 'translateY(0)';
      } else {
        section.style.opacity = '0';
        section.style.transform = 'translateY(20px)';
      }
    });
  }
  
  // Set initial state
  sections.forEach(section => {
    section.style.opacity = '0';
    section.style.transform = 'translateY(20px)';
    section.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
  });
  
  // Check sections on load
  setTimeout(checkSections, 100);
  
  // Check sections on scroll
  window.addEventListener('scroll', checkSections);
});