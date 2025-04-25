document
  .getElementById("send-button")
  .addEventListener("click", async function () {
    const userMessage = document.querySelector('input[type="text"]').value;

    if (userMessage.trim() !== "") {
      // Create and add the sender label ("You")
      const senderLabel = document.createElement("div");
      senderLabel.classList.add("sender-label");
      senderLabel.textContent = "You"; // Add the label "You"

      // Create and add the actual user message
      const messageDiv = document.createElement("div");
      messageDiv.classList.add("user-message");
      messageDiv.textContent = userMessage;

      // Append the sender label and the message directly to the chat-messages container
      document.querySelector(".chat-messages").appendChild(senderLabel);
      document.querySelector(".chat-messages").appendChild(messageDiv);

      // Scroll to the latest message with smooth behavior
      scrollToBottom();

      // Clear the input field
      document.querySelector('input[type="text"]').value = "";

      // Scroll to the latest message
      scrollToBottom();

      // Remove any previous typing animation before adding a new one
      const existingTypingDiv = document.querySelector(".bot-thinking");
      if (existingTypingDiv) {
        existingTypingDiv.remove();
      }

      // Display "Chatbot is thinking..." animation
      const botThinkingDiv = document.createElement("div");
      botThinkingDiv.classList.add("bot-thinking");
      botThinkingDiv.textContent = "typing...";
      document.querySelector(".chat-messages").appendChild(botThinkingDiv);

      try {
        console.log("Sending message to the backend:", userMessage); // Debug: log the user's message

        // Send the user's message to the Flask backend using application/x-www-form-urlencoded format
        const response = await fetch("/questions", {
          method: "POST",
          headers: {
            "Content-Type": "application/x-www-form-urlencoded", // Send data as form-encoded
          },
          body: new URLSearchParams({
            user_input: userMessage, // Send the user input as form data
          }),
        });

        console.log("Response status:", response.status); // Debug: log the response status

        if (!response.ok) {
          throw new Error("Network response was not ok");
        }

        const data = await response.json(); // Parse the JSON response

        console.log("Response data:", data); // Debug: log the response data

        if (data.error) {
          throw new Error(data.error); // Handle any error from the API
        }

        // Remove the "Chatbot is thinking..." animation
        const botThinkingDivAfter = document.querySelector(".bot-thinking");
        if (botThinkingDivAfter) {
          botThinkingDivAfter.remove();
        }

        // Process the bot response
        const botMessageDiv = document.createElement("div");
        botMessageDiv.classList.add("bot-message-container"); // Create a container for the message and label

        // Create and add the sender label ("HRA-chatbot")
        const senderLabel = document.createElement("div");
        senderLabel.classList.add("sender-label");
        senderLabel.textContent = "HRA-chatbot"; // Add the label "HRA-chatbot"

        // Create and add the actual bot message
        const messageDiv = document.createElement("div");
        messageDiv.classList.add("bot-message");
        // Format the bot's response using the formatMessage function
        messageDiv.innerHTML = formatMessage(data.response); // Use innerHTML to insert the formatted message
        // Append the label and the message to the container
        botMessageDiv.appendChild(senderLabel);
        botMessageDiv.appendChild(messageDiv);

        // Append the container to the chat-messages container
        document.querySelector(".chat-messages").appendChild(botMessageDiv);

        // Scroll to the latest message with smooth behavior
        scrollToBottom();
      } catch (error) {
        console.error("Error:", error); // Debug: log the error if fetch fails

        // Show an error message if the fetch request fails
        const botErrorDiv = document.createElement("div");
        botErrorDiv.classList.add("bot-message");
        botErrorDiv.textContent = "Sorry, there was an issue with the server.";
        document.querySelector(".chat-messages").appendChild(botErrorDiv);
      }
    }
  });

function goBack() {
  window.history.back(); // This takes the user back to the previous page
}

function scrollToBottom() {
  const chatBox = document.querySelector(".chat-box");

  // Wait for the next event loop (to ensure the DOM is updated)
  setTimeout(() => {
    chatBox.scrollTo({
      top: chatBox.scrollHeight,
      behavior: "smooth", // Enable smooth scrolling
    });
  }, 100); // 100ms delay
}

// Optional: Allow the Enter key to send the message
document
  .querySelector('input[type="text"]')
  .addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
      document.getElementById("send-button").click();
    }
  });

// Initialize the bot with a greeting message after a 1.5-second delay
document.addEventListener("DOMContentLoaded", function () {
  // Delay the greeting message by 1.5 seconds
  setTimeout(function () {
    // Create a container for the bot's message and label
    const botMessageDiv = document.createElement("div");
    botMessageDiv.classList.add("bot-message-container"); // Container for message and label

    // Create and add the sender label ("HRA-chatbot")
    const senderLabel = document.createElement("div");
    senderLabel.classList.add("sender-label");
    senderLabel.textContent = "HRA-chatbot"; // Add the label "HRA-chatbot"

    // Create and add the actual bot message
    const messageDiv = document.createElement("div");
    messageDiv.classList.add("bot-message");
    // Format the bot's response using the formatMessage function
    messageDiv.innerHTML = formatMessage(
      "Hello! 👋, I am here to answer questions about HRA queries, how can I help you?😊"
    ); // Use innerHTML to insert the formatted message

    // Append the label and the message to the container
    botMessageDiv.appendChild(senderLabel);
    botMessageDiv.appendChild(messageDiv);

    // Append the bot message container to the chat-messages container
    document.querySelector(".chat-messages").appendChild(botMessageDiv);

    // Scroll to the latest message
    document.querySelector(".chat-box").scrollTo({
      top: document.querySelector(".chat-box").scrollHeight,
      behavior: "smooth", // This enables smooth scrolling
    });
  }, 1500); // 1.5 second delay
});

function formatMessage(message) {
  // Step 1: Bold and capitalize words inside **...**
  message = message.replace(/\*\*([^*]+)\*\*/g, (match, p1) => {
    return `<strong>${p1.toUpperCase()}</strong>`; // Capitalize and bold the text
  });

  // Step 2: Handle bullet points
  // Split the message by newlines and treat only lines starting with '*' as bullet points
  message = message
    .split("\n")
    .map((line) => {
      if (line.trim().startsWith("*")) {
        // Convert lines starting with '*' to list items
        return `<li>${line.replace(/^\*+/g, "").trim()}</li>`; // Remove the leading '*' and trim extra spaces
      }
      return line; // Leave other lines as is
    })
    .join("<br>"); // Join the lines with <br> to preserve line breaks

  // Wrap the bullet points in <ul> tag (only those that were converted to <li>)
  message = message
    .replace(/<li>/g, "<ul><li>")
    .replace(/<\/li>/g, "</li></ul>");

  // Step 3: Additional formatting (for links, breaks, etc.)
  message = message.replace(
    /(https?:\/\/[^\s]+)/g,
    '<a href="$1" target="_blank">Click here</a>'
  );

  return message;
}
