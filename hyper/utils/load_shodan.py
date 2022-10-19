from shodan.helpers import iterate_files, open_file, write_banner
from hyper.dashboard.models import device

def load_file(file_name):
    for banner in iterate_files(file_name):
        result = device()
        result.ip = banner['ip_str']
        result.country = banner['location']["country_code"]
        result.state = banner['location']["region_code"]
        result.coords = f"{banner['location']['latitude']},{banner['location']['longitude']}"
        result.save()
