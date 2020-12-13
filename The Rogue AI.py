# The following Logic Puzzle can be found on Ted-Ed:    https://www.youtube.com/watch?v=qMFpOcLroOg

levels = 25

Steps = [1,3,4]


def minimax_AB(depth,step, maxP,alpha,beta):
    if(depth == 0):
        return (step *-1,0) if maxP else (step,0)

    if maxP:
        maxEval = -10000
        move = 0
        for step in Steps:
            if depth - step >= 0:
                eval,usedMove = minimax_AB(depth-step, step, False, alpha, beta)
                if eval > maxEval:
                    maxEval = eval
                    move = step
                alpha = max(alpha,eval)
                if beta <= alpha:
                    break
        return maxEval, move
    
    else:
        minEval = 10000
        move = 0
        for step in Steps:
            if depth - step >= 0:
                eval,usedStep = minimax_AB(depth-step,step, True, alpha, beta)
                if eval < minEval:
                    minEval = eval
                    move = step
                beta = min(beta,eval)
                if beta <= alpha:
                    break
        return minEval, move

def minimax(depth,step, maxP):
    if(depth == 0):
        return (step *-1,0) if maxP else (step,0)

    if maxP:
        maxEval = -10000
        move = 0
        for step in Steps:
            if depth - step >= 0:
                eval,usedMove = minimax(depth-step, step, False)
                if eval > maxEval:
                    maxEval = eval
                    move = step
        return maxEval, move
    
    else:
        minEval = 10000
        move = 0
        for step in Steps:
            if depth - step >= 0:
                eval,usedStep = minimax(depth-step,step, True)
                if eval < minEval:
                    minEval = eval
                    move = step
        return minEval, move


while levels >= 0:
    print("Levels remaining: %d" %(levels))
    user_move = int(input("Enter your move(1,3,4): "))
    # wins, user_move = minimax(levels, 0, True, -10000, 10000)
    if user_move in Steps and levels - user_move >= 0:
        print("User played %d"%(user_move))
        levels -= user_move
        print("Levels remaining: %d" %(levels))
        if levels == 0:
            print("AI loses")
            break
        wins, computer_move = minimax_AB(levels, user_move, True, -10000,10000)
        levels -= computer_move
        print("AI played: %d" %(computer_move))
        if levels == 0:
            print("You lose")
            break
    else:
        print("Invalid move")