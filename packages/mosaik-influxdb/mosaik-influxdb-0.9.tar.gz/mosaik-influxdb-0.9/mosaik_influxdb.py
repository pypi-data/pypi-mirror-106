"""
Store mosaik simulation data in an InfluxDB database.

"""
import collections
import pprint

import mosaik_api
from influxdb import InfluxDBClient
import json
import datetime
import random


__version__ = '1.0'
META = {
    'models': {
        'Database': {
            'public': True,
            'any_inputs': True,
            'params': ['influxDBHost', 'influxDBPort', 'influxDBUser', 'influxDBPass', 'influxDBName', 'influxTableName'],
            'attrs': [],
        },
    },
}

def uniqueid():
    seed = random.getrandbits(32)
    while True:
       yield seed
       seed += 1

class MosaikInfluxDB(mosaik_api.Simulator):
    def __init__(self):
        super().__init__(META)
        self.eid = None
        self.data = collections.defaultdict(lambda:
                                            collections.defaultdict(list))
        self.step_size = None

        self.influxDBconnection= None
        self.influxTableName= None

    def init(self, sid, step_size):
        self.step_size = step_size
        return self.meta


    def create(self, num, model, influxDBHost='localhost', influxDBPort='8086', influxDBUser='', influxDBPass='',influxDBName='influx_Test',influxTableName='influx_mosaik'):
        if num > 1 or self.eid is not None:
            raise RuntimeError('Can only create one instance of Monitor.')

        self.influxDBconnection = InfluxDBClient(host=influxDBHost, port=influxDBPort, username=influxDBUser,
                                                 password=influxDBPass)
        self.influxDBconnection.create_database(influxDBName)
        self.influxDBconnection.switch_database(influxDBName)

        self.influxTableName= influxTableName

        self.eid = 'Database'
        return [{'eid': self.eid, 'type': model}]

    def step(self, time, inputs):
        data = inputs[self.eid]

        json_body = [
            {"measurement": "influx_mosaik", "tags": {"Relation": "", "Simulator":"", "Entity":""}, "time": "%Y-%m-%d %H:%M:%S", "fields": ""}]
        json_body[0]['measurement'] = self.influxTableName

        # get new date and time
        now = datetime.datetime.now()

        for attr, values in data.items():
            for src, value in values.items():
                self.data[src][attr].append(value)
                # get unique id
                unique_sequence = uniqueid()
                id1 = next(unique_sequence)

                json_body[0]['time'] = now.strftime("%Y-%m-%d %H:%M:%S")

                if len(src.split('-')) == 2:
                    _simulator=src.split('.')[0]
                    _simulatortype = src.split('-')[0].split('-')[0]
                    _entitytype = src.split('-')[1].split('_')[0].split('.')[1]
                    _entity=src.split('.')[1]
                elif len(src.split('-')) == 3:
                    _source = src.split('-')[0:2]
                    _destination = src.split('-')[2]
                    _destinationtype = src.split('-')[2].split('_')[0]


                json_body[0]['tags'] = {"Relation": src, "id": id1, "Simulatior": _simulator, "Entity": _entity, "SimulatorType": _simulatortype, "EntityType": _entitytype}

                json_body[0]['fields'] = {str(attr): str(value)}
                self.influxDBconnection.write_points(json_body)

        return time + self.step_size

    def finalize(self):
        pass


def main():
    mosaik_api.start_simulation(MosaikInfluxDB())


if __name__ == '__main__':
    mosaik_api.start_simulation(MosaikInfluxDB())