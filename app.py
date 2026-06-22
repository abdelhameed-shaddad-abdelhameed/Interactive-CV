import streamlit as st
import time
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

# 1. إعدادات الصفحة
st.set_page_config(page_title="A.Mansour | AI Engineer", page_icon="🧠", layout="wide")

# 2. تصميم CSS (خلفية الـ Glassmorphism)
st.markdown("""
<style>
    .stApp { background: radial-gradient(circle at top right, #1a1025 0%, #0b0f19 50%, #020617 100%); color: #e2e8f0; }
    .glass-card { background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(16px); border: 1px solid rgba(255, 255, 255, 0.05); border-radius: 16px; padding: 20px; margin-bottom: 15px; }
    .skill-badge { display: inline-block; background: rgba(0, 242, 254, 0.1); color: #00f2fe; border: 1px solid rgba(0, 242, 254, 0.3); padding: 5px 12px; border-radius: 20px; margin: 3px; font-size: 13px; font-weight: 600; }
</style>
""", unsafe_allow_html=True)

# 3. وظيفة الـ RAG (تحميل ملف الـ PDF)
@st.cache_resource
def load_cv_knowledge():
    # تأكد أن ملف الـ PDF موجود في نفس المجلد
    loader = PyPDFLoader("ABDELHAMEED SHADDAD MANSOUR.pdf")
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_documents(documents)
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma.from_documents(texts, embeddings)
    return db

# تحميل البيانات (لازم الملف يكون مرفوع في المستودع)
try:
    db = load_cv_knowledge()
except:
    db = None
    st.sidebar.error("CV PDF file not found. Upload 'ABDELHAMEED_MANSOUR_CV.pdf'")

# 4. واجهة المستخدم
st.title("🌌 Abdelhameed Mansour | AI Portfolio")
tab1, tab2 = st.tabs(["🚀 Portfolio", "🤖 AI RAG Assistant"])

with tab1:
    st.write("Welcome to my interactive space. Navigate through projects and my professional AI background.")
    # (هنا تقدر تكمل باقي عرض المشاريع زي ما كنا عاملين)

with tab2:
    st.subheader("💬 AI Assistant (RAG Enabled)")
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask about my experience..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        if db:
            docs = db.similarity_search(prompt, k=2)
            context = "\n".join([d.page_content for d in docs])
            response = f"Based on my resume details: {context}"
        else:
            response = "Error: CV data not loaded."
            
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
