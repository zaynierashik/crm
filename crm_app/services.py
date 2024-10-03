import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from django.db.models import Sum
from .models import Requirement
from .utils import get_exchange_rates  # Import the exchange rates function

def prepare_total_revenue_data():
    # Retrieve exchange rates
    exchange_rates = get_exchange_rates()

    # Aggregate the total revenue for each company
    company_revenue_data = (
        Requirement.objects.values('company')
        .annotate(total_revenue=Sum('price'))
        .order_by('company')
    )

    X = []
    y = []

    # Convert each company's total revenue to USD
    for item in company_revenue_data:
        company_id = item['company']
        total_revenue = item['total_revenue'] or 0
        
        # Convert all company's requirements to USD
        requirements = Requirement.objects.filter(company=company_id)
        total_revenue_usd = 0
        for req in requirements:
            conversion_rate = exchange_rates.get(req.currency, 1)
            total_revenue_usd += (req.price or 0) / conversion_rate
        
        X.append([len(requirements)])  # Using the number of requirements as a feature
        y.append(total_revenue_usd)  # Total revenue in USD

    X = np.array(X)
    y = np.array(y)

    print(f'Features (X) = {X}')
    print(f'Target (y) = {y}')
    return X, y

def train_total_revenue_prediction_model():
    X, y = prepare_total_revenue_data()

    # Check if we have enough data to train
    if len(X) < 2:
        print("Not enough data points to train the model.")
        return None

    # Split data into training and validation sets (e.g., 80% training, 20% validation)
    train_size = int(0.8 * len(X))
    X_train, X_val = X[:train_size], X[train_size:]
    y_train, y_val = y[:train_size], y[train_size:]

    # Create and train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict on the validation set
    y_pred = model.predict(X_val)

    # Calculate accuracy metrics
    mae = mean_absolute_error(y_val, y_pred)
    mse = mean_squared_error(y_val, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_val, y_pred)

    print(f"Mean Absolute Error (MAE): {mae}")
    print(f"Mean Squared Error (MSE): {mse}")
    print(f"Root Mean Squared Error (RMSE): {rmse}")
    print(f"R² Score: {r2}")

    return model

def predict_total_revenue():
    model = train_total_revenue_prediction_model()

    # Ensure the model was trained before attempting prediction
    if not model:
        return "Insufficient data for prediction."

    # Predict based on the current number of companies and their requirements
    company_count = Requirement.objects.values('company').distinct().count()
    predicted_revenue = model.predict([[company_count]])

    return predicted_revenue
