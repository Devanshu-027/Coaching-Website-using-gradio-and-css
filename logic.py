import random

def get_response(message, history):
    """
    Simple rule-based chatbot logic for the Coaching Institute.
    In a real deployment, this could call an OpenAI API.
    """
    msg = message.lower()
    
    # 1. Greetings
    if any(word in msg for word in ["hello", "hi", "hey", "start"]):
        return "Hello! Welcome to Elite Coaching. I'm your AI assistant. How can I help you today? You can ask about courses, fees, or our results."

    # 2. Courses
    if "course" in msg or "class" in msg:
        return "We offer premium courses for JEE, NEET, and Foundation (Class 9-10). Our 'Elite Batch' guarantees personal mentorship. Would you like to know about the fee structure?"

    # 3. Fees
    if "fee" in msg or "cost" in msg or "price" in msg:
        return "Our premium courses start at $2,000/year. We believe in value-driven education. We also offer merit-based scholarships up to 100%. Visit the 'Courses' tab for detailed pricing."

    # 4. Results / Success
    if "result" in msg or "selection" in msg:
        return "We have a 45% selection ratio in top institutes, which is 5x the industry average. Last year, 120 of our students cracked IIT JEE Advanced."

    # 5. Contact
    if "contact" in msg or "call" in msg or "location" in msg:
        return "You can visit us at our flagship center in Tech Park, or call us at +1-800-ELITE-EDU. The 'Contact' tab has a map and form."

    # Default fallback
    fallback_responses = [
        "That's a great question. Could you clarify a bit more?",
        "I specialize in answering questions about our institute. Ask me about courses or results!",
        "Our team is also available on WhatsApp for specific queries. Check the Contact page."
    ]
    return random.choice(fallback_responses)
