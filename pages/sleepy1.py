import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="ESG 분야별 추천", layout="wide")
st.title("🌱 ESG 기반 분야별 투자 추천 기업")

# 분야별 이미지 매핑
sector_images = {
    "Technology": "https://cdn-icons-png.flaticon.com/512/1055/1055687.png",
    "Healthcare": "https://cdn-icons-png.flaticon.com/512/2833/2833143.png",
    "Financials": "https://cdn-icons-png.flaticon.com/512/3285/3285885.png",
    "Energy": "https://cdn-icons-png.flaticon.com/512/1046/1046793.png",
    "Consumer Staples": "https://cdn-icons-png.flaticon.com/512/1046/1046751.png",
    "Industrials": "https://cdn-icons-png.flaticon.com/512/3050/3050525.png",
    "Utilities": "https://cdn-icons-png.flaticon.com/512/189/189664.png",
    "Communication Services": "https://cdn-icons-png.flaticon.com/512/5974/5974635.png",
    "Real Estate": "https://cdn-icons-png.flaticon.com/512/2356/2356785.png",
    "Materials": "https://cdn-icons-png.flaticon.com/512/4965/4965730.png"
}

uploaded_file = st.file_uploader("📁 ESG CSV 파일을 업로드하세요", type="csv")

# 파일 업로드 여부에 따라 CSV 로드
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
    "Name", "Sector", 
    "Environment Risk Score", 
    "Social Risk Score", 
    "Governance Risk Score"
]
df = df[required_cols].dropna()

# 점수 계산
df["Total Risk"] = (
    df["Environment Risk Score"] +
    df["Social Risk Score"] +
    df["Governance Risk Score"]
)
df["Score"] = 100 - df["Total Risk"] * 2

# 섹터 선택
sectors = df["Sector"].dropna().unique()
selected_sector = st.selectbox("🔍 분석할 분야(Sector)를 선택하세요", sorted(sectors))

# 추천 기업 필터링
sector_df = df[df["Sector"] == selected_sector]
recommended = sector_df[sector_df["Score"] >= 70].sort_values("Score", ascending=False)

st.subheader(f"✅ '{selected_sector}' 분야의 추천 기업")
st.metric("추천 기업 수", f"{len(recommended)}개")

# 섹터 이미지
image_url = sector_images.get(selected_sector, "https://cdn-icons-png.flaticon.com/512/891/891419.png")

for _, row in recommended.iterrows():
    with st.container():
        col1, col2 = st.columns([1, 5])
        with col1:
            st.image(image_url, width=60)
        with col2:
            st.markdown(f"**{row['Name']}**")
            st.markdown(f"🌟 ESG 점수: **{row['Score']:.2f}**")

st.info("✔️ ESG 점수는 낮은 리스크 기반이며, 70점 이상이면 안정적인 기업으로 간주됩니다.")
