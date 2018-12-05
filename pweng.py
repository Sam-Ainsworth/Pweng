import core
import core.server
    
CONFIG = core.load_config()
core.register_controllers()

core.server.start_server(CONFIG['host'],CONFIG['port'])


