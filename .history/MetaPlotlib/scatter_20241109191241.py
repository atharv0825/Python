import matplotlib.pyplot as plt

def scatter_plot():
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    plt.scatter(x, y, color='blue', marker='o')
    plt.title("Scatter Plot")
    plt.show()

if __name__ == "__main__":
    scatter_plot()
