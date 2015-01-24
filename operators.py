# coding=utf-8
from configuration import Configuration

__author__ = 'Michał Ciołczyk'


def taxi_fare(dist):
    return 20 + 1.5 * dist


def walk(state, who, from_place, to_place):
    if state.location[who] == from_place:
        state.location = to_place
        state.time += Configuration.distance(from_place, to_place) / Configuration.walking_velocity() * 60
        return state
    else:
        return False


def call_taxi(state, _, from_place):
    state.location['taxi'] = from_place
    state.time += 10
    return state


def drive_taxi(state, _, from_place, to_place):
    if from_place != state.location['taxi']:
        return False
    state.location['taxi'] = to_place
    state.location['me'] = to_place
    state.time += Configuration.distance(from_place, to_place) / Configuration.taxi_velocity() * 60
    return state


def get_into_bus(state, _, from_place):
    if Configuration.can_get_to_bus(from_place):
        return False
    state.location['bus'] = from_place
    bus_dt = int(60.0 / Configuration.bus_frequency_per_hour())
    if state.time % bus_dt > 0:
        state.time += bus_dt - state.time % bus_dt
    return state


def drive_bus(state, _, from_place):
    pass