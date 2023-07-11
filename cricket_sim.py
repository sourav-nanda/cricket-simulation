import random
from datetime import datetime

class Player:

    def __init__(self, name, bowling, batting, fielding, running, experience):
        '''
        Player definitions
        '''
        self.name = name
        self.bowling = bowling
        self.batting = batting
        self.fielding = fielding
        self.running = running
        self.experience = experience
        self.agg_performance=bowling+batting+fielding+running+experience
        self.played=False
        self.is_out=False

class Team:

    def __init__(self, name, players):

        '''
        Team definitions
        '''

        self.name=name
        self.players=players
        self.wickets = 0
        self.runs=0
        self.toss_choice=None
        self.captain=None
        self.batsman=None
        self.bowler=None
        self.batting_order=None
        self.bowling_order=None


    def select_captain(self):
        '''
        Selects the captain of the team from the available players 
        on the basis of the aggregate or sum of all the skills possesed by the player
        '''

        candidates={}


        # map(lambda c:candidates.update({c:c.agg_performance}),self.players)                  #No need for storing as it is only used to update candidates dict 

        for c in self.players:
            candidates.update({c:c.agg_performance})
        

        self.captain=sorted(candidates.items(),key=lambda val:val[1],reverse=True)[0][0]
        # print(self.captain.name,self.captain.agg_performance)
        

        
    def decide_batting_order(self):

        '''
        Decides the batting order for the team by sorting players 
        in descending order based on their batting skills
        '''

        batting_order={batsman:batsman.batting for batsman in self.players}

        # map(lambda batsman:batting_order.update({batsman:batsman.batting}),self.players)       #No need for storing as it is only used to update batting_order dict 


        batting_order=dict((sorted(batting_order.items(),key=lambda val:val[1],reverse=True)))         
        self.batting_order=list(batting_order.keys())
        

        # print(batting_table)
    
    def decide_bowling_order(self):

        '''
        Decides the bowling order for the team by sorting players
        in descending order based on their bowling skills
        '''
        bowling_order={}

        bowling_order={bowler:bowler.bowling for bowler in self.players}

        # map(lambda bowler:bowling_order.update({bowler:bowler.bowling}),self.players)         #No need for storing as it is only used to update bowling_order dict 
        
        bowling_order=dict(sorted(bowling_order.items(),key=lambda val:val[1],reverse=True))
        self.bowling_order=list(bowling_order.keys())
        
        
    def select_batsman(self):
        '''
        Selects the batsman from the available players
        '''

        for batsman in self.batting_order:
            if batsman.played==False:
                self.batsman=batsman
                batsman.played=True
                break
            else:
                for player in self.players:
                    player.played = False
                self.batting_order.remove(batsman)
                # continue

    def select_bowler(self):
        
        '''
        Selects the bowler from the available players
        '''

        for bowler in self.bowling_order:
            if bowler.played==False:
                self.bowler=bowler
                bowler.played=True
                break
            else:
                # for player in self.players:
                #     player.played = False
                self.bowling_order.remove(bowler)
                continue


class Field:

    def __init__(self, field_size, fan_ratio, pitch_conditions, home_adv,max_wickets):
        self.field_size = field_size
        self.fan_ratio = fan_ratio
        self.pitch_conditions = pitch_conditions
        self.home_adv = home_adv
        
    
class Umpire:
    def __init__(self):
        self.runs = 0
        # self.current_team = None

    def make_decision(self, batting_team,match):
        '''
        Makes a decision on the outcome of a ball based on player statistics, field conditions, etc.
        '''
        decision = random.choices(["run", "dot", "wicket"],[0.6,0.2,0.2])[0]               #Bias used as runs are a more frequent event compared to the other two


        # if batting_team.batsman is None:
        #     match.end_match()
            

        if decision == "run":

            runs_scored = random.randint(0, 6)
            self.runs += runs_scored
            print(f"{batting_team.batsman.name} scores {runs_scored} run(s)!")

        elif decision == "wicket":

            batting_team.batsman.is_out=True
            print("Out!")
            batting_team.wickets+=1 if batting_team.wickets<match.max_wickets else match.change_innings()
            
            batting_team.select_batsman()

        else:

            print("Dot ball!")




class Commentator:
    def __init__(self):

        self.commentary = {
            0: "Dot ball!",
            1: "Scored one run.",
            2: "Two runs completed.",
            3: "Three runs.",
            4: "It's a boundary!",
            6: "That's a Sixer!",
            -1: "Out! The batsman is bowled.",
            -2: "Caught! Brilliant catch by the fielder.",
            -3: "Run out! ",
        }

    def comment(self, batsman, bowler, runs,wickets,overs):
        '''
        Provides commentary on the ongoing game events such as runs, wickets, etc.
        '''

        print('\n',datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        print(f" Batsman: {batsman.name} | Bowler: {bowler.name}")
        print(f"Score: runs/wickets")
        print(f"Score: {runs}/{wickets}")
        print(f"Overs: {overs}")
        


        if runs in self.commentary:
            commentary = self.commentary[runs]
            print(f"{batsman.name} scores {abs(runs)} run(s) against {bowler.name}. {commentary}")
        


class Match:

    def __init__(self, team1, team2, field, umpire, commentator, overs_per_innings,max_wickets):
        
        self.balls=0
        self.overs=0

        self.team1 = team1
        self.team2 = team2
        self.field = field
        
        self.umpire = umpire
        self.commentator = commentator
        self.overs_per_innings=overs_per_innings
        self.max_wickets=max_wickets
        
        self.completed_overs=0
        
        self.batting_team = None
        self.bowling_team = None
        
        self.current_team=None
        self.opponent_team = None
        

        self.is_match_ended = False

    def toss(self):
        '''
        Simulates the toss to decide which team bats or bowls first
        '''
        choice,teams=random.randint(0,1),[self.team1, self.team2]
        self.current_team,self.opponent_team = teams[choice],teams[not(choice)]
        
    
        self.current_team.toss_choice=random.choice(('Bat','Bowl'))

        self.current_team.select_captain()
        self.opponent_team.select_captain()
        
        # if self.current_team.toss_choice == "Bat":

        #     self.current_team.decide_batting_order()
        #     self.opponent_team.decide_bowling_order()
        # else:
        #     self.current_team.decide_bowling_order()
        #     self.opponent_team.decide_batting_order()


        if self.current_team.toss_choice == "Bat":
            self.batting_team,self.bowling_team=self.current_team,self.opponent_team
        else:
            self.batting_team,self.bowling_team=self.opponent_team,self.current_team
        
        # self.umpire.current_team=self.batting_team
            

    def start_match(self):
        '''
        Starts the cricket match and handles overall simulation
        '''
        self.toss()

        self.batting_team.decide_batting_order();self.bowling_team.decide_bowling_order();

        # self.batting_team.select_batsman()
        # self.bowling_team.select_bowler()
        


        # Simulation runs till the match ends or the innings end
        while not self.is_match_ended or self.current_team.batting_order:  #(self.current_team.batting_order or self.current_team.bowling_order)

            # if self.batting_team.batsman.is_out:
            self.batting_team.select_batsman()

            self.bowling_team.select_bowler()
            
            self.play_ball()

        self.end_match()


    def play_ball(self):
        '''
        Simulates playing a ball and checks if the innings need to be changed or match ends
        '''
        self.balls += 1

        #Start the innings of the current team
        if self.batting_team.batsman is not None and self.bowling_team.bowler is not None:
            self.commentator.comment(self.batting_team.batsman, self.bowling_team.bowler, self.batting_team.runs, self.batting_team.wickets, self.overs)
        
        self.umpire.make_decision(self.batting_team,self)

        if self.balls % 6 == 0:
            self.overs += 1
            self.balls=0
            
        # Increment the runs scored by the batsman
        self.current_team.runs += self.umpire.runs
        # self.umpire.runs=0


        # Check if the innings need to be changed or match ends
        if self.overs >= self.overs_per_innings:
            self.change_innings()


    def change_innings(self):
        '''
        Changes the innings and updates the current batting and bowling teams
        '''
        
        self.batting_team,self.bowling_team = self.bowling_team,self.batting_team
        
        self.batting_team.decide_batting_order()
        self.bowling_team.decide_bowling_order()

        if not self.batting_team.batting_order:
            self.end_match()
            
        self.batting_team.select_batsman()
        self.bowling_team.select_bowler()

        # self.overs = 0
        self.balls=0
        print(f"{self.batting_team.name} starts batting.")
        

    def end_match(self):
        '''
        Ends the cricket match and displays the final results
        '''
        self.is_match_ended = True

        # Display the final results of the match
        print("Match ended.")
        print(f"{self.current_team.name} scored {self.current_team.runs}/{self.current_team.wickets} in {self.overs} overs.")
        print(f"{self.opponent_team.name} needs {self.current_team.runs + 1} runs to win.")

        if self.current_team.runs > self.opponent_team.runs:
            print(f"{self.current_team.name} won the match!")
        elif self.current_team.runs < self.opponent_team.runs:
            print(f"{self.opponent_team.name} won the match!")
        else:
            print("The match ended in a tie.")





#Instantiate Players a total of 22 and 11 per team

azam = Player("Babar Azam", 0.12, 0.86, 0.92, 0.81, 0.88)
de_villiers = Player("AB de Villiers", 0.14, 0.92, 0.88, 0.86, 0.91)
dhoni = Player("MS Dhoni", 0.21, 0.82, 0.97, 0.82, 0.92)
gayle = Player("Chris Gayle", 0.16, 0.88, 0.86, 0.76, 0.84)
hasan = Player("Shakib Al Hasan", 0.17, 0.85, 0.88, 0.82, 0.91)
kane = Player("Kane Williamson", 0.10, 0.88, 0.91, 0.81, 0.89)
kohli = Player("Virat Kohli", 0.13, 0.89, 0.94, 0.76, 0.86)
kumar_s = Player("Kumar Sangakkara", 0.14, 0.84, 0.94, 0.81, 0.89)
r_sharma = Player("Rohit Sharma", 0.22, 0.89, 0.90, 0.77, 0.85)
sachin = Player("Sachin Tendulkar", 0.17, 0.93, 0.97, 0.81, 0.94)
smith = Player("Steve Smith", 0.10, 0.88, 0.91, 0.76, 0.86)
warner = Player("David Warner", 0.13, 0.85, 0.90, 0.81, 0.87)
root = Player("Joe Root", 0.11, 0.89, 0.95, 0.78, 0.83)
buttler = Player("Jos Buttler", 0.19, 0.90, 0.86, 0.83, 0.88)
bravo = Player("Dwayne Bravo", 0.15, 0.83, 0.83, 0.80, 0.83)
steyn = Player("Dale Steyn", 0.23, 0.93, 0.90, 0.88, 0.88)
rashid = Player("Rashid Khan", 0.18, 0.88, 0.93, 0.81, 0.87)
bumrah = Player("Jasprit Bumrah", 0.12, 0.90, 0.91, 0.88, 0.88)
amla = Player("Hashim Amla", 0.15, 0.86, 0.88, 0.81, 0.88)
tamim = Player("Tamim Iqbal", 0.15, 0.83, 0.86, 0.80, 0.85)
lara = Player("Brian Lara", 0.18, 0.93, 0.94, 0.88, 0.89)
ponting = Player("Ricky Ponting", 0.12, 0.89, 0.93, 0.81, 0.88)
malinga = Player("Lasith Malinga", 0.24, 0.91, 0.90, 0.88, 0.89)

#Instantiate teams
team1 = Team("Team A", [dhoni,r_sharma,sachin,kumar_s,de_villiers,warner,root,buttler,bravo,steyn,rashid])
team2 = Team("Team B", [kane,gayle,kohli,smith,azam ,hasan,bumrah,amla,tamim,lara,ponting,malinga])

#Instantiate Umpire, Commentator & Field
umpire=Umpire()
commentator=Commentator()
field = Field("Medium", 0.8, "Dry", 0.2, 10)

overs_per_innings=5  #input("Enter overs per innings:")
max_wickets=10

#Instantiate match
match = Match(team1, team2, field, umpire, commentator, overs_per_innings,max_wickets)


#Begin match
match.start_match()