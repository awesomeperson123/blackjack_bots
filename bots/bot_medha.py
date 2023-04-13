class Bot:
    def blackjack_score(self, hand):
        #TODO: return the score of the hand
        score = 0
        num_aces = 0
        for card in hand:
            if card.rank >= 10:
                score += 10
            if card.rank < 10 and card.rank > 1:
                score += card.rank
            if card.rank < 2:
                num_aces += 1
                score += 11
        for i in range(num_aces):
            if score > 21:
                score -= 10
        return score

    def get_decision(self, dealer_up_card, hand, dealer_prev_hand):
        score = self.blackjack_score(hand)
        if dealer_up_card.rank == 2:
            if score in [4, 5, 6, 7, 8, 9, 12]:
                return "hit"
            if score in [10, 11]:
                return "double down"
            if score in [13, 14, 15, 16, 17, 18, 19, 20, 21]:
                return "stand"
        if dealer_up_card.rank == 3:
            if score in [4, 5, 6, 7, 8, 12]:
                return "hit"
            if score in [9, 10, 11]:
                return "double down"
            if score in [13, 14, 15, 16, 17, 18, 19, 20, 21]:
                return "stand"
        if dealer_up_card.rank == 4:
            if score in [4, 5, 6, 7, 8]:
                return "hit"
            if score in [9, 10, 11]:
                return "double down"
            if score in [12, 13, 14, 15, 16, 17, 18, 19, 20, 21]:
                return "stand"
        if dealer_up_card.rank == 4:
            if score in [4, 5, 6, 7, 8]:
                return "hit"
            if score in [9, 10, 11]:
                return "double down"
            if score in [12, 13, 14, 15, 16, 17, 18, 19, 20, 21]:
                return "stand"
        if dealer_up_card.rank == 5:
            if score in [4, 5, 6, 7, 8]:
                return "hit"
            if score in [9, 10, 11]:
                return "double down"
            if score in [12, 13, 14, 15, 16, 17, 18, 19, 20, 21]:
                return "stand"
        if dealer_up_card.rank == 6:
            if score in [4, 5, 6, 7, 8]:
                return "hit"
            if score in [9, 10, 11]:
                return "double down"
            if score in [12, 13, 14, 15, 16, 17, 18, 19, 20, 21]:
                return "stand"
        if dealer_up_card.rank == 7:
            if score in [4, 5, 6, 7, 8, 9, 12, 13, 14, 15]:
                return "hit"
            if score in [10, 11]:
                return "double down"
            if score in [16, 17, 18, 19, 20, 21]:
                return "stand"
        if dealer_up_card.rank == 8:
            if score in [4, 5, 6, 7, 8, 9, 12, 13, 14, 15]:
                return "hit"
            if score in [10, 11]:
                return "double down"
            if score in [16, 17, 18, 19, 20, 21]:
                return "stand"
        if dealer_up_card.rank == 9:
            if score in [4, 5, 6, 7, 8, 9, 12, 13, 14, 15]:
                return "hit"
            if score in [10, 11]:
                return "double down"
            if score in [16, 17, 18, 19, 20, 21]:
                return "stand"
        if dealer_up_card.rank >= 10:
            if score in [4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15]:
                return "hit"
            if score == 11:
                return "double down"
            if score in [16, 17, 18, 19, 20, 21]:
                return "stand"
        if dealer_up_card.rank == 1:
            if score in [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
                return "hit"
            if score in  [16, 17, 18, 19, 20, 21]:
                return "stand"
