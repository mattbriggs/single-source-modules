import json
import pystache as ST
import common_utilities as CU

with open(r"C:\git\mb\single-source-modules\source\contextdata.json", 'r') as json_file:
    full_context = json.load(json_file)

source_files = CU.get_files(r"C:\git\mb\single-source-modules\source")

contexts = ["asdk", "ash", "mdc"]

for context in contexts:
    for path in source_files:
        file_name = path.split("\\")[-1]
        template = CU.get_text_from_file(path)
        context_dict = {}
        for term in full_context.keys():
            context_dict[term] = full_context[term][context]
        outpath = "C:\\git\\mb\\single-source-modules\\share\\{}\\{}".format(context, file_name)
        text = ST.render(template, context_dict)
        CU.write_text(text, outpath)
        print("Created: {}".format(outpath))