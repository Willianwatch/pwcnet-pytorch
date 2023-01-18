class Args:
    def __init__(self) -> None:
        self.maxdisp = 256
        self.fac = -1
        self.logname = "logname"
        self.database = "/"
        self.epochs = 300
        self.loadmodel = None
        self.savemodel = "./"
        self.retrain = False
        self.stage = "chairs"
        self.ngpus = 1