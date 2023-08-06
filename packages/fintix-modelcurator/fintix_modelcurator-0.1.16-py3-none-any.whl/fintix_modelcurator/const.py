import os
import sys

NoResult = None
NoError = None

DB_SCHEMA = "io_fintix"
DB_URL_KEY = "quarkus.datasource.jdbc.url"
DB_USER_KEY = "quarkus.datasource.username"
DB_PWD_KEY = "quarkus.datasource.password"

LOGFILE = "fintix.log"
if sys.platform == "win32":
    USERNAME = os.environ.get("USERNAME", None)
    FINTIX_HOME_DIR = os.path.join(os.environ.get("USERPROFILE", os.path.join("C:\\Users\\", USERNAME)), ".fintix")
    FINTIX_IO_DATA_DIR = os.path.join(FINTIX_HOME_DIR, "data")
    FINTIX_IO_LOG_DIR = os.path.join(FINTIX_HOME_DIR, "logs", "modelcurator")
else:
    FINTIX_IO_DATA_DIR = "/var/lib/fintix"
    FINTIX_IO_LOG_DIR = "/var/log/fintix"

LOCAL_DEPLOY_MODEL_REPO = os.path.join(FINTIX_IO_DATA_DIR, "models")

MILLISECOND_PER_UNIT = {
    "s": 1000,
    "m": 60 * 1000,
    "h": 60 * 60 * 1000,
    "d": 24 * 60 * 60 * 1000
}
