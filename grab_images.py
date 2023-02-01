



class Inventory:
    def __init__(self):
        self.field_name = None
        self.dicom_data = None

        """MAGIC NUMBERS"""
        self.SID = 1.5
        self.BB_Count = 5

        """Note DRR is the DRR.(Name) ie the FieldNameInput slice of DRR"""
        self.DRR = None
        self.DRR_Box_Centers = None
        self.DRR_BB_Centers = None
        self.DRR_BB_Radii = None
        self.DRR_BB_Sensitivity = None
        self.DRR_BB_EdgeThreshold = None

        """Note Portal is the Portal.(Name) ie the FieldNameInput slice of portal"""
        self.Portal = None
        self.Portal_Box_Centers = None
        self.Portal_BB_Centers = None
        self.Portal_BB_Radii = None
        self.Portal_BB_Sensitivity = None
        self.Portal_BB_EdgeThreshold = None

        self.MLC_Apertures = None