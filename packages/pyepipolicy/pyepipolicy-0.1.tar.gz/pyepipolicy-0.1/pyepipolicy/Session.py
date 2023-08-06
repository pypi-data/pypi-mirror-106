import random

import requests
import json
from datetime import datetime
from datetime import timedelta
import copy
import inspect

class Session:
    def __init__(self, path):
        f = open(path)
        json_session = json.load(f)
        f.close()
        self.json_session = json_session

    def run(self, config, days=None):
        session = copy.deepcopy(self.json_session)

        if days is not None:
            start_day = datetime.strptime(session['features']['start_date'], '%Y-%m-%d').date()
            session['features']['end_date'] = (start_day + timedelta(days=days)).strftime("%Y-%m-%d")

        id = random.randint(0, 10**10)
        req = {
            "status": "start",
            "id": id,
            "name": "run" + str(id),
            "session": session
        }
        res = requests.post(config.connection_string, data=json.dumps(req))
        if res.status_code == 200:
            return SimulationResults(json.loads(res.content))
        else:
            raise Exception('Simulation error: ' + str(res))

    def get_intervention(self, intervention_name):
        interventions = self.json_session['interventions']
        for intervention in interventions:
            if intervention['name'] == intervention_name:
                return intervention

    def get_intervention_effect(self, intervention_name):
        intervention = self.get_intervention(intervention_name)
        return intervention['effect']

    def get_intervention_cost(self, intervention_name):
        intervention = self.get_intervention(intervention_name)
        return intervention['cost']

    def set_intervention_function(self, intervention_name, function, type):
        interventions = self.json_session['interventions']
        for intervention in interventions:
            if intervention['name'] == intervention_name:
                intervention[type] = inspect.getsource(function)

    def set_intervention_effect(self, intervention_name, function):
        self.set_intervention_function(intervention_name, function, 'effect')

    def set_intervention_cost(self, intervention_name, function):
        self.set_intervention_function(intervention_name, function, 'cost')
