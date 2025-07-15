import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="ESG 3D 분석", layout="wide")
st.title("🌱 S&P 500 ESG 리스크 3D 시각화")

uploaded_file = st.file_uploader("📁 ESG CSV 파일을 업로드하세요", type="csv")

# 파일이 업로드되지 않았을 경우 기본 CSV 로드
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.info("✅ 업로드된 파일을 사용합니다.")
elif os.path.exists("SP 500 ESG Risk Ratings.csv"):
    df = pd.read_csv("SP 500 ESG Risk Ratings.csv")
    st.info("📄 기본 ESG 파일('SP 500 ESG Risk Ratings.csv')을 불러왔습니다.")
else:
    st.error("❌ 파일이 업로드되지 않았고, 기본 CSV 파일도 존재하지 않습니다.")
    st.stop()

# 필요한 컬럼 추출 및 결측치 제거
required_cols = [
    "Name", "Environment Risk Score", 
    "Social Risk Score", "Governance Risk Score"
]
df_filtered = df[required_cols].dropna()

st.success(f"✅ {len(df_filtered)}개 기업의 데이터가 로딩되었습니다.")

# 3D 그래프 그리기
fig = px.scatter_3d(
    df_filtered,
    x="Environment Risk Score",
    y="Social Risk Score",
    z="Governance Risk Score",
    hover_name="Name",
    color="Environment Risk Score",
    title="S&P 500 기업의 ESG 리스크 3D 시각화",
    labels={
        "Environment Risk Score": "환경 리스크",
        "Social Risk Score": "사회 리스크",
        "Governance Risk Score": "지배구조 리스크"
    }
)

# 마커 크기 및 스타일 설정
fig.update_traces(marker=dict(size=3, line=dict(width=0.3, color='DarkSlateGrey')))
fig.update_layout(
    height=700,
    margin=dict(l=0, r=0, b=0, t=50),
    scene_camera=dict(
        eye=dict(x=1.5, y=1.5, z=1.2)
    ),
    scene=dict(
        xaxis_title="🌿 환경 리스크",
        yaxis_title="👥 사회 리스크",
        zaxis_title="🏛️ 지배구조 리스크",
        bgcolor="white"
    )
)

st.plotly_chart(fig, use_container_width=True)
st.caption("💡 ESG 리스크 점수가 낮을수록 지속가능성과 건전성이 높습니다.")
