

taomlar = ['osh', 'manti','somsa']

nonushta = taomlar[:]
nonushta.remove('osh')
nonushta.append('shashlik')
nonushta.append(('qozonkabob'))
print(taomlar)

nonushta = tuple(nonushta)
print(nonushta)
nonushta =list(nonushta)
nonushta[0] = "qatiq"
print(nonushta)