import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
                    break  # Прерываем цикл, чтобы не изменять список во время итерации
        return finishers

class TournamentTest(unittest.TestCase):
    all_results = []

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner1 = Runner("Усэйн", speed=10)
        self.runner2 = Runner("Андрей", speed=9)
        self.runner3 = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            print(result)

    def test_race_usain_and_nik(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        TournamentTest.all_results.append({k: str(v) for k, v in results.items()})
        self.assertEqual(results[1].name, 'Усэйн')
        self.assertEqual(results[2].name, 'Ник')

    def test_race_andrey_and_nik(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        TournamentTest.all_results.append({k: str(v) for k, v in results.items()})
        self.assertEqual(results[1].name, 'Андрей')
        self.assertEqual(results[2].name, 'Ник')

    def test_race_usain_andrey_and_nik(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        TournamentTest.all_results.append({k: str(v) for k, v in results.items()})
        self.assertEqual(results[1].name, 'Усэйн')
        self.assertEqual(results[2].name, 'Андрей')
        self.assertEqual(results[3].name, 'Ник')

if __name__ == '__main__':
    unittest.main()