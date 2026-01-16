import gradio as gr
from logic import get_response
import os

# Load custom CSS
css = open("style.css").read()

# --- Content Data ---

def get_hero_html():
    return """
    <div style="text-align: center; padding: 4rem 0;">
        <h1 class="hero-text">ELITE COACHING<br>INSTITUTE</h1>
        <p class="hero-subtext">Forging Champions. Defining Futures.</p>
        <div style="display: flex; justify-content: center; gap: 1rem;">
            <button class="cta-button">Explore Courses</button>
            <button class="cta-button" style="background: transparent; border: 1px solid rgba(255,255,255,0.3);">Book Demo</button>
        </div>
    </div>
    """

def get_stats_html():
    return """
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem; margin-top: 3rem;">
        <div class="glass-card" style="text-align: center;">
            <div class="stat-number">45%</div>
            <div class="stat-label">Selection Ratio</div>
        </div>
        <div class="glass-card" style="text-align: center;">
            <div class="stat-number">120+</div>
            <div class="stat-label">IIT JEE Selections</div>
        </div>
        <div class="glass-card" style="text-align: center;">
            <div class="stat-number">15+</div>
            <div class="stat-label">Years Excellence</div>
        </div>
    </div>
    """

def get_about_html():
    return """
    <div class="glass-card">
        <h2>Our Philosophy</h2>
        <p style="font-size: 1.1rem; line-height: 1.6; color: var(--text-muted);">
            At Elite Coaching, we don't just teach; we transform. Our curriculum is designed by ex-IITians and industry leaders to foster critical thinking, not just rote memorization. We believe every student has the potential to be a ranker with the right guidance.
        </p>
    </div>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin-top: 2rem;">
        <div class="glass-card">
            <h3>Mission</h3>
            <p>To provide accessible, high-quality education that bridges the gap between potential and performance.</p>
        </div>
        <div class="glass-card">
            <h3>Vision</h3>
            <p>To be the global benchmark for competitive exam preparation and holistic student development.</p>
        </div>
    </div>
    """

def get_course_card(title, price, features):
    feature_list = "".join([f"<li style='margin-bottom: 0.5rem;'>✓ {f}</li>" for f in features])
    return f"""
    <div class="glass-card" style="display: flex; flex-direction: column; height: 100%;">
        <h3 style="color: var(--accent-color); margin-bottom: 0.5rem;">{title}</h3>
        <div style="font-size: 2rem; font-weight: 700; margin-bottom: 1.5rem;">{price}</div>
        <ul style="list-style: none; padding: 0; color: var(--text-muted); flex-grow: 1; margin-bottom: 2rem;">
            {feature_list}
        </ul>
        <button class="cta-button" style="width: 100%;">Enroll Now</button>
    </div>
    """

# --- Main App ---

with gr.Blocks(css=css, title="KAVITA COACHING CLASSES", theme=gr.themes.Glass()) as demo:
    
    # State for navigation
    page_state = gr.State("home")

    # --- Navbar ---
    with gr.Row(elem_classes="glass-card", elem_id="nav-bar"):
        with gr.Column(scale=1):
            gr.HTML("<h3 style='margin:0; padding-top: 5px;'>ELITE.</h3>")
        with gr.Column(scale=4):
            with gr.Row():
                btn_home = gr.Button("Home", elem_classes="nav-button")
                btn_about = gr.Button("About Us", elem_classes="nav-button")
                btn_courses = gr.Button("Courses", elem_classes="nav-button")
                btn_contact = gr.Button("Contact & AI", elem_classes="nav-button")

    # --- Pages ---

    # 1. Home Page
    with gr.Column(visible=True) as home_col:
        gr.HTML(get_hero_html())
        gr.HTML(get_stats_html())
    
    # 2. About Page
    with gr.Column(visible=False) as about_col:
        gr.Markdown("# About Us", elem_classes="hero-text")
        gr.HTML(get_about_html())
        
        with gr.Row(elem_classes="glass-card"):
             gr.Markdown("### Faculty Highlights\n\n* **Dr. A. Sharma** - PhD Physics (20 Yrs Exp)\n* **Prof. K. Verma** - Ex-IIT Kanpur (Maths Wizard)\n* **Ms. S. Gupta** - NEET Specialist")

    # 3. Courses Page
    with gr.Column(visible=False) as courses_col:
        gr.Markdown("# Our Premium Courses", elem_classes="hero-text")
        with gr.Row():
            gr.HTML(get_course_card("JEE Advanced", "$2,500/yr", ["Daily Live Classes", "1-on-1 Mentorship", "Hardcopy Material", "24/7 Doubt Support"]))
            gr.HTML(get_course_card("NEET Medical", "$2,200/yr", ["NCERT Focused", "Biology Labs", "Weekly Mock Tests", "AI Performance Analysis"]))
            gr.HTML(get_course_card("Foundation (9-10)", "$1,500/yr", ["Olympiad Prep", "School Syllabus", "Logic Building", "Coding Basics"]))

    # 4. Contact & AI Page
    with gr.Column(visible=False) as contact_col:
        gr.Markdown("# Contact & Support", elem_classes="hero-text")
        
        with gr.Row():
            with gr.Column(scale=1):
                gr.Markdown("""
                ### Get in Touch
                
                **Address:**  
                Elite Tower, Knowledge Park III,  
                Tech City, CA 90210
                
                **Phone:**  
                +1 (800) ELITE-EDU
                
                **Email:**  
                admissions@elitecoaching.com
                """)
                # Placeholder for map
                gr.HTML("<div class='glass-card' style='height: 200px; display: flex; align-items: center; justify-content: center; background: rgba(0,0,0,0.3);'>Google Map Placeholder</div>")
                
                # Contact Form
                with gr.Group():
                    gr.Markdown("### Send a Message")
                    name_input = gr.Textbox(label="Name", placeholder="John Doe", elem_classes="glass-card")
                    email_input = gr.Textbox(label="Email", placeholder="john@example.com", elem_classes="glass-card")
                    msg_input = gr.Textbox(label="Message", lines=3, elem_classes="glass-card")
                    submit_contact = gr.Button("Send Message", elem_classes="cta-button")
                    contact_output = gr.Markdown()

            # AI Chatbot Section
            with gr.Column(scale=1, elem_classes="glass-card"):
                gr.Markdown("### 🤖 Elite AI Assistant")
                # Removed type="messages" to support standard format or fix 6.0 compatibility
                chatbot = gr.Chatbot(label="Chat with us", height=400) 
                msg = gr.Textbox(label="Ask about fees, courses, or results...", placeholder="Type here...", elem_classes="glass-card")
                clear = gr.Button("Clear Chat", elem_classes="nav-button")

                def user(user_message, history):
                    # Standard Gradio format: history is list of [user_msg, bot_msg]
                    return "", history + [[user_message, None]]

                def bot(history):
                    if not history:
                        return history
                    user_message = history[-1][0]
                    # Logic expects string message and history list
                    bot_message = get_response(user_message, history[:-1]) 
                    history[-1][1] = bot_message
                    return history

                msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
                    bot, chatbot, chatbot
                )
                clear.click(lambda: None, None, chatbot, queue=False)
                
                # Simple contact form logic
                def submit_form(n, e, m):
                    return f"Thanks {n}! We have received your message and will contact {e} shortly."
                
                submit_contact.click(submit_form, [name_input, email_input, msg_input], contact_output)

    # --- Navigation Logic ---
    def nav_home(): return [gr.update(visible=True), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False)]
    def nav_about(): return [gr.update(visible=False), gr.update(visible=True), gr.update(visible=False), gr.update(visible=False)]
    def nav_courses(): return [gr.update(visible=False), gr.update(visible=False), gr.update(visible=True), gr.update(visible=False)]
    def nav_contact(): return [gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=True)]

    btn_home.click(nav_home, None, [home_col, about_col, courses_col, contact_col])
    btn_about.click(nav_about, None, [home_col, about_col, courses_col, contact_col])
    btn_courses.click(nav_courses, None, [home_col, about_col, courses_col, contact_col])
    btn_contact.click(nav_contact, None, [home_col, about_col, courses_col, contact_col])

# Launch the app
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=5000)
