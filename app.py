import gradio as gr
from traffic_model import load_and_train_model, predict

# Load and train model
model = load_and_train_model("TrafficTwoMonth.csv")

def ui_predict(Time, Date, Day_of_the_week, CarCount, BikeCount, BusCount, TruckCount, Total):
    input_data = {
        'Time': Time,
        'Date': int(Date),
        'Day of the week': Day_of_the_week,
        'CarCount': int(CarCount),
        'BikeCount': int(BikeCount),
        'BusCount': int(BusCount),
        'TruckCount': int(TruckCount),
        'Total': int(Total)
    }
    try:
        prediction = predict(model, input_data)
        return f"Predicted Traffic Situation: {prediction}"
    except Exception as e:
        return f"Error: {str(e)}"

day_options = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

iface = gr.Interface(
    fn=ui_predict,
    inputs=[
        gr.Textbox(label="Time (e.g., 12:00:00 AM)"),
        gr.Number(label="Date (day of month)"),
        gr.Dropdown(day_options, label="Day of the Week"),
        gr.Number(label="Car Count", value=0, precision=0),
        gr.Number(label="Bike Count", value=0, precision=0),
        gr.Number(label="Bus Count", value=0, precision=0),
        gr.Number(label="Truck Count", value=0, precision=0),
        gr.Number(label="Total Traffic", value=0, precision=0)
    ],
    outputs="text",
    title="Traffic Situation Predictor",
    description="Enter traffic data to predict the traffic situation."
)

iface.launch()
