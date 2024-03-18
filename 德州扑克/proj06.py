
import cards

def less_than(c1,c2):
    '''Return 
           True if c1 is smaller in rank, 
           True if ranks are equal and c1 has a 'smaller' suit
           False otherwise'''
    if c1.rank() < c2.rank():
        return True
    elif c1.rank() == c2.rank() and c1.suit() < c2.suit():
        return True
    return False
    
def min_in_list(L):
    '''Return the index of the mininmum card in L'''
    min_card = L[0]  # first card
    min_index = 0
    for i,c in enumerate(L):
        if less_than(c,min_card):  # found a smaller card, c
            min_card = c
            min_index = i
    return min_index
        
def cannonical(H):
    ''' Selection Sort: find smallest and swap with first in H,
        then find second smallest (smallest of rest) and swap with second in H,
        and so on...'''
    for i,c in enumerate(H):
        # get smallest of rest; +i to account for indexing within slice
        min_index = min_in_list(H[i:]) + i 
        H[i], H[min_index] = H[min_index], c  # swap
    return H

def flush_7(H):
    '''Return a list of 5 cards forming a flush,
       if at least 5 of 7 cards form a flush in H, a list of 7 cards, 
       False otherwise.'''
    H = cannonical(H)
    d = {}
    for i in H:
        if i.suit() in d:
            d[i.suit()].append(i)
        else:
            d[i.suit()] = [i]
    for i,j in d.items():
        if len(j) >= 5:
            return cannonical(d[i][:5])
    return []

def straight_7(H):
    H = cannonical(H)
    '''Return a list of 5 cards forming a straight,
       if at least 5 of 7 cards form a straight in H, a list of 7 cards, 
       False otherwise.'''
    for i in range(3):
        flag = 1
        r = [c for c in H[i:i+5]]
        for j in range(1,5):
            if r[j].value() != r[j-1].value() + 1:
                flag = 0
                break
        if flag:
            return cannonical(r)
    return []
def straight_flush_7(H):
    '''Return a list of 5 cards forming a straight flush,
       if at least 5 of 7 cards form a straight flush in H, a list of 7 cards, 
       False otherwise.'''
    H = cannonical(H)
    if straight_7(H):
        H = straight_7(H)
        if flush_7(H):
            return cannonical(H)
        else:
            return []
    else:
        return []

def four_7(H):
    '''Return a list of 4 cards with the same rank,
       if 4 of the 7 cards have the same rank in H, a list of 7 cards, 
       False otherwise.'''
    H = cannonical(H)
    d = {}
    for i in H:
        if i.rank() in d:
            d[i.rank()].append(i)
        else:
            d[i.rank()] = [i]
    for i, j in d.items():
        if len(j) >= 4:
            return cannonical(d[i][:4])
    return []

def three_7(H):
    '''Return a list of 3 cards with the same rank,
       if 3 of the 7 cards have the same rank in H, a list of 7 cards, 
       False otherwise.
       You may assume that four_7(H) is False.'''
    H = cannonical(H)
    d = {}
    for i in H:
        if i.rank() in d:
            d[i.rank()].append(i)
        else:
            d[i.rank()] = [i]
    for i, j in d.items():
        if len(j) >= 3:
            return cannonical(d[i][:3])
    return []
        
def two_pair_7(H):
    '''Return a list of 4 cards that form 2 pairs,
       if there exist two pairs in H, a list of 7 cards, 
       False otherwise.  
       You may assume that four_7(H) and three_7(H) are both False.'''
    H = cannonical(H)
    d = {}
    for i in H:
        if i.rank() in d:
            d[i.rank()].append(i)
        else:
            d[i.rank()] = [i]
    d = sorted(d.items(),key=lambda x:len(x[1]),reverse=True)
    if len(d[0][1]) == 2 and len(d[1][1]) == 2:
        return cannonical(d[0][1] + d[1][1])
    return []

def one_pair_7(H):
    '''Return a list of 2 cards that form a pair,
       if there exists exactly one pair in H, a list of 7 cards, 
       False otherwise.  
       You may assume that four_7(H), three_7(H) and two_pair(H) are False.'''
    H = cannonical(H)
    d = {}
    for i in H:
        if i.rank() in d:
            d[i.rank()].append(i)
        else:
            d[i.rank()] = [i]
    d = sorted(d.items(), key=lambda x: len(x[1]), reverse=True)
    if len(d[0][1]) == 2:
        return cannonical(d[0][1])
    return []

def full_house_7(H):
    '''Return a list of 5 cards forming a full house,
       if 5 of the 7 cards form a full house in H, a list of 7 cards, 
       False otherwise.
       You may assume that four_7(H) is False.'''
    H = cannonical(H)
    d = {}
    for i in H:
        if i.rank() in d:
            d[i.rank()].append(i)
        else:
            d[i.rank()] = [i]
    d = sorted(d.items(), key=lambda x: len(x[1]), reverse=True)
    if len(d[0][1]) == 3 and len(d[1][1]) == 2:
        return cannonical(d[0][1] + d[1][1])
    return []

def main():
    D = cards.Deck()
    D.shuffle()
       
    while True:
        # create community cards
        community_list = []
        hand_1_list = []
        hand_2_list = []
        for i in range(5):
            community_list.append(D.deal())
        for i in range(2):
            hand_1_list.append(D.deal())
        for i in range(2):
            hand_2_list.append(D.deal())
        # create Player 1 hand
        # create Player 2 hand

        print("-"*40)
        print("Let's play poker!\n")
        print("Community cards:",community_list)
        print("Player 1:",hand_1_list)
        print("Player 2:",hand_2_list)
        print()
        while True:
            if straight_flush_7(hand_1_list+community_list) and straight_flush_7(hand_2_list+community_list):
                print("TIE with straight flush:",straight_flush_7(hand_1_list+community_list))
                break
            elif straight_flush_7(hand_1_list+community_list) or straight_flush_7(hand_2_list+community_list):
                if straight_flush_7(hand_1_list+community_list):
                    print("Player 1 wins with straight flush:",straight_flush_7(hand_1_list+community_list))
                else:
                    print("Player 2 wins with straight flush:", straight_flush_7(hand_2_list+community_list))
                break
            if four_7(hand_1_list + community_list) and four_7(hand_2_list + community_list):
                print("TIE with 4 of a kind:", four_7(hand_1_list + community_list))
                break
            elif four_7(hand_1_list + community_list) or four_7(hand_2_list + community_list):
                if four_7(hand_1_list + community_list):
                    print("Player 1 wins with 4 of a kind:", four_7(hand_1_list + community_list))
                else:
                    print("Player 2 wins with 4 of a kind:", four_7(hand_2_list + community_list))
                break
            if full_house_7(hand_1_list + community_list) and full_house_7(hand_2_list + community_list):
                print("TIE with a full house:", full_house_7(hand_1_list + community_list))
                break
            elif full_house_7(hand_1_list + community_list) or full_house_7(hand_2_list + community_list):
                if full_house_7(hand_1_list + community_list):
                    print("Player 1 wins with a full house:", full_house_7(hand_1_list + community_list))
                else:
                    print("Player 2 wins with a full house:", full_house_7(hand_2_list + community_list))
                break
            if flush_7(hand_1_list + community_list) and flush_7(hand_2_list + community_list):
                print("TIE with a flush:", flush_7(hand_1_list + community_list))
                break
            elif flush_7(hand_1_list + community_list) or flush_7(hand_2_list + community_list):
                if flush_7(hand_1_list + community_list):
                    print("Player 1 wins with a flush:", flush_7(hand_1_list + community_list))
                else:
                    print("Player 2 wins with a flush:", flush_7(hand_2_list + community_list))
                break
            if straight_7(hand_1_list + community_list) and straight_7(hand_2_list + community_list):
                print("TIE with a straight:", straight_7(hand_1_list + community_list))
                break
            elif straight_7(hand_1_list + community_list) or straight_7(hand_2_list + community_list):
                if straight_7(hand_1_list + community_list):
                    print("Player 1 wins with a straight:", straight_7(hand_1_list + community_list))
                else:
                    print("Player 2 wins with a straight:", straight_7(hand_2_list + community_list))
                break
            if three_7(hand_1_list + community_list) and three_7(hand_2_list + community_list):
                print("TIE with 3 of a kind:", three_7(hand_1_list + community_list))
                break
            elif three_7(hand_1_list + community_list) or three_7(hand_2_list + community_list):
                if three_7(hand_1_list + community_list):
                    print("Player 1 wins with 3 of a kind:", three_7(hand_1_list + community_list))
                else:
                    print("Player 2 wins with 3 of a kind:", three_7(hand_2_list + community_list))
                break
            if two_pair_7(hand_1_list + community_list) and two_pair_7(hand_2_list + community_list):
                print("TIE with two pairs:", two_pair_7(hand_1_list + community_list))
                break
            elif two_pair_7(hand_1_list + community_list) or two_pair_7(hand_2_list + community_list):
                if two_pair_7(hand_1_list + community_list):
                    print("Player 1 wins with two pairs:", two_pair_7(hand_1_list + community_list))
                else:
                    print("Player 2 wins with two pairs:", two_pair_7(hand_2_list + community_list))
                break
            if one_pair_7(hand_1_list + community_list) and one_pair_7(hand_2_list + community_list):
                print("TIE with two pairs:", one_pair_7(hand_1_list + community_list))
                break
            elif one_pair_7(hand_1_list + community_list) or one_pair_7(hand_2_list + community_list):
                if one_pair_7(hand_1_list + community_list):
                    print("Player 1 wins with one pairs:", one_pair_7(hand_1_list + community_list))
                else:
                    print("Player 2 wins with one pairs:", one_pair_7(hand_2_list + community_list))
                break
            c1 = cannonical(hand_1_list + community_list)[-1]
            c2 = cannonical(hand_2_list + community_list)[-1]
            if c1.rank() < c2.rank():
                print("Player 2 wins with High card,:", c2)
            elif c1.rank() == c2.rank() and c1.suit() < c2.suit():
                print("Player 2 wins with High card,:", c2)
            else:
                print("Player 1 wins with High card,:", c1)
            break
        print()
        if len(D) < 9:
            print('Deck has too few cards so game is done.')
            break
        choose = input('Do you wish to play another hand?(Y or N)')
        if choose == 'y':
            pass
        else:
            break

if __name__ == "__main__":
    main()