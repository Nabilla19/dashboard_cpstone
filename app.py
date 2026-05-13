import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="MindEase - EDA Dashboard",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- DATA LOADING ---
@st.cache_data
def load_data():
    return pd.read_csv("mental_health_clean.csv")

df = load_data()

# --- LANGUAGES ---
LANGUAGES = {
    "English": {
        "title": "MindEase: Mental Health Analysis",
        "subtitle": "Data-Driven Risk Assessment Module | Team CC26-PSU186",
        "tagline": "Transforming data into early detection solutions for student well-being.",
        "tab_problem": "📋 Problem & Solution",
        "tab_eda": "📊 EDA & Business Insights",
        "tab_conclusion": "🎯 Final Conclusion",
        "filters": "Analysis Filters",
        "risk_dist_title": "1. Mental Health Risk Distribution",
        "risk_dist_insight": "<b>Insight</b>: Most students are in the low-risk category, but those in medium and high-risk categories require significant attention.",
        "q1_title": "Q1: Factors Affecting Mental Health Risk",
        "q1_insight": "<b>Insight</b>: Stress, anxiety, and depression scores are the primary drivers of mental health index and dropout risk.",
        "q2_title": "Q2: Academic Pressure & Sleep vs Stress",
        "q2_insight": "<b>Insight</b>: Higher academic pressure and fewer sleep hours are strongly correlated with increased stress levels.",
        "q3_title": "Q3: Social Support & Depression",
        "q3_insight": "<b>Insight</b>: High social support acts as a critical buffer, effectively lowering depression scores.",
        "q4_title": "Q4: Digital Usage & Anxiety",
        "q4_insight": "<b>Insight</b>: High screen time and internet usage show a clear trend of increasing anxiety scores.",
        "problem_header": "Problem Analysis",
        "problem_list": [
            "High stress and burnout due to academic pressure.",
            "Lack of self-awareness regarding mental health states.",
            "Risky self-diagnosis through inaccurate internet sources.",
            "Limited access to data-driven early detection tools.",
            "Lack of safe spaces for expression."
        ],
        "solution_header": "Proposed Solution: MindEase",
        "solution_text": "A data-driven Risk Assessment system classifying mental health risks (Low, Medium, High) integrated with daily mood tracking and interactive analytics.",
        "footer_text": "MindEase EDA Dashboard | Coding Camp 2026"
    },
    "Bahasa Indonesia": {
        "title": "MindEase: Analisis Kesehatan Mental",
        "subtitle": "Modul Asesmen Risiko Berbasis Data | Tim CC26-PSU186",
        "tagline": "Mengubah data menjadi solusi deteksi dini untuk kesejahteraan mahasiswa.",
        "tab_problem": "📋 Masalah & Solusi",
        "tab_eda": "📊 EDA & Insight Bisnis",
        "tab_conclusion": "🎯 Kesimpulan Akhir",
        "filters": "Filter Analisis",
        "risk_dist_title": "1. Distribusi Tingkat Risiko Mental",
        "risk_dist_insight": "<b>Insight</b>: Sebagian besar mahasiswa berada pada kategori risiko rendah, namun terdapat juga mahasiswa dengan risiko sedang dan tinggi yang perlu diperhatikan.",
        "q1_title": "Q1: Faktor Utama Risiko Mental",
        "q1_insight": "<b>Insight</b>: Faktor yang paling mempengaruhi risiko kesehatan mental mahasiswa adalah stress_level, anxiety_score, dan depression_score. Ketiga variabel tersebut memiliki hubungan kuat terhadap mental_health_index dan dropout_risk.",
        "q2_title": "Q2: Tekanan Akademik & Tidur vs Stres",
        "q2_insight": "<b>Insight</b>: Semakin tinggi tekanan akademik, tingkat stres cenderung meningkat. Sebaliknya, mahasiswa dengan jam tidur lebih rendah memiliki tingkat stres yang lebih tinggi.",
        "q3_title": "Q3: Pengaruh Dukungan Sosial",
        "q3_insight": "<b>Insight</b>: Dukungan sosial yang tinggi cenderung menurunkan tingkat depresi mahasiswa secara signifikan.",
        "q4_title": "Q4: Screen Time & Internet terhadap Anxiety",
        "q4_insight": "<b>Insight</b>: Mahasiswa dengan durasi penggunaan layar dan internet yang tinggi cenderung memiliki tingkat kecemasan yang lebih tinggi.",
        "problem_header": "Analisis Permasalahan",
        "problem_list": [
            "Stres, kecemasan, dan burnout akibat tekanan akademik dan gaya hidup.",
            "Kurangnya kesadaran individu terhadap kondisi kesehatan mental sendiri.",
            "Kecenderungan self-diagnosis melalui internet yang sering kali tidak akurat.",
            "Minimnya akses cepat terhadap alat deteksi dini kesehatan mental berbasis data.",
            "Kurangnya media yang aman untuk mengekspresikan perasaan tanpa takut dihakimi."
        ],
        "solution_header": "Solusi yang Dikembangkan",
        "solution_text": "Sistem Mental Health Risk Assessment berbasis data yang mengklasifikasikan risiko (Low, Medium, High) berdasarkan faktor stres, pola tidur, tekanan akademik, dan dukungan sosial.",
        "footer_text": "Dashboard EDA MindEase | Coding Camp 2026"
    }
}

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🧠 MindEase</h1>", unsafe_allow_html=True)
    selected_lang = st.selectbox("🌐 Language", options=["Bahasa Indonesia", "English"])
    t = LANGUAGES[selected_lang]
    st.markdown("---")
    st.subheader(f"🛠️ {t['filters']}")
    gender_f = st.multiselect("Gender", df["gender"].unique(), df["gender"].unique())
    age_f = st.slider("Age", 17, 30, (17, 30))
    
    st.markdown("---")
    st.info("💡 **Masalah Utama**: Kurangnya sistem yang dapat membantu individu mengetahui tingkat risiko kesehatan mental secara dini dan berbasis data.")

filtered_df = df[
    (df["gender"].isin(gender_f)) &
    (df["age"].between(age_f[0], age_f[1]))
]

# --- CSS ---
st.markdown(f"""
    <style>
    :root {{
        --primary: #FF4B4B;
        --text-dark: #1E293B;
        --sidebar-text: #FFFFFF;
    }}
    .stApp {{ background-color: white; color: var(--text-dark); }}
    
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
    [data-testid="stSidebar"] label, [data-testid="stSidebar"] span {{
        color: white !important;
    }}

    .main-header {{
        background: linear-gradient(135deg, #FF4B4B 0%, #FF8F8F 100%);
        padding: 2rem;
        border-radius: 20px;
        color: white;
        margin-bottom: 2rem;
    }}
    .main-header h1, .main-header p {{ color: white !important; margin: 0; }}
    
    .card {{
        background: #F8FAFC;
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 5px solid var(--primary);
        margin-bottom: 1rem;
    }}
    
    .insight-box {{
        background: #F1F5F9;
        padding: 1.2rem;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
        margin-top: 10px;
        font-weight: 500;
        color: #1E293B !important;
    }}
    
    .stTabs [data-baseweb="tab-list"] {{ gap: 10px; }}
    .stTabs [data-baseweb="tab"] {{
        background-color: #F1F5F9 !important;
        border-radius: 10px 10px 0 0;
        padding: 10px 20px;
        color: #64748B !important;
    }}
    .stTabs [aria-selected="true"] {{
        background-color: white !important;
        color: var(--primary) !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown(f"""
    <div class="main-header">
        <h1>{t['title']}</h1>
        <p style="font-weight: 700; font-size: 1.1rem;">{t['subtitle']}</p>
        <p style="opacity: 0.9;">{t['tagline']}</p>
    </div>
    """, unsafe_allow_html=True)

# --- TABS ---
tab1, tab2, tab3 = st.tabs([t['tab_problem'], t['tab_eda'], t['tab_conclusion']])

with tab1:
    col_p, col_s = st.columns(2)
    with col_p:
        st.subheader(f"🔍 {t['problem_header']}")
        for p in t['problem_list']:
            st.markdown(f"- {p}")
        st.markdown(f"""
            <div style="background:#FFF1F1; padding:1rem; border-radius:10px; border:1px solid #FFD1D1; margin-top:1rem;">
                <b>Masalah Utama:</b><br>Kurangnya sistem yang dapat membantu individu dalam mengetahui tingkat risiko kesehatan mental mereka secara dini dan berbasis data.
            </div>
        """, unsafe_allow_html=True)
        
    with col_s:
        st.subheader(f"💡 {t['solution_header']}")
        st.write(t['solution_text'])
        st.info("**Fitur Sistem MindEase:**")
        st.markdown("""
        - **Mood tracking harian**
        - **Analisis data pengguna**
        - **Dashboard interaktif**
        """)
        st.image("https://img.freepik.com/free-vector/mental-health-awareness-concept_23-2148531012.jpg", width=300)

with tab2:
    # 1. Risk Level Distribution
    st.subheader(t['risk_dist_title'])
    fig1 = px.histogram(filtered_df, x="risk_level", color="risk_level", 
                        color_discrete_map={'Low':'#00CC96', 'Medium':'#FFA15A', 'High':'#EF553B'},
                        template="plotly_white", category_orders={"risk_level": ["Low", "Medium", "High"]})
    st.plotly_chart(fig1, width='stretch')
    st.markdown(f'<div class="insight-box">{t["risk_dist_insight"]}</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Q2: Exam Pressure & Sleep vs Stress
    st.subheader(t['q2_title'])
    c1, c2 = st.columns(2)
    with c1:
        fig_ep = px.scatter(filtered_df.sample(min(2000, len(filtered_df))), x="exam_pressure", y="stress_level", 
                            trendline="ols", title="Exam Pressure vs Stress", template="plotly_white")
        st.plotly_chart(fig_ep, width='stretch')
    with c2:
        fig_sl = px.scatter(filtered_df.sample(min(2000, len(filtered_df))), x="sleep_hours", y="stress_level", 
                            trendline="ols", title="Sleep Hours vs Stress", template="plotly_white")
        st.plotly_chart(fig_sl, width='stretch')
    st.markdown(f'<div class="insight-box">{t["q2_insight"]}</div>', unsafe_allow_html=True)

    st.markdown("---")

    # Q3: Social Support vs Depression
    st.subheader(t['q3_title'])
    fig_soc = px.scatter(filtered_df.sample(min(2000, len(filtered_df))), x="social_support", y="depression_score", 
                        trendline="ols", color="social_support", color_continuous_scale="Viridis", template="plotly_white")
    st.plotly_chart(fig_soc, width='stretch')
    st.markdown(f'<div class="insight-box">{t["q3_insight"]}</div>', unsafe_allow_html=True)

    st.markdown("---")

    # Q4: Screen Time & Internet vs Anxiety
    st.subheader(t['q4_title'])
    c3, c4 = st.columns(2)
    with c3:
        fig_st = px.scatter(filtered_df.sample(min(2000, len(filtered_df))), x="screen_time", y="anxiety_score", 
                            trendline="ols", template="plotly_white")
        st.plotly_chart(fig_st, width='stretch')
    with c4:
        fig_iu = px.scatter(filtered_df.sample(min(2000, len(filtered_df))), x="internet_usage", y="anxiety_score", 
                            trendline="ols", template="plotly_white")
        st.plotly_chart(fig_iu, width='stretch')
    st.markdown(f'<div class="insight-box">{t["q4_insight"]}</div>', unsafe_allow_html=True)

    st.markdown("---")

    # Heatmap
    st.subheader("Correlation Heatmap")
    corr = filtered_df[["stress_level", "anxiety_score", "depression_score", "burnout_score", "mental_health_index", "dropout_risk"]].corr()
    fig_heat = px.imshow(corr, text_auto=".2f", color_continuous_scale='RdBu_r', template="plotly_white")
    st.plotly_chart(fig_heat, width='stretch')
    st.markdown(f'<div class="insight-box">{t["q1_insight"]}</div>', unsafe_allow_html=True)

with tab3:
    st.markdown(f"## { "Final Conclusion" if selected_lang=='English' else 'Kesimpulan Akhir Analisis' }")
    st.write("""
    Berdasarkan hasil analisis, kondisi kesehatan mental mahasiswa dipengaruhi oleh berbagai faktor akademik, gaya hidup, dan sosial:
    - **Faktor Akademik**: Tingkat stres mahasiswa cenderung meningkat seiring tingginya tekanan akademik.
    - **Pola Tidur**: Mahasiswa dengan jam tidur yang lebih sedikit cenderung memiliki tingkat stres yang lebih tinggi.
    - **Dukungan Sosial**: Dukungan sosial yang baik terbukti membantu menurunkan tingkat depresi mahasiswa secara signifikan.
    - **Penggunaan Digital**: Penggunaan screen time dan internet usage yang tinggi memiliki hubungan dengan meningkatnya tingkat kecemasan.
    
    **Kesimpulan Akhir:** Faktor akademik, gaya hidup, dan dukungan sosial memiliki pengaruh penting terhadap risiko kesehatan mental mahasiswa, yang dapat diprediksi berdasarkan pola data yang ada.
    """)
    
    st.success("**Solusi MindEase:** Pengembangan sistem Mental Health Risk Assessment berbasis data sangat krusial untuk membantu deteksi dini risiko mental (Low, Medium, High).")

# --- FOOTER ---
st.markdown("---")
st.markdown(f"<div style='text-align: center; color: #64748B;'>{t['footer_text']}</div>", unsafe_allow_html=True)