# -*- coding: utf-8 -*-
from pyhop import pyhop

__author__ = 'Michał Ciołczyk'


class Configuration(object):
    # Velocities
    @staticmethod
    def walking_velocity():
        return 5

    @staticmethod
    def taxi_velocity():
        return 20

    @staticmethod
    def bus_velocity():
        return 15

    # Distances
    @staticmethod
    def distances_map():
        return {
            'park': {
                'home': 80,
                'intersection1': 20,
            },
            'home': {
                'park': 80,
                'intersection3': 5,
            },
            'intersection1': {
                'park': 20,
                'intersection2': 15,
            },
            'intersection2': {
                'intersection1': 15,
                'intersection3': 10,
            },
            'intersection3': {
                'intersection2': 10,
                'home': 5
            }
        }

    @staticmethod
    def distance(from_place, to_place):
        return Configuration.distances_map()[from_place][to_place]

    # Buses
    @staticmethod
    def can_get_to_bus(from_place):
        bus_locations = ['park', 'intersection1', 'intersection2', 'intersection3']
        return bus_locations.__contains__(from_place)

    @staticmethod
    def bus_frequency_per_hour():
        return 6

    @staticmethod
    def bus_fare(from_place, to_place):
        return 1 + 0.1 * Configuration.distance(from_place, to_place)

    # Taxi

    @staticmethod
    def taxi_fare(from_place, to_place):
        return 20 + 1.5 * Configuration.distance(from_place, to_place)

    # States

    @staticmethod
    def initialize_state():
        state = pyhop.State('My state')
        state.cash = dict()
        state.cash['me'] = 500  # in dollars
        state.time = dict()
        state.time['me'] = 500  # in minutes
        state.owe = dict()
        state.owe['me'] = 0
        state.location = dict()
        state.location['me'] = 'park'
        return state