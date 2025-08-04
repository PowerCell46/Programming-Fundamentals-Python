from abc import ABC, abstractmethod


class MovieRate(ABC):
    @abstractmethod
    def warnIfNotAllowed(self, age: int) -> None:
        pass


class Pg13MovieRate(MovieRate):
    def warnIfNotAllowed(self, age: int) -> None:
        if age < 13:
            raise ValueError("You are not allowed to watch this movie!")


class AdultsOnlyMovieRate(MovieRate):
    def warnIfNotAllowed(self, age: int) -> None:
        if age < 18:
            raise ValueError("You are not allowed to watch this movie!")


class Movie:
    def __init__(self, name: str, rate: MovieRate) -> None:
        self._name = name
        self._rate = rate

    def warnIfNotAllowed(self, age: int) -> None:
        return self._rate.warnIfNotAllowed(age)

    def getName(self) -> str:
        return self._name


class MovieWatcher:
    def __init__(self, age: int) -> None:
        self.age = age

    def watchMovie(self, movie: Movie) -> None:
        movie.warnIfNotAllowed(self.age)

        print(f'Watching the movie \'{movie.getName()}\'.')


theExorcist = Movie("The Exorcist", AdultsOnlyMovieRate())
gremlins = Movie("Gremlins", Pg13MovieRate())

jane = MovieWatcher(12)
# jane.watchMovie(theExorcist)
# jane.watchMovie(gremlins)

joe = MovieWatcher(16)
# joe.watchMovie(theExorcist)
joe.watchMovie(gremlins)
