import requests
from pprint import pprint
import json
import cowsay
import pyfiglet


def session_vcenter_vm():
    url = "http://x.x.x.x:8000/rest/com/"
    payload = {}
    headers = {
      'x-api-key': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
      'Authorization': 'Basic xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx==',
      'Content-Type': 'text/plain'
    }
    response = requests.request("POST", url, headers=headers, data = payload)
    return (response.text[10:42])

def list_vcenter_vm(session_id):
    url = "http://x.x.x.x:8000/rest/"
    payload = {}
    headers = {
      'Accept': 'application/json',
      'x-api-key': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
      'vmware-api-session-id': ' ',
      'Authorization': 'Basic xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx=='
    }
    headers['vmware-api-session-id'] = session_id
    response = requests.request("GET", url, headers=headers, data = payload)
    return(response.text)

def isilon_session():
    url = "http://x.x.x.x:8000/session/1/session"
    payload = "{\n\"username\": \"xxx\",\n\"password\": \"xxxxx\",\n\"services\": [\"platform\",\"namespace\"]\n}"
    headers = {
      'x-api-key': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
      'Content-Type': 'application/json',
      'Authorization': 'Basic xxxxxxxxxxxxxxxxxxxxxxxx'
    }
    response = requests.request("POST", url, headers=headers, data = payload)
    return(response.text)

def isilon_namspace():
    url = "http://x.x.x.x:8000/namespace/enterprise"
    payload = {}
    headers = {
      'x-api-key': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
      'Authorization': 'Basic xxxxxxxxxxxxxxxxxxxxxxxx'
    }
    response = requests.request("GET", url, headers=headers, data = payload)
    return(response.text)

def ansible():
    url = "http://x.x.x.x:8000/api/v1/hosts"
    payload = {}
    headers = {
    'x-api-key': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'Authorization': 'Basic xxxxxxxxxxxxxxxx'
    }
    response = requests.request("GET", url, headers=headers, data = payload)
    return(response.text)


if __name__ == "__main__":
    result = pyfiglet.figlet_format("Apigee", font = "starwars")
    print(result)
    session_id = session_vcenter_vm()
    result_vm = list_vcenter_vm(session_id)
    print(json.dumps(result_vm))
    cowsay.stegosaurus("List of vCenter VMs")
    #cowsay.tux("List of vCenter VMs")
    isilon_session()
    result_namespace = isilon_namspace()
    print(json.dumps(result_namespace))
    cowsay.stegosaurus("List of Isilon Namespace")
    #cowsay.dragon("List of Isilon Namespace")
    #cowsay.tux("List of Isilon Namespace")
    result_namespace1 = ansible()
    print(json.dumps(result_namespace1))
    cowsay.stegosaurus("List of Ansible Hosts")
