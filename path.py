from collections import defaultdict

chips = 35
map_thing = [[8, 8, 4, 4, 5], [4,9,6,4,8], [8,6,4,1,2], [4,8,2,6,3], [0,6,8,8,4]]
start_index = (4,0)
end_index = (0,4)
end_row, end_col = end_index
sub_paths = defaultdict(lambda: defaultdict(list))

"""I use the strategy to find the most direct route to the goal that meets the cost requirement. When the cost requirement along the most direct route available is exceeded, the algorithm will back up one step and try a different direction, continuing in the most direct alternate route possible.

But it turns out that the solution will require doubling back, which will not work with the direct route approach. I must add support for moving away from the goal as a last resort before resuming a direct route strategy.

There is a bit of optimization you can do with a (sort of) dynamic programming strategy in this problem. About the best I can think of doing is to keep track of every path that reaches the end state but fails to have the correct score. Then, store every sub-path of that path and their scores. Then if you traverse via another route to a space that is in the set of sub-paths, you can check if you get to the end with the right score with those paths before continuing on with the naive algorithm.

It turns out using this strategy *does* help in finding the path with fewer naive steps."""

def take_step(curr_index, score, path, path_scores):
    #First check for a shortcut sub-path from this index
    goal_score = 35-score
    if curr_index in sub_paths and goal_score in sub_paths[curr_index]:
        print("Found this shortcut: The path " + str(sub_paths[curr_index][goal_score]) + " has score " + str(goal_score))
        print("This is a valid path(ding!): " + str(path + sub_paths[curr_index][goal_score]))
        return True

    #Set all the values for this step
    path.append(curr_index)
    row, col = curr_index
    path_scores.append(map_thing[row][col])
    score += map_thing[row][col]
    
    #The outcome at an end state
    if curr_index == end_index:
        print("Score at the end: %d" % score)
        if score == 35:
            print("This is a valid path: " + str(path))
            return True
        
        #Invalid end path, so record the sub-paths that we can reuse later
        temp_path = []
        temp_path_scores = []
        for n in reversed(range(len(path))):
            temp_path.insert(0, path[n])
            temp_path_scores.insert(0, path_scores[n])
            temp_score = sum(path_scores[n:])
            if temp_score < 35 and temp_score not in sub_paths[path[n]]:
                sub_paths[path[n]][temp_score] = path[n:]
        
        return False
        
    #Score is exceeded before the end, so retreat
    if score >= 35:
        return False
    
    #Convenience variables to follow the most direct route
    row_close_dir = cmp(end_row - row, 0)
    col_close_dir = cmp(end_col - col, 0)
    row_close_index = (row + row_close_dir, col)
    col_close_index = (row, col + col_close_dir)
    
    #Direct route cases
    #Move one row toward the goal        
    if row_close_dir != 0 and take_step(row_close_index, score, path[:], path_scores[:]):
        return True
    #Move one column toward the goal
    if  col_close_dir != 0 and take_step(col_close_index, score, path[:], path_scores[:]):
        return True
    
    #Support for moving away from the goal if none of the other paths worked
    row_down_index = (row + 1, col)
    row_up_index = (row - 1, col)
    
    #Move one row away from the goal. Make sure we don't go off the edge!
    if row_down_index[0] != row_close_index[0] and row < len(map_thing)-1 and take_step(row_down_index, score, path[:], path_scores[:]):
        return True
    if row_up_index[0] != row_close_index[0] and row > 0 and take_step(row_up_index, score, path[:], path_scores[:]):
        return True
    
    col_right_index = (row, col + 1)
    col_left_index = (row, col - 1)
    
    #Move one columns away from the goal. Make sure we don't go off the edge!
    if col_right_index[1] != col_close_index[1] and col < len(map_thing[row])-1 and take_step(col_right_index, score, path[:], path_scores[:]):
        return True
    if col_left_index[1] != col_close_index[1] and col > 0 and take_step(col_left_index, score, path[:], path_scores[:]):
        return True
    
    return False
    

if __name__ == '__main__':

    take_step(start_index, 0, [], [])
