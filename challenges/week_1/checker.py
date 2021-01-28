import bus_fare_challenge as solution
import datetime
import unittest


class TestBusFareChallenge(unittest.TestCase):
    def setUp(self) -> None:
        self.date = datetime.datetime.now().date()
        self.day = self.date.strftime("%a")
        self.charts = {
            "Mon": 100,
            "Tue": 100,
            "Wed": 100,
            "Thu": 100,
            "Fri": 100,
            "Sat": 60,
            "Sun": 80,
        }

    def test_date(self) -> None:
        """
        Tests whether the date returned by the program is correct.
        """
        actual = self.date
        given = solution.date
        self.assertEqual(actual, given, f"Today's date is Wrong by {given - actual}!")

    def test_day(self) -> None:
        """
        Tests whether the day returned by the program is correct.
        """
        actual = self.day
        given = solution.day
        self.assertEqual(
            actual, given, f"Today is wrong, expexted {actual} but got {given}!"
        )

    def test_fare(self) -> None:
        """
        Tests whether the fare returned by the program is correct.
        """
        actual = self.charts[self.day]
        given = solution.fare
        self.assertEqual(
            actual, given, f"Fare is wrong, expected {actual} but got {given}!"
        )


if __name__ == "__main__":
    print("=========================================================================")
    print("=========================================================================")
    print("===== Start: Checking Return Values For Today's  Date, Day and Fare =====")
    unittest.main(exit=False)
    print("===== End: Checking Return Values For Today's  Date, Day and Fare =======")
    print("=========================================================================")
