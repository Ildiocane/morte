# Map times authored against the v1 edit (assets/edit-v1.cutmap.json) onto the current edit (assets/edit.cutmap.json),
# via source time. Writes assets/timemap.json: new-edit time for every old-edit time sampled at 0.05s.
import json
old = json.load(open('assets/edit-v1.cutmap.json')); new = json.load(open('assets/edit.cutmap.json'))
def old_to_src(t):
    p = old[0]
    for q in old:
        if q['edit_start'] <= t: p = q
    return min(p['src_start'] + (t - p['edit_start']), p['src_end'])
def src_to_new(s):
    for q in new:
        if s < q['src_start']: return q['edit_start']          # removed region -> next kept piece
        if s <= q['src_end']: return q['edit_start'] + (s - q['src_start'])
    last = new[-1]; return last['edit_start'] + (last['src_end'] - last['src_start'])
end = old[-1]['edit_start'] + old[-1]['src_end'] - old[-1]['src_start']
table = [round(src_to_new(old_to_src(i * 0.05)), 3) for i in range(int(end / 0.05) + 2)]
for i in range(1, len(table)): table[i] = max(table[i], table[i - 1])   # monotonic
json.dump(table, open('assets/timemap.json', 'w'))
print(len(table), 'samples; old end', round(end, 2), '-> new', table[-1])
