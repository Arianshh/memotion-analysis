import pickle


def load_pickled_obj(name, add):
    with open(add + name + '.pkl', 'rb') as f:
        return pickle.load(f)


def save_pickled_obj(obj, name, add):
    with open(add + name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
