import requests
import pandas as pd
from insightspy.utils import single_spaced
import getpass

class PortalSession():
    def __init__(self, api_key = None, url = "https://insights.arpeggiobio.com"):
        session = requests.Session()
        self._session = session
        self.url = url
        if api_key is not None:
            self._update_credentials(api_key)
        

    def _update_credentials(self, access_token):
        self.access_token = access_token
        self._session.headers.update({'Authorization': 'Bearer {access_token}'})

    def _get(self, route, params = {}, expect_data = False):
        """Generic GET request

        Wrapper for generic get request to the Arpeggio portal

        Args:
            route (str): string for the route to call. Do not include the core domain
                (e.g. `https://insights.arpeggiobio.com`).
            params (dict): dictionary of parameters to pass to the route
            expect_data (bool): whether to expect data from the response

        Returns:
            result (dict): A dictionary `{status:status_code, response:requests.response}`
        """
        request = self._session.get(
            f'{self.url}/{route}',
            params = params
        )
        response = request.json()
        if request.status_code != 200:
            raise requests.exceptions.RequestException(
                single_spaced(f'{request.status_code}: {response["notification"]}'))
        if expect_data and response["data"] is None:
            raise ValueError(single_spaced(response["notification"]))
        return({"status":request.status_code, "response":response})

    def post(self, route, json = {}, expect_data = False):
        """Generic POST request

        Wrapper for generic POST request to the Arpeggio portal

        Args:
            route (str): string for the route to call. Do not include the core domain
                (e.g. `https://insights.arpeggiobio.com`).
            json (dict): dictionary of parameters to pass to the route in the body of the
                request as a json
            expect_data (bool): whether to expect data from the response

        Returns:
            result (dict): A dictionary `{status:status_code, response:requests.response}`
        """
        request = self._session.post(
            f'{self.url}/{route}',
            json = json
        )
        response = request.json()
        if request.status_code != 200:
            raise requests.exceptions.RequestException(
                single_spaced(f'{request.status_code}: {response["notification"]}'))
        if expect_data and response["data"] is None:
            raise ValueError(single_spaced(response["notification"]))
        return({"status":request.status_code, "response":response})

    def login(self, email = None, password = None, api_key = None, ):
        """Login to Arpeggio portal

        Logs in current session to the Arpeggio portal. All subsequent requests will be
        authenticated with these credentials. Will try the `api_key` first if
        specified. If `api_key` is not present can use the same `email` and `password`
        that is used to log in to the portal.

        Args:
            api_key (str): login key
            email (str): email used to login to the arpeggio portal
            password (str): password used to login to the arpeggio portal
        """
        if api_key is None:
            if email is not None and password is None:
                password = getpass.getpass()
            elif email is None and password is None:
                raise ValueError("Please specify login credentials")
            access_response = self.post("user/login", {'email' : email, "password": password}, True)
            self._update_credentials(access_response["response"]["data"]["token"])
        else:
            raise NotImplementedError("API key login not yet implemented")
        print("Login succeeded")

    def projects(self):
        """List projects

        Lists projects accessible withthin the current portal session. Project access is
        limited by user id.

        Returns:
            DataFrame: table of project descriptions and ids
        """
        out = [ {'project_id' : v["project_id"], "description": v["description"] }
            for k,v in self.post("project/retrieve", expect_data= True)["response"]["data"].items()]
        return(pd.DataFrame.from_dict(out))

    def set_project(self, project_id):
        """Set current project

        Limits resources available in the current session to those accessible from the
        specified `project_id`. See available project ids with
        :meth:`~PortalSession.projects`

        Args:
            project_id (int): project id.

        Returns: DataFrame: table of project descriptions and ids
        """
        self.post("project/session", {'project_id': project_id})

    def samples(self, tag_suffix = "_tag_dupl"):
        """List samples

        Lists samples accessible withthin the current portal session. Sample access is
        limited by user id and the current session project if one is set.

        Args:
            tag_suffix (str):  the suffix that is appended to the column name if a tag
                shares the same name as one of the columns in the core database used to
                describe the samples

        Returns:
            DataFrame: table of sample metadata
        """
        export_keys = ["sample_id", "description", "sample_type", "reference_genome",
            "revision_id", "tags"]
        out = [ {key: v[key] for key in export_keys}
            for v in self.post("sample/retrieve", {"tagsAsDict":True}, expect_data=True)["response"]["data"]]
        out = pd.DataFrame.from_dict(out)
        return(out.join(pd.DataFrame(out.pop('tags').values.tolist()), rsuffix = tag_suffix))

    def pipeline_revisions(self):
        """List available pipelines

        Lists pipelines accessible within the current portal session. Pipeline access is
        limited by user id and the current session project if one is set.

        Returns:
            DataFrame: table of pipeline metadata
        """
        return(pd.DataFrame.from_dict(
            self._get('pipelinesDb/project_pipelines_revisions')["response"]["data"]))

    def gene_tpm(self, sample_ids):
        if isinstance(sample_ids, int):
            sample_ids = [sample_ids]
        counts =  self.post(
            'sample/TPM',
            {"sample_ids": sample_ids, "minimal": True},
            expect_data=True)["response"]["data"]
        out = pd.DataFrame.from_dict(counts[0], orient = "index")
        return(out)


