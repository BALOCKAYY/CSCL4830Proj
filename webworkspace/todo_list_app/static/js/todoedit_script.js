document.addEventListener("DOMContentLoaded", function() {
    console.log("Page Loaded - JavaScript Running ✅");

    const todoInput = document.querySelector("input[name='todo']");
    const dueInput = document.querySelector("input[name='due']");
    const deleteLinks = document.querySelectorAll(".btn-delete");

    // ✅ Function to check for error messages
    function checkForErrorMessage() {
        const errorMessages = document.querySelectorAll(".error-message");
        if (errorMessages.length > 0) {
            console.log("🚀 Error message(s) found: ", errorMessages.length);
            return errorMessages;
        } else {
            console.log("❌ No error messages found in DOM.");
            return null;
        }
    }

    // ✅ Function to remove error messages when user types
    function removeErrorMessage() {
        console.log("User is typing... ✅");
        let errorMessages = checkForErrorMessage();
        if (errorMessages) {
            console.log("✅ Removing error messages now!");
            errorMessages.forEach(msg => msg.remove());
        } else {
            console.log("❌ Still no error messages to remove.");
        }
    }

    // ✅ Attach event listeners to inputs for removing errors
    if (todoInput) {
        console.log("To-Do input detected ✅");
        todoInput.addEventListener("input", removeErrorMessage);
        todoInput.addEventListener("focus", removeErrorMessage);
    } else {
        console.log("Error: To-Do input not found ❌");
    }

    if (dueInput) {
        console.log("Due input detected ✅");
        dueInput.addEventListener("input", removeErrorMessage);
        dueInput.addEventListener("focus", removeErrorMessage);
    } else {
        console.log("Error: Due input not found ❌");
    }

    // ✅ Function to get CSRF token for secure requests
    function getCSRFToken() {
        return document.querySelector("[name=csrfmiddlewaretoken]").value;
    }

    // ✅ Handle Delete Functionality (AJAX)
    deleteLinks.forEach(link => {
        link.addEventListener("click", function(event) {
            event.preventDefault(); // Prevent page reload

            if (!confirm("Are you sure you want to delete this To-Do?")) {
                return;
            }

            const todoId = link.getAttribute("data-todo-id");
            fetch(link.href, {
                method: "POST",
                headers: {
                    "X-CSRFToken": getCSRFToken(),
                    "X-Requested-With": "XMLHttpRequest"
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === "success") {
                    console.log(`✅ To-Do ${todoId} Deleted Successfully`);
                    if (link.closest("tr")) {
                        link.closest("tr").remove(); // ✅ Remove row in `todo_edit.html`
                    } else if (link.closest(".todo-item")) {
                        link.closest(".todo-item").remove(); // ✅ Remove item in `todo_info.html`
                    }
                } else {
                    console.error("❌ Error Deleting To-Do:", data.message);
                }
            })
            .catch(error => console.error("❌ Request Failed:", error));
        });
    });
});

