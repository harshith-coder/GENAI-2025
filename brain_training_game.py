#!/usr/bin/env python3
"""
Brain Training Game - A Fun and Engaging Application
This game helps erase loneliness, prevent boredom, and improve cognitive skills!
"""

import random
import time
import os
import sys

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_banner():
    """Display welcome banner"""
    banner = """
    ╔════════════════════════════════════════════════════════╗
    ║       🧠 BRAIN TRAINING GAME - Challenge Yourself! 🧠   ║
    ╚════════════════════════════════════════════════════════╝
    
    ⭐ Erase Boredom ⭐ Have Fun ⭐ Boost Your IQ ⭐
    """
    print(banner)

def number_memory_game():
    """Memory challenge - remember and repeat numbers"""
    clear_screen()
    print("\n🔢 NUMBER MEMORY CHALLENGE 🔢")
    print("=" * 50)
    print("Memorize the number sequence and type it back!")
    print("The sequence gets longer with each level.\n")
    
    level = 1
    score = 0
    
    while True:
        sequence_length = 2 + level
        sequence = [random.randint(0, 9) for _ in range(sequence_length)]
        
        print(f"\n📊 Level {level} - Memorize this sequence:")
        print("\n" + " ".join(map(str, sequence)))
        
        time.sleep(2 + level * 0.5)
        clear_screen()
        
        print("\n" + "?" * 50)
        print("Now type the sequence you just saw!")
        
        try:
            user_input = input("\nYour answer: ").strip().replace(" ", "")
            user_sequence = [int(d) for d in user_input if d.isdigit()]
            
            if user_sequence == sequence:
                score += level * 10
                print(f"\n✅ CORRECT! +{level * 10} points!")
                print(f"💯 Current Score: {score}")
                level += 1
                time.sleep(2)
            else:
                print(f"\n❌ Oops! The correct sequence was: {' '.join(map(str, sequence))}")
                print(f"\n🏆 Final Score: {score} points!")
                print(f"🎯 You reached Level {level}!")
                break
                
        except (ValueError, IndexError):
            print(f"\n❌ Invalid input! The correct sequence was: {' '.join(map(str, sequence))}")
            print(f"\n🏆 Final Score: {score} points!")
            break
        
        if level > 10:
            print(f"\n🎉 AMAZING! You're a memory master!")
            print(f"🏆 Final Score: {score} points!")
            break
    
    input("\nPress Enter to return to menu...")

def math_challenge_game():
    """Quick math quiz to boost IQ"""
    clear_screen()
    print("\n🧮 MATH CHALLENGE 🧮")
    print("=" * 50)
    print("Solve as many math problems as you can!")
    print("You have 30 seconds!\n")
    
    input("Press Enter to start...")
    
    score = 0
    start_time = time.time()
    duration = 30
    questions_answered = 0
    
    while time.time() - start_time < duration:
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        operation = random.choice(['+', '-', '*'])
        
        if operation == '+':
            correct_answer = num1 + num2
        elif operation == '-':
            correct_answer = num1 - num2
        else:
            correct_answer = num1 * num2
        
        remaining_time = int(duration - (time.time() - start_time))
        print(f"\n⏰ Time remaining: {remaining_time}s")
        print(f"What is {num1} {operation} {num2}?")
        
        try:
            user_answer = int(input("Your answer: "))
            questions_answered += 1
            
            if user_answer == correct_answer:
                score += 10
                print("✅ Correct! +10 points")
            else:
                print(f"❌ Wrong! The answer was {correct_answer}")
        except ValueError:
            print("Invalid input! Moving to next question...")
        except EOFError:
            break
    
    clear_screen()
    print("\n⏰ TIME'S UP!")
    print(f"\n🏆 Final Score: {score} points!")
    print(f"📝 Questions Answered: {questions_answered}")
    if questions_answered > 0:
        accuracy = (score / (questions_answered * 10)) * 100
        print(f"🎯 Accuracy: {accuracy:.1f}%")
    
    input("\nPress Enter to return to menu...")

def pattern_matching_game():
    """Pattern matching game with colors"""
    clear_screen()
    print("\n🎨 COLOR PATTERN MATCHING 🎨")
    print("=" * 50)
    print("Watch the color pattern and repeat it!")
    print("Colors: R=Red, G=Green, B=Blue, Y=Yellow\n")
    
    colors = ['R', 'G', 'B', 'Y']
    color_names = {'R': '🔴 Red', 'G': '🟢 Green', 'B': '🔵 Blue', 'Y': '🟡 Yellow'}
    
    level = 1
    score = 0
    
    while True:
        pattern_length = 2 + level
        pattern = [random.choice(colors) for _ in range(pattern_length)]
        
        print(f"\n📊 Level {level} - Watch this pattern:")
        for color in pattern:
            print(f"  {color_names[color]}")
        
        time.sleep(2 + level * 0.5)
        clear_screen()
        
        print("\n" + "?" * 50)
        print("Now type the pattern! (e.g., RGBY)")
        print("R=Red, G=Green, B=Blue, Y=Yellow\n")
        
        user_input = input("Your answer: ").strip().upper()
        user_pattern = list(user_input.replace(" ", ""))
        
        if user_pattern == pattern:
            score += level * 15
            print(f"\n✅ PERFECT! +{level * 15} points!")
            print(f"💯 Current Score: {score}")
            level += 1
            time.sleep(2)
        else:
            correct = ''.join(pattern)
            print(f"\n❌ Oops! The correct pattern was: {correct}")
            for color in pattern:
                print(f"  {color_names[color]}")
            print(f"\n🏆 Final Score: {score} points!")
            print(f"🎯 You reached Level {level}!")
            break
        
        if level > 8:
            print(f"\n🎉 INCREDIBLE! You have an amazing visual memory!")
            print(f"🏆 Final Score: {score} points!")
            break
    
    input("\nPress Enter to return to menu...")

def word_scramble_game():
    """Unscramble words to test vocabulary and quick thinking"""
    clear_screen()
    print("\n📝 WORD SCRAMBLE 📝")
    print("=" * 50)
    print("Unscramble the words as fast as you can!\n")
    
    words = [
        "PYTHON", "CODING", "BRAIN", "PUZZLE", "MEMORY",
        "GENIUS", "SMART", "LEARNING", "CHALLENGE", "THINKING",
        "ALGORITHM", "COMPUTER", "PROGRAM", "CREATIVE", "LOGIC"
    ]
    
    score = 0
    rounds = 5
    
    for round_num in range(1, rounds + 1):
        word = random.choice(words)
        scrambled = list(word)
        random.shuffle(scrambled)
        scrambled_word = ''.join(scrambled)
        
        print(f"\n🎯 Round {round_num}/{rounds}")
        print(f"Unscramble this: {scrambled_word}")
        
        start_time = time.time()
        user_answer = input("Your answer: ").strip().upper()
        time_taken = time.time() - start_time
        
        if user_answer == word:
            points = max(10, int(50 - time_taken * 2))
            score += points
            print(f"✅ CORRECT! +{points} points (faster = more points)")
            print(f"💯 Current Score: {score}")
        else:
            print(f"❌ Wrong! The word was: {word}")
    
    print(f"\n🏆 Final Score: {score} points!")
    print(f"🎓 That's {score / (rounds * 50) * 100:.1f}% of maximum possible!")
    
    input("\nPress Enter to return to menu...")

def reaction_time_game():
    """Test your reaction speed"""
    clear_screen()
    print("\n⚡ REACTION TIME CHALLENGE ⚡")
    print("=" * 50)
    print("Press Enter as FAST as you can when you see GO!")
    print("But be careful - don't press too early!\n")
    
    input("Press Enter when ready...")
    
    total_time = 0
    rounds = 3
    
    for round_num in range(1, rounds + 1):
        print(f"\n🎯 Round {round_num}/{rounds}")
        print("Get ready...")
        
        wait_time = random.uniform(1, 3)
        time.sleep(wait_time)
        
        print("\n🟢 GO! Press Enter NOW!")
        start = time.time()
        input()
        reaction = time.time() - start
        
        total_time += reaction
        print(f"⏱️  Your time: {reaction:.3f} seconds")
        
        if reaction < 0.3:
            print("🚀 Lightning fast!")
        elif reaction < 0.5:
            print("⚡ Very quick!")
        elif reaction < 0.7:
            print("👍 Good reflexes!")
        else:
            print("🐌 You can do better!")
    
    average = total_time / rounds
    print(f"\n📊 Average Reaction Time: {average:.3f} seconds")
    
    if average < 0.4:
        print("🏆 AMAZING! You have superhuman reflexes!")
    elif average < 0.6:
        print("⭐ Great job! You're faster than most!")
    else:
        print("💪 Keep practicing to improve your speed!")
    
    input("\nPress Enter to return to menu...")

def main_menu():
    """Display main menu and handle game selection"""
    while True:
        clear_screen()
        display_banner()
        
        print("\n🎮 SELECT YOUR GAME:")
        print("\n1. 🔢 Number Memory Challenge")
        print("2. 🧮 Math Challenge")
        print("3. 🎨 Color Pattern Matching")
        print("4. 📝 Word Scramble")
        print("5. ⚡ Reaction Time Challenge")
        print("6. 🚪 Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            number_memory_game()
        elif choice == '2':
            math_challenge_game()
        elif choice == '3':
            pattern_matching_game()
        elif choice == '4':
            word_scramble_game()
        elif choice == '5':
            reaction_time_game()
        elif choice == '6':
            clear_screen()
            print("\n👋 Thanks for playing! Keep your brain sharp! 🧠")
            print("Come back anytime to challenge yourself!\n")
            sys.exit(0)
        else:
            print("\n❌ Invalid choice! Please select 1-6.")
            time.sleep(2)

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        clear_screen()
        print("\n\n👋 Game interrupted. Thanks for playing! 🧠\n")
        sys.exit(0)
