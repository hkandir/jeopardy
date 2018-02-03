import json
import pprint as pp

# data = {
#   "Vocabulary":{
#     "question": "on",
#     "timer": 15,
#     "timerUnit": "s",
#     "nameGroup1": "Apple",
#     "nameGroup2": "Orange"
#     },
#   "Grammer":{
#     "question": "on",
#     "timer": 15,
#     "timerUnit": "s",
#     "nameGroup1": "Apple",
#     "nameGroup2": "Orange"},
#   "Tenses":{
#     "question": "on",
#     "timer": 15,
#     "timerUnit": "s",
#     "nameGroup1": "Apple",
#     "nameGroup2": "Orange"
#     },
#   "Punctuation":{
#    "question": "on",
#    "timer": 15,
#    "timerUnit": "s",
#    "nameGroup1": "Apple",
#    "nameGroup2": "Orange"
#  }
# }

# data = {
# "Vocabulary":{
#       "0":{
#           "question": "on",
#           "timer": 15,
#           "timerUnit": "s",
#           "nameGroup1": "Apple",
#           "nameGroup2": "Orange"
#         },
#         "1":{
#             "question": "on",
#             "timer": 15,
#             "timerUnit": "s",
#             "nameGroup1": "Apple",
#             "nameGroup2": "Orange"
#           },
#           "2":{
#               "question": "on",
#               "timer": 15,
#               "timerUnit": "s",
#               "nameGroup1": "Apple",
#               "nameGroup2": "Orange"
#             },
#             "3":{
#                 "question": "on",
#                 "timer": 15,
#                 "timerUnit": "s",
#                 "nameGroup1": "Apple",
#                 "nameGroup2": "Orange"
#               }
#     },
#   "Grammer":{
#     "0":{
#     "question": "on",
#     "timer": 15,
#     "timerUnit": "s",
#     "nameGroup1": "Apple",
#     "nameGroup2": "Orange"
#       },
#       "1":{
#       "question": "on",
#       "timer": 15,
#       "timerUnit": "s",
#       "nameGroup1": "Apple",
#       "nameGroup2": "Orange"
#         },
#         "2":{
#         "question": "on",
#         "timer": 15,
#         "timerUnit": "s",
#         "nameGroup1": "Apple",
#         "nameGroup2": "Orange"
#           },
#           "3":{
#           "question": "on",
#           "timer": 15,
#           "timerUnit": "s",
#           "nameGroup1": "Apple",
#           "nameGroup2": "Orange"
#             }
#   },
#   "Tenses":{
#     "0":{"question": "on",
#     "timer": 15,
#     "timerUnit": "s",
#     "nameGroup1": "Apple",
#     "nameGroup2": "Orange"},
#     "1":{"question": "on",
#     "timer": 15,
#     "timerUnit": "s",
#     "nameGroup1": "Apple",
#     "nameGroup2": "Orange"},
#     "2":{"question": "on",
#     "timer": 15,
#     "timerUnit": "s",
#     "nameGroup1": "Apple",
#     "nameGroup2": "Orange"},
#     "3":{"question": "on",
#     "timer": 15,
#     "timerUnit": "s",
#     "nameGroup1": "Apple",
#     "nameGroup2": "Orange"}
#     },
#   "Punctuation":{
#     "0":{"question": "on",
#     "timer": 15,
#     "timerUnit": "s",
#     "nameGroup1": "Apple",
#     "nameGroup2": "Orange"},
#     "1":{"question": "on",
#     "timer": 15,
#     "timerUnit": "s",
#     "nameGroup1": "Apple",
#     "nameGroup2": "Orange"},
#     "2":{"question": "on",
#     "timer": 15,
#     "timerUnit": "s",
#     "nameGroup1": "Apple",
#     "nameGroup2": "Orange"},
#     "3":{"question": "on",
#     "timer": 15,
#     "timerUnit": "s",
#     "nameGroup1": "Apple",
#     "nameGroup2": "Orange"}
#  }
# }

# Reading Questions
with open('Questions.json', 'r') as f:
     data = json.load(f)

pp.pprint(data['Vocabulary']['0']['question'])

# # Writing JSON data
# with open('data.json', 'w') as f:
#      json.dump(data, f, indent=1)
#
# # Reading data back
# with open('data.json', 'r') as f:
#      data2 = json.load(f)
#
# pp.pprint(data2)
