def J3(distances_string):
    dists = distances_string.split(" ")   
    dist_matrix = []   
    for i in range(5):
        dist_matrix.append([])   
        for j in range(5):
            if(j >= i):
                if(i == j):
                    dist_matrix[i].append(0)   
                else:
                    dist_matrix[i].append(dist_matrix[i][j - 1] + int(dists[j - 1]))   
            else:
                dist_matrix[i].append(dist_matrix[j][i])   
    return dist_matrix   

distances = input()   
answer = J3(distances)   
for i in range(5):
    print(*answer[i])   