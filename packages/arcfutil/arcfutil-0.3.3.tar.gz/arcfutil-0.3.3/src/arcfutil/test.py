from copy import deepcopy
import aff

# SIXTEENTH = 60000 / 225 / 4

# step = 4 * 10

# fromt = 8865
# destt = 9105
# # frombpm = -225
# # destbpm = 0
# part = 24
# basebpm = 225


# arc = aff.arc(8889, 9399, 1, 0.75, 'siso', 0, 0.5, 1, True)
# part -= 1
# stept = (destt - fromt) / 10
# # print(arc[8889])
# for i in range(1, 11, 2):
#     newarc = deepcopy(arc)
#     newarc.time = fromt + i * stept
#     newarc.totime = fromt + (i + 1) * stept
#     # print(arc[fromt + (i - 1) * stept])
#     newarc.fromx = arc[fromt + i * stept][0]
#     newarc.fromy = arc[fromt + i * stept][1]
#     newarc.tox = arc[fromt + (i + 2) * stept][0]
#     newarc.toy = arc[fromt + (i + 2) * stept][1]
#     newarc.slideeasing = 's'
#     print(newarc)
#     if newarc.time >= destt:
#         break

# fromt = 9105
# destt = 9399
# for i in range(0, 13, 1):
#     newarc = deepcopy(arc)
#     newarc.time = fromt + i * stept

#     newarc.totime = fromt + (i + 1) * stept
#     newarc.fromx = arc[fromt + i * stept][0]
#     newarc.fromy = arc[fromt + i * stept][1]
#     newarc.tox = arc[fromt + (i + 1) * stept][0]
#     newarc.toy = arc[fromt + (i + 1) * stept][1]
#     newarc.slideeasing = 's'
#     print(newarc)
#     if newarc.time >= destt:
#         break

# part -= 1
# stept = (destt - fromt) / part
# for i in range(1, part + 1, 2):
#     newarc = deepcopy(arc)
#     newarc.time = fromt + i * stept
#     newarc.totime = fromt + (i + 1) * stept
#     newarc.fromx = arc[fromt + (i - 1) * stept][0]
#     newarc.fromy = arc[fromt + (i - 1) * stept][1]
#     newarc.tox = arc[fromt + (i + 1) * stept][0]
#     newarc.toy = arc[fromt + (i + 1) * stept][1]
#     newarc.slideeasing = 's'
#     print(newarc)

# part -= 1
# stept = (destt - fromt) / part
# for i in range(0, part + 1):
#     newarc = deepcopy(arc)
#     newarc.time = fromt + i * stept
#     newarc.totime = fromt + (i + 1) * stept
#     newarc.fromx = arc[fromt + i * stept][0]
#     newarc.fromy = arc[fromt + i * stept][1]
#     newarc.tox = arc[fromt + (i + 1) * stept][0]
#     newarc.toy = arc[fromt + (i + 1) * stept][1]
#     newarc.slideeasing = 's'
#     print(newarc)
#     if newarc.totime >= destt:
#         break

# part -= 1
# stept = (destt - fromt) / part
# stepbpm = (destbpm - frombpm) / part
# for i in range(part + 1):
#     print(aff.timing(fromt + i * stept, frombpm + i * stepbpm))

# part -= 1
# zero = True
# stept = (destt - fromt) / part
# stepbpm = (-100) / (part - 1)
# for i in range(part + 1):
#     if zero and i != part:
#         print(aff.timing(fromt + i * stept, i * stepbpm))
#     elif i == part:
#         print(aff.timing(fromt + i * stept, basebpm))
#     else:
#         print(aff.timing(fromt + i * stept, basebpm * 2))

#     zero = not zero

# print(aff.loads('C:/Users/direwolf/arcfutil_output/tempestissimo/3_ano.aff'))

# start = 187600
# end = 188000
# status = False
# while(start + 100 <= end):
#     print(aff.arc(start, start + 100, 0, 0, 's', 1, 1, 0, status))
#     start += 100
#     # status = not status

notelist = aff.loads('test.aff')
aff.dumps(notelist, 'test_out.aff')
