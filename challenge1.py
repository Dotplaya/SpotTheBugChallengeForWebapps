# Challenge:
# You are conducting a code review for a messaging application. Your task is to identify and address any vulnerabilities in the codebase.
@app.route("/messages/send", methods=["POST"])
def send_message():
    recipient_id = request.form.get("recipient_id")
    message_content = request.form.get("content")
    
    recipient = get_user(recipient_id)
    if recipient is None:
        return "Recipient not found."
    
    sender = get_current_user()
    if sender is None:
        return "User not authenticated."

    message = create_message(sender.id, recipient_id, message_content)
    if message is None:
        return "Failed to send message."

    return "Message sent successfully."
