import pandas as pd
import os
import sys

def create_directory_structure():
    """Create the necessary directories if they don't exist"""
    # 프로젝트 루트 디렉토리 경로 얻기
    root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    # 생성할 디렉토리 목록
    directories = [
        'data/raw',
        'data/processed', 
        'data/external',
        'notebooks',
        'src/data',
        'src/features',
        'src/visualization',
        'reports/figures'
    ]
    
    # 각 디렉토리 생성
    for directory in directories:
        dir_path = os.path.join(root_dir, directory)
        os.makedirs(dir_path, exist_ok=True)
        print(f"Directory checked/created: {dir_path}")

def download_titanic_data():
    """Download Titanic dataset from seaborn and save to data/raw"""
    try:
        # 프로젝트 루트 디렉토리 경로 얻기
        root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        
        # Load Titanic dataset from seaborn
        import seaborn as sns
        titanic_data = sns.load_dataset('titanic')
        
        # Create data directory if it doesn't exist
        create_directory_structure()
        
        # Save to CSV
        output_path = os.path.join(root_dir, 'data/raw/titanic.csv')
        titanic_data.to_csv(output_path, index=False)
        print(f"Data successfully downloaded and saved to {output_path}")
        print(f"Shape of the dataset: {titanic_data.shape}")
        
        # Basic info about the dataset
        print("\nBasic information about the dataset:")
        print(titanic_data.info())
        
        return titanic_data
        
    except Exception as e:
        print(f"Error downloading data: {str(e)}")
        return None

if __name__ == "__main__":
    # 스크립트 직접 실행 시 데이터 다운로드
    download_titanic_data()