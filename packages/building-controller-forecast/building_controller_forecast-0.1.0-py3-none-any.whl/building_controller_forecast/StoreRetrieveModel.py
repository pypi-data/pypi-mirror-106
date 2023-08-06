try:
    import unzip_requirements
except ImportError:
    pass
from src import DynamicImporter as dy
import config as cfg
module = cfg.environment["storeretrievemodule"]


def download_file(model_path):
    global module
    di = dy.DynamicImporter(module, "download_file")
    download_file = di.get_class()
    return download_file(model_path)


def upload_file(model,filepath):
    di = dy.DynamicImporter(module, "upload_file")
    upload_file = di.get_class()
    upload_file(model,filepath)
    return
