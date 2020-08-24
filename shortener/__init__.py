VERSION = (0, 1, 1, "final", 0)

VERSION_STR = ".".join(["%02d" % (i,) for i in VERSION[:2]])


def get_version():
    version = '%s.%s' % (VERSION[0], VERSION[1])
    if VERSION[2]:
        version = '%s.%s' % (version, VERSION[2])
    if VERSION[3] == 'alpha':
        version = '%s-alpha.%s' % (version, VERSION[4])
    else:
        if VERSION[3] != 'final':
            version = '%s %s %s' % (version, VERSION[3], VERSION[4])
    return version

__version__ = get_version()
