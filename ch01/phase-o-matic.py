# We are importing additional built-in functionality from Python into the program
import random

verbs = ['Leverage', 'Sync', 'Target', 'Gamify', 'Offline', 'Crowd-source', '24/7', 'Lean-in', '30,000 foot']
adjectives = ['A/B Tested', 'Freemium', 'Hyperlocal', 'Siloed', 'B-to-B', 'Oriented', 'Cloud-based', 'API-based']
nouns = ['Early Adpoter', 'Low-hanging Fruit', 'Pipeline', 'Splash Page', 'Productivity', 'Process', 'Tipping Point', 'Paradigm']

verb = random.choice(verbs)
adjective = random.choice(adjectives)
noun = random.choice(nouns)

phrase = verb + ' ' + adjective + ' ' + noun

print(phrase)
