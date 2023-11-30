import argparse
import json
import csv

def process_json_file(json_path):
    with open(json_path, 'r') as file:
        data = json.load(file)

    csv_path = json_path.replace('.json', '.csv')

    with open(csv_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write header
        csv_writer.writerow(['asn', 'filtering', 'confidence', 'source'])

        # Write data
        for asn, entries in data.items():
            for entry in entries:
                asn_value = entry.get('asn', asn)
                filter_type = entry.get('filter_type', 'unknown')
                
                # Convert percent to a 0 to 1 range
                percent = float(entry.get('percent', 0)) / 100.0
                
                source = entry.get('source', 'N/A')

                csv_writer.writerow([asn_value, filter_type, percent, source])

    print(f"CSV file has been created: {csv_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process JSON file and convert to CSV")
    parser.add_argument("json_path", help="Path to the JSON file")
    args = parser.parse_args()

    process_json_file(args.json_path)

