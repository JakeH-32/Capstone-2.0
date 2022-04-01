import modelBuilder as mb
import pandas as pd

def initialize():
    # data = mb.importData()
    # distributions = mb.distributionBuilder(data)  # build the chi-squared upper and lower bound dist for each Q
    # questionDifficulty = mb.difficulty(data)  # build student perceived difficulty model
    # problem = mb.startingQ(data, questionDifficulty)
    data = pd.read_csv("data.csv")
    distributions = pd.read_csv("distributions.csv")
    questionDifficulty = pd.read_csv("questionDifficulty.csv")
    problem = mb.startingQ(data, questionDifficulty)
    return problem, questionDifficulty, distributions  # return all that we found
