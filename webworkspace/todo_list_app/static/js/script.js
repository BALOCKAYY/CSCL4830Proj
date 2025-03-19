// script.js

document.addEventListener("DOMContentLoaded", function() {
  // Highlight active navigation link when clicked
  const navLinks = document.querySelectorAll("header nav a");
  navLinks.forEach(link => {
    link.addEventListener("click", function(event) {
      navLinks.forEach(l => l.classList.remove("active"));
      event.target.classList.add("active");
    });
  });

  // Confirm deletion for each delete link in the to-do table
  const deleteLinks = document.querySelectorAll(".todo-table a[href*='delete_todo']");
  deleteLinks.forEach(link => {
    link.addEventListener("click", function(event) {
      if (!confirm("Are you sure you want to delete this to-do item?")) {
        event.preventDefault();
      }
    });
  });
});

