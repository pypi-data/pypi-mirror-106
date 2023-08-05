"""Run flowgraph module, runs the temporary flowgraph located in temp/flowgraph.py

    Returns:
        time: time needed for flowgraph execution
        num_right: number of rightfully decoded messages
        num_dec: number of decoded messages
    """

import subprocess
import re
import time as td
import logging

_logger = logging.getLogger(__name__)


def profile_flowgraph(string_input, timeout, template):
    """
    Runs the actual flowgraph
    Args:
        template: template to use
        string_input: string input to verify against
        timeout : maximum number of seconds to let the flowgraph run

    Returns: the number of decoded messages

    """
    _logger.debug("Starting new flowgraph run")
    # set starttime
    start_time = td.time()
    # call bash script to exectue flowgraph
    subprocess.call("gr_lora_sdr_profiler/bash_scripts/run.sh {}".format(timeout), shell=True)
    time = td.time() - start_time
    subprocess.call("gr_lora_sdr_profiler/bash_scripts/convert.sh", shell=True)
    # open output for parsing processing
    with open("temp/out2.txt", "r") as file1:
        try:
            stdout = file1.readlines()
        except (RuntimeError, TypeError, NameError):
            _logger.error("Error reading the output of the run")
            stdout = "nothing"

    return parse_stdout(stdout, string_input, time, template)


def parse_stdout(stdout, string_input, time, template):
    """
    Parses the stdout file of the flowgraph runner to find the number
    of decoded and rightfully decoded messages

    Args:
        stdout ([lines]): output of stdout
        string_input ([string]): string to match against
        time (int): execeution time
        template (string) : template file to use

    Returns:
        [int]: number of rightlyfull decoded messages
    """
    # Number of rightlyfully decoded messages
    num_right = 0
    # Number of decoded messages
    num_dec = 0
    # for each line in stdout find the number of rightfull and decoded messages
    for out in stdout:
        try:
            line = str(out)
            re_text_right = "msg:" + str(string_input)
            out_right = re.search(re_text_right, line)
            re_text_dec = "msg:"
            out_dec = re.search(re_text_dec, line)
            # check if the search found match objects
            if out_right is not None:
                num_right = num_right + 1
            if out_dec is not None:
                num_dec = num_dec + 1
        except (RuntimeError, TypeError, NameError):
            _logger.error("Error in parsing from line %s of template %s", line, template)

    return num_right, num_dec, time
