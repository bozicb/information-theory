import math
import pandas as pd

def entropy(probabilities):
    return sum([p*math.log(p,2) for p in probabilities])*(-1) # apply entropy formula to probabilities

def ig(abt):
    num_columns = len(abt.columns)
    num_rows = len(abt.index)
    target = abt.columns[num_columns-1]
    features = abt.columns[0:num_columns-1]
    ps = []
    for l in abt[target].unique():
        ps.append(abt[target].value_counts()[l]/num_rows)
    e = entropy(ps)
    rems = []
    for feature in features:
        levels = abt[feature].unique()
        part_ents = []
        for level in levels:
            weight = abt[feature].value_counts()[level]/num_rows
            ent = entropy(abt.loc[abt[feature] == level][target].value_counts()/len(abt.loc[abt[feature] == level]))
            part_ents.append(weight*ent)
        rems.append(sum(part_ents))
    infGains = e - rems
    return pd.DataFrame({'feature':features,'IG':infGains})

def ig_ratio(iG, feature_entropy):
    return iG/feature_entropy # I know, this is deadly, right? :D

def gini_index(probabilities):
    return 1-sum([p**2 for p in probabilities]) # a lil' list comprehension for the gini index, not too shabby ...
