import streamlit as st
import time

# إعدادات الصفحة
st.set_page_config(page_title="A.Mansour | Terminal", page_icon="💻", layout="wide")

# تصميم CSS مخصص - ثيم الهاكر (مريح للعين)
st.markdown("""
<style>
    /* خط الأكواد */
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@300;400;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Fira Code', monospace;
        background-color: #0d1117; /* أسود مطفي مريح جداً زي GitHub Dark */
        color: #c9d1d9; /* رمادي فاتح للقراءة المريحة */
    }

    /* تأثير الـ Scanline الخفيف للخلفية */
    body::before {
        content: " ";
        display: block;
        position: absolute;
        top: 0; left: 0; bottom: 0; right: 0;
        background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%), linear-gradient(90deg, rgba(255, 0, 0, 0.06), rgba(0, 255, 0, 0.02), rgba(0, 0, 255, 0.06));
        z-index: 2;
        background-size: 100% 2px, 3px 100%;
        pointer-events: none;
    }

    /* القائمة الجانبية */
    [data-testid="stSidebar"] {
        background-color: #010409;
        border-right: 1px solid #00ff41; /* أخضر تيرمينال */
    }

    /* العناوين */
    h1, h2, h3 {
        color: #00ff41 !important; /* أخضر هاكر هادي */
    }

    /* كروت المشاريع */
    .project-card { 
        background-color: #161b22; 
        padding: 20px; 
        border-radius: 4px; 
        border-left: 3px solid #00ff41; 
        margin-bottom: 15px; 
        border-top: 1px solid #30363d;
        border-right: 1px solid #30363d;
        border-bottom: 1px solid #30363d;
    }
    .project-card h3 { margin-top: 0; }
    .project-card p { color: #8b949e; font-family: sans-serif; font-size: 14px; }

    /* فقاعات المهارات */
    .skill-tag { 
        display: inline-block; 
        background-color: #000000; 
        color: #00ff41; 
        border: 1px solid #00ff41;
        padding: 4px 10px; 
        margin: 4px; 
        font-size: 13px; 
    }

    /* أزرار الروابط */
    .stButton>button { 
        background: #010409;
        color: #00ff41; 
        border: 1px solid #00ff41;
        border-radius: 2px; 
        transition: 0.3s;
    }
    .stButton>button:hover {
        background: #00ff41;
        color: #000;
    }
</style>
""", unsafe_allow_html=True)

# ----------------- القائمة الجانبية -----------------
with st.sidebar:
    try:
        st.image("profile.jpg", width=150) 
    except:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=150)
        
    st.title("root@amansour:~#")
    st.markdown("<p style='color: #8b949e; font-size: 14px;'>Python Automation & AI QA</p>", unsafe_allow_html=True)
    
    st.markdown("📍 **Loc:** Cairo, Egypt")
    st.markdown("📧 **Mail:** abdelhameed.m91@gmail.com")
    st.markdown("📱 **Tel:** +201069531984")
    
    st.divider()
    
    try:
        with open("ABDELHAMEED SHADDAD MANSOUR.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
            st.download_button("📄 ./download_cv.sh", data=PDFbyte, file_name="Abdelhameed_Mansour_CV.pdf", mime="application/octet-stream")
    except FileNotFoundError:
        st.warning("⚠️ File 'ABDELHAMEED_MANSOUR_CV.pdf' not found.")

    st.divider()
    st.markdown("🔗 **[LinkedIn](https://linkedin.com/in/abdelhameed-mansour-911034151/)**")
    st.markdown("🐙 **[GitHub](https://github.com/abdelhameed-shaddad-abdelhameed)**")

# ----------------- المحتوى الرئيسي (Tabs) -----------------
tab1, tab2 = st.tabs(["[ ./portfolio.sh ]", "[ ./ai_assistant.py ]"])

# ---- التبويبة الأولى: البورتفوليو ----
with tab1:
    st.title(">> SYSTEM.INITIALIZED")

    st.header(">> whoami")
    st.write("""
    <div style='font-family: sans-serif; color: #c9d1d9; line-height: 1.6;'>
    A highly skilled Software Automation Engineer and Senior AI QA Specialist with a solid foundation in systems integration. I specialize in architecting test automation frameworks, building scalable Python tools, and evaluating Large Language Models (LLMs) for production-grade AI systems.
    <br><br>
    My expertise spans across designing Python automation scripts (Selenium, Playwright), training advanced AI models (Claude Code via Labelbox/Alignerr), and building interactive SaaS dashboards (Streamlit).
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.header(">> core_modules.sys")
    skills = ["Python (Expert)", "Prompt Engineering", "LLM Evaluation (RLHF)", "Playwright & Selenium", "Streamlit", "API Integrations", "C# & Windows Forms", "SQL Auditing"]
    st.markdown("".join([f'<span class="skill-tag">{s}</span>' for s in skills]), unsafe_allow_html=True)

    st.divider()

    st.header(">> executable_projects.dir")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div class="project-card">
            <h3>🐋 WhaleTracker SaaS</h3>
            <p>Multi-tenant market intelligence dashboard (Python/Streamlit) with tier-based access and real-time visualization.</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("Run GitHub_Repo", "https://github.com/abdelhameed-shaddad-abdelhameed/WhaleTracker-saas")

        st.markdown("""
        <div class="project-card">
            <h3>🤖 Web Automation Tool</h3>
            <p>Advanced Python/Playwright bot simulating human behavior to bypass detection and scrape data.</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("Run GitHub_Repo", "https://github.com/abdelhameed-shaddad-abdelhameed/Python-Web-Automation-Tool")

    with c2:
        st.markdown("""
        <div class="project-card">
            <h3>🎯 WhaleHunter Pro</h3>
            <p>Real-time digital asset monitoring engine for automated alerts and secure data extraction.</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("Run GitHub_Repo", "https://github.com/abdelhameed-shaddad-abdelhameed/WhaleTracker")

        st.markdown("""
        <div class="project-card">
            <h3>🏪 Sweet-Shop POS</h3>
            <p>C# Windows Forms desktop application for comprehensive inventory and cart logic management.</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("Run GitHub_Repo", "https://github.com/abdelhameed-shaddad-abdelhameed/Sweet-Shop-POS-System")


# ---- التبويبة الثانية: AI Chatbot ----
with tab2:
    st.title(">> TERMINAL_AI_AGENT")
    st.caption("Ask me anything about Abdelhameed's skills, experience, or projects.")

    # تهيئة الذاكرة للشات
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Hello! I am an AI trained on Abdelhameed Mansour's resume. Do you want to know about his **Skills**, **Experience**, or **Projects**?"}]

    # عرض الرسايل القديمة
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # استقبال سؤال جديد
    if prompt := st.chat_input("Type your command here (e.g., 'skills', 'experience')..."):
        # عرض سؤال المستخدم
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # الرد الآلي بناءً على الكلمات المفتاحية
        prompt_lower = prompt.lower()
        if "skill" in prompt_lower or "tech" in prompt_lower:
            response = "Abdelhameed's core skills include **Python (Expert)**, **Prompt Engineering**, **LLM Evaluation (RLHF)**, **Playwright/Selenium**, **Streamlit**, and **API Integrations**. He also has a strong background in SQL and C#."
        elif "experience" in prompt_lower or "work" in prompt_lower or "job" in prompt_lower:
            response = "He is currently a **Senior AI QA Engineer** on platforms like Alignerr and Labelbox, evaluating Claude Code. He also works as a **Freelance Automation Engineer** building Python bots. Previously, he co-founded a cosmetics company where he managed ERP integrations (Odoo/Daftra)."
        elif "project" in prompt_lower or "portfolio" in prompt_lower:
            response = "His top projects include **WhaleTracker SaaS** (a multi-tenant Streamlit dashboard), **WhaleHunter Pro** (a real-time blockchain monitoring tool), and an advanced **Python Web Automation Bot**."
        elif "contact" in prompt_lower or "email" in prompt_lower or "hire" in prompt_lower:
            response = "You can reach him via email at **abdelhameed.m91@gmail.com** or call **+201069531984**."
        else:
            response = "I'm a simulated AI Agent. I understand keywords like **Skills**, **Experience**, **Projects**, and **Contact**. Could you specify what you'd like to know about Abdelhameed?"

        # عرض رد الذكاء الاصطناعي
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
