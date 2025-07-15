import streamlit as st
import pandas as pd

st.set_page_config(page_title="ESG 분야별 추천", layout="wide")
st.title("🌱 ESG 기반 분야별 투자 추천 기업")

# CSV 파일 업로드
uploaded_file = st.file_uploader("📁 ESG CSV 파일을 업로드하세요", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # 필요한 컬럼 선택 및 전처리
    required_cols = [
        "Name", "Sector", 
        "Environment Risk Score", 
        "Social Risk Score", 
        "Governance Risk Score"
    ]
    df = df[required_cols].dropna()

    # 총 리스크와 점수 계산
    df["Total Risk"] = (
        df["Environment Risk Score"] +
        df["Social Risk Score"] +
        df["Governance Risk Score"]
    )
    df["Score"] = 100 - df["Total Risk"] * 2  # 점수 계산 공식

    # 분야(섹터) 선택 UI
    sectors = df["Sector"].dropna().unique()
    selected_sector = st.selectbox("🔍 분석할 분야(Sector)를 선택하세요", sorted(sectors))

    # 선택한 분야의 기업 중 추천 (80점 이상)
    sector_df = df[df["Sector"] == selected_sector]
    recommended = sector_df[sector_df["Score"] >= 80].sort_values("Score", ascending=False)

    st.subheader(f"✅ '{selected_sector}' 분야의 추천 기업")
    st.metric("추천 기업 수", f"{len(recommended)}개")

    st.dataframe(recommended[["Name", "Score"]].set_index("Name").round(2))

    st.info("✔️ ESG 점수는 낮은 리스크를 기반으로 계산되며, 80점 이상이면 안정성과 지속 가능성이 높은 기업으로 간주됩니다.")
else:
    st.warning("CSV 파일을 업로드해주세요.")
