import mosaik
import mosaik.util
import mosaik_influxdb

SIM_CONFIG = {
    'ExampleSim': {
        'python': 'simulator_mosaik:ExampleSim',
    },
    'Collector': {
        'cmd': 'python collector.py %(addr)s',
    },
   # 'influx': {
   #     'cmd': 'python influx-collector.py %(addr)s',
   # },
  'DB': {'python': 'mosaik_influxdb:MosaikInfluxDB'},

}
END = 10 * 60  # 10 minutes

# Create World
world = mosaik.World(SIM_CONFIG)

# Start simulators
examplesim = world.start('ExampleSim', eid_prefix='Model_')
collector = world.start('Collector', step_size=60)
influx = world.start('DB', step_size=60)


# Instantiate models
model = examplesim.ExampleModel(init_val=10)
monitor = collector.Monitor()
influx_monitor = influx.Database(influxDBHost='localhost', influxDBPort='8086', influxDBUser='', influxDBPass='',
                         influxDBName='influx_Unit_Test')

# Connect entities
world.connect(model, monitor, 'val', 'delta')
world.connect(model, influx_monitor, 'val', 'delta')
# Create more entities
more_models = examplesim.ExampleModel.create(2, init_val=5)
mosaik.util.connect_many_to_one(world, more_models, monitor, 'val', 'delta')
mosaik.util.connect_many_to_one(world, more_models, influx_monitor, 'val', 'delta')
# Run simulation
world.run(until=END)