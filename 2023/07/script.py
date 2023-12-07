import sys
from collections import Counter


def p1_convert(c: str) -> int:
    conversion = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    if c.isdigit():
        return int(c)
    else:
        return conversion[c]

def p2_convert(c: str) -> int:
    conversion = {"T": 10, "J": 1, "Q": 12, "K": 13, "A": 14}
    if c.isdigit():
        return int(c)
    else:
        return conversion[c]

def grade_from_counts(counts):
   if counts[-1] == 5: return 7
   elif counts[-1] == 4: return 6
   elif counts[-1] == 3 and counts[-2] == 2: return 5
   elif counts[-1] == 3: return 4
   elif counts[-1] == 2 and counts[-2] == 2: return 3
   elif counts[-1] == 2: return 2
   else: return 1

def p1_grade_hand(hand: list[int]) -> int:
   counts = sorted(Counter(hand).values())
   return grade_from_counts(counts)

def p2_grade_hand(hand: list[int]) -> int:
   counts = dict(Counter(hand))

   if 1 in counts and counts[1] < 5:
       j_count = counts[1]
       del counts[1]
       counts = sorted(counts.values())
       counts[-1] = counts[-1] + j_count
       return grade_from_counts(counts)
   else:
      return grade_from_counts(sorted(counts.values()))       

def winnings(graded_hands: list):
   return sum(((idx + 1) * bid for idx, (_, _, bid) in enumerate(graded_hands)))


p1_graded_hands = []
p2_graded_hands = []

for line in sys.stdin:
   hand, bid = line.rstrip().split(" ")

   p1_hand = [p1_convert(c) for c in hand]
   p1_grade = p1_grade_hand(p1_hand)
   p1_graded_hands.append((p1_grade, p1_hand, int(bid)))

   p2_hand = [p2_convert(c) for c in hand]
   p2_grade = p2_grade_hand(p2_hand)
   p2_graded_hands.append((p2_grade, p2_hand, int(bid)))

p1_graded_hands.sort()
p2_graded_hands.sort()

print(winnings(p1_graded_hands),winnings(p2_graded_hands))
