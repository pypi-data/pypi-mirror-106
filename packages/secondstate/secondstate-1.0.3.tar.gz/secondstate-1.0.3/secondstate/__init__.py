# Copyright (c) 2021, Fruiti Limited
# All rights reserved.

# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

import logging

from .converters import (
    convert_custom_timestamp_range,
    convert_iso_datetime_to_timestamp,
)

logger = logging.getLogger(__name__)


class SecondState:
    def __init__(self) -> None:
        self.state = []
        self.state_start_timestamp = 0
        self.state_finish_timestamp = 0

    def get_state(self) -> list:
        return self.state

    def initialise_state(self, start: str, finish: str) -> list:
        self.state_start_timestamp = convert_iso_datetime_to_timestamp(start)
        self.state_finish_timestamp = convert_iso_datetime_to_timestamp(finish)

        difference = self.state_finish_timestamp - self.state_start_timestamp

        self.state = [0 for x in range(difference)]

        return self.get_state()

    def toggle_availability(self, start: str, finish: str, set: bool) -> list:
        """
        Toggle availability in the state by replacing zeros with ones or vice-versa
        at the relevant seconds.
        """
        start_timestamp = convert_iso_datetime_to_timestamp(start)
        finish_timestamp = convert_iso_datetime_to_timestamp(finish)

        start_difference = start_timestamp - self.state_start_timestamp
        if start_difference < 0:
            start_difference = 0

        finish_difference = finish_timestamp - self.state_start_timestamp
        state_length = len(self.get_state())
        if finish_difference >= state_length:
            finish_difference = state_length - 1

        for x in range(start_difference, finish_difference):
            self.state[x] = 1 if set else 0

        return self.get_state()

    def set_availability(self, start: str, finish: str) -> list:
        return self.toggle_availability(start, finish, True)

    def unset_availability(self, start: str, finish: str):
        return self.toggle_availability(start, finish, False)

    def get_availability(self, **kwargs) -> list:
        """
        Return a list of time ranges that allow enough time for the required
        duration
        """
        duration_seconds = 0
        custom_format = False

        for key, value in kwargs.items():
            if key == "minutes":
                duration_seconds = value * 60
            elif key == "seconds":
                duration_seconds = value
            elif key == "custom_format":
                custom_format = value

        if duration_seconds == 0:
            logger.fatal("Please specify minutes or seconds")
            raise ValueError

        possible_epochs = self.get_possible_epochs()

        result = []

        for epoch in possible_epochs:
            while epoch[0] + duration_seconds - 1 <= epoch[1]:
                start = epoch[0] + self.state_start_timestamp
                finish = epoch[0] + self.state_start_timestamp + duration_seconds
                result.append(f"{start}_{finish}")
                epoch[0] += duration_seconds

        if not custom_format:
            iso_datetimes_ranges = []
            for custom_timestamp_range in result:
                iso_datetimes_ranges.append(
                    convert_custom_timestamp_range(custom_timestamp_range)
                )
            result = iso_datetimes_ranges

        return result

    def get_epoch_groups(self, epochs: list) -> list:
        """
        See:
        https://stackoverflow.com/questions/2154249/identify-groups-of-continuous-numbers-in-a-list
        """
        first = last = epochs[0]
        for n in epochs[1:]:
            if n - 1 == last:  # Part of the group, bump the end
                last = n
            else:  # Not part of the group, yield current group and start a new
                yield first, last
                first = last = n
        yield first, last  # Yield the last group

    def get_possible_epochs(self) -> list:
        """
        Return a list of possible epoch ranges that are within the schedule availability
        """
        epochs = []
        for index, value in enumerate(self.state):
            if value == 1:
                epochs.append(index)

        result = []
        if epochs:
            for epoch_range in self.get_epoch_groups(epochs):
                result.append([epoch_range[0], epoch_range[1]])
        return result
