"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730615250"  # TODO


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)
    
    def distance(self, point_1: Point) -> float:
        """Calculate the difference between two points."""
        x_dis: float = self.x - point_1.x
        y_dis: float = self.y - point_1.y
        d: float = sqrt(x_dis ** 2 + y_dis ** 2)
        return d


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.
    def tick(self) -> None:
        """Reassign the object's location attribute."""
        self.location = self.location.add(self.direction)
        if self.is_infected() >= constants.INFECTED:
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()
        
    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable():
            return "gray"
        if self.is_infected():
            return "red"
        if self.is_immune():
            return "dark green"
        else:
            return "gray"
    
    def contract_disease(self) -> None:
        """Assign the INFECTED constant to the sickness attribute."""
        self.sickness: int = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Check if the cell is vulnerable."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False
    
    def is_infected(self) -> bool:
        """Check if the cell is infected."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False
    
    def contact_with(self, other: Cell) -> None:
        """Called when two Cell objects do make contact."""
        if self.is_vulnerable() and other.is_infected():
            self.contract_disease() 
        if self.is_infected() and other.is_vulnerable():
            other.contract_disease()

    def immunize(self) -> None:
        """Immunize the cell."""
        self.sickness = constants.IMMUNE
    
    def is_immune(self) -> bool:
        """Check whether the cell is immnue."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected: int, immune: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        if infected >= cells or infected <= 0 or immune >= cells or immune < 0:
            raise ValueError("Some number of the Cell objects must begin infected.")

        for i in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            if i < infected:
                cell.contract_disease()
            if i >= infected and i < infected + immune:
                cell.immunize()
            self.population.append(cell)

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)

    def random_location(self) -> Point:
        """Generate a random location."""
        # TODO
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        # TODO
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        number: int = 0
        while number < len(self.population):
            if self.population[number].is_infected():
                return False
            number += 1
        return True

    def check_contacts(self) -> None:
        """Compare the distance between every two Cell objects' location attributes in the population."""
        for cell in range(len(self.population)):
            for i in range(cell + 1, len(self.population)):
                value: Point = self.population[i].location
                if self.population[cell].location.distance(value) < constants.CELL_RADIUS:
                    self.population[cell].contact_with(self.population[i])