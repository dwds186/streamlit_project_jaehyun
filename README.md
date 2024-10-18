# streamlit_project_jaehyun

# 📊 Loan Approval Prediction - 대출 승인 예측

이 프로젝트는 **Streamlit**을 사용하여 대출 승인 예측 데이터셋을 시각화하는 웹 애플리케이션입니다.  
주어진 데이터는 **loan_status**(승인 여부)로 표시된 이진 타겟 값을 예측하는 데 사용됩니다.

## 📁 데이터 설명

- **`train.csv`**: 대출 승인 여부 예측을 위한 학습 데이터셋입니다.
  - **loan_status**: 대출이 승인되었는지 여부를 나타내는 이진 값 (0 또는 1).
  - 그 외 다양한 수치형 및 범주형 특징(features)을 포함합니다.

## 🚀 주요 기능

1. **데이터 미리보기**  
   - 데이터셋의 첫 몇 행을 표 형태로 표시합니다.

2. **통계 요약 및 대출 상태 분포**  
   - 데이터의 기본 통계 정보와 **loan_status**의 분포를 막대 그래프로 시각화합니다.

3. **수치형 특징의 분포**  
   - 사용자가 선택한 수치형 변수의 히스토그램 및 KDE(Kernel Density Estimation) 그래프를 제공합니다.

4. **상관관계 히트맵**  
   - 수치형 변수들 간의 상관관계를 히트맵으로 시각화합니다.

## 🛠️ 설치 및 실행 방법

1. **필수 라이브러리 설치**
   ```bash
   pip install streamlit pandas seaborn matplotlib
