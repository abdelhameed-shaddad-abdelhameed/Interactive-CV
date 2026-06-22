import streamlit as st
import os
import time

# استدعاء مكتبات الـ RAG
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. إعدادات الصفحة
st.set_page_config(page_title="A.Mansour | AI Engineer", page_icon="🧠", layout="wide")

# 2. تصميم CSS (ثيم Glassmorphism الحديث)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Space Grotesk', sans-serif;
    }
    .stApp {
        background: radial-gradient(circle at top right, #1a1025 0%, #0b0f19 50%, #020617 100%);
        color: #e2e8f0;
    }
    [data-testid="stSidebar"] {
        background-color: rgba(11, 15, 25, 0.8) !important;
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(255, 255, 255, 0.05);
    }
    h1, h2, h3 { color: #ffffff !important; font-weight: 700 !important; }
    .gradient-text {
        background: linear-gradient(90deg, #00f2fe 0%, #4facfe 50%, #bc13fe 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
    }
    .glass-card { 
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 10px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .glass-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0, 242, 254, 0.15);
        border: 1px solid rgba(0, 242, 254, 0.3);
    }
    .glass-card h3 { color: #00f2fe !important; font-size: 1.3rem; margin-top: 0; }
    .glass-card p { color: #94a3b8; font-size: 0.95rem; line-height: 1.6; }
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
    }
    .stButton>button { 
        background: transparent;
        color: #e2e8f0; 
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 8px; 
        transition: 0.3s;
        width: 100%;
    }
    .stButton>button:hover { border-color: #bc13fe; color: #bc13fe; }
    hr { border-color: rgba(255,255,255,0.05); }
</style>
""", unsafe_allow_html=True)

# 3. إعداد الـ RAG وبناء الذاكرة (استخدام FAISS بدلاً من Chroma)
@st.cache_resource
def load_cv_knowledge():
    cv_path = "cv.pdf"
    if not os.path.exists(cv_path):
        return None
    
    loader = PyPDFLoader(cv_path)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_documents(documents)
    
    # تحميل الموديل المجاني
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    # بناء قاعدة البيانات باستخدام FAISS
    db = FAISS.from_documents(texts, embeddings)
    return db

# تشغيل دالة تحميل السي في
vector_db = load_cv_knowledge()

# 4. القائمة الجانبية (Sidebar)
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
    
    cv_file = "cv.pdf"
    if os.path.exists(cv_file):
        with open(cv_file, "rb") as pdf_file:
            st.download_button("📄 Download Resume (PDF)", data=pdf_file.read(), file_name="cv.pdf", mime="application/octet-stream")
    else:
        st.warning(f"⚠️ Missing: {cv_file}")

    st.divider()
    st.markdown("🔗 **[LinkedIn Profile](https://linkedin.com/in/abdelhameed-mansour-911034151/)**")
    st.markdown("🐙 **[GitHub Portfolio](https://github.com/abdelhameed-shaddad-abdelhameed)**")

# 5. المحتوى الرئيسي والـ Tabs
st.markdown("<h1 class='gradient-text'>Interactive Tech Portfolio & AI Agent</h1>", unsafe_allow_html=True)
st.caption("👈 Use the tabs below to switch between my Project Portfolio and my AI Assistant.")

tab1, tab2 = st.tabs(["🚀 Portfolio & Skills", "🤖 Chat with my AI Assistant"])

# -------- التبويبة الأولى: البورتفوليو --------
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
        # تقسيم الزراير لمشروع الـ SaaS
        btn_col1, btn_col2 = st.columns(2)
        with btn_col1:
            st.link_button("Code on GitHub 🐙", "https://github.com/abdelhameed-shaddad-abdelhameed/WhaleTracker-saas", key="btn1")
        with btn_col2:
            st.link_button("View Live App 🌐", "https://whaletracker-saas-fjjtyqjg8fpn9kfy6eqh2s.streamlit.app/", key="live_btn1")
            
        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("""
        <div class="glass-card">
            <h3>🤖 Python Web Automation Tool</h3>
            <p>An advanced automation bot built with Python and Playwright. Simulates human behavior to interact with complex websites, bypass detection, and scrape data efficiently.</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("View Code on GitHub 🐙", "https://github.com/abdelhameed-shaddad-abdelhameed/Python-Web-Automation-Tool", key="btn2")

    with c2:
        st.markdown("""
        <div class="glass-card">
            <h3>🎯 WhaleHunter Pro</h3>
            <p>Real-time digital asset monitoring engine built with Python and Streamlit for automated alert generation and secure data extraction.</p>
        </div>
        """, unsafe_allow_html=True)
        # تقسيم الزراير لمشروع الـ WhaleHunter
        btn_col3, btn_col4 = st.columns(2)
        with btn_col3:
            st.link_button("Code on GitHub 🐙", "https://github.com/abdelhameed-shaddad-abdelhameed/WhaleTracker", key="btn3")
        with btn_col4:
            st.link_button("View Live App 🌐", "https://whaletracker.streamlit.app/", key="live_btn3")
            
        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("""
        <div class="glass-card">
            <h3>🏪 Sweet-Shop POS</h3>
            <p>A comprehensive desktop application for inventory and cart logic management utilizing C# and Windows Forms to streamline retail operations.</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("View Code on GitHub 🐙", "https://github.com/abdelhameed-shaddad-abdelhameed/Sweet-Shop-POS-System", key="btn4")

# -------- التبويبة الثانية: AI Chatbot (RAG) --------
with tab2:
    st.markdown("### 💬 Abdelhameed's AI Copilot (RAG Powered)")
    st.caption("This AI reads directly from my uploaded CV to answer your questions accurately.")

    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Hello! I am connected to Abdelhameed's resume. Ask me about his experience or projects!"}]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask about my LLM Evaluation experience..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # استخراج الإجابة من السي في باستخدام RAG
        if vector_db:
            try:
                # البحث عن أقرب جملتين في السي في لسؤال المستخدم
                docs = vector_db.similarity_search(prompt, k=2)
                extracted_context = "\n\n".join([f"- {d.page_content}" for d in docs])
                
                response = f"**Based on the retrieved context from my CV:**\n\n{extracted_context}"
            except Exception as e:
                response = f"An error occurred while searching the document: {e}"
        else:
            response = "I couldn't load the CV database. Please ensure 'cv.pdf' is in the repository."

        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
