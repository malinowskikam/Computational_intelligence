import plotly.graph_objects as go
import pandas
from apyori import apriori


class Rule:
    def __init__(self,premises,conclusions,support,confidence,lift):
        self.premises = premises
        self.conclusions = conclusions
        self.support = support
        self.confidence = confidence
        self.lift = lift

    def __repr__(self):
        return "Rule: " + str(self.premises) + " => " + str(self.conclusions) \
               + "\nSupport: " + str(self.support)\
               + "\nConfidence: " + str(self.confidence)\
               + "\nLift: " + str(self.lift)

    def about_survivability(self):
        return 'Yes' in self.conclusions \
               or 'No' in self.conclusions

    def about_gender_distribiution(self):
        return 'Male' in self.conclusions \
               or 'Female' in self.conclusions


data = pandas.read_csv("titanic.csv").drop("ID",axis=1).values
rules = apriori(data, min_confidence=0.7)
rules_list = list()

for item in rules:

    rules_list.append(Rule(
        list(item.ordered_statistics[0].items_base),
        list(item.ordered_statistics[0].items_add),
        item.support,
        item.ordered_statistics[0].confidence,
        item.ordered_statistics[0].lift
    ))

rules_list.sort(key=lambda x: x.confidence, reverse=True)

rules_survived = list()
rules_gender = list()

for rule in rules_list:
    if rule.about_survivability():
        rules_survived.append(rule)
    if rule.about_gender_distribiution():
        rules_gender.append(rule)


for rule in rules:
    print('==============')
    print(rule)
    print('==============')
    print()

fig_crew_gender = go.Figure(
    data=go.Pie(
        title="Załoga Titanica",
        labels=["Mężczyźni","Kobiety"],
        values=[0.9740112994350282,1-0.9740112994350282]
    )
)
fig_crew_gender.show()

fig_male_survivability = go.Figure(
    data=go.Pie(
        title="Przeżywalność Mężczyzn",
        labels=["Przeżyli","Nie Przeżyli"],
        values=[1-0.7972405518896222,0.7972405518896222]
    )
)
fig_male_survivability.show()

fig_female_survivability = go.Figure(
    data=go.Pie(
        title="Przeżywalność Kobiet",
        labels=["Przeżyły","Nie Przeżyły"],
        values=[0.7319148936170213,1-0.7319148936170213]
    )
)
fig_female_survivability.show()
