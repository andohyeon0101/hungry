import streamlit as st
import pandas as pd

st.set_page_config(page_title="ESG 분야별 추천", layout="wide")
st.title("🌱 ESG 기반 분야별 투자 추천 기업")

# 테스트용 공개 이미지
ESG_IMAGE_URL = "https://cdn-icons-png.flaticon.com/512/3081/3081648.png"

uploaded_file = st.file_uploader("📁 ESG CSV 파일을 업로드하세요", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # 필요한 컬럼만 사용
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

    # 추천 기업 필터링 (70점 이상)
    sector_df = df[df["Sector"] == selected_sector]
    recommended = sector_df[sector_df["Score"] >= 70].sort_values("Score", ascending=False)

    st.subheader(f"✅ '{selected_sector}' 분야의 추천 기업")
    st.metric("추천 기업 수", f"{len(recommended)}개")

    # 이미지와 함께 출력
    for _, row in recommended.iterrows():
        with st.container():
            col1, col2 = st.columns([1, 5])
            with col1:
                st.image(ESG_IMAGE_URL, width=60)
            with col2:
                st.markdown(f"**{row['Name']}**")
                st.markdown(f"🌟 ESG 점수: **{row['Score']:.2f}**")

    st.info("✔️ ESG 점수는 낮은 리스크를 기반으로 계산되며, 70점 이상이면 안정적인 기업으로 간주됩니다.")
else:
    st.warning("CSV 파일을 업로드해주세요.")
