

class DataLoader:
    """
    loads chunks of FHIR data in groups of batch_size
    subject to filter
    """
    def __init__(self, filter, data_path, batch_size, group_patient_data=False):
        """
        params:
        filter: fhirclient.datalaoder.Filter object which defines what data to keep
        data_path: path to data folder
        batch_size: int
        """
        pass

