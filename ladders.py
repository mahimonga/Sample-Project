step = {1:38, 4:14, 9:31, 21:42, 28:84, 51:67, 72:91, 80:99}
def ladders(x):
    if x in step.keys():
        final_val = step[x]
        return final_val
    return x
