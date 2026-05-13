import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def prepare_data(input_file, output_file):
    # 1. Load Data
    print(f"Loading data from {input_file}...")
    df = pd.read_csv(input_file)
    
    # 2. Encoding Categorical Variables
    # Mengubah 'gender' dan 'risk_level' menjadi numerik
    le = LabelEncoder()
    df['gender'] = le.fit_transform(df['gender'])
    
    # Mapping manual untuk risk_level agar urutannya bermakna (Ordinal)
    risk_mapping = {'Low': 0, 'Medium': 1, 'High': 2}
    df['risk_level'] = df['risk_level'].map(risk_mapping)
    
    # 3. Feature Scaling
    # Menyamakan skala untuk fitur numerik (kecuali target risk_level)
    features = df.drop(columns=['risk_level'])
    target = df['risk_level']
    
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    
    df_final = pd.DataFrame(scaled_features, columns=features.columns)
    df_final['risk_level'] = target.values
    
    # 4. Save Processed Data
    df_final.to_csv(output_file, index=False)
    print(f"Success! Model-ready data saved to {output_file}")
    print(f"Total records: {len(df_final)}")
    print(f"Columns: {list(df_final.columns)}")

if __name__ == "__main__":
    prepare_data('mental_health_clean.csv', 'mental_health_model_ready.csv')
