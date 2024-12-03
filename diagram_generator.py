import matplotlib.pyplot as plt
import os

def generate_methodology_diagram():
    # Ensure assets directory exists or create it
    output_dir = "assets"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Path to save the diagram
    output_path = os.path.join(output_dir, "methodology_diagram.png")

    # Generate a custom methodology diagram
    fig, ax = plt.subplots(figsize=(10, 6))

    # Creating a simple flowchart-like diagram (you can adjust this based on your logic)
    ax.annotate("Data Collection", xy=(0.1, 0.8), xytext=(0.1, 0.9),
                arrowprops=dict(arrowstyle='->', lw=1.5))
    ax.annotate("Data Preprocessing", xy=(0.3, 0.8), xytext=(0.3, 0.9),
                arrowprops=dict(arrowstyle='->', lw=1.5))
    ax.annotate("Data Analysis", xy=(0.5, 0.8), xytext=(0.5, 0.9),
                arrowprops=dict(arrowstyle='->', lw=1.5))
    ax.annotate("Visualization", xy=(0.7, 0.8), xytext=(0.7, 0.9),
                arrowprops=dict(arrowstyle='->', lw=1.5))

    # Add some labels for explanation
    ax.text(0.1, 0.75, "Collect Covid-19 Data", fontsize=12)
    ax.text(0.3, 0.75, "Clean & Process Data", fontsize=12)
    ax.text(0.5, 0.75, "Analyze Data", fontsize=12)
    ax.text(0.7, 0.75, "Display Visualizations", fontsize=12)

    ax.axis('off')  # Hide axes to make it look cleaner

    # Save the diagram to the assets folder
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()

    print(f"Methodology diagram saved at {output_path}")
