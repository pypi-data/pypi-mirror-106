# Copyright 2021 The Kubeflow Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Utilities functions KFP DSL."""

import re
from typing import Callable, List, Optional, Union

from kfp.components import _structures
from kfp.pipeline_spec import pipeline_spec_pb2

_COMPONENT_NAME_PREFIX = 'comp-'
_TASK_NAME_PREFIX = 'task-'
_EXECUTOR_LABEL_PREFIX = 'exec-'

# TODO: Support all declared types in
# components._structures.CommandlineArgumenType
_CommandlineArgumentType = Union[str, int, float,
                                 _structures.InputValuePlaceholder,
                                 _structures.InputPathPlaceholder,
                                 _structures.OutputPathPlaceholder,
                                 _structures.InputUriPlaceholder,
                                 _structures.OutputUriPlaceholder,]


def sanitize_component_name(name: str) -> str:
  """Sanitizes component name."""
  return _COMPONENT_NAME_PREFIX + _sanitize_name(name)


def sanitize_task_name(name: str) -> str:
  """Sanitizes task name."""
  return _TASK_NAME_PREFIX + _sanitize_name(name)


def sanitize_executor_label(label: str) -> str:
  """Sanitizes executor label."""
  return _EXECUTOR_LABEL_PREFIX + _sanitize_name(label)


def _sanitize_name(name: str) -> str:
  """Sanitizes name to comply with IR naming convention.

  The sanitized name contains only lower case alphanumeric characters and
  dashes.
  """
  return re.sub('-+', '-', re.sub('[^-0-9a-z]+', '-',
                                  name.lower())).lstrip('-').rstrip('-')


def get_value(value: Union[str, int, float]) -> pipeline_spec_pb2.Value:
  """Gets pipeline value proto from Python value."""
  result = pipeline_spec_pb2.Value()
  if isinstance(value, str):
    result.string_value = value
  elif isinstance(value, int):
    result.int_value = value
  elif isinstance(value, float):
    result.double_value = value
  else:
    raise TypeError(
        'Got unexpected type %s for value %s. Currently only support str, int '
        'and float.' % (type(value), value))
  return result


def remove_task_name_prefix(sanitized_task_name: str) -> str:
  """Removes the task name prefix from sanitized task name.

  Args:
    sanitized_task_name: The task name sanitized via `sanitize_task_name(name)`.

  Returns:
    The name with out task name prefix.

  Raises:
    AssertionError if the task name doesn't have the expected prefix.
  """
  assert sanitized_task_name.startswith(_TASK_NAME_PREFIX)
  return sanitized_task_name[len(_TASK_NAME_PREFIX):]


# TODO: share with dsl._component_bridge
def _input_artifact_uri_placeholder(input_key: str) -> str:
  return "{{{{$.inputs.artifacts['{}'].uri}}}}".format(input_key)


def _input_artifact_path_placeholder(input_key: str) -> str:
  return "{{{{$.inputs.artifacts['{}'].path}}}}".format(input_key)


def _input_parameter_placeholder(input_key: str) -> str:
  return "{{{{$.inputs.parameters['{}']}}}}".format(input_key)


def _output_artifact_uri_placeholder(output_key: str) -> str:
  return "{{{{$.outputs.artifacts['{}'].uri}}}}".format(output_key)


def _output_artifact_path_placeholder(output_key: str) -> str:
  return "{{{{$.outputs.artifacts['{}'].path}}}}".format(output_key)


def _output_parameter_path_placeholder(output_key: str) -> str:
  return "{{{{$.outputs.parameters['{}'].output_file}}}}".format(output_key)


def resolve_cmd_lines(cmds: Optional[List[_CommandlineArgumentType]],
                       is_output_parameter: Callable[[str], bool]) -> None:
  """Resolves a list of commands/args."""

  def _resolve_cmd(cmd: Optional[_CommandlineArgumentType]) -> Optional[str]:
    """Resolves a single command line cmd/arg."""
    if cmd is None:
      return None
    elif isinstance(cmd, (str, float, int)):
      return str(cmd)
    elif isinstance(cmd, _structures.InputValuePlaceholder):
      return _input_parameter_placeholder(cmd.input_name)
    elif isinstance(cmd, _structures.InputPathPlaceholder):
      return _input_artifact_path_placeholder(cmd.input_name)
    elif isinstance(cmd, _structures.InputUriPlaceholder):
      return _input_artifact_uri_placeholder(cmd.input_name)
    elif isinstance(cmd, _structures.OutputPathPlaceholder):
      if is_output_parameter(cmd.output_name):
        return _output_parameter_path_placeholder(cmd.output_name)
      else:
        return _output_artifact_path_placeholder(cmd.output_name)
    elif isinstance(cmd, _structures.OutputUriPlaceholder):
      return _output_artifact_uri_placeholder(cmd.output_name)
    else:
      raise TypeError('Got unexpected placeholder type for %s' % cmd)

  if not cmds:
    return
  for idx, cmd in enumerate(cmds):
    cmds[idx] = _resolve_cmd(cmd)
