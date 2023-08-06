# SPDX-License-Identifier: MIT

from __future__ import absolute_import

import logging
import sys
from xml.etree import cElementTree as ET

from bandit.core import docs_utils

LOG = logging.getLogger(__name__)


def report(manager, fileobj, sev_level, conf_level, lines=-1):
    """Prints issues in XML format

    :param manager: the bandit manager object
    :param fileobj: The output file object, which may be sys.stdout
    :param sev_level: Filtering severity level
    :param conf_level: Filtering confidence level
    :param lines: Number of lines to report, -1 for all
    """

    issues = manager.get_issue_list(sev_level=sev_level, conf_level=conf_level)
    root = ET.Element("testsuite", name="bandit", tests=str(len(issues) or 1))

    for issue in issues:
        test = issue.test
        testcase = ET.SubElement(root, "testcase", classname=issue.fname, name=test)

        text = "Test ID: %s Severity: %s Confidence: %s\n%s\nLocation %s:%s"
        text = text % (
            issue.test_id,
            issue.severity,
            issue.confidence,
            issue.text,
            issue.fname,
            issue.lineno,
        )
        ET.SubElement(
            testcase,
            "error",
            more_info=docs_utils.get_url(issue.test_id),
            type=issue.severity,
            message=issue.text,
        ).text = text
    if not issues:
        testcase = ET.SubElement(root, "testcase", name="NO-ISSUES")
        ET.SubElement(testcase, "skipped", message="No issues found.")

    tree = ET.ElementTree(root)

    if fileobj.name == sys.stdout.name:
        fileobj = sys.stdout.buffer
    elif fileobj.mode == "w":
        fileobj.close()
        fileobj = open(fileobj.name, "wb")

    with fileobj:
        tree.write(fileobj, encoding="utf-8", xml_declaration=True)

    if fileobj.name != sys.stdout.name:
        LOG.info("JUnit output written to file: %s", fileobj.name)
