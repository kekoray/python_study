import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def Analysis(path="./log/log.txt"):
    with open("./log/log.txt", "r") as f:
        data_list = f.readlines()
    data_list = [i.strip() for i in data_list]
    data = [i.split("\t") for i in data_list]
    arr = np.array(data)
    df = pd.DataFrame(arr[:, 1], index=arr[:, 0], columns=["song"])
    record = df["song"].value_counts()
    return df, record


def Visualization(data):
    plt.figure()
    plt.bar(data.index, data.values)
    plt.xlabel("song")
    plt.ylabel("num")
    plt.show()


if __name__ == "__main__":
    _, df = Analysis()
    Visualization(df)
