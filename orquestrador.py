from ibm_watson import DiscoveryV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from requests.auth import HTTPBasicAuth
from ibm_cloud_sdk_core.api_exception import ApiException

import json
import csv
import requests
import numpy as np
import pandas as pd

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


def askDiscovery(pergunta):

    apikey = 'ZFd4ATmFd2zfGPcOIb14krOmYpX3yTEgum4jromwb1I1'
    collection_id = 'd36fe302-d108-48be-8a07-87d7c0a958b3'
    environment_id = '8aedd3e9-c7c1-4bc7-b9dd-4425ebbfc980'
    url = 'https://api.eu-de.discovery.watson.cloud.ibm.com/instances/abd52fa4-a3a7-4f45-bba2-cfc8f08bc135'
    version = '2019-04-30'


    authenticator = IAMAuthenticator(apikey)
    auth = HTTPBasicAuth('apikey', apikey)
    discovery = DiscoveryV1(
        version=version,
        authenticator=authenticator
    )

    headers = {
        'content-type': "application/json"
        }
        
    discovery.set_service_url(url)



    # url = 'postgresql://hlwgjrahxtmpnf:216297ca385f774aed9e96542a69498b0c54821ed7408a56119f48c242572d03@ec2-3-225-204-194.compute-1.amazonaws.com:5432/d4jndugd7upmbt'


    # engine = create_engine(url, echo = False)
    # db = scoped_session(sessionmaker(bind=engine))

    # #dataframe = pd.read_sql('dataframe',engine)

    result = discovery.query(environment_id=environment_id, collection_id=collection_id, deduplicate=False, highlight=True, passages=True, passages_count=5, natural_language_query= pergunta, count=5)
    
    

    return result.get_result()["passages"]


print(askDiscovery("curricularização"))

              
            
            