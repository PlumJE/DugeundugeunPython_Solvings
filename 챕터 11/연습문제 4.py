import pickle

file = open("test.dat", "wb")
pickle.dump(12, file)
pickle.dump(3.14, file)
pickle.dump([1, 2, 3, 4, 5], file)

file = open("test.dat", "rb")
for i in range(3):
    print(pickle.load(file))
