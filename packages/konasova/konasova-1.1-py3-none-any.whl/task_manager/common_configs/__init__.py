import os
from .schema_common_api_conf import CommonApiConf
from .schema_db_conf import DBConf

BASE_CONFIG_DIR = os.path.join('.','configs')

DB_CONFIG_DIR = os.path.join(BASE_CONFIG_DIR, 'db_conf.ini')

COMMON_API_CONFIG_DIR = os.path.join(BASE_CONFIG_DIR, 'common_api_conf.ini')



mapping_type = {
    DB_CONFIG_DIR: DBConf,
    COMMON_API_CONFIG_DIR: CommonApiConf
}
