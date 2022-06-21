import os
import json
import fhirclient.models.bundle as bun


class DataLoader:
    """
    loads chunks of FHIR data in groups of batch_size
    subject to filter
    """
    def __init__(self, filt, data_path, batch_size):
        """
        params:
        filt: fhirclient.dataloader.Filter object which defines what data to keep
        data_path: path to data folder
        batch_size: int
        """
        self.filt = filt
        self.data_path = data_path
        self.batch_size = batch_size
        self.files = os.listdir(data_path)

    def __getitem__(self, index):
        """
        returns a batch of data
        """
        batch = []
        for i in range(index * self.batch_size, (index + 1) * self.batch_size):
            if i >= len(self.files):
                break
            with open(self.data_path + '/' + self.files[i], 'r') as json_file:
                data = json.load(json_file)
            bundle_obj = bun.Bundle(jsondict=data, strict=False)
            filtered_bundle = self.filt.filter(bundle_obj)
            batch.append(filtered_bundle)
        return batch

    def __len__(self):
        return len(self.files) // self.batch_size


class Filter:
    """
    given a fhirclient.models.bundle.Bundle remove data (or set to None)
    based on criteria stored in this object
    """
    def __init__(self, resource_types, data_types, keep_paths=None, remove_paths=None):
        """
        params:
        resource_types: list of fhirclient.models.resource.Resource subclass names to use
        data_types: list of fhirclient.filter.DATATYPE constants to use
        keep_paths: list of paths to keep no matter what
        remove_paths: list of paths to remove no matter what
        """
        self.resource_types = resource_types
        self.data_types = data_types
        self.keep_paths = keep_paths
        self.remove_paths = remove_paths

    def filter(self, bundle):
        """
        params:
        bundle: fhirclient.models.bundle.Bundle object to filter
        returns: fhirclient.models.bundle.Bundle object with filtered data
        """
        for entry in bundle.entry:
            if type(entry.resource) not in self.resource_types:
                bundle.entry.remove(entry)
            else:
                bundle.entry.resoruce = self.filter_resource(entry.resource)

        return bundle


    def filter_resource(self, resource):


