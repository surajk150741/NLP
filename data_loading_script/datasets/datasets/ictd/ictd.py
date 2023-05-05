# Copyright 2020 The HuggingFace Datasets Authors and the current dataset script contributor.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# Lint as: python3
"""ICTD: The IA choosing table dataset"""

import csv
import json
import os

import datasets

# Verbose: using or containing more words than are needed.
# Logging: logging methods allow us to easily adjust the level of verbosity of the entire library.
logger = datasets.logging.get_logger(__name__)

_CITATION = """\
@article{
       author = {Suraj Kumar},
        title = "{ICTD: Choosing table related to a natural language query}",
        year = 2022
}
"""

_DESCRIPTION = """\
This new dataset is designed to assign a table/schema to any natural language query as an input \
for example, "all campaigns that are active" is related to "campaign" table. and "number of houses with 5 bedrooms" 
is related to well being table.
"""

#_URL = "https://surajjkumar.github.io/dataset/"
_URL = "https://surajjkumar.github.io/ictd_dataset/datasets/"
_URLS = {
        "train": _URL + "train.json",
        "dev": _URL + "dev.json",
        #"train": _URL + "train.csv",
        #"dev": _URL + "dev.csv"
}

## *args, **kwargs:  https://www.geeksforgeeks.org/args-kwargs-python/
        
class ICTDConfig(datasets.BuilderConfig):
    """BuilderConfig for ICTD."""

    def __init__(self, **kwargs):
        """BuilderConfig for ICTD.
        Args:
          **kwargs: keyword arguments forwarded to super.
        """
        super(ICTDConfig, self).__init__(**kwargs)

class ictd(datasets.GeneratorBasedBuilder):
    """ICTD: The IA choosing table dataset. Version 1.1."""

    BUILDER_CONFIGS = [
        ICTDConfig(
            name="plain_text",
            version=datasets.Version("1.0.0", ""),
            description="Plain text",
        ),
    ]

    def _info(self):
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            
            features=datasets.Features(
                {
                    "title": datasets.Value("string"),
                    "table_names": datasets.features.Sequence(
                        {
                            "nlq": datasets.Value("string"),
                            "table": datasets.Value("string"),
                        }
                    ),
                }
            ),
            # No default supervised_keys (as we have to pass both question
            # and context as input).
            supervised_keys=None,
            homepage="https://surajjkumar.github.io/",
            citation=_CITATION,
            
            #task_templates=[
                #QuestionAnsweringExtractive(
                    #question_column="question", context_column="context", answers_column="answers"
                #)
            #],
            
        )

    def _split_generators(self, dl_manager):
        # TODO: This method is tasked with downloading/extracting the data and defining the splits depending on the configuration
        # If several configurations are possible (listed in BUILDER_CONFIGS), the configuration selected by the user is in self.config.name

        # ##### DownloadManager.download_and_extract() takes the dictionary of URLs we generated above and downloads the data files. 
        # Once the files are downloaded, use SplitGenerator to organize each split in the dataset.
        # This is a simple class that contains: 
        # 1. The name of the split. You should use the standard split names: Split.TRAIN, Split.TEST, and Split.VALIDATION. 
        # 2. gen_kwargs provides the file paths to the data files to load for each split.
        ## SplitGenerator:  ( name: str, gen_kwargs: typing.Dict = <factory> ) :
        #   name(str) — Name of the Split for which the generator will create the examples.
        print(_URLS)
        downloaded_files = dl_manager.download_and_extract(_URLS)

        return [
            datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={"filepath": downloaded_files["train"]}),
            datasets.SplitGenerator(name=datasets.Split.VALIDATION, gen_kwargs={"filepath": downloaded_files["dev"]}),
        ]

################### _generate_examples() for csv file###################

    #def _generate_examples(self, filepath): 
        # DatasetBuilder._generate_examples takes the file path provided by gen_kwargs to read and parse the data files. 
        # You need to write a function that loads the data files and extracts the columns.
        # Your function should yield a tuple of an id_, and an example from the dataset.
        #logger.info("generating examples from = %s", filepath)
        #with open(filepath) as f:
        #    ictd = csv.DictReader(f)
        #    print(ictd)
################### _generate_examples() for json file###################

    def _generate_examples(self, filepath): 
        # DatasetBuilder._generate_examples takes the file path provided by gen_kwargs to read and parse the data files. 
        # You need to write a function that loads the data files and extracts the columns.
        # Your function should yield a tuple of an id_, and an example from the dataset.
        logger.info("generating examples from = %s", filepath)
        with open(filepath) as f:
            id_ = 0
            ictd = json.load(f)
            #print(ictd)
            
            for entry in ictd["data"]:
                #print(entry["title"])
                title = entry["title"]
                
                
                for table in entry["table_names"]:
                    #print(table['nlq'])
                    nlq = table["nlq"]
                    #print(table['table'])
                    table_name = table["table"]
                    
                    yield id_, {
                        "title": title,
                        "table_names": {
                                "nlq": nlq,
                                "table": table_name,
                            },
                        
                    }
                    id_ += 1
                    

                   
if __name__ == "__main__":
    print ("lets see")
    instance = ictd()
    #print(instance._generate_examples())
    for i in instance._generate_examples("/home/deeplearning/data_loading_script/train.json"):
        print(i)

#print(instance._generate_examples("/home/deeplearning/data_loading_script/train.json").cache_info())

