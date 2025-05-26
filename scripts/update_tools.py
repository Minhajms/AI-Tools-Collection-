import requests
import pandas as pd

def verify_links(csv_file):
    df = pd.read_csv(csv_file)
    for index, row in df.iterrows():
        try:
            response = requests.head(row['Link'], timeout=5)
            if response.status_code != 200:
                print(f"Invalid link for {row['Tool']}: {row['Link']}")
        except requests.RequestException:
            print(f"Error checking {row['Tool']}: {row['Link']}")

if __name__ == "__main__":
    verify_links("data/ai_tools.csv")
