# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 21:10:04 2026

@author: shama
"""

def compute_scores(score1, score2, score3):
    total_points = score1 + score2 + score3
    average_score = total_points / 3
    return total_points, average_score

def main():
    # Input
    last_name = input("Enter the student's last name: ")
    score1 = float(input("Enter exam score 1: "))
    score2 = float(input("Enter exam score 2: "))
    score3 = float(input("Enter exam score 3: "))

    # Process
    total_points, average_score = compute_scores(score1, score2, score3)

    # Output
    print(f"Student Last Name: {last_name}")
    print(f"Total Points: {total_points:.2f}")
    print(f"Average Exam Score: {average_score:.2f}")

main()