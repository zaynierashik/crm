import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.decomposition import PCA
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from .models import Company

def perform_kmeans_clustering(n_clusters=3):
    # Fetch data from the Company model
    queryset = Company.objects.select_related('sector', 'created_by').all()
    data = list(queryset.values('sector', 'city', 'country', 'state', 'address', 'created_by'))
    
    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    # Updated preprocessing pipelines for numeric and categorical data
    numeric_features = []  # Add any purely numeric fields if available
    categorical_features = ['sector', 'city', 'country', 'state', 'created_by']  # Treat 'sector' as categorical

    numeric_transformer = StandardScaler()
    categorical_transformer = OneHotEncoder(handle_unknown='ignore')

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features),
        ]
    )
    
    # Create the clustering pipeline
    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('pca', PCA(n_components=2)),  # Reducing dimensions to two for simplicity
        ('cluster', KMeans(n_clusters=n_clusters, random_state=42))
    ])
    
    # Perform clustering
    X = df[numeric_features + categorical_features]
    clusters = pipeline.fit_predict(X)
    
    # Save clusters back to the database or return for further analysis
    for idx, company in enumerate(queryset):
        company.cluster = clusters[idx]
        company.save()
    
    return clusters