from utils import log_message
from data_loader import load_data
from analytics import run_analysis
from visualization import plot_results

def main():
    log_message("Starting Cryptocurrency_Analytics_Platform...")

    # Load data
    data = load_data("data/raw/sample.csv")

    # Run analysis
    results = run_analysis(data)
    log_message(f"Analysis Results: {results}")

    # Visualize results
    plot_results(results)

    log_message("Pipeline finished successfully.")

if __name__ == "__main__":
    main()
