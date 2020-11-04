from tensorflow import keras
from tensorflow.keras import layers, metrics
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split


class Model():
    def __init__(self):
        self.data_iris = datasets.load_iris()
        self.model = keras.Sequential()
        self.x_learn_iris = list()
        self.x_test_iris = list()
        self.y_learn_iris = list()
        self.y_test_iris = list()
        self.y_learn_output_list = list()
        self.y_test_output_list = list()
        self.epochs = 600

    def prepare_data(self):
        x_iris = self.data_iris["data"]
        y_iris = self.data_iris["target"]

        self.x_learn_iris, self.x_test_iris, self.y_learn_iris, self.y_test_iris = train_test_split(x_iris, y_iris, test_size=0.2, random_state=17)

        for i in range(len(self.y_learn_iris)):
            self.y_learn_output_list.append([0] * 3)
            self.y_learn_output_list[-1][self.y_learn_iris[i]] = 1

        for i in range(len(self.y_test_iris)):
            self.y_test_output_list.append([0] * 3)
            self.y_test_output_list[-1][self.y_test_iris[i]] = 1

    def networking(self):
        self.model.add(keras.Input(shape=(4,)))
        self.model.add(layers.Dense(3, activation='tanh'))
        self.model.add(layers.Dense(3, activation="softmax"))
        self.model.compile(optimizer="adam", loss="binary_crossentropy", 
                    metrics=["accuracy"])
        # self.model.summary()
        self.model.fit(x=np.array(self.x_learn_iris), y=np.array(self.y_learn_output_list),\
                       epochs=self.epochs, verbose=0)

    def testing(self):
        y_pred = self.model.predict(np.array(self.x_test_iris))
        print(y_pred)
        score = self.model.evaluate(np.array(self.x_test_iris), np.array(self.y_test_output_list))

    def prediction(self, data):
        y_pred = self.model.predict(data)
        # y_pred_list = y_pred.to_list()
        # print(np.where(y_pred == y_pred.max()))
        return np.where(y_pred == y_pred.max())[-1][0]

        


if __name__ == "__main__":
    m = Model()
    m.prepare_data()
    m.networking() 
    m.testing()
