# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 21:35:33 2026

@author: shama
"""

def compute_bowling_scores(game1, game2, game3, handicap):
    average_score = (game1 + game2 + game3) / 3
    average_with_handicap = average_score + handicap
    return average_score, average_with_handicap

def main():
    # Input
    last_name = input("Enter bowler's last name: ")
    game1 = float(input("Enter game 1 score: "))
    game2 = float(input("Enter game 2 score: "))
    game3 = float(input("Enter game 3 score: "))
    handicap = float(input("Enter handicap: "))

    # Process
    average_score, average_with_handicap = compute_bowling_scores(game1, game2, game3, handicap)

    # Output
    print(f"Bowler Last Name: {last_name}")
    print(f"Average Score: {average_score:.2f}")
    print(f"Average Score with Handicap: {average_with_handicap:.2f}")

main()