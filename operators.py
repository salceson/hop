# coding=utf-8
__author__ = 'Michał Ciołczyk'


def taxi_fare(dist):
    return 20 + 1.5 * dist


def walk(state, who, from_place, to_place):
    if state.location[who] == from_place:
        state.location = to_place
        return state
    else:
        return False


def call_taxi(state, _, from_place):
    state.location['taxi'] = from_place
    return state

