import random as rd
import os
from art import logo

def randomCard():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = rd.choice(cards)
  return card

def calculateScore(cards):
  score = sum(cards)
  if score == 21 and len(cards) == 2:
    return 0
  if 11 in cards and score < 21:
    cards.remove(11)
    cards.append(1)
  score = sum(cards)
  return score
 
def compareScore(userScore, dealerScore):
  if userScore > 21 and dealerScore > 21:
    return "You went over. You lose "

  if userScore == dealerScore:
    return "Draw "
  elif dealerScore == 0:
    return "Lose, opponent has Blackjack "
  elif userScore == 0:
    return "Win with a Blackjack"
  elif userScore > 21:
    return "You went over. You lose "
  elif dealerScore > 21:
    return "Opponent went over. You win"
  elif userScore > dealerScore:
    return "You win"
  else:
    return "You lose "
    
def playGame():
  print(logo)
  userCards = []
  dealerCards = []
  isGameOver = False

  for _ in range(2):
    userCards.append(randomCard())
    dealerCards.append(randomCard())
  
  while not isGameOver:
    userScore = calculateScore(userCards)
    dealerScore = calculateScore(dealerCards)
    compareScore(userScore, dealerScore)
    print(f"   Your cards: {userCards}, current score: {userScore}")
    print(f"   Dealer's first card: {dealerCards[0]}")

    if userScore == 0 or dealerScore == 0 or userScore > 21:
      isGameOver = True
    else:
      anotherCard = input("Type 'y' to get another card, type 'n' to pass: ")
      if anotherCard == "y":
        userCards.append(randomCard())
      else:
        isGameOver = True
  while dealerScore != 0 and dealerScore < 17:
    dealerCards.append(randomCard())
    dealerScore = calculateScore(dealerCards)

  print(f"   Your final hand: {userCards}, final score: {userScore}")
  print(f"   Computer's final hand: {dealerCards}, final score: {dealerScore}")
  print(compareScore(userScore, dealerScore))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  os.system('cls')
  playGame()
