from google.cloud.bigquery import Client as GoogleBigQueryClient
from google.cloud import bigquery
from google.cloud.exceptions import NotFound

class Client(GoogleBigQueryClient):
    def __init__(self, project=None, credentials=None, _http=None):
        super().__init__(project=project, credentials=credentials, _http=_http)

    def create_bq_dataset(self, dataset_name: str, location: str = 'US'):
        dataset_ref = self.dataset(dataset_name)
        dataset = bigquery.Dataset(dataset_ref)
        dataset.location = location
        dataset = self.create_dataset(dataset)

    # full_table_name format: 'project_id.dataset_id.table_name'
    def check_bq_table_exist(self, full_table_name):
        """ This function check if a table exist in big query dataset of a project.
            full_table_name format: project_id.dataset_id.table_name
        """
        try:
            self.get_table(full_table_name)
        except NotFound:
            raise NotFound(f"The table {full_table_name} was not found")
