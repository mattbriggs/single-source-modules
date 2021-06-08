import json
import pystache as ST
import common_utilities as CU

with open(r"C:\git\mb\single-source-modules\modules\contextdata.json", 'r') as json_file:
    context_dict = json.load(json_file)

source_files = CU.get_files(r"C:\git\mb\single-source-modules\modules")

contexts = ["context1", "context2", "context3"]

sub_dict = {}
for path in source_files:
    file_name = path.split("\\")[-1]
    template = CU.get_text_from_file(path)
    for i in list(context_dict.keys()):
        for context in contexts:
            sub_dict[i] = context_dict[i][context]
            page = ST.render(template, sub_dict)
            outpath = "C:\\git\\mb\\single-source-modules\\{}\\{}".format(context, file_name)
            CU.write_text(page, outpath)
            print("Created: {}".format(outpath))