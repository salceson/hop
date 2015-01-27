# -*- coding: utf-8 -*-
from configuration import Configuration
from pyhop import pyhop

__author__ = 'Michał Ciołczyk'


## OPERATORS

# Walk

def walk(state, who, from_place, to_place):
    if state.location[who] == from_place:
        state.location[who] = to_place
        time_required = Configuration.distance(from_place, to_place) / Configuration.walking_velocity() * 60
        if time_required > state.time[who]:
            return False
        state.time[who] -= time_required
        return state
    else:
        return False


# Taxi

def call_taxi(state, a, from_place):
    state.location['taxi'] = from_place
    if state.time[a] < 10:
        return False
    state.time[a] -= 10
    return state


def ride_taxi(state, a, from_place, to_place):
    if from_place != state.location['taxi']:
        return False
    state.location['taxi'] = to_place
    state.location['me'] = to_place
    state.owe[a] = Configuration.taxi_fare(from_place, to_place)
    time_required = Configuration.distance(from_place, to_place) / Configuration.taxi_velocity() * 60
    if time_required > state.time[a]:
            return False
    state.time[a] -= time_required
    return state


def pay_driver(state, a):
    if state.cash[a] >= state.owe[a]:
        state.cash[a] = state.cash[a] - state.owe[a]
        state.owe[a] = 0
        return state
    else:
        return False


# Bus

def get_into_bus(state, a, from_place, to_place):
    if not Configuration.can_get_to_bus(from_place):
        return False
    if not Configuration.can_get_to_bus(to_place):
        return False
    state.location['bus'] = from_place
    bus_dt = int(60.0 / Configuration.bus_frequency_per_hour())
    if state.time[a] % bus_dt > 0:
        time_required = bus_dt - state.time % bus_dt
        if time_required > state.time[a]:
            return False
        state.time[a] -= time_required
    return state


def ride_bus(state, a, from_place, to_place):
    if from_place != state.location['bus']:
        return False
    state.location['bus'] = to_place
    state.location['me'] = to_place
    state.owe[a] = Configuration.bus_fare(from_place, to_place)
    time_required = Configuration.distance(from_place, to_place) / Configuration.bus_velocity() * 60
    if time_required > state.time[a]:
            return False
    state.time[a] -= time_required
    return state


def pay_for_bus(state, a):
    if state.cash[a] >= state.owe[a]:
        state.cash[a] = state.cash[a] - state.owe[a]
        state.owe[a] = 0
        return state
    else:
        return False


## METHODS

def travel_on_foot(_, a, from_place, to_place):
    if Configuration.distance(from_place, to_place) <= Configuration.max_distance_on_foot():
        return [('walk', a, from_place, to_place)]
    return False


def travel_by_taxi(state, a, from_place, to_place):
    if state.cash[a] >= Configuration.taxi_fare(from_place, to_place):
        return [('call_taxi', a, from_place), ('ride_taxi', a, from_place, to_place), ('pay_driver', a)]
    return False


def travel_by_bus(state, a, from_place, to_place):
    if state.cash[a] >= Configuration.bus_fare(from_place, to_place):
        return [('get_into_bus', a, from_place, to_place), ('ride_bus', a, from_place, to_place), ('pay_for_bus', a)]
    return False


## INITIALIZATION

def initialize_operators(to_print=False):
    pyhop.declare_operators(walk, call_taxi, ride_taxi, pay_driver, get_into_bus, ride_bus, pay_for_bus)
    if to_print:
        pyhop.print_operators()
    pass


def initialize_methods(to_print=False):
    pyhop.declare_methods('travel', travel_on_foot, travel_by_taxi, travel_by_bus)
    if to_print:
        pyhop.print_methods()
    pass