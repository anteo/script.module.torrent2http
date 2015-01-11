
class Error(Exception):
    TORRENT_ERROR = 12
    UNKNOWN_PLATFORM = 1
    XBMC_HOME_NOT_DEFINED = 2
    NOEXEC_FILESYSTEM = 3
    REQUEST_ERROR = 5
    INVALID_DOWNLOAD_PATH = 6
    BIND_ERROR = 7
    POPEN_ERROR = 8
    PROCESS_ERROR = 9
    TIMEOUT = 10
    INVALID_FILE_INDEX = 11

    def __init__(self, message, code=0, **kwargs):
        self.message = message
        self.code = code
        self.kwargs = kwargs

    def __str__(self):
        return self.message