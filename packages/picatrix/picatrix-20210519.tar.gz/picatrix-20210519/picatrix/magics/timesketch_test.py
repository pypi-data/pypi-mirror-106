# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for the picatrix framework."""
from typing import Optional
from typing import Text

from picatrix.lib import framework
from picatrix.lib import manager

"""
def connect(
def get_context_date(
def get_context_row(
def is_view_object(input_object: Any) -> bool:
def format_data_frame_row(
def get_sketch_details(sketch_id: Optional[int] = 0) -> Text:
def set_active_sketch(sketch_id: int):
def timesketch_get_sketch(data='') -> api_sketch.Sketch:
def timesketch_add_manual_event(
def timesketch_upload_file(data: Text, name: Optional[Text] = ''):
def query_timesketch(
def timesketch_list_views(
def timesketch_query(
def timesketch_context_date(
def timesketch_context_row(
def timesketch_get_timelines(data: Text) -> Dict[str, api_timeline.Timeline]:
def timesketch_create_sketch(
def timesketch_get_views(data: Optional[Text] = '') -> Dict[str, api_view.View]:
def timesketch_query_view(data: api_view.View) -> pd.DataFrame:
def timesketch_set_active_sketch(data: Text):
def timesketch_upload_data(
def timesketch_list_timelines(data: Optional[Text] = '') -> Text:
def timesketch_get_aggregations(
def timesketch_available_aggregators(
def timesketch_get_token_status(data: Optional[Text] = '') -> Text:
def timesketch_refresh_token(data: Optional[Text] = '') -> Text:
def timesketch_run_aggregation_dsl(
def timesketch_run_aggregator(
def timesketch_get_sketches(
def timesketch_get_searchindices(data: Optional[Text] = '') -> Dict[Text, Text]:
def timesketch_search_by_label(
def timesketch_get_starred_events(
def timesketch_events_with_comments(
def timesketch_list_stories(
"""
