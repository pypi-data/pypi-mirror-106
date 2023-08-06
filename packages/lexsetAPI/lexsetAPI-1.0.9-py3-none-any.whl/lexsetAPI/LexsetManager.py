import requests
import json
import yaml
import base64

class simulation:
    simPath = './path.yaml'
    token = "x9123z"
    numImages = 100
    simID = 111
    dataID = 111
    simEncodedstr = 'tempEncode'
    datasetURL ="./path.zip"
    isComplete = False
    dataSetItems = ""

    def _init_(self): #set global variables
        self.token = token
        self.numImages = numImages
        self.simID = simID
        self.dataID = dataID
        self.simPath = simPath
        self.simEncodedstr = simEncodedstr
        self.datasetURL = datasetURL
        self.isComplete = False
        self.dataSetItems = ""

    def createSimulation(self):
        url = "https://lexsetapi.azurewebsites.net/api/Simulations/NewSimulation"

        #Encode config
        with open(self.simPath) as fast:
            simString = json.dumps(yaml.load(fast))
            simEncoded = base64.b64encode(simString.encode("utf-8"))
            self.simEncodedstr = str(simEncoded, "utf-8")

        payload = json.dumps({
          "id": 0,
          "userid": 1,
          "simulationconfig": self.simEncodedstr,
          "randomseed": 1,
          "renderjobid": 0,
          "imagecount": self.numImages
        })
        headers = {
          'Authorization': 'Bearer ' + self.token,
          'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        parseResponse = json.loads(response.text)
        print("Response:")
        print(response.text)

        #save simulation ID and dataset ID
        self.simID = parseResponse["id"]
        self.dataID = parseResponse["datasetid"]

    def startSimulation(self):
        url = "https://lexsetapi.azurewebsites.net/api/Simulations/StartSimulation?id=" + str(self.simID)

        payload={}
        headers = {
        'Authorization': 'Bearer ' + self.token
        }

        response = requests.request("POST", url, headers=headers, data=payload)

    def getStatus(self):
        url = "https://lexsetapi.azurewebsites.net/api/simulations/getsimulationstatus?id=" + str(self.simID)

        payload={}
        headers = {
        'Authorization': 'Bearer ' + self.token
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        parseResponse = json.loads(response.text)
        self.isComplete = parseResponse["isComplete"]

    def getDatasetItems(self):
        url = "https://lexsetapi.azurewebsites.net/api/datasetitems/getdatasetitems?dataset_id=" + str(self.dataID)

        payload={}
        headers = {
        'Authorization': 'Bearer ' + self.token
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        parseResponse = json.loads(response.text)
        self.dataSetItems = json.loads(response.text)

    def stopSimulation(self):
        url = "https://lexsetapi.azurewebsites.net/api/simulations/stopsimulation?id=" + str(self.simID)

        payload={}
        headers = {
        'Authorization': 'Bearer ' + self.token
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

    def downloadData(self):
        url = "https://lexsetapi.azurewebsites.net/api/datasets/getdatasetarchives?dataset_id=" + str(self.dataID)

        payload={}
        headers = {
        'Authorization': 'Bearer ' + self.token
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)
        parseResponse = json.loads(response.text)
        print("Response:")
        print(response.text)
        self.datasetURL = parseResponse[0]["url"]
