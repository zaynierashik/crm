import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.decomposition import PCA
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from .models import Company

def perform_kmeans_clustering(n_clusters=3):
    queryset = Company.objects.select_related('sector', 'created_by').all()
    data = list(queryset.values('sector', 'city', 'country', 'state', 'address', 'created_by'))
    df = pd.DataFrame(data)
    numeric_features = []
    categorical_features = ['sector', 'city', 'country', 'state', 'created_by']

    numeric_transformer = StandardScaler()
    categorical_transformer = OneHotEncoder(handle_unknown='ignore')
    preprocessor = ColumnTransformer(transformers=[('num', numeric_transformer, numeric_features), ('cat', categorical_transformer, categorical_features),])
    
    pipeline = Pipeline(steps=[('preprocessor', preprocessor), ('pca', PCA(n_components=2)),
        ('cluster', KMeans(n_clusters=n_clusters, random_state=42))
    ])
    
    X = df[numeric_features + categorical_features]
    clusters = pipeline.fit_predict(X)
    
    for idx, company in enumerate(queryset):
        company.cluster = clusters[idx]
        company.save()
    
    return clusters