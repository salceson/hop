# -*- coding: utf-8 -*-
__author__ = 'Michał Ciołczyk'


class Configuration(object):
    # Velocities
    @staticmethod
    def walking_velocity():
        return 0.1

    @staticmethod
    def taxi_velocity():
        return 2

    # Distances
    @staticmethod
    def distances_map():
        return {
            'park': {
                'home': 80,
            },
            'home': {
                'park': 80,
            },
        }

    @staticmethod
    def distance(from_place, to_place):
        return Configuration.distances_map()[from_place][to_place]

    # Buses
    @staticmethod
    def can_get_to_bus(from_place):
        bus_locations = ['park', 'intersection', 'school']
        return bus_locations.__contains__(from_place)

    @staticmethod
    def bus_frequency_per_hour():
        return 6

    # States

    @staticmethod
    def initialize_state():
        pass