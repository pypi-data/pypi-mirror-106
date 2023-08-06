from bs4 import BeautifulSoup, NavigableString
import statistics
import string
import pandas as pd

# def children_tags_lookahead_counts(children_tags:list, end_nodes:list):
#   """
#   Function to check if the end nodes containing any returnable node

#   Params:
#     children_tags (list): [...BSoup-HTML...]
#     end_nodes (list): [...list of tags to look ahead...]

#   For example:
#     children_tags incl: <p><p>Nested Paragraph</p></p>
#     end_nodes = ['p']
#     yield --> (1) and a follow-up should set BSoup to return False

#     children_tags incl: <p>Single Paragraph</p>
#     end_nodes = ['p']
#     yield --> (0) and a follow-up should set BSoup to return True
#   """
#   func = lambda child: len(child(end_nodes))
#   return map(func, children_tags)


def end_node_with_text(tag,
                       end_nodes: list = ['div', 'li', 'p'],
                       nodes_unless_last=['div'], 
                       incl_embed_navstr: bool = True
                       ) -> bool:
    """
    Function to return only the desired end DOM nodes with containing text
    With default setting, this could be used direct as BeautifulSoup callback: soup(func)
    With setting, setup a lambda callback for this: soup(lambda x: func(x, **kwargs))

    tag: Beautiful Soup nodes
    end_nodes (list): desired nodes as end nodes 
    nodes_unless_last (list): nodes that could escape. Only return the nodes if it has no more children end nodes
    incl_embed_navstr (bool): allowed soup to return nodes that are not end-nodes,\
      given it is not one of the target end_nodes

    Example:
      tag = HTML<li><p> A list text </p></li>
      end_nodes = ['p', 'li]
      incl_embed_navstr = False/ True
      returns --> <p> A list text </p>

      tag = HTML<li><a> An anchor text </a></li>
      end_nodes = ['p', 'li]
      incl_embed_navstr = True 
      returns --> <li><a> An anchor text </a></li>

      tag = HTML<li><a> An anchor text </a></li>
      end_nodes = ['p', 'li]
      incl_embed_navstr = False 
      returns --> None (since <a> is end-node & not in end_nodes)
    """
    num_child_with_end_nodes = len(tag.findChildren(end_nodes))
    # check of the endnode is of type
    # if tag.name not in end_nodes:
    if tag.name not in nodes_unless_last and num_child_with_end_nodes > 0:
        return False

    # check if there it is a empty text node
    # passthrough if some text inside
    if not ''.join(tag.text.split()):
        return False

    # check if the children nodes have deeper tag or
    # when not containing other end-nodes itself
    # just NavigableString, <em><b><strong> etc....
    # nav_str_res = list(children_tags_lookahead_counts(
    #   tag.findChildren(), end_nodes=end_nodes)
    # )
    # num_child_with_end_nodes = len(tag.findChildren(end_nodes))

    if (
        tag.name in end_nodes and  # current at end node that would return myself
        num_child_with_end_nodes == 0
    ):
        return True if incl_embed_navstr else False

    # check if there are some other tag wrapping around
    if len(tag(text=False)) > 0:
        return False

    # final node
    return True


class TextUnits:
    """
    TextUnits aims to find the EndNods with text using BeautifulSoup. TextUnits 
    class provides some basic functionalities: 
      1. easier retrieval of the end nodes results 
      2. basic numerical and statistics operation on the end nodes text

    Methods are grouped as follow: 
     1. tag_<method_name>: Methods that operate on the tags of TextUnits.units
     2. text_<method_name>: Methods that operate the text of TextUnits.units

    The default end_node_func returns only <p>, <div>, <li> text end nodes. 
    You could define a more sophiscated one in order find the end nodes 

    self.units -> [BS-end-nodes, ....]
    """

    def __init__(self, end_node_func):
        self.end_node_func = end_node_func  # func obj on how to define text end nodes
        self.units = None  # class attrib of text units based on add_soup

    def add_soup(self, soup):
        # define self.unit after class initialzing
        # to locate all the text end nodes
        self.units = soup(self.end_node_func)

    # some class helper to check attribs existence
    def check_units(func):
        def func_wrapper(self, *args, **kwargs):
            assert self.units, "You have to use .add_soup() to define textunits first"
            return func(self, *args, **kwargs)
        return func_wrapper

    # class methods

    @check_units
    def tag_filter(self, tagname: str) -> list:
        if tagname == 'all':
            return self.units
        filtered = filter(lambda unit: unit.name == tagname, self.units)
        return list(filtered)

    def tag_count(self, tagname: str) -> int:
        filtered = self.tag_filter(tagname)
        return len(list(filtered))

    def text_counts(self, tagname: str) -> list:
        filtered = self.tag_filter(tagname)
        return [len(unit.text.split()) for unit in filtered]

    def text_total(self, tagname: str) -> list:
        return sum(self.text_counts(tagname))

    def text_stats(self, stats, tagname: str) -> float:
        return getattr(statistics, stats)(self.text_counts(tagname))


### TagFeaturesCreator is for creating features based on the html tags ###

class TagFeaturesCreator:
    """
      TagFeaturesCreator is a Class Interface that generate dictionary-like features
      for TextUnits Object 

      To use TagFeaturesCreator: 
      1. Create an instance of `TagFeaturesCreator`: MyClass(TagFeaturesCreator)
      2. define super().__init__(*args, **kwargs) in that instance 
      3. Add methods that return a SINGLE value for a SINGLE TextUnits.units
        - name your method as 'unit_<feature_name>'
        - set your methods argument as (self, unit)
        - any variables should be defined within the method or the class instance

      4. After defining all the features methods, simply run .create_features()
      5. The results would be: {'feature_name': [feature_of_each_text_unit], ...}
    """

    def __init__(self, text_units: TextUnits):
        assert isinstance(
            text_units, TextUnits), "text_unit needs to be a TextUnits"
        # This function provide BS-bool to define end nodes with text
        self.text_units = text_units
        self.units = text_units.units

    @property
    def get_units(self):
        # this return the extracted text units
        return self.units

    def unit_get_raw(self, unit):
        """Retreive the raw text from a TextUnit (trimmed space)"""
        # add a bullet symbol if it is a list item
        for tag in unit('a'):        
            tag = tag.string.replace_with(f'"{tag.text}"') if tag.string else tag

        for tag in unit('li'):
            tag = tag.string.replace_with(f'- {tag.text}') if tag.string else tag

        # return ' '.join(unit.text.split())
        return ' '.join(unit.text.split())

    def unit_get_text(self, unit):
        """Retrieve beautify text from a TextUnit"""
        text = self.unit_get_raw(unit)

        # remove punctuation
        return text.translate(text.maketrans('', '', string.punctuation))

    def __feature_methods__(self):
        class_name = self.__class__.__name__

        methods_list = []
        for defined in dir(self):
            if defined.startswith('unit_'):
                methods_list.append(defined)
        return methods_list

    def create_features(self, excl: list = ['get_raw', 'get_text'], as_df=True) -> dict:
        """This method returns features of the units 

        Params:
        excl: list of features creation method to exclude under 'unit_' prefix

        """
        # extract all the text-units methods
        feature_methods = self.__feature_methods__()

        # generate prefix for the excl list
        excl = [f'unit_{name}' for name in excl] if excl else None
        _ = list(map(getattr(feature_methods, 'remove'), excl)) if excl else None

        # retrieve the text units
        units = self.get_units
        # features collection is a dictionary {'feature_name': [unit results]}
        features = {}

        for method in feature_methods:
            # print(method)
            # generate feature names and map the feature into a dict res
            feature_name = method.split('unit_')[-1]

            def inclass_method_callback(
                unit): return getattr(self, method)(unit)
            res = list(map(inclass_method_callback, units))

            # input the results into the dictionary
            features[feature_name] = res

        return pd.DataFrame(features) if as_df else features
