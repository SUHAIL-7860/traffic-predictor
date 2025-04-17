# Traffic Situation Predictor

This is a machine learning-based web application that predicts traffic situations based on given input parameters like vehicle counts, time, and day of the week.

---

## 🛠 Technologies Used

- **Python** 🐍
- **Gradio** – for building the web-based interface
- **Pandas** – for data manipulation
- **Scikit-learn** – for building and training the machine learning model

---

## 📁 Project Structure

- `app.py`: Main application that launches a Gradio interface for prediction.
- `traffic_model.py`: Contains model training and prediction logic.
- `TrafficTwoMonth.csv`: (Required) A CSV dataset with traffic data used to train the model. *Note: This file is not included in the current package.*
- `README.md`: Documentation of the project.

---

## ⚙️ How It Works

1. **Time Preprocessing**: Converts input time like `12:00:00 AM` into minutes since midnight.
2. **Feature Engineering**: Applies one-hot encoding to the day of the week and uses vehicle counts and time as numeric features.
3. **Model**: A `RandomForestClassifier` is trained on historical traffic data.
4. **Prediction**: Based on the input values, the model predicts the traffic situation (e.g., Heavy, Moderate, Light).

---

## 🚀 Getting Started

### 1. Clone or Download

Download or clone this repo. Make sure `app.py`, `traffic_model.py`, and your dataset (`TrafficTwoMonth.csv`) are in the same directory.

### 2. Install Requirements

```bash
pip install gradio pandas scikit-learn
```

### 3. Run the Application

```bash
python app.py
```

The Gradio interface will launch in your browser where you can input traffic data.

---

## 🧪 Example Input

- Time: `08:30:00 AM`
- Date: `14`
- Day of the Week: `Tuesday`
- Car Count: `120`
- Bike Count: `80`
- Bus Count: `15`
- Truck Count: `10`
- Total Traffic: `225`

### 📤 Output

```text
Predicted Traffic Situation: Heavy
```

---

## 🧠 Model Details

- **Algorithm**: Random Forest Classifier
- **Preprocessing**: One-Hot Encoding for categorical data
- **Evaluation**: You can add accuracy or F1-score by evaluating on test data

---

## 📌 Notes

- Ensure the dataset `TrafficTwoMonth.csv` is present in the same directory as `app.py`.
- The app is designed to be lightweight and easily extendable.

---

## 📝 License

This project is for educational purposes. You can modify and use it freely.

---

## 👨‍💻 Author

Developed by [Mohd. Suhail]
