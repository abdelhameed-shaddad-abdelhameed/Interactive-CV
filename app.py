import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="Abdelhameed Mansour | Interactive CV", page_icon="👨‍💻", layout="wide")

# تصميم CSS مخصص - ثيم الـ Cyberpunk (نيون فسفوري)
st.markdown("""
<style>
    /* استدعاء خط تكنولوجي */
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');
    
    html, body, [class*="css"]  {
        font-family: 'Share Tech Mono', monospace;
    }

    /* ألوان القائمة الجانبية */
    [data-testid="stSidebar"] {
        background-color: #090014; /* أسود بلمحة بنفسجي داكن */
        border-right: 2px solid #bc13fe; /* خط موف فسفوري */
        box-shadow: 2px 0 20px rgba(188, 19, 254, 0.2);
    }

    /* العناوين (أخضر فسفوري) */
    h1, h2, h3 {
        color: #39ff14 !important;
        text-shadow: 0 0 10px rgba(57, 255, 20, 0.4);
    }

    /* تصميم الزراير (أخضر وأسود) */
    .stButton>button { 
        width: 100%; 
        background: transparent;
        color: #39ff14; 
        border: 1px solid #39ff14;
        border-radius: 5px; 
        font-weight: bold; 
        box-shadow: 0 0 10px rgba(57, 255, 20, 0.2);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: #39ff14;
        color: #000;
        box-shadow: 0 0 20px rgba(57, 255, 20, 0.6);
        border: 1px solid #39ff14;
    }

    /* كروت المشاريع (تأثير وهج أحمر وموف) */
    .project-card { 
        background-color: #0d0d0d; 
        padding: 20px; 
        border-radius: 8px; 
        border-left: 4px solid #ff007f; /* أحمر/بينك فسفوري */
        box-shadow: 0 4px 15px rgba(255, 0, 127, 0.15); 
        margin-bottom: 15px; 
        transition: transform 0.3s, box-shadow 0.3s;
    }
    .project-card:hover {
        transform: translateY(-5px);
        border-left: 4px solid #bc13fe; /* يتحول لموف عند الوقوف عليه */
        box-shadow: 0 8px 25px rgba(188, 19, 254, 0.4);
    }
    .project-card p {
        color: #d1d5db;
        font-family: sans-serif; /* خط عادي للقراءة المريحة */
    }

    /* فقاعات المهارات (موف نيون) */
    .skill-tag { 
        display: inline-block; 
        background-color: rgba(188, 19, 254, 0.1); 
        color: #bc13fe; 
        border: 1px solid #bc13fe;
        padding: 6px 15px; 
        border-radius: 20px; 
        margin: 5px; 
        font-size: 14px; 
        font-weight: bold;
        box-shadow: 0 0 10px rgba(188, 19, 254, 0.2);
        letter-spacing: 1px;
    }

    /* الفواصل */
    hr {
        border-color: #39ff14;
        opacity: 0.3;
    }
</style>
""", unsafe_allow_html=True)

# ----------------- القائمة الجانبية (Sidebar) -----------------
with st.sidebar:
    # ⚠️ غير اسم 'profile.jpg' هنا لو رفعت صورتك باسم تاني
    try:
        st.image("profile.jpg", width=180) 
    except:
        # صورة بديلة لو ملقاش صورتك
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=180)
        
    st.title("Abdelhameed Mansour")
    st.markdown("<p style='color: #bc13fe; font-size: 18px;'>⚡ Python Automation & AI QA Engineer</p>", unsafe_allow_html=True)
    
    st.markdown("📍 **Location:** Cairo, Egypt")
    st.markdown("📧 **Email:** abdelhameed.m91@gmail.com")
    st.markdown("📱 **Phone:** +201069531984")
    
    st.divider()
    
    # زرار تحميل الـ PDF
    try:
        with open("ABDELHAMEED_MANSOUR_CV.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
            st.download_button(
                label="📄 DOWNLOAD SYSTEM_FILE_CV.PDF",
                data=PDFbyte,
                file_name="Abdelhameed_Mansour_Senior_AI_QA.pdf",
                mime="application/octet-stream"
            )
    except FileNotFoundError:
        st.warning("⚠️ System File Missing: 'ABDELHAMEED_MANSOUR_CV.pdf'")

    st.divider()
    st.markdown("🔗 **[INITIATE_LINKEDIN_CONNECTION](https://linkedin.com/in/abdelhameed-mansour-911034151/)**")
    st.markdown("🐙 **[ACCESS_GITHUB_DATABANK](https://github.com/abdelhameed-shaddad-abdelhameed)**")

# ----------------- المحتوى الرئيسي -----------------

st.title(">> INITIALIZING INTERACTIVE PORTFOLIO_")

# نبذة عنك
st.header(">> SYSTEM.SUMMARY")
st.write("""
<div style='font-family: sans-serif; color: #e5e7eb; line-height: 1.6;'>
A highly skilled Software Automation Engineer and Senior AI QA Specialist with a solid foundation in systems integration. I specialize in architecting test automation frameworks, building scalable Python tools, and evaluating Large Language Models (LLMs) for production-grade AI systems.
<br><br>
With extensive experience bridging the gap between technical execution and business logic, I don't just write code; I build robust integrations and verify complex logic. My expertise spans across designing Python automation scripts (Selenium, Playwright), training advanced AI models (Claude Code via Labelbox/Alignerr), and building interactive SaaS dashboards (Streamlit).
</div>
""", unsafe_allow_html=True)

st.divider()

# قسم المهارات
st.header(">> CORE.MODULES")
skills = ["Python (Expert)", "Prompt Engineering", "LLM Evaluation (RLHF)", "Playwright & Selenium", "Streamlit", "API Integrations", "C# & Windows Forms", "SQL Auditing", "Multi-tenant SaaS"]

skills_html = "".join([f'<span class="skill-tag">{skill}</span>' for skill in skills])
st.markdown(skills_html, unsafe_allow_html=True)

st.divider()

# قسم المشاريع
st.header(">> EXECUTABLE.PROJECTS")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="project-card">
        <h3 style="color: #ff007f;">🐋 WhaleTracker SaaS</h3>
        <p>A multi-tenant live market intelligence dashboard using Python and Streamlit, featuring robust admin panels, tier-based access control, and real-time data visualization.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("EXECUTE GitHub_Link", "https://github.com/abdelhameed-shaddad-abdelhameed/WhaleTracker-saas")

    st.markdown("""
    <div class="project-card">
        <h3 style="color: #ff007f;">🤖 Web Automation Tool</h3>
        <p>An advanced automation bot built with Python and Playwright. Simulates human behavior to interact with complex websites, bypass detection, and scrape data efficiently.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("EXECUTE GitHub_Link", "https://github.com/abdelhameed-shaddad-abdelhameed/Python-Web-Automation-Tool")

with col2:
    st.markdown("""
    <div class="project-card">
        <h3 style="color: #bc13fe;">🎯 WhaleHunter Pro</h3>
        <p>Real-time digital asset monitoring engine built with Python and Streamlit for automated alert generation and secure data extraction.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("EXECUTE GitHub_Link", "https://github.com/abdelhameed-shaddad-abdelhameed/WhaleTracker")

    st.markdown("""
    <div class="project-card">
        <h3 style="color: #bc13fe;">🏪 Sweet-Shop POS</h3>
        <p>A comprehensive desktop application for inventory and cart logic management utilizing C# and Windows Forms to streamline retail operations.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("EXECUTE GitHub_Link", "https://github.com/abdelhameed-shaddad-abdelhameed/Sweet-Shop-POS-System")

st.divider()

# قسم الخبرة
st.header(">> EXPERIENCE.LOG")
with st.expander("Senior AI QA Engineer | Alignerr / Labelbox Platform (Jan 2024 - Present)", expanded=True):
    st.markdown("""
    <div style='font-family: sans-serif; color: #d1d5db;'>
    <ul>
        <li>Executed high-level technical evaluations for Claude Code to refine model reasoning and coding capabilities.</li>
        <li>Developed sophisticated multi-turn prompts to test production-ready engineering practices.</li>
        <li>Conducted detailed technical audits of model outputs, ensuring code correctness and modularity.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with st.expander("Freelance Automation & Testing Engineer (Jan 2024 - Present)"):
    st.markdown("""
    <div style='font-family: sans-serif; color: #d1d5db;'>
    <ul>
        <li>Design and deploy custom Python automation scripts using Selenium and Playwright.</li>
        <li>Build robust frameworks for cross-system data validation and execute backend data verification using complex SQL queries.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with st.expander("Systems Integration & Operations Manager | New Cairo Cosmetics (Jan 2018 - Jan 2024)"):
    st.markdown("""
    <div style='font-family: sans-serif; color: #d1d5db;'>
    <ul>
        <li>Managed the digital transformation and complete ERP implementation (Odoo, Daftra) for supply chain operations.</li>
        <li>Ensured 100% data accuracy across modules through rigorous auditing and workflow optimization.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
