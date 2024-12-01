# 타이타닉 생존 분석 프로젝트 구조

```
titanic_analysis/
├── data/
│   ├── raw/  
│   │   └── titanic.csv       # 원본 데이터
│   └── processed/  
│       └── titanic_processed.csv  # 전처리된 데이터
│
├── notebooks/
│   ├── 01_data_preprocessing.ipynb    # 데이터 전처리 노트북
│   ├── 02_eda.ipynb                   # 탐색적 데이터 분석 노트북
│   └── 03_ml_analysis.ipynb           # 머신러닝 분석 노트북
│
└─── venv/                     # 가상환경 (git에서는 제외)
```

## 주요 파일 및 디렉토리 설명

### 1. data/

- raw/: Seaborn에서 다운로드한 원본 타이타닉 데이터셋
- processed/: 전처리 완료된 데이터셋

### 2. notebooks/

- 01_data_preprocessing.ipynb: 데이터 클리닝 및 전처리
- 02_eda.ipynb: 탐색적 데이터 분석 및 시각화
- 03_ml_analysis.ipynb: 머신러닝 모델링 및 평가
