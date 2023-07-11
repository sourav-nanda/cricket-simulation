# Cricket Match Simulation - Readme

## Introduction

Welcome to the Cricket Match Simulation! This code implements a simulation that allows you to experience a virtual cricket match. Whether you're a cricket enthusiast or simply curious about the game, this simulation will provide you with a taste of the excitement and strategy involved in this popular sport.

## How It Works

The simulation is built using classes and methods that represent various components of a cricket match. Let's take a closer look at each of these components.

### Players

In this simulation, each player is represented by the `Player` class. Each player has unique attributes such as their `name`, `batting` skill level, `bowling` skill level, `fielding` ability, `running` speed, and overall `experience`. These attributes are used to calculate the player's `aggregate performance`. Additionally, the `played` attribute keeps track of whether a player has already participated in the match.

### Teams

Two teams compete against each other in the simulation, and they are represented by the `Team` class. Each team has a `name` and a list of `players`. Throughout the match, the team's `wickets` (number of players dismissed) and `runs` (score) are recorded. When a team wins the toss, they make a `toss_choice` - deciding whether to bat or bowl. The `captain` attribute represents the team's captain, and the `batting_order` stores the sequence in which players will bat.

The `Team` class includes methods to select the captain based on players' aggregate performances (`select_captain()`), and to decide the batting order based on players' batting skill levels (`decide_batting_order()`). The `select_batsman()` method is used to determine the next batsman to play.

### Field

The `Field` class represents the cricket field where the match takes place. It takes into account factors such as `field_size` (the dimensions of the field), `fan_ratio` (the ratio of spectators of both teams), `pitch_conditions` (the state of the playing surface), `home_adv` (the advantage of playing on the home ground), and `max_wickets` (the maximum number of wickets).

### Umpire

The `Umpire` class represents the match umpire. It plays a crucial role in making decisions during the match. It keeps track of the current number of `runs` scored and the `current_team` playing. When a ball is bowled, the `make_decision()` method randomly determines the outcome for the batsman, such as "run," "wicket," or "dot."

### Commentator

The `Commentator` class provides commentary on the ongoing match. It has a collection of predefined commentary strings associated with different events, such as runs scored, wickets taken, and more. The `comment()` method prints the commentary for a specific event, including the batsman, bowler, current score, and overs.

### Match

The `Match` class represents the entire cricket match. It brings together the teams, field, umpire, commentator, and other components. When creating a `Match` instance, you need to provide the two teams, field conditions, umpire, commentator, and the number of overs per innings.

The `Match` class includes methods to conduct the toss and determine the batting and bowling teams (`toss()`). It also initiates the match and handles the batting and bowling process (`start_match()`). The `play_ball()` method simulates a ball being played and updates the score and wickets accordingly. Finally, the `end_match()` method prints the result of the match.

## Usage

To use the code, you can create instances of the various classes according to your desired players, teams, field conditions, and overs per innings. Once the setup is complete, you can call the `start_match()` method on the `Match` instance to begin the simulation.

In the provided code, sample players, teams, umpire, commentator, field conditions, and overs per innings are already created. The simulation is initiated by calling the `start_match()` method on the `match` instance.
