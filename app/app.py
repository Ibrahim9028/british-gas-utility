

from flask import Flask, jsonify
import csv

app = Flask(__name__)


@app.route("/health")
def health():
    return "Application is healthy"


@app.route("/readings")
def readings():
    data = []

    with open("app/readings.csv", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data.append({
                "customer_id": row["customer_id"],
                "meter_id": row["meter_id"],
                "gas_kwh": float(row["gas_kwh"]),
                "electricity_kwh": float(row["electricity_kwh"])
            })

    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
