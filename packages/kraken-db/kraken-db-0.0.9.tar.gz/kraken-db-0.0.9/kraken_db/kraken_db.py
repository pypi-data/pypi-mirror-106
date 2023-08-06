from kraken_g_api.kraken_firestore import Kraken_firestore as KF
from kraken_g_api.kraken_storage import Kraken_storage as KS
import json

class Kraken_db:

    def __init__(self, key_location = 'key.json', project_id = 'kraken-v1'):
        """ Initialization of class
		"""
        
        self.kf = KF(key_location, project_id)
        self.ks = KS(key_location)

        self.base_path = 'v1/'


    def get(self, record_type, record_id):

        record = self.get_from_ks(record_type, record_id)

        return record
    

    def get_from_ks(self, record_type, record_id):

        path = self.base_path + '/' + record_type + '/' + record_id + '.json'
        content = self.ks.get(path)
        record = json.loads(content)

        return record


    def post(self, record_type, record_id, record):
        """ Post a record to kraken db
        """

        self.post_to_kf(record_type, record_id, record)
        self.post_to_ks(record_type, record_id, record)

        return


    def post_to_ks(self, record_type, record_id, record):

        content = json.dumps(record, default=str, indent = 4)

        path = self.base_path + '/' + record_type + '/' + record_id + '.json'

        self.ks.post(path, content)

        return


    def post_to_kf(self, record_type, record_id, record):

        path = record_type + '/' + record_id

        self.kf.post(path, record)
        return