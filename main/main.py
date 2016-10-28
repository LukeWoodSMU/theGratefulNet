from parsing.prepare_data import data_manager
from glob import glob
from RNN import RNN
import numpy as np

vocab_size = 2575

dm = data_manager(vocab_size=vocab_size)

for i in glob("../data/*"):
    dm.add_data(i)

model = RNN(word_dim = vocab_size)

x_train, y_train = dm.get_training_data()
# This is with a random loss
print("Expected loss: %f" % (np.log(vocab_size)))
print("Actual loss: %f" % (model.calculate_loss(x_train[:1000],y_train[:1000])))
for x, y in zip(x_train, y_train):
    model.train(x,y)
    print("Actual loss: %f" % (model.calculate_loss(x_train[:1000],y_train[:1000])))