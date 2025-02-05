# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class JobSpecification(Model):
    """Specifies details of the jobs to be created on a schedule.

    :param priority: The priority of jobs created under this schedule.
     Priority values can range from -1000 to 1000, with -1000 being the
     lowest priority and 1000 being the highest priority. The default value
     is 0.
    :type priority: int
    :param display_name: The display name for jobs created under this
     schedule. It need not be unique and can contain any Unicode characters
     up to a maximum length of 1024.
    :type display_name: str
    :param uses_task_dependencies: The flag that determines if this job will
     use tasks with dependencies.
    :type uses_task_dependencies: bool
    :param constraints: The execution constraints for jobs created under this
     schedule.
    :type constraints: :class:`JobConstraints
     <azure.batch.models.JobConstraints>`
    :param job_manager_task: The details of a Job Manager task to be launched
     when a job is started under this schedule.
    :type job_manager_task: :class:`JobManagerTask
     <azure.batch.models.JobManagerTask>`
    :param job_preparation_task: The Job Preparation task for jobs created
     under this schedule.
    :type job_preparation_task: :class:`JobPreparationTask
     <azure.batch.models.JobPreparationTask>`
    :param job_release_task: The Job Release task for jobs created under this
     schedule.
    :type job_release_task: :class:`JobReleaseTask
     <azure.batch.models.JobReleaseTask>`
    :param common_environment_settings: A list of common environment variable
     settings. These environment variables are set for all tasks in jobs
     created under this schedule (including the Job Manager, Job Preparation
     and Job Release tasks).
    :type common_environment_settings: list of :class:`EnvironmentSetting
     <azure.batch.models.EnvironmentSetting>`
    :param pool_info: The pool on which the Batch service runs the tasks of
     jobs created under this schedule.
    :type pool_info: :class:`PoolInformation
     <azure.batch.models.PoolInformation>`
    :param metadata: A list of name-value pairs associated with each job
     created under this schedule as metadata.
    :type metadata: list of :class:`MetadataItem
     <azure.batch.models.MetadataItem>`
    """ 

    _attribute_map = {
        'priority': {'key': 'priority', 'type': 'int'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'uses_task_dependencies': {'key': 'usesTaskDependencies', 'type': 'bool'},
        'constraints': {'key': 'constraints', 'type': 'JobConstraints'},
        'job_manager_task': {'key': 'jobManagerTask', 'type': 'JobManagerTask'},
        'job_preparation_task': {'key': 'jobPreparationTask', 'type': 'JobPreparationTask'},
        'job_release_task': {'key': 'jobReleaseTask', 'type': 'JobReleaseTask'},
        'common_environment_settings': {'key': 'commonEnvironmentSettings', 'type': '[EnvironmentSetting]'},
        'pool_info': {'key': 'poolInfo', 'type': 'PoolInformation'},
        'metadata': {'key': 'metadata', 'type': '[MetadataItem]'},
    }

    def __init__(self, priority=None, display_name=None, uses_task_dependencies=None, constraints=None, job_manager_task=None, job_preparation_task=None, job_release_task=None, common_environment_settings=None, pool_info=None, metadata=None):
        self.priority = priority
        self.display_name = display_name
        self.uses_task_dependencies = uses_task_dependencies
        self.constraints = constraints
        self.job_manager_task = job_manager_task
        self.job_preparation_task = job_preparation_task
        self.job_release_task = job_release_task
        self.common_environment_settings = common_environment_settings
        self.pool_info = pool_info
        self.metadata = metadata
