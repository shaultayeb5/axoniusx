from pipeline import run_pipeline
from utils import log

def main():
    log("Running pipeline...")
    df = run_pipeline()
    df.to_csv("output/features.csv", index=False)
    log(f"Finished! Processed {len(df)} rows.")

if __name__ == "__main__":
    main()
