import streamlit as st
import datetime

# 페이지 설정
st.set_page_config(
    page_title="기업 지속 발전 가이드",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 사이드바 목차
st.sidebar.title("📚 목차")
sections = {
    "개요": "overview",
    "핵심 원칙": "principles",
    "전략적 접근": "strategies",
    "실행 방법": "implementation",
    "평가 지표": "metrics",
    "사례 연구": "case_studies",
    "참고 자료": "references"
}

selected_section = st.sidebar.radio("섹션 선택", list(sections.keys()))

# 메인 헤더
st.title("🏢 기업 지속 발전 가이드")
st.markdown("*지속 가능한 기업 경영을 위한 종합 가이드*")

# 정보 박스
st.info("이 문서는 기업이 장기적으로 지속 가능한 발전을 이루기 위한 핵심 전략과 실행 방안을 제시합니다.")

# 마지막 업데이트 정보
current_date = datetime.datetime.now().strftime("%Y년 %m월 %d일")
st.caption(f"마지막 업데이트: {current_date}")

st.divider()

# 개요 섹션
if selected_section == "개요":
    st.header("1. 개요")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        **기업 지속 발전**(Corporate Sustainability)은 기업이 경제적 성과를 달성하면서도 환경적 책임과 사회적 가치를 동시에 추구하는 경영 철학입니다.
        
        ### 정의
        기업 지속 발전은 다음 세 가지 핵심 요소로 구성됩니다:
        - **경제적 지속가능성**: 장기적 수익성과 재정 안정성
        - **환경적 지속가능성**: 환경 보호와 자원의 효율적 활용
        - **사회적 지속가능성**: 사회적 책임과 이해관계자 가치 창출
        
        ### 중요성
        현대 기업 환경에서 지속 발전은 선택이 아닌 필수입니다. 소비자, 투자자, 정부 모두 기업의 지속가능성을 중요하게 평가하고 있습니다.
        """)
    
    with col2:
        st.markdown("""
        ### 📊 주요 통계
        - 전 세계 CEO의 **83%**가 지속가능성을 핵심 전략으로 인식
        - 지속가능한 기업의 평균 **ROI 15% 증가**
        - 밀레니얼 세대의 **73%**가 지속가능한 제품에 더 많은 비용 지불 의향
        
        ### 🎯 핵심 목표
        1. 장기적 성장
        2. 리스크 관리
        3. 브랜드 가치 제고
        4. 이해관계자 신뢰 구축
        """)

# 핵심 원칙 섹션
elif selected_section == "핵심 원칙":
    st.header("2. 핵심 원칙")
    
    st.markdown("### 2.1 Triple Bottom Line (3P)")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        #### 💰 Profit (수익)
        - 장기적 수익성 확보
        - 효율적 자원 활용
        - 혁신을 통한 경쟁력 강화
        - 지속가능한 비즈니스 모델 개발
        """)
    
    with col2:
        st.markdown("""
        #### 👥 People (사람)
        - 직원 복지와 안전
        - 지역사회 기여
        - 고객 만족과 신뢰
        - 인권 존중과 다양성
        """)
    
    with col3:
        st.markdown("""
        #### 🌍 Planet (지구)
        - 환경 보호와 보존
        - 탄소 배출 감소
        - 순환 경제 구현
        - 재생 가능 에너지 활용
        """)
    
    st.divider()
    
    st.markdown("### 2.2 ESG 경영")
    
    tab1, tab2, tab3 = st.tabs(["환경 (E)", "사회 (S)", "지배구조 (G)"])
    
    with tab1:
        st.markdown("""
        #### 🌱 환경 (Environmental)
        - **기후 변화 대응**: 탄소 중립 목표 설정 및 달성
        - **자원 효율성**: 물, 에너지, 원자재의 효율적 사용
        - **폐기물 관리**: 재활용과 폐기물 최소화
        - **생물 다양성**: 생태계 보호와 복원 활동
        """)
    
    with tab2:
        st.markdown("""
        #### 🤝 사회 (Social)
        - **인적 자본**: 교육, 훈련, 다양성 프로그램
        - **지역사회**: 사회공헌과 지역 발전 기여
        - **고객 관계**: 제품 안전과 고객 만족
        - **공급망 관리**: 윤리적 조달과 공정한 거래
        """)
    
    with tab3:
        st.markdown("""
        #### ⚖️ 지배구조 (Governance)
        - **이사회 독립성**: 투명하고 독립적인 이사회 구성
        - **윤리 경영**: 부패 방지와 윤리적 의사결정
        - **리스크 관리**: 체계적인 위험 관리 시스템
        - **이해관계자 참여**: 투명한 소통과 참여 채널
        """)

# 전략적 접근 섹션
elif selected_section == "전략적 접근":
    st.header("3. 전략적 접근")
    
    st.markdown("### 3.1 지속가능성 통합 전략")
    
    strategy_tabs = st.tabs(["비전 수립", "목표 설정", "실행 계획", "모니터링"])
    
    with strategy_tabs[0]:
        st.markdown("""
        #### 🎯 비전 수립
        
        **단계별 접근법:**
        1. **현황 분석**: 기업의 현재 지속가능성 수준 평가
        2. **이해관계자 분석**: 주요 이해관계자의 기대와 요구사항 파악
        3. **중대성 평가**: 기업과 이해관계자에게 중요한 이슈 식별
        4. **비전 설정**: 명확하고 달성 가능한 지속가능성 비전 수립
        
        **예시 비전:**
        - "2030년까지 탄소 중립 달성"
        - "지속가능한 혁신으로 더 나은 미래 창조"
        - "사회와 환경에 긍정적 영향을 미치는 기업"
        """)
    
    with strategy_tabs[1]:
        st.markdown("""
        #### 📊 목표 설정 (SMART 원칙)
        
        **Specific (구체적)**: 명확하고 구체적인 목표
        **Measurable (측정가능)**: 정량적 지표로 측정 가능
        **Achievable (달성가능)**: 현실적이고 달성 가능한 수준
        **Relevant (관련성)**: 기업 전략과 연관성
        **Time-bound (시간제한)**: 명확한 달성 기한 설정
        
        **목표 예시:**
        - 2025년까지 재생에너지 비율 50% 달성
        - 2030년까지 폐기물 매립 제로 달성
        - 여성 임원 비율 30% 달성
        """)
    
    with strategy_tabs[2]:
        st.markdown("""
        #### 🚀 실행 계획
        
        **1. 조직 구조 개편**
        - 지속가능성 전담 부서 설치
        - 임원급 CSO(Chief Sustainability Officer) 임명
        - 부서별 지속가능성 담당자 지정
        
        **2. 정책 및 절차 수립**
        - 지속가능성 정책 문서화
        - 업무 프로세스에 지속가능성 고려사항 반영
        - 공급업체 행동 강령 수립
        
        **3. 교육 및 인식 제고**
        - 전 직원 지속가능성 교육 실시
        - 지속가능성 문화 확산 프로그램
        - 인센티브 시스템 도입
        """)
    
    with strategy_tabs[3]:
        st.markdown("""
        #### 📈 모니터링 및 평가
        
        **정기적 평가 체계:**
        - 월별 KPI 모니터링
        - 분기별 성과 리뷰
        - 연간 지속가능성 보고서 발간
        
        **개선 활동:**
        - 갭 분석 및 개선 방안 도출
        - 모범 사례 공유 및 확산
        - 외부 전문가 자문 활용
        
        **투명성 확보:**
        - 이해관계자 대상 정기 보고
        - 웹사이트 공개 및 소통
        - 제3자 검증 실시
        """)

# 실행 방법 섹션
elif selected_section == "실행 방법":
    st.header("4. 실행 방법")
    
    implementation_option = st.selectbox(
        "실행 영역 선택",
        ["환경 관리", "사회적 책임", "지배구조 개선", "혁신 관리"]
    )
    
    if implementation_option == "환경 관리":
        st.markdown("### 🌍 환경 관리 실행 방법")
        
        env_col1, env_col2 = st.columns(2)
        
        with env_col1:
            st.markdown("""
            #### 탄소 배출 관리
            **단계별 접근:**
            1. **현황 파악**: 탄소 배출량 측정 및 분석
            2. **목표 설정**: 감축 목표 및 일정 수립
            3. **실행 계획**: 구체적 감축 방안 실행
            4. **모니터링**: 지속적 추적 및 개선
            
            **구체적 방법:**
            - 에너지 효율 개선 프로젝트
            - 재생에너지 도입
            - 친환경 교통 수단 활용
            - 원격 근무 확대
            """)
        
        with env_col2:
            st.markdown("""
            #### 자원 효율성 향상
            **물 관리:**
            - 물 사용량 모니터링
            - 재활용 시스템 구축
            - 누수 방지 시스템 도입
            
            **폐기물 관리:**
            - 3R 원칙 (Reduce, Reuse, Recycle)
            - 순환 경제 모델 도입
            - 폐기물 분리수거 체계화
            
            **에너지 관리:**
            - 스마트 에너지 관리 시스템
            - LED 조명 교체
            - 건물 에너지 효율 개선
            """)
    
    elif implementation_option == "사회적 책임":
        st.markdown("### 🤝 사회적 책임 실행 방법")
        
        social_tabs = st.tabs(["직원 관리", "지역사회", "고객 관계"])
        
        with social_tabs[0]:
            st.markdown("""
            #### 👥 직원 관리
            
            **다양성 및 포용성:**
            - 다양한 배경의 인재 채용
            - 성별, 연령, 장애 등 차별 금지
            - 포용적 기업 문화 조성
            - 다양성 교육 프로그램 운영
            
            **복지 및 안전:**
            - 안전한 근무 환경 조성
            - 직원 건강 프로그램 운영
            - 일-생활 균형 지원
            - 스트레스 관리 프로그램
            
            **교육 및 개발:**
            - 체계적인 교육 훈련 프로그램
            - 경력 개발 경로 제공
            - 멘토링 시스템 운영
            - 평생 학습 문화 조성
            """)
        
        with social_tabs[1]:
            st.markdown("""
            #### 🏘️ 지역사회 기여
            
            **사회공헌 활동:**
            - 교육 지원 프로그램
            - 환경 보호 활동 참여
            - 취약계층 지원 사업
            - 문화 예술 후원 활동
            
            **지역 경제 활성화:**
            - 지역 업체 우선 구매
            - 지역 인재 채용 확대
            - 지역 기술 혁신 지원
            - 창업 지원 프로그램 운영
            
            **파트너십 구축:**
            - NGO와의 협력 사업
            - 정부 기관과의 협력
            - 학계와의 연구 협력
            - 국제 기구와의 협력
            """)
        
        with social_tabs[2]:
            st.markdown("""
            #### 🛍️ 고객 관계 관리
            
            **제품 안전성:**
            - 엄격한 품질 관리 시스템
            - 정기적인 안전성 테스트
            - 신속한 리콜 시스템
            - 고객 피드백 반영 체계
            
            **고객 만족:**
            - 고객 서비스 품질 향상
            - 고객 불만 처리 시스템
            - 고객 참여 프로그램
            - 맞춤형 서비스 제공
            
            **투명한 소통:**
            - 제품 정보 공개
            - 가격 정책 투명성
            - 고객 의견 수렴 채널
            - 정기적인 고객 설문조사
            """)

# 평가 지표 섹션
elif selected_section == "평가 지표":
    st.header("5. 평가 지표")
    
    st.markdown("### 5.1 핵심 성과 지표 (KPI)")
    
    kpi_category = st.selectbox(
        "지표 카테고리 선택",
        ["환경 지표", "사회 지표", "경제 지표", "지배구조 지표"]
    )
    
    if kpi_category == "환경 지표":
        st.markdown("#### 🌱 환경 성과 지표")
        
        env_metrics = {
            "탄소 배출량": {"단위": "tCO2e", "목표": "연간 5% 감소", "현황": "측정 중"},
            "에너지 효율": {"단위": "kWh/제품", "목표": "연간 3% 개선", "현황": "개선 중"},
            "물 사용량": {"단위": "㎥/제품", "목표": "연간 10% 감소", "현황": "추적 중"},
            "폐기물 재활용률": {"단위": "%", "목표": "85% 달성", "현황": "80%"},
            "재생에너지 비율": {"단위": "%", "목표": "50% 달성", "현황": "35%"}
        }
        
        for metric, data in env_metrics.items():
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric(metric, data["현황"])
            with col2:
                st.write(f"**단위**: {data['단위']}")
            with col3:
                st.write(f"**목표**: {data['목표']}")
            with col4:
                progress = 70 if "%" in data["현황"] else 60
                st.progress(progress)
    
    elif kpi_category == "사회 지표":
        st.markdown("#### 👥 사회 성과 지표")
        
        social_metrics = {
            "직원 만족도": {"단위": "점/5점", "목표": "4.5점 이상", "현황": "4.2점"},
            "안전사고 발생률": {"단위": "건/년", "목표": "0건", "현황": "2건"},
            "여성 관리자 비율": {"단위": "%", "목표": "30%", "현황": "25%"},
            "교육 시간": {"단위": "시간/인", "목표": "40시간", "현황": "35시간"},
            "지역사회 투자": {"단위": "억원", "목표": "10억원", "현황": "8억원"}
        }
        
        for metric, data in social_metrics.items():
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric(metric, data["현황"])
            with col2:
                st.write(f"**단위**: {data['단위']}")
            with col3:
                st.write(f"**목표**: {data['목표']}")
            with col4:
                progress = 75 if "%" in data["현황"] else 65
                st.progress(progress)
    
    elif kpi_category == "경제 지표":
        st.markdown("#### 💰 경제 성과 지표")
        
        economic_metrics = {
            "지속가능성 투자 ROI": {"단위": "%", "목표": "15%", "현황": "12%"},
            "친환경 제품 매출 비중": {"단위": "%", "목표": "40%", "현황": "30%"},
            "비용 절감 효과": {"단위": "억원", "목표": "50억원", "현황": "35억원"},
            "혁신 투자 비율": {"단위": "%", "목표": "5%", "현황": "4%"},
            "공급망 효율성": {"단위": "점/100점", "목표": "85점", "현황": "78점"}
        }
        
        for metric, data in economic_metrics.items():
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric(metric, data["현황"])
            with col2:
                st.write(f"**단위**: {data['단위']}")
            with col3:
                st.write(f"**목표**: {data['목표']}")
            with col4:
                progress = 80 if "%" in data["현황"] else 70
                st.progress(progress)
    
    elif kpi_category == "지배구조 지표":
        st.markdown("#### ⚖️ 지배구조 성과 지표")
        
        governance_metrics = {
            "이사회 독립성": {"단위": "%", "목표": "50%", "현황": "45%"},
            "윤리 교육 이수율": {"단위": "%", "목표": "100%", "현황": "95%"},
            "내부 감사 횟수": {"단위": "회/년", "목표": "12회", "현황": "10회"},
            "컴플라이언스 위반": {"단위": "건", "목표": "0건", "현황": "1건"},
            "투명성 지수": {"단위": "점/100점", "목표": "90점", "현황": "85점"}
        }
        
        for metric, data in governance_metrics.items():
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric(metric, data["현황"])
            with col2:
                st.write(f"**단위**: {data['단위']}")
            with col3:
                st.write(f"**목표**: {data['목표']}")
            with col4:
                progress = 85 if "%" in data["현황"] else 75
                st.progress(progress)

# 사례 연구 섹션
elif selected_section == "사례 연구":
    st.header("6. 사례 연구")
    
    case_study = st.selectbox(
        "사례 선택",
        ["글로벌 기업 A", "국내 기업 B", "중소기업 C", "스타트업 D"]
    )
    
    if case_study == "글로벌 기업 A":
        st.markdown("### 🌍 글로벌 기업 A: 탄소 중립 달성 사례")
        
        case_col1, case_col2 = st.columns(2)
        
        with case_col1:
            st.markdown("""
            #### 배경 및 도전 과제
            - **업종**: 제조업 (전자제품)
            - **규모**: 직원 50,000명, 매출 100조원
            - **도전**: 2030년 탄소 중립 달성 목표
            
            #### 추진 전략
            1. **재생에너지 전환**: 모든 사업장 100% 재생에너지 사용
            2. **에너지 효율화**: AI 기반 스마트 팩토리 구축
            3. **공급망 관리**: 협력사 탄소 배출 관리
            4. **제품 혁신**: 친환경 제품 개발 집중
            """)
        
        with case_col2:
            st.markdown("""
            #### 주요 성과
            - **탄소 배출량**: 2019년 대비 60% 감소
            - **재생에너지 비율**: 85% 달성
            - **에너지 효율**: 30% 향상
            - **비용 절감**: 연간 500억원 절약
            
            #### 핵심 성공 요인
            - 최고경영진의 강력한 의지
            - 전사적 참여 체계 구축
            - 기술 혁신과 투자
            - 이해관계자 협력
            """)
        
        st.success("**교훈**: 명확한 목표 설정과 체계적인 실행이 성공의 핵심")
    
    elif case_study == "국내 기업 B":
        st.markdown("### 🇰🇷 국내 기업 B: ESG 경영 혁신 사례")
        
        st.markdown("""
        #### 기업 개요
        - **업종**: 화학 기업
        - **규모**: 직원 15,000명, 매출 20조원
        - **특징**: ESG 경영을 통한 기업 가치 혁신
        
        #### 혁신 과정
        """)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            #### 1단계: 기반 구축
            - ESG 전담 조직 신설
            - 경영진 ESG 교육
            - 정책 및 가이드라인 수립
            - 이해관계자 맵핑
            """)
        
        with col2:
            st.markdown("""
            #### 2단계: 실행 강화
            - 친환경 제품 개발
            - 안전 관리 시스템 강화
            - 지역사회 사회공헌 확대
            - 지배구조 개선
            """)
        
        with col3:
            st.markdown("""
            #### 3단계: 성과 창출
            - ESG 평가 등급 상승
            - 주가 상승 효과
            - 우수 인재 영입
            - 글로벌 진출 확대
            """)
        
        st.info("**핵심 성과**: MSCI ESG 등급 B → AA 상승, 주가 50% 상승")

# 참고 자료 섹션
elif selected_section == "참고 자료":
    st.header("7. 참고 자료")
    
    reference_type = st.selectbox(
        "자료 유형",
        ["국제 기준", "국내 법규", "보고서", "도구 및 템플릿"]
    )
    
    if reference_type == "국제 기준":
        st.markdown("### 🌐 국제 기준 및 가이드라인")
        
        standards = {
            "UN Global Compact": {
                "설명": "유엔 글로벌 컴팩트 10대 원칙",
                "분야": "인권, 노동, 환경, 반부패",
                "링크": "https://www.unglobalcompact.org/"
            },
            "GRI Standards": {
                "설명": "글로벌 지속가능성 보고 표준",
                "분야": "경제, 환경, 사회 성과 보고",
                "링크": "https://www.globalreporting.org/"
            },
            "SASB Standards": {
                "설명": "지속가능회계기준위원회 표준",
                "분야": "산업별 지속가능성 회계 기준",
                "링크": "https://www.sasb.org/"
            },
            "TCFD": {
                "설명": "기후변화 관련 재무정보 공개 태스크포스",
                "분야": "기후변화 리스크 공시",
                "링크": "https://www.fsb-tcfd.org/"
            },
            "ISO 26000": {
                "설명": "사회적 책임 국제 표준",
                "분야": "사회적 책임 가이드라인",
                "링크": "https://www.iso.org/iso-26000-social-responsibility.html"
            }
        }
        
        for name, info in standards.items():
            with st.expander(f"📋 {name}"):
                st.markdown(f"""
                **설명**: {info['설명']}
                
                **적용 분야**: {info['분야']}
                
                **웹사이트**: {info['링크']}
                """)
    
    elif reference_type == "국내 법규":
        st.markdown("### 🇰🇷 국내 법규 및 정책")
        
        regulations = [
            "환경영향평가법",
            "저탄소 녹색성장 기본법",
            "지속가능발전법",
            "사회적 가치 기본법",
            "중대재해처벌법",
            "ESG 공시 의무화",
            "K-택소노미"
        ]
        
        for regulation in regulations:
            st.markdown(f"- **{regulation}**: 지속가능성 관련 주요 법규")
    
    elif reference_type == "보고서":
        st.markdown("### 📊 주요 보고서 및 연구")
        
        reports_col1, reports_col2 = st.columns(2)
        
        with reports_col1:
            st.markdown("""
            #### 글로벌 보고서
            - **UN SDGs Progress Report**: 지속가능발전목표 진행 상황
            - **World Economic Forum Global Risks Report**: 글로벌 리스크 분석
            - **McKinsey Sustainability Report**: 지속가능성 트렌드 분석
            - **PwC CEO Survey**: CEO 지속가능성 인식 조사
            
            #### 환경 관련 보고서
            - **IPCC Climate Change Report**: 기후변화 과학적 근거
            - **IEA Energy Transition Report**: 에너지 전환 현황
            - **CDP Climate Change Report**: 기업 탄소 공시 현황
            """)
        
        with reports_col2:
            st.markdown("""
            #### 국내 보고서
            - **한국거래소 ESG 정보공개 가이던스**: ESG 공시 가이드
            - **기업지배구조원 ESG 평가**: 국내 기업 ESG 평가
            - **지속가능발전위원회 K-SDGs**: 한국형 지속가능발전목표
            - **환경부 녹색경영 가이드**: 환경 경영 실무 가이드
            
            #### 산업별 보고서
            - **제조업 지속가능성 보고서**: 제조업 특화 가이드
            - **금융업 ESG 가이드**: 금융권 ESG 경영 방향
            - **IT업계 탄소중립 로드맵**: IT 기업 환경 전략
            """)
    
    elif reference_type == "도구 및 템플릿":
        st.markdown("### 🛠️ 실무 도구 및 템플릿")
        
        tools_tabs = st.tabs(["평가 도구", "계획 템플릿", "보고서 양식"])
        
        with tools_tabs[0]:
            st.markdown("""
            #### 📝 평가 도구
            
            **지속가능성 성숙도 평가 체크리스트**
            - 현재 지속가능성 수준 진단
            - 개선 영역 식별
            - 우선순위 설정 지원
            
            **ESG 리스크 평가 매트릭스**
            - 환경, 사회, 지배구조 리스크 분석
            - 리스크 수준 평가
            - 대응 방안 수립
            
            **이해관계자 분석 도구**
            - 주요 이해관계자 식별
            - 관심사항 및 영향력 분석
            - 참여 전략 수립
            """)
        
        with tools_tabs[1]:
            st.markdown("""
            #### 📋 계획 수립 템플릿
            
            **지속가능성 전략 계획서**
            - 비전 및 목표 설정
            - 실행 계획 수립
            - 예산 및 자원 배분
            
            **ESG 실행 로드맵**
            - 단계별 실행 계획
            - 마일스톤 설정
            - 책임자 지정
            
            **KPI 관리 대시보드**
            - 핵심 지표 설정
            - 진행 상황 추적
            - 성과 분석
            """)
        
        with tools_tabs[2]:
            st.markdown("""
            #### 📄 보고서 양식
            
            **지속가능성 보고서 템플릿**
            - GRI 기준 적용
            - 섹션별 작성 가이드
            - 데이터 수집 양식
            
            **ESG 성과 보고서**
            - 환경, 사회, 지배구조 성과
            - 정량적 지표 포함
            - 개선 계획 명시
            
            **이해관계자 보고서**
            - 이해관계자별 맞춤 보고
            - 핵심 메시지 전달
            - 투명성 확보
            """)

# 추가 기능들
st.divider()

# 유용한 링크 섹션
with st.expander("🔗 유용한 링크"):
    link_col1, link_col2, link_col3 = st.columns(3)
    
    with link_col1:
        st.markdown("""
        #### 국제 기구
        - [UN Global Compact](https://www.unglobalcompact.org/)
        - [GRI](https://www.globalreporting.org/)
        - [SASB](https://www.sasb.org/)
        - [TCFD](https://www.fsb-tcfd.org/)
        """)
    
    with link_col2:
        st.markdown("""
        #### 국내 기관
        - [한국거래소](https://www.krx.co.kr/)
        - [기업지배구조원](https://www.cgs.or.kr/)
        - [지속가능발전위원회](https://www.ncsd.go.kr/)
        - [환경부](https://www.me.go.kr/)
        """)
    
    with link_col3:
        st.markdown("""
        #### 평가 기관
        - [MSCI ESG](https://www.msci.com/esg)
        - [S&P Global ESG](https://www.spglobal.com/esg/)
        - [Sustainalytics](https://www.sustainalytics.com/)
        - [CDP](https://www.cdp.net/)
        """)

# 계산기 도구
with st.expander("🧮 지속가능성 계산기"):
    calc_type = st.selectbox("계산기 유형", ["탄소 배출량", "물 사용량", "에너지 효율", "ROI"])
    
    if calc_type == "탄소 배출량":
        st.subheader("탄소 배출량 계산기")
        
        calc_col1, calc_col2 = st.columns(2)
        
        with calc_col1:
            electricity = st.number_input("전력 사용량 (kWh/년)", value=0, min_value=0)
            gas = st.number_input("가스 사용량 (㎥/년)", value=0, min_value=0)
            oil = st.number_input("유류 사용량 (L/년)", value=0, min_value=0)
        
        with calc_col2:
            # 배출 계수 (단순화된 값)
            electricity_factor = 0.4781  # kgCO2/kWh
            gas_factor = 2.176  # kgCO2/㎥
            oil_factor = 2.58  # kgCO2/L
            
            total_emissions = (electricity * electricity_factor + 
                             gas * gas_factor + 
                             oil * oil_factor) / 1000  # tCO2로 변환
            
            st.metric("연간 총 배출량", f"{total_emissions:.2f} tCO2")
            st.metric("전력 배출량", f"{electricity * electricity_factor / 1000:.2f} tCO2")
            st.metric("가스 배출량", f"{gas * gas_factor / 1000:.2f} tCO2")
            st.metric("유류 배출량", f"{oil * oil_factor / 1000:.2f} tCO2")

# 체크리스트 도구
with st.expander("✅ 지속가능성 체크리스트"):
    st.subheader("지속가능성 실행 체크리스트")
    
    checklist_categories = {
        "환경": [
            "탄소 배출량 측정 및 관리",
            "에너지 효율 개선 계획",
            "재생에너지 도입 검토",
            "폐기물 관리 시스템 구축",
            "물 사용량 모니터링"
        ],
        "사회": [
            "직원 안전 보건 시스템",
            "다양성 및 포용 정책",
            "지역사회 기여 활동",
            "고객 만족도 관리",
            "공급망 윤리 관리"
        ],
        "지배구조": [
            "이사회 독립성 확보",
            "윤리 경영 시스템",
            "리스크 관리 체계",
            "투명성 보고 체계",
            "이해관계자 소통 채널"
        ]
    }
    
    for category, items in checklist_categories.items():
        st.markdown(f"#### {category} 영역")
        for item in items:
            st.checkbox(item, key=f"check_{category}_{item}")

# 푸터
st.divider()
st.markdown("""
<div style='text-align: center; color: #666; font-size: 0.9em;'>
    <p>본 가이드는 기업의 지속가능한 발전을 위한 참고 자료입니다.</p>
    <p>구체적인 실행 계획은 각 기업의 상황에 맞게 조정하여 적용하시기 바랍니다.</p>
    <p>© 2024 기업 지속 발전 가이드. 지속가능한 미래를 위한 첫 걸음.</p>
</div>
""", unsafe_allow_html=True)
