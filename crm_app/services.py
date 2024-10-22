import numpy as np
from sklearn.linear_model import LinearRegression
from django.db.models import Sum
from .models import Requirement, Company

def prepare_company_revenue_data():
    # Aggregate the revenue (sum of price) by company
    company_revenue_data = (
        Requirement.objects.values('company')
        .annotate(total_revenue=Sum('price'))
        .order_by('company')
    )

    # Extract features and targets for the model
    X = np.array([item['company'] for item in company_revenue_data]).reshape(-1, 1)
    y = np.array([item['total_revenue'] for item in company_revenue_data])

    print(f'Value of X = {X}')
    print(f'Value of Y = {y}')
    return X, y

def train_revenue_prediction_model():
    X, y = prepare_company_revenue_data()

    # Create and train the linear regression model
    model = LinearRegression()
    model.fit(X, y)

    return model

def predict_revenue_for_company(company_id):
    model = train_revenue_prediction_model()

    # Predict revenue for a specific company
    predicted_revenue = model.predict([[company_id]])

    return predicted_revenue