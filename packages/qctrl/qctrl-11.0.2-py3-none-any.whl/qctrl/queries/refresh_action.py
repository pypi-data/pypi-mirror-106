# Copyright 2021 Q-CTRL. All rights reserved.
#
# Licensed under the Q-CTRL Terms of service (the "License"). Unauthorized
# copying or use of this file, via any medium, is strictly prohibited.
# Proprietary and confidential. You may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#     https://q-ctrl.com/terms
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS. See the
# License for the specific language.
# pylint:disable=missing-module-docstring
from typing import Union

from .base import PatternQuery


class RefreshActionQuery(PatternQuery):  # pylint:disable=too-few-public-methods
    """Query used to check action completion."""

    query_pattern = """
        query refreshAction($modelId: String!) {
            coreAction(modelId: $modelId) {
                coreAction {
                    ... on %(field_type)s {
                        action {
                            modelId
                            name
                            status
                            errors {
                                exception
                            }
                            progress
                            result
                        }
                        errors {
                            fields
                            message
                        }
                    }
                }
                errors {
                    message
                    fields
                }
            }
        }
    """

    def _get_variable_values(
        self, action_id: Union[str, int]
    ):  # pylint:disable=arguments-differ
        return {"modelId": str(action_id)}
