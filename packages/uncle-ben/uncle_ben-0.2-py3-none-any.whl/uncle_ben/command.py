from subprocess import getstatusoutput

from uncle_ben.logging import logger


def cmd(command):
    sts, output = getstatusoutput(command)
    logger.debug(f"[{command}] = ({sts}, {output})")
    if sts != 0:
        raise Exception(output)
    return output
