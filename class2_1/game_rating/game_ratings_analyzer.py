import csv

def normalize_path(path): 
    return path.replace("\\", "/")

def is_valid_rating(r):
    return 0 <= r <= 10

def is_tie(games,i):
    if(i==0):
        return False
    return games[i][1] == games[i-1][1]

def read_ratings(file_path):
    ratings = {}
    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            title = row["title"]
            rating = int(row["rating"])
            if title in ratings:
                ratings[title].append(rating)
            else:
                ratings[title] = [rating]
    return ratings

def generate_report(ratings, top_n):
    averages = {}
    for title, scores in ratings.items():
        averages[title] = sum(scores) / len(scores)

    sorted_games = sorted(averages.items(), key=lambda x: x[1], reverse=True)         

    j=0
    
    for i in range(top_n):  #iterate하면서 해당 값 realRate 값이 특정 등수 안에 들때까지 반복
         
        if( is_valid_rating(j)) :
            title, avg = sorted_games[i]
            if(not is_tie(sorted_games, i)):
                j= j+1
            print(f"{j}. {title} - Avg Rating: {avg:.2f}")


def main():
    path = "game_rating\\data\\game_ratings.csv"
    file_path = normalize_path(path)
    ratings = read_ratings(file_path)
    generate_report(ratings, 10)

if __name__ == "__main__":
    main()
