import numpy as np
from sklearn.linear_model import LinearRegression
from django.db.models import Sum
from .models import Requirement
from .utils import get_exchange_rates

def prepare_total_revenue_data():
    exchange_rates = get_exchange_rates()
    company_revenue_data = (Requirement.objects.values('company').annotate(total_revenue=Sum('price')).order_by('company'))

    X = []
    y = []
    company_ids = []
    for item in company_revenue_data:
        company_id = item['company']
        total_revenue = item['total_revenue'] or 0
        requirements = Requirement.objects.filter(company=company_id)
        total_revenue_usd = 0
        for req in requirements:
            conversion_rate = exchange_rates.get(req.currency, 1)
            total_revenue_usd += (req.price or 0) / conversion_rate
        
        X.append([len(requirements)])
        y.append(total_revenue_usd)
        company_ids.append(company_id)
    
    X = np.array(X)
    y = np.array(y)
    return X, y, company_ids

def train_total_revenue_prediction_model():
    X, y, company_ids = prepare_total_revenue_data()
    if len(X) < 2:
        print("Not enough data points to train the model.")
        return None, None

    model = LinearRegression()
    model.fit(X, y)
    return model, company_ids

def predict_total_revenue_for_all_companies():
    model, company_ids = train_total_revenue_prediction_model()
    if not model:
        return "Insufficient data for prediction."

    predictions = {}
    for company_id in company_ids:
        requirements_count = Requirement.objects.filter(company=company_id).count()
        predicted_revenue = model.predict([[requirements_count]])
        predictions[company_id] = predicted_revenue[0]
    
    return predictions