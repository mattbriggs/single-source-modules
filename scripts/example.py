

# https://github.com/defunkt/pystache

import json
import chevron as ST

context_variables = '''{
    "concept1": {
        "context1": "concept1",
        "context2": "idea1",
        "context3": "entity1"
    },
    "animal": {
        "context1": "dog",
        "context2": "cat",
        "context3": "fish"
    }
}'''

var = json.loads(context_variables)

text = '''During the first weeks of their acquaintance Morgan had been as puzzling
as a page in an unknown language—altogether different from the obvious
little Anglo-Saxons who had misrepresented childhood to {{concept1}}.
Indeed the whole mystic volume in which the boy had been amateurishly
bound demanded some practice in translation.  To-day, after a
considerable interval, there is something phantasmagoria, like a
prismatic reflexion or a serial novel, in {{concept1}}'s memory of the
queerness of the Moreens.  If it were not for a few tangible tokens—a
lock of Morgan's hair cut by his own hand, and the half-dozen letters
received from him when they were disjoined—the whole episode and the
figures peopling it would seem too inconsequent for anything but
dreamland.  Their supreme quaintness was their success—as it appeared to
him for a while at the time; since he had never seen a family so
brilliantly equipped for failure.  Wasn't it success to have kept him so
hatefully long?  Wasn't it success to have drawn him in that first
morning at déjeuner, the Friday he came—it was enough to _make_ one
superstitious—so that he utterly committed himself, and this not by
calculation or on a signal, but from a happy instinct which made them,
like a band of gipsies, work so neatly together?  They amused him as much
as if they had really been a band of gipsies.  He was still young and had
not seen much of the world—his {{concept1}} years had been properly arid;
therefore the reversed conventions of the Moreens—for they had _their_
desperate proprieties—struck him as topsy-turvy.  He had encountered
nothing like them at Oxford; still less had any such note been struck to
his younger American ear during the four years at {{animal}} in which he had
richly supposed himself to be reacting against a Puritan strain.  The
reaction of the {{concept1}}, at any rate, went ever so much further.  He had
thought himself very sharp that first day in hitting them all off in his
mind with the **cosmopolite** label.  Later it seemed feeble and
colourless—confessedly helplessly provisional.

{{#context1 }}
This is context one.
{{/context1 }}

{{#context2 }}
  This is context two.
{{/context2 }}

{{#context3 }}
  This is context three.
{{/context3 }}
'''

#filter dictionary by key

contexts = ["context1", "context2", "context3"]
for context in contexts:
    print("{}====".format(context))
    context_dict = {}
    for term in var.keys():
        context_dict[term] = var[term][context]
    context_dict[context] = True
    print(context_dict)

    print(ST.render(text, context_dict))