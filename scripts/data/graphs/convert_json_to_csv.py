import csv
import json
import argparse

def convert_json_to_csv(json_file_path, csv_file_path):
    # Load JSON data from file
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    # Open CSV file for writing
    with open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write header
        csv_writer.writerow(["subgraph", "policy", "percentage", "value", "trial"])

        # Write data to CSV
        for metric, metric_data in data.items():
            for _, entries in metric_data.items():
                for metric_name, thresholds in entries.items():
                    for threshold, values in thresholds.items():
                        # Determine the number of values
                        num_values = len(values)

                        # Write values and labels
                        for i in range(num_values):
                            csv_writer.writerow([metric, metric_name, threshold, values[i], i + 1])

    print(f"CSV file has been created at: {csv_file_path}")

if __name__ == "__main__":
    # Create command-line argument parser
    parser = argparse.ArgumentParser(description="Convert JSON to CSV")
    parser.add_argument("json_file", help="Path to the JSON file")
    #parser.add_argument("csv_file", help="Path to the CSV file to be created")

    # Parse command-line arguments
    args = parser.parse_args()
    csv_path = args.json_file.replace('.json', '.csv')

    # Call the function with the provided file paths
    convert_json_to_csv(args.json_file, csv_path)

