import os
import logging
import yaml
import requests
import shutil
import time
import json

blacksea_default_directory = '~/.blacksea'
blacksea_default_config_file_name = "/config.yaml"






def _get_logger():
    logger = logging.getLogger(__name__)
    log_format = '%(asctime)s %(name)s %(levelname)s: %(message)s'
    log_date_format = '%m/%d/%Y %I:%M:%S %p'
    logging.basicConfig(format=log_format,
                        datefmt=log_date_format,
                        )
    
    if os.getenv('CLI_LOG_LEVEL') is not None:
        logger.setLevel(os.getenv('CLI_LOG_LEVEL'))
    else:
        logger.setLevel(logging.INFO)

    return logger


def getConfigPath(name):
    env_dir = blacksea_default_directory + "/" + name
    config_path = os.path.expanduser(env_dir)
    return config_path

def add_environment(name,api_key,url):
    logger = _get_logger()

    

    config_path = getConfigPath(name)
    logger.debug(f"Adding env to folder {config_path}")

    config = {}
    config['name'] = name
    config['api_key'] = api_key
    config['url'] = url

    if os.path.exists(config_path):
        my_dir = os.path.expanduser(config_path)
        shutil.rmtree(my_dir)

    os.makedirs(config_path)
    config_file = config_path + blacksea_default_config_file_name

    

    with open(config_file, 'w') as outfile:
        yaml.dump(config, outfile, default_flow_style=False)

    
    return config


def delete_environment(name):
    logger = _get_logger()
    logger.debug(f"Deleting env {name}")
    config_path = getConfigPath(name)
    my_dir = os.path.expanduser(config_path)
    shutil.rmtree(my_dir)


def get_environment(name):
    logger = _get_logger()

    config_path = getConfigPath(name)
    config_file = config_path + blacksea_default_config_file_name
    if not os.path.exists(config_file):
        return None
    with open(config_file) as file:
        env_config = yaml.load(file, Loader=yaml.FullLoader)

    
    logger.debug(env_config)
    return env_config


def init():

    my_dir = os.path.expanduser(blacksea_default_directory)

    os.makedirs(my_dir,exist_ok=True)
    return True

def destroy():
    my_dir = os.path.expanduser(blacksea_default_directory)
    shutil.rmtree(my_dir,ignore_errors=True)

def _getHeader(environment):
    headers = {
        "X-API-KEY": environment['api_key'],
        "Accept": "application/json",
        "Content-Type": "application/json; charset=utf-8"

    }

    return headers

def submit_execution(execution_json,environment):
    logger = _get_logger()

    headers = _getHeader(environment)

    with open(execution_json, 'r') as file:
        data = json.load(file)

    execution_url = environment['url'] + "/v1/execution"
    logger.debug(f"Submitting execution to {execution_url}")
    #Submit Execution
    r = requests.post(execution_url, headers=headers, json=data)
    logger.debug(f"Response Status from API : {r.status_code}")
    if r.status_code != 201:        
        raise Exception(f'The submission returns {r.text}')

    response_data = r.json()
    execution_id = response_data['general']['executionId']
    logger.debug(f"Execution ID : {execution_id}" )

    return execution_id

def get_result(execution_id,environment):

    logger = _get_logger()

    headers = _getHeader(environment)

    result = {}

    execution_url = environment['url'] + "/v1/execution"

    r = requests.get(execution_url + "/" + execution_id, headers=headers)
    if r.status_code != 200:
        raise Exception(f'The submission returns {r.text}')

    response_data = r.json()
    status = response_data['general']['status']
    logger.debug(f"Execution Status : {status}")

    if status == "failed":
        logger.error(
            f"Fail Code : {response_data['general']['executionFailure']['failCode']}")
        logger.error(
            f"Fail Reason : {response_data['general']['executionFailure']['failReason']}")
        

    elif status == "succeeded":
        logger.info(
            f"Result Url : {response_data['general']['executionResult']['resultHttpUrl']}")

        url = response_data['general']['executionResult']['resultHttpUrl']
        
        result['url'] = url
        result['executionId'] = execution_id        
        result['environment'] = environment
        result['exec_start_time'] = response_data['general']['executionStartDateTime']
        result['exec_stop_time'] = response_data['general']['executionStopDateTime']
        result['raw_data'] = response_data
    else :
        pass

    result['status'] = status

    return result

    

            

def submit_execution_and_get_result(execution_json,environment):
    logger = _get_logger()

    execution_id = submit_execution(execution_json=execution_json,environment=environment)

    logger.debug(f"Execution ID: {execution_id}")
    
    execution_url = environment['url'] + "/v1/execution"
    headers = _getHeader(environment)
    
    while True:
        
        result = get_result(execution_id,environment)
        logger.debug(f"Result : {result['status']}")
        if result['status'] == "succeeded" or result['status'] == "failed":
            break
        
        logger.debug(f"Waiting...")
        time.sleep(1)

    return result




def download_file(url,environment):
    headers = _getHeader(environment=environment)
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, headers=headers,stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk:
                f.write(chunk)
    return local_filename

if __name__ == "__main__":
    ''' Do nothing '''
    
