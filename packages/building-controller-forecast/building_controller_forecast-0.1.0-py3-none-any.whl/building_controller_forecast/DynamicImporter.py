
import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../")
import config as cfg
isaws = cfg.environment["isaws"]
folder = cfg.environment["path"]+"." if not isaws else ""
class DynamicImporter:
    """"""

    # ----------------------------------------------------------------------
    def __init__(self, module_name, class_name):
        """Constructor"""
        global folder
        self.module = __import__(folder+module_name,globals(),locals(),["create_features","train_model","predict_data"] )
        # sub_module = getattr(self.module,module_name)
        self.my_class = getattr(self.module, class_name)

    def get_class(self):
        return self.my_class
