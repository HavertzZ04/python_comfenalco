#This program ask to users a year in order to find the UEFA Champions League Winner, also it provides how many championms league the teams won, it asks at the end if users want to continue checking more records or otherwise they want to close the program 

champions_league_winners = {
    'Real Madrid': [1956, 1957, 1958, 1959, 1960, 1966, 1998, 2000, 2002, 2014, 2016, 2017, 2018, 2022],
    'AC Milan': [1963, 1969, 1989, 1990, 1994, 2003, 2007],
    'Liverpool': [1977, 1978, 1981, 1984, 2005, 2019],
    'Bayern Munich': [1974, 1975, 1976, 2001, 2013, 2020],
    'Barcelona': [1992, 2006, 2009, 2011, 2015],
    'Ajax': [1971, 1972, 1973, 1995],
    'Manchester United': [1968, 1999, 2008],
    'Inter Milan': [1964, 1965, 2010],
    'Juventus': [1985, 1996],
    'Benfica': [1961, 1962],
    'Nottingham Forest': [1979, 1980],
    'Porto': [1987, 2004],
    'Chelsea': [2012, 2021],
    'Borussia Dortmund': [1997],
    'Marseille': [1993],
    'Feyenoord': [1970],
    'Celtic': [1967],
    'Hamburg': [1983],
    'Steaua București': [1986],
    'PSV Eindhoven': [1988],
    'Aston Villa': [1982],
    'Manchester City': [2023]
}


def exit_validation(func):
    def wrapper():
        while True:
            print(func())
            
            print("0. Exit")
            print("1. Check another year")
            
            answer = input("\nYour answer here: ")
            
            if answer == "0" :
                print("\nHave a good day, bye")
                break                    
    return wrapper


@exit_validation
def winner_year():
    year = int(input("Enter the year to find the UEFA Champions League Winner: "))
    
    for team, years in champions_league_winners.items():
        if year in years:
            return(f"\n{team} was the winner of {year}, in total this team has {len(years)} Champions League\n")
        
    return(f"\nNo winner found in {year}\n")
            

winner_year()
