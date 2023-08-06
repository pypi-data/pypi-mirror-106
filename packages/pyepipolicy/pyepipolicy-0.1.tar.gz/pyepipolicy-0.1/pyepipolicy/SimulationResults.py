import json

class SimulationResults:
    def __init__(self, simulation_results):
        self.results = simulation_results

    def save(self, path):
        with open(path, 'w') as outfile:
            json.dump(self.results, outfile)

    def compartment(self, name, group_name="All"):
        """
        Returns a time series of all compartment values through the entire simulation
        """
        res = []
        for day in self.results:
            for compartment in day['result'][0]['compartments']:
                if compartment['compartment_name'] == name:
                    for group in compartment['groups']:
                        if group['group_name'] == group_name:
                            res.append(group['count'])
        return res

    def r0(self):
        """
        Returns a time series of all r0 values through the entire simulation
        """
        return [day['result'][0]['r_0'] for day in self.results]
