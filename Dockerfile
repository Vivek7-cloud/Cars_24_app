FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY cars_flask_app.py .

COPY models/xgb_car_price_model.pkl ./models/

EXPOSE 5000

CMD ["python", "cars_flask_app.py"]