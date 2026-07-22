import matplotlib.pyplot as plt


def bar_chart(df, x, y, title=None):

    plt.figure(figsize=(10, 5))

    plt.bar(df[x], df[y])

    plt.title(title)

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()