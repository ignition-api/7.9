"""SFC Functions.

The following functions give you access to interact with the SFCs in the
Gateway.
"""

from __future__ import print_function

__all__ = [
    "cancelChart",
    "getRunningCharts",
    "getVariables",
    "pauseChart",
    "redundantCheckpoint",
    "resumeChart",
    "setVariable",
    "setVariables",
    "startChart",
]

from typing import Any, AnyStr, Dict, Optional

from com.inductiveautomation.ignition.common import BasicDataset
from com.inductiveautomation.sfc.api import PyChartScope


def cancelChart(instanceId):
    # type: (AnyStr) -> None
    """Cancels the execution of a running chart instance.

    Any running steps will be told to stop, and the chart will enter
    Canceling state.

    Args:
        instanceId: The ID of the chart instance to cancel.
    """
    print(instanceId)


def getRunningCharts(charPath=None):
    # type: (Optional[AnyStr]) -> BasicDataset
    """Retrieves information about running charts.

    Can search all running charts, or be filtered charts at a specific
    path. This function will return charts that are in a Paused state.

    Args:
        charPath: The path to a chart to filter on: i.e.,
            "folder/chartName". If specified, only charts at the path
            will be included in the returned dataset. If omitted, the
            function will return data for all active charts.

    Returns:
        A dataset with information on the active chart.
    """
    print(charPath)
    return BasicDataset()


def getVariables(instanceId):
    # type: (AnyStr) -> PyChartScope
    """Get the variables in a chart instance's scope.

    Commonly used to check the value of a Chart Parameter, or determine
    how long the chart has been running for.

    Args:
        instanceId: The instance identifier of the chart.

    Returns:
        A python dictionary of variables. Step scopes for active steps
        are found under the "activeSteps" key.
    """
    print(instanceId)
    return PyChartScope()


def pauseChart(instanceId):
    # type: (AnyStr) -> None
    """Pauses a running chart instance.

    Any running steps will be told to pause, and the chart will enter
    Pausing state.

    Args:
        instanceId: The ID of the chart instance to pause.
    """
    print(instanceId)


def redundantCheckpoint(instanceId):
    # type: (AnyStr) -> None
    """Synchronizes chart and step variables of the specified chart
    instance across a redundant cluster, allowing the chart instance to
    continue where it left off if a redundant failover occurs.

    Args:
        instanceId: The instance identifier of the chart.
    """
    print(instanceId)


def resumeChart(instanceId):
    # type: (AnyStr) -> None
    """Resumes a chart that was paused.

    Steps which were previously paused will be resumed, and chart will
    enter Resuming state.

    Args:
        instanceId: The ID of the chart instance to resume.

    Raises:
        KeyError: If the ID does not match any running chart instance.
    """
    if not instanceId:
        raise KeyError("Invalid UUID string: {}".format(instanceId))


def setVariable(
    instanceId,  # type: AnyStr
    stepId,  # type: AnyStr
    variableName,  # type: AnyStr
    variableValue,  # type: Any
):
    # type: (...) -> None
    """Sets a variable inside a currently running chart.

    Args:
        instanceId: The instance identifier of the chart.
        stepId: The id for a step inside of a chart. If omitted the
            function will target a chart scoped variable.
        variableName: The name of the variable to set.
        variableValue: The value for the variable to be set to.
    """
    print(instanceId, stepId, variableName, variableValue)


def setVariables(
    instanceId,  # type: AnyStr
    stepId,  # type: AnyStr
    variableMap,  # type: Dict[AnyStr, Any]
):
    # type: (...) -> None
    """Sets any number of variables inside a currently running chart.

    Args:
        instanceId: The instance identifier of the chart.
        stepId: The id for a step inside of a chart. If omitted
            the function will target a chart scoped variable.
        variableMap: A dictionary containing the name:value pairs
            of the variables to set.
    """
    print(instanceId, stepId, variableMap)


def startChart(
    path,  # type: AnyStr
    arguments,  # type: Dict[AnyStr, Any]
):
    # type: (...) -> AnyStr
    """Starts a new instance of a chart.

    The chart must be set to "Callable" execution mode.

    Args:
        path: The path to the chart, for example:
            "ChartFolder/ChartName".
        arguments: A dictionary of arguments. Each key-value pair in the
            dictionary becomes a variable in the chart scope and will
            override any default.

    Returns:
        The unique ID of this chart.
    """
    print(path, arguments)
    return "UUID"
