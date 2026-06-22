import streamlit as st
import time

# إعدادات الصفحة
st.set_page_config(page_title="A.Mansour | AI Engineer", page_icon="🧠", layout="wide")

# تصميم CSS مخصص - ثيم الذكاء الاصطناعي الحديث (Glassmorphism)
st.markdown("""
<style>
    /* استدعاء خط عصري جداً للتكنولوجيا */
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Space Grotesk', sans-serif;
    }

    /* خلفية التطبيق: تدرج لوني يعبر عن التكنولوجيا العميقة */
    .stApp {
        background: radial-gradient(circle at top right, #1a1025 0%, #0b0f19 50%, #020617 100%);
        color: #e2e8f0;
    }

    /* تصميم القائمة الجانبية */
    [data-testid="stSidebar"] {
        background-color: rgba(11, 15, 25, 0.8) !important;
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(255, 255, 255, 0.05);
    }

    /* العناوين والتدرج اللوني (Cyan to Purple) */
    h1, h2, h3 {
        color: #ffffff !important;
        font-weight: 700 !important;
    }
    
    .gradient-text {
        background: linear-gradient(90deg, #00f2fe 0%, #4facfe 50%, #bc13fe 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
    }

    /* كروت المشاريع (تأثير الزجاج الذكي) */
    .glass-card { 
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .glass-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0, 242, 254, 0.15);
        border: 1px solid rgba(0, 242, 254, 0.3);
    }
    .glass-card h3 { 
        margin-top: 0; 
        color: #00f2fe !important;
        font-size: 1.3rem;
    }
    .glass-card p { 
        color: #94a3b8; 
        font-size: 0.95rem; 
        line-height: 1.6;
    }

    /* فقاعات المهارات (أزرار مضيئة) */
    .skill-badge { 
        display: inline-block; 
        background: linear-gradient(90deg, rgba(79, 172, 254, 0.1) 0%, rgba(0, 242, 254, 0.1) 100%);
        color: #00f2fe; 
        border: 1px solid rgba(0, 242, 254, 0.3);
        padding: 8px 16px; 
        border-radius: 30px; 
        margin: 5px; 
        font-size: 14px; 
        font-weight: 600;
        transition: all 0.3s;
    }
    .skill-badge:hover {
        background: linear-gradient(90deg, #4facfe 0%, #00f2fe 100%);
        color: #000;
        box-shadow: 0 0 15px rgba(0, 242, 254, 0.4);
    }

    /* أزرار الروابط العامة */
    .stButton>button { 
        background: transparent;
        color: #e2e8f0; 
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 8px; 
        transition: 0.3s;
    }
    .stButton>button:hover {
        border-color: #bc13fe;
        color: #bc13fe;
    }
    
    hr { border-color: rgba(255,255,255,0.05); }
</style>
""", unsafe_allow_html=True)

# ----------------- القائمة الجانبية -----------------
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    try:
        st.image("profile.jpg", width=160) 
    except:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=160)
        
    st.markdown("<h2 style='margin-bottom: 0;'>Abdelhameed Mansour</h2>", unsafe_allow_html=True)
    st.markdown("<p class='gradient-text' style='font-size: 14px;'>Senior AI QA & Python Engineer</p>", unsafe_allow_html=True)
    
    st.markdown("📍 **Location:** Cairo, Egypt")
    st.markdown("📧 **Email:** abdelhameed.m91@gmail.com")
    st.markdown("📱 **Phone:** +201069531984")
    
    st.divider()
    
    try:
        with open("ABDELHAMEED SHADDAD MANSOUR.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
            st.download_button("📄 Download Resume (PDF)", data=PDFbyte, file_name="Abdelhameed_Mansour_CV.pdf", mime="application/octet-stream")
    except FileNotFoundError:
        st.warning("⚠️ Resume PDF not found.")

    st.divider()
    st.markdown("🔗 **[LinkedIn Profile](https://linkedin.com/in/abdelhameed-mansour-911034151/)**")
    st.markdown("🐙 **[GitHub Portfolio](https://github.com/abdelhameed-shaddad-abdelhameed)**")

# ----------------- المحتوى الرئيسي (Tabs) -----------------
st.markdown("<h1 class='gradient-text'>Interactive Tech Portfolio & AI Agent</h1>", unsafe_allow_html=True)
st.caption("👈 Use the tabs below to switch between my Project Portfolio and my AI Assistant.")

# هنا مكان التابات (Tabs) اللي بتفصل بين السي في وشات الذكاء الاصطناعي
tab1, tab2 = st.tabs(["🚀 Portfolio & Skills", "🤖 Chat with my AI Assistant"])

# ---- التبويبة الأولى: البورتفوليو ----
with tab1:
    st.header("🧠 Professional Summary")
    st.markdown("""
    <div style='color: #cbd5e1; line-height: 1.8; font-size: 1.05rem;'>
    A highly skilled Software Automation Engineer and Senior AI QA Specialist with a solid foundation in systems integration. I specialize in architecting test automation frameworks, building scalable Python tools, and evaluating Large Language Models (LLMs) for production-grade AI systems.
    <br><br>
    My expertise spans across designing Python automation scripts (Selenium, Playwright), training advanced AI models (Claude Code via Labelbox/Alignerr), and building interactive SaaS dashboards (Streamlit).
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.header("⚡ Core Technologies")
    skills = ["Python (Expert)", "Prompt Engineering", "LLM Evaluation (RLHF)", "Playwright & Selenium", "Streamlit", "API Integrations", "C# & Windows Forms", "SQL Auditing", "Multi-tenant SaaS"]
    st.markdown("".join([f'<span class="skill-badge">{s}</span>' for s in skills]), unsafe_allow_html=True)

    st.divider()

    st.header("🛠️ Featured Architecture & Projects")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div class="glass-card">
            <h3>🐋 WhaleTracker SaaS</h3>
            <p>A multi-tenant live market intelligence dashboard using Python and Streamlit, featuring robust admin panels, tier-based access control, and real-time data visualization.</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("View Code on GitHub 🐙", "https://github.com/abdelhameed-shaddad-abdelhameed/WhaleTracker-saas")

        st.markdown("""
        <div class="glass-card">
            <h3>🤖 Python Web Automation Tool</h3>
            <p>An advanced automation bot built with Python and Playwright. Simulates human behavior to interact with complex websites, bypass detection, and scrape data efficiently.</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("View Code on GitHub 🐙", "https://github.com/abdelhameed-shaddad-abdelhameed/Python-Web-Automation-Tool")

    with c2:
        st.markdown("""
        <div class="glass-card">
            <h3>🎯 WhaleHunter Pro</h3>
            <p>Real-time digital asset monitoring engine built with Python and Streamlit for automated alert generation and secure data extraction.</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("View Code on GitHub 🐙", "https://github.com/abdelhameed-shaddad-abdelhameed/WhaleTracker")

        st.markdown("""
        <div class="glass-card">
            <h3>🏪 Sweet-Shop POS</h3>
            <p>A comprehensive desktop application for inventory and cart logic management utilizing C# and Windows Forms to streamline retail operations.</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("View Code on GitHub 🐙", "https://github.com/abdelhameed-shaddad-abdelhameed/Sweet-Shop-POS-System")


# ---- التبويبة الثانية: AI Chatbot ----
with tab2:
    st.markdown("### 💬 Abdelhameed's AI Copilot")
    st.caption("I am an automated AI agent programmed with Abdelhameed's professional background. Ask me anything about his skills or experience!")

    # تهيئة الذاكرة للشات
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Hello! 👋 I am Abdelhameed's AI assistant. Do you want to know about his **Skills**, **Experience**, or **Projects**?"}]

    # عرض الرسايل القديمة
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # استقبال سؤال جديد
    if prompt := st.chat_input("Ask me about his LLM Evaluation experience or Python skills..."):
        # عرض سؤال المستخدم
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # الرد الآلي
        prompt_lower = prompt.lower()
        if "skill" in prompt_lower or "tech" in prompt_lower or "python" in prompt_lower:
            response = "Abdelhameed's core skills include **Python (Expert)**, **Prompt Engineering**, **LLM Evaluation (RLHF)**, **Playwright/Selenium**, and building **Streamlit** applications. He is also proficient in SQL, C#, and API Integrations."
        elif "experience" in prompt_lower or "work" in prompt_lower or "job" in prompt_lower or "ai" in prompt_lower:
            response = "Currently, he operates as a **Senior AI QA Engineer** (Freelance) on platforms like Alignerr and Labelbox, focusing on advanced multi-turn technical prompting and evaluating models like Claude Code. He also works as a **Freelance Automation Engineer** optimizing processes by 40%."
        elif "project" in prompt_lower or "portfolio" in prompt_lower or "whale" in prompt_lower:
            response = "His key projects include **WhaleTracker SaaS** (multi-tenant architecture), **WhaleHunter Pro** (live market data monitoring), and an advanced **Python Web Automation bot**."
        elif "contact" in prompt_lower or "email" in prompt_lower or "hire" in prompt_lower:
            response = "You can reach him directly via email at **abdelhameed.m91@gmail.com** or call **+201069531984**. He is open to exploring AI and Python-related opportunities!"
        else:
            response = "I am specifically tuned to answer questions about Abdelhameed's professional background. Try asking me about his **Skills**, **Projects**, or **Experience**!"

        # عرض رد الذكاء الاصطناعي
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
