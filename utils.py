import time 
import errno 
import logging

def waitZap2Start(zap, timeOut):
    version = None 

    for i in range(0, timeOut):
        try:
            version = zap.core.version 
            logging.debug("Zap version {}".format(version))
            logging.debug("Connexion en {} secondes".format(i))
            break 
        except IOError:
            time.sleep(1)

    if not version:
        raise IOError(errno.EIO, 'Impossible de co Zap après {} secondes'.format(timeOut))
