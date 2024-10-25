import pandas as pd
from sklearn.cluster import KMeans
from .models import Company

def perform_kmeans_clustering(n_clusters=3):
    # Fetch data from the Company model
    queryset = Company.objects.select_related('sector').all()
    data = list(queryset.values('sector', 'city', 'country'))  # Retrieves sector ID if it's a ForeignKey
    
    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    # Convert categorical data to numerical (encoding)
    df['city'] = df['city'].astype('category').cat.codes
    df['country'] = df['country'].astype('category').cat.codes

    # Prepare data for clustering
    X = df[['sector', 'city', 'country']].values

    # Perform K-Means clustering
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(X)
    
    # Assign clusters to companies
    clusters = kmeans.labels_

    # Save the clusters back to the database or use for further analysis
    for idx, company in enumerate(queryset):
        company.cluster = clusters[idx]
        company.save()
    
    return clusters