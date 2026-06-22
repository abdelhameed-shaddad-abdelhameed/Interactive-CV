import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="Abdelhameed Mansour | Interactive CV", page_icon="👨‍💻", layout="wide")

# تصميم CSS مخصص لتحسين الشكل
st.markdown("""
<style>
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; }
    .project-card { background-color: #1e293b; padding: 20px; border-radius: 10px; border: 1px solid #334155; margin-bottom: 15px; }
    .skill-tag { display: inline-block; background-color: #3b82f6; color: white; padding: 5px 10px; border-radius: 15px; margin: 3px; font-size: 14px; }
</style>
""", unsafe_allow_html=True)

# ----------------- القائمة الجانبية (Sidebar) -----------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=150) # صورة بروفايل افتراضية (ممكن تغيرها بلينك صورتك)
    st.title("Abdelhameed Mansour")
    st.subheader("Python Automation & AI QA Engineer")
    
    st.markdown("📍 **Location:** Cairo, Egypt")
    st.markdown("📧 **Email:** abdelhameed.m91@gmail.com")
    st.markdown("📱 **Phone:** +201069531984")
    
    st.divider()
    
    # زرار تحميل الـ PDF
    try:
        with open("ABDELHAMEED SHADDAD MANSOUR.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
            st.download_button(
                label="📄 Download Resume (PDF)",
                data=PDFbyte,
                file_name="Abdelhameed_Mansour_Senior_AI_QA.pdf",
                mime="application/octet-stream"
            )
    except FileNotFoundError:
        st.warning("⚠️ Please upload 'ABDELHAMEED_MANSOUR_CV.pdf' to the repository to enable download.")

    st.divider()
    st.markdown("[🔗 LinkedIn Profile](https://linkedin.com/in/abdelhameed-mansour-911034151/)")
    st.markdown("[🐙 GitHub Profile](https://github.com/abdelhameed-shaddad-abdelhameed)")

# ----------------- المحتوى الرئيسي -----------------

st.title("Welcome to my Interactive Portfolio 👋")

# نبذة عنك
st.header("💡 Professional Summary")
st.write("""
A highly skilled Software Automation Engineer and Senior AI QA Specialist with a solid foundation in systems integration. I specialize in architecting test automation frameworks, building scalable Python tools, and evaluating Large Language Models (LLMs) for production-grade AI systems.

With extensive experience bridging the gap between technical execution and business logic, I don't just write code; I build robust integrations and verify complex logic. My expertise spans across designing Python automation scripts (Selenium, Playwright), training advanced AI models (Claude Code via Labelbox/Alignerr), and building interactive SaaS dashboards (Streamlit).
""")

st.divider()

# قسم المهارات
st.header("🛠️ Core Technical Skills")
skills = ["Python (Expert)", "Prompt Engineering", "LLM Evaluation (RLHF)", "Playwright & Selenium", "Streamlit", "API Integrations", "C# & Windows Forms", "SQL & Database Auditing", "Multi-tenant SaaS Architecture"]

skills_html = "".join([f'<span class="skill-tag">{skill}</span>' for skill in skills])
st.markdown(skills_html, unsafe_allow_html=True)

st.divider()

# قسم المشاريع (اللي إنت بعت لينكاتها)
st.header("🚀 Featured Projects")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="project-card">
        <h3>🐋 WhaleTracker SaaS</h3>
        <p>A multi-tenant live market intelligence dashboard using Python and Streamlit, featuring robust admin panels, tier-based access control, and real-time data visualization.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("View on GitHub", "https://github.com/abdelhameed-shaddad-abdelhameed/WhaleTracker-saas")

    st.markdown("""
    <div class="project-card">
        <h3>🤖 Python Web Automation Tool</h3>
        <p>An advanced automation bot built with Python and Playwright. Simulates human behavior to interact with complex websites, bypass detection, and scrape data efficiently.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("View on GitHub", "https://github.com/abdelhameed-shaddad-abdelhameed/Python-Web-Automation-Tool")

with col2:
    st.markdown("""
    <div class="project-card">
        <h3>🎯 WhaleHunter Pro</h3>
        <p>Real-time digital asset monitoring engine built with Python and Streamlit for automated alert generation and secure data extraction.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("View on GitHub", "https://github.com/abdelhameed-shaddad-abdelhameed/WhaleTracker")

    st.markdown("""
    <div class="project-card">
        <h3>🏪 Sweet-Shop POS System</h3>
        <p>A comprehensive desktop application for inventory and cart logic management utilizing C# and Windows Forms to streamline retail operations.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("View on GitHub", "https://github.com/abdelhameed-shaddad-abdelhameed/Sweet-Shop-POS-System")

st.divider()

# قسم الخبرة
st.header("💼 Professional Experience")
with st.expander("Senior AI QA Engineer | Alignerr / Labelbox Platform (Jan 2024 - Present)", expanded=True):
    st.write("""
    * Executed high-level technical evaluations for Claude Code to refine model reasoning and coding capabilities.
    * Developed sophisticated multi-turn prompts to test production-ready engineering practices.
    * Conducted detailed technical audits of model outputs, ensuring code correctness and modularity.
    """)

with st.expander("Freelance Automation & Testing Engineer (Jan 2024 - Present)"):
    st.write("""
    * Design and deploy custom Python automation scripts using Selenium and Playwright.
    * Build robust frameworks for cross-system data validation and execute backend data verification using complex SQL queries.
    """)

with st.expander("Systems Integration & Operations Manager | New Cairo Cosmetics (Jan 2018 - Jan 2024)"):
    st.write("""
    * Managed the digital transformation and complete ERP implementation (Odoo, Daftra) for supply chain operations.
    * Ensured 100% data accuracy across modules through rigorous auditing and workflow optimization.
    """)





