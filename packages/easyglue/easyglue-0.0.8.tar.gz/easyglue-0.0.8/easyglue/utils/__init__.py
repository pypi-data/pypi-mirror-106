import re


def reader_method(func):
    """
    Decorator method, designed to be used in all methods that read a dataset and return it as a DynamicFrame. The
    decorator will call the wrapped method, then will clear all the options dictionaries so that options from a read
    don't reappear in the next read.
    :param func: Reader function
    :return: Result of the reader function
    """

    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        self.connection_options_dict.clear()
        self.format_options_dict.clear()
        self.additional_options_dict.clear()
        return result

    return wrapper


def writer_method(func):
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        self.connection_options_dict.clear()
        self.format_options_dict.clear()
        self.additional_options_dict.clear()
        return result

    return wrapper


QUALIFIED_NAME_MATCH_REGEX = "[a-zA-Z0-9_]+\\.[a-zA-Z0-9_]+"
QUALIFIED_NAME_MATCH_CAPTURE = "[a-zA-Z0-9_]+"


def validate_qualified_name(qualified_name: str) -> tuple:
    """
    Validates that the provided qualified name is in the form of "database.table" and if so, returns each part
    :param qualified_name: Qualified name of the table
    :return: Database name, table name
    """
    if not re.match(QUALIFIED_NAME_MATCH_REGEX, qualified_name):
        raise ValueError('Provided table name is not in the form of "database.table"')
    else:
        matches = re.findall(QUALIFIED_NAME_MATCH_CAPTURE, qualified_name)
        return matches[0], matches[1]
