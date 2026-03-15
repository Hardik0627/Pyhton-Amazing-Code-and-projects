# Cricket Scoreboard Manager

class CricketScoreboard:
    def __init__(self):
        self.team = ""
        self.runs = 0
        self.wickets = 0
        self.overs = 0
        self.balls = 0

    def start_match(self):
        self.team = input("Enter Batting Team Name: ")
        self.runs = 0
        self.wickets = 0
        self.overs = 0
        self.balls = 0
        print("\nMatch Started!\n")

    def add_runs(self):
        r = int(input("Runs scored (0-6): "))
        self.runs += r
        self.next_ball()

    def wicket(self):
        if self.wickets < 10:
            self.wickets += 1
            print("WICKET!")
        else:
            print("All out!")
        self.next_ball()

    def next_ball(self):
        self.balls += 1
        if self.balls == 6:
            self.overs += 1
            self.balls = 0

    def show_score(self):
        print("\n------ SCOREBOARD ------")
        print("Team:", self.team)
        print("Score:", f"{self.runs}/{self.wickets}")
        print("Overs:", f"{self.overs}.{self.balls}")
        print("------------------------\n")


# Main Program
scoreboard = CricketScoreboard()

while True:
    print("🏏 Cricket Scoreboard Menu")
    print("1. Start Match")
    print("2. Add Runs")
    print("3. Wicket")
    print("4. Show Score")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        scoreboard.start_match()
    elif choice == "2":
        scoreboard.add_runs()
    elif choice == "3":
        scoreboard.wicket()
    elif choice == "4":
        scoreboard.show_score()
    elif choice == "5":
        print("Match Ended!")
        break
    else:
        print("Invalid choice!")