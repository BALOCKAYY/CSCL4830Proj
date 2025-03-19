// Wait for the document to fully load
document.addEventListener("DOMContentLoaded", function() {
  // Highlight the active navigation link on click
  const navLinks = document.querySelectorAll("header nav a");

  navLinks.forEach(link => {
    link.addEventListener("click", function(event) {
      // Remove active class from all links
      navLinks.forEach(l => l.classList.remove("active"));
      // Add active class to the clicked link
      event.target.classList.add("active");
    });
  });
});

