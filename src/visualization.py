import matplotlib.pyplot as plt

def plot_results(results: dict):
    """Plot a simple bar chart of numeric results."""
    metrics = {k: v for k, v in results.items() if isinstance(v, (int, float))}
    if not metrics:
        print("No numeric results to plot.")
        return

    plt.bar(metrics.keys(), metrics.values())
    plt.title("Cryptocurrency Analytics Summary")
    plt.show()
