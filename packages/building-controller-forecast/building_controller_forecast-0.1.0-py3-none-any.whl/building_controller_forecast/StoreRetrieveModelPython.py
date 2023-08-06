try:
    import unzip_requirements
except ImportError:
    pass
	
import pickle
import config as cfg


PROJECT_PATH = cfg.environment["projectpath"]
FOLDER = cfg.environment["path"]


def download_file(model_path):
    model_path = PROJECT_PATH + "\\"+FOLDER+ '\models\\' + model_path
    return pickle.load(open(model_path, "rb"))


def upload_file(model, filepath):
    model_path = PROJECT_PATH + "\\" + FOLDER+ '\models\\' + filepath
    with open(model_path, "wb") as f:
        pickle.dump(model,f)
    return
