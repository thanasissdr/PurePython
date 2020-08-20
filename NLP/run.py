from preprocessing.character_preprocessors import WhiteSpacePunctuationProcessor
from preprocessing.tokenizers import SpaceTokenizer

from string_matching.fuzzywuzzy_style.main import FuzzyPipeline


char_preprocessor = WhiteSpacePunctuationProcessor()
tokenizer = SpaceTokenizer()

fuzzy_pipeline = FuzzyPipeline(char_preprocessor, tokenizer)
print(fuzzy_pipeline.token_set_ratio("fuzzy", "fuzzy being"))

