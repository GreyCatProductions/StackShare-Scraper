import os
import csv


def save_to_csv(data: dict, dir_path: str):
    os.makedirs(dir_path, exist_ok=True)
    file_path = os.path.join(dir_path, "one giant.csv")

    if "Name" not in data:
        raise ValueError("Data dictionary must contain a 'Name' key.")

    headers = list(data.keys())
    file_exists = os.path.exists(file_path)

    with open(file_path, mode="a" if file_exists else "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(headers)

        row = [data["Name"]]
        for key in headers[1:]:
            values = data[key]
            row.append(values if isinstance(values, list) else [values])

        writer.writerow(row)
